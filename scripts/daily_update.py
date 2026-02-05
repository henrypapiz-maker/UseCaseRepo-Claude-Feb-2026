#!/usr/bin/env python3
"""
Daily AI Use Cases Workbook Updater

This script automates the daily update of the AI Use Cases workbook by:
1. Checking GitHub repositories for activity
2. Searching for new AI research articles
3. Updating the Excel workbook
4. Generating a summary report

Usage:
    python daily_update.py [--full | --repos-only | --research-only] [--no-commit]

Requirements:
    pip install openpyxl requests python-dateutil
"""

import argparse
import json
import logging
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

try:
    import requests
    from dateutil import parser as date_parser
    from openpyxl import load_workbook
    from openpyxl.styles import PatternFill
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install openpyxl requests python-dateutil")
    sys.exit(1)

# Configuration
WORKBOOK_PATH = Path(__file__).parent.parent / "AI_Use_Cases_Comprehensive_2026.xlsx"
LOG_DIR = Path(__file__).parent.parent / "logs"

# GitHub repositories to monitor
GITHUB_REPOS = {
    "finance": [
        "AI4Finance-Foundation/FinRobot",
        "vas3k/TaxHacker",
        "hananedupouy/LLMs-in-Finance",
        "georgezouq/awesome-ai-in-finance",
        "The-AI-Alliance/deep-research-agent-for-finance",
        "tinztwins/finllm-apps",
        "kennethleungty/Finance-LLMs",
        "firmai/financial-machine-learning",
        "sergepaulc/Machine-Learning-for-Finance",
    ],
    "manufacturing": [
        "frappe/erpnext",
        "frePPLe/frepple",
        "frenkowski/SCIMAI-Gym",
        "ankitrajsh/Supply-Chain-Optimization",
    ],
    "legal": [
        "Open-Source-Legal/OpenContracts",
        "LexPredict/lexpredict-lexnlp",
        "Liquid-Legal-Institute/Legal-Text-Analytics",
    ],
}

# Research sources to check
RESEARCH_SOURCES = {
    "hyperscaler": [
        {"name": "Google DeepMind", "url": "https://deepmind.google/blog/"},
        {"name": "Microsoft Research", "url": "https://www.microsoft.com/en-us/research/"},
        {"name": "AWS ML Blog", "url": "https://aws.amazon.com/blogs/machine-learning/"},
    ],
    "big4": [
        {"name": "Deloitte AI", "url": "https://www.deloitte.com/global/en/services/consulting/research/"},
        {"name": "McKinsey AI", "url": "https://www.mckinsey.com/capabilities/quantumblack/our-insights"},
        {"name": "PwC AI", "url": "https://www.pwc.com/us/en/tech-effect/ai-analytics.html"},
        {"name": "KPMG AI", "url": "https://kpmg.com/us/en/capabilities-services/advisory-services/ai.html"},
    ],
    "ai_studio": [
        {"name": "OpenAI", "url": "https://openai.com/research/"},
        {"name": "Anthropic", "url": "https://www.anthropic.com/research"},
    ],
    "academic": [
        {"name": "Stanford HAI", "url": "https://hai.stanford.edu/news"},
        {"name": "MIT CSAIL", "url": "https://www.csail.mit.edu/news"},
    ],
}

# Status thresholds
STALE_THRESHOLD_DAYS = 180  # 6 months
INACTIVE_THRESHOLD_DAYS = 365  # 12 months

# Styles
ACTIVE_FILL = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
STALE_FILL = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
INACTIVE_FILL = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")


def setup_logging():
    """Configure logging to file and console."""
    LOG_DIR.mkdir(exist_ok=True)
    log_file = LOG_DIR / f"{datetime.now().strftime('%Y-%m-%d')}_update.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(sys.stdout),
        ],
    )
    return logging.getLogger(__name__)


def check_github_repo(repo: str) -> dict:
    """Check a GitHub repository for activity status."""
    url = f"https://api.github.com/repos/{repo}"
    headers = {"Accept": "application/vnd.github.v3+json"}

    # Add token if available
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        pushed_at = date_parser.parse(data["pushed_at"])
        days_since_push = (datetime.now(pushed_at.tzinfo) - pushed_at).days

        if days_since_push <= 30:
            status = "ACTIVE"
        elif days_since_push <= STALE_THRESHOLD_DAYS:
            status = "MODERATE"
        elif days_since_push <= INACTIVE_THRESHOLD_DAYS:
            status = "STALE"
        else:
            status = "INACTIVE"

        return {
            "repo": repo,
            "name": data["name"],
            "pushed_at": pushed_at.strftime("%b %d, %Y"),
            "days_since_push": days_since_push,
            "status": status,
            "stars": data["stargazers_count"],
            "forks": data["forks_count"],
            "open_issues": data["open_issues_count"],
            "description": data.get("description", ""),
        }
    except requests.RequestException as e:
        return {
            "repo": repo,
            "error": str(e),
            "status": "ERROR",
        }


def check_all_repos(logger) -> dict:
    """Check all configured GitHub repositories."""
    logger.info("Checking GitHub repositories...")
    results = {"finance": [], "manufacturing": [], "legal": []}

    for category, repos in GITHUB_REPOS.items():
        for repo in repos:
            logger.info(f"  Checking {repo}...")
            result = check_github_repo(repo)
            results[category].append(result)

            if result.get("status") == "ERROR":
                logger.warning(f"    Error: {result.get('error')}")
            else:
                logger.info(f"    Status: {result['status']} (last push: {result['pushed_at']})")

    return results


def update_workbook(repo_results: dict, research_articles: list, logger) -> dict:
    """Update the Excel workbook with new data."""
    if not WORKBOOK_PATH.exists():
        logger.error(f"Workbook not found: {WORKBOOK_PATH}")
        return {"error": "Workbook not found"}

    logger.info(f"Updating workbook: {WORKBOOK_PATH}")
    wb = load_workbook(WORKBOOK_PATH)
    changes = {"repos_updated": 0, "articles_added": 0}

    # Update GitHub Repo Synopsis sheet if it exists
    if "GitHub Repo Synopsis" in wb.sheetnames:
        ws = wb["GitHub Repo Synopsis"]
        logger.info("  Updating GitHub Repo Synopsis...")

        # Find repos and update their status
        for row in range(2, ws.max_row + 1):
            repo_name = ws.cell(row=row, column=1).value
            if repo_name:
                # Find matching result
                for category_results in repo_results.values():
                    for result in category_results:
                        if result.get("repo") and result["repo"].split("/")[1] in str(repo_name):
                            if result.get("status") != "ERROR":
                                # Update last update date
                                ws.cell(row=row, column=2).value = result["pushed_at"]
                                # Update status
                                ws.cell(row=row, column=3).value = result["status"]
                                # Update stars
                                ws.cell(row=row, column=4).value = result["stars"]

                                # Apply status color
                                status_cell = ws.cell(row=row, column=3)
                                if result["status"] == "ACTIVE":
                                    status_cell.fill = ACTIVE_FILL
                                elif result["status"] in ["STALE", "MODERATE"]:
                                    status_cell.fill = STALE_FILL
                                else:
                                    status_cell.fill = INACTIVE_FILL

                                changes["repos_updated"] += 1
                            break

    # Add new research articles if provided
    if research_articles and "AI Research & White Papers" in wb.sheetnames:
        ws = wb["AI Research & White Papers"]
        logger.info(f"  Adding {len(research_articles)} new research articles...")

        for article in research_articles:
            ws.append([
                article.get("source_type", ""),
                article.get("organization", ""),
                article.get("title", ""),
                article.get("date", ""),
                article.get("synopsis", ""),
                article.get("url", ""),
            ])
            changes["articles_added"] += 1

    # Save workbook
    wb.save(WORKBOOK_PATH)
    logger.info(f"  Workbook saved. Changes: {changes}")

    return changes


def generate_summary(repo_results: dict, changes: dict, logger) -> str:
    """Generate a summary report of the update."""
    today = datetime.now().strftime("%Y-%m-%d")

    # Count repo statuses
    status_counts = {"ACTIVE": 0, "MODERATE": 0, "STALE": 0, "INACTIVE": 0, "ERROR": 0}
    active_repos = []
    stale_repos = []

    for category_results in repo_results.values():
        for result in category_results:
            status = result.get("status", "ERROR")
            status_counts[status] = status_counts.get(status, 0) + 1

            if status == "ACTIVE":
                active_repos.append(result["repo"])
            elif status in ["STALE", "INACTIVE"]:
                stale_repos.append(f"{result['repo']} ({result.get('days_since_push', '?')} days)")

    summary = f"""
================================================================================
Daily AI Use Cases Workbook Update Summary
Date: {today}
================================================================================

GITHUB REPOSITORIES
-------------------
Total Checked: {sum(status_counts.values())}
  - Active (≤30 days):     {status_counts['ACTIVE']}
  - Moderate (≤6 months):  {status_counts['MODERATE']}
  - Stale (6-12 months):   {status_counts['STALE']}
  - Inactive (>12 months): {status_counts['INACTIVE']}
  - Errors:                {status_counts['ERROR']}

WORKBOOK UPDATES
----------------
  - Repos updated:    {changes.get('repos_updated', 0)}
  - Articles added:   {changes.get('articles_added', 0)}

ATTENTION NEEDED
----------------
"""

    if stale_repos:
        summary += "Stale/Inactive Repositories:\n"
        for repo in stale_repos:
            summary += f"  - {repo}\n"
    else:
        summary += "No stale repositories detected.\n"

    summary += """
================================================================================
"""

    return summary


def commit_changes(message: str, logger):
    """Commit changes to git."""
    try:
        # Check if there are changes to commit
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            cwd=WORKBOOK_PATH.parent,
        )

        if not result.stdout.strip():
            logger.info("No changes to commit.")
            return False

        # Add and commit
        subprocess.run(["git", "add", str(WORKBOOK_PATH)], cwd=WORKBOOK_PATH.parent, check=True)
        subprocess.run(
            ["git", "commit", "-m", message],
            cwd=WORKBOOK_PATH.parent,
            check=True,
        )
        logger.info("Changes committed to git.")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Git error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Daily AI Use Cases Workbook Updater")
    parser.add_argument("--full", action="store_true", default=True, help="Run all steps (default)")
    parser.add_argument("--repos-only", action="store_true", help="Only check GitHub repositories")
    parser.add_argument("--research-only", action="store_true", help="Only search for research articles")
    parser.add_argument("--no-commit", action="store_true", help="Don't commit changes to git")
    args = parser.parse_args()

    logger = setup_logging()
    logger.info("=" * 60)
    logger.info("Starting Daily AI Use Cases Workbook Update")
    logger.info("=" * 60)

    repo_results = {}
    research_articles = []

    # Step 1: Check GitHub repos
    if not args.research_only:
        repo_results = check_all_repos(logger)

    # Step 2: Search for research (placeholder - requires API keys or manual input)
    if not args.repos_only:
        logger.info("Research article search requires manual input or API integration.")
        logger.info("Use Claude Code with /daily-ai-update for AI-powered research search.")

    # Step 3: Update workbook
    changes = update_workbook(repo_results, research_articles, logger)

    # Step 4: Generate summary
    summary = generate_summary(repo_results, changes, logger)
    print(summary)
    logger.info(summary)

    # Step 5: Commit changes
    if not args.no_commit and changes.get("repos_updated", 0) > 0:
        today = datetime.now().strftime("%Y-%m-%d")
        commit_changes(f"Daily update: {today} - {changes['repos_updated']} repos updated", logger)

    logger.info("Daily update complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
