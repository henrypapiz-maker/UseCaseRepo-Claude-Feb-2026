#!/usr/bin/env bash
# ============================================================
# Claude Code Skills & MCP Setup Script
# ============================================================
# Run this after cloning the repo to install all skills and
# authenticate MCP servers.
#
# Usage:
#   chmod +x setup-skills.sh
#   ./setup-skills.sh
# ============================================================

set -euo pipefail

echo "=== Claude Code Project Setup ==="
echo ""

# -------------------------------------------------------
# 1. Environment
# -------------------------------------------------------
if [ ! -f .env ]; then
  echo "[env] Creating .env from .env.example..."
  cp .env.example .env
  echo "[env] Please edit .env and fill in your API keys."
else
  echo "[env] .env already exists, skipping."
fi

echo ""

# -------------------------------------------------------
# 2. MCP Server Registration
# -------------------------------------------------------
echo "=== Registering MCP Servers ==="

echo "[mcp] Adding Vercel (OAuth — will authenticate in browser)..."
claude mcp add --transport http vercel https://mcp.vercel.com 2>/dev/null || echo "  -> vercel already configured or claude CLI not available"

echo "[mcp] Adding GitHub..."
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ 2>/dev/null || echo "  -> github already configured or claude CLI not available"

echo "[mcp] Adding Neon (OAuth — will authenticate in browser)..."
claude mcp add --transport http neon https://mcp.neon.tech/mcp 2>/dev/null || echo "  -> neon already configured or claude CLI not available"

echo ""

# -------------------------------------------------------
# 3. Developer & Engineering Skills
# -------------------------------------------------------
echo "=== Installing Developer & Engineering Skills ==="

# Anthropic official skills
echo "[skills] Anthropic official: web-artifacts-builder, frontend-design, mcp-builder, webapp-testing"
for skill in web-artifacts-builder frontend-design mcp-builder webapp-testing; do
  claude skill install "anthropics/skills/${skill}" 2>/dev/null || echo "  -> ${skill}: install manually from https://github.com/anthropics/skills"
done

# Superpowers (20+ battle-tested dev skills)
echo "[skills] Superpowers (planning, reviewing, testing, debugging)..."
claude skill install "obra/superpowers" 2>/dev/null || echo "  -> superpowers: install manually from https://github.com/obra/superpowers"

# AgentSys (task-to-production workflows)
echo "[skills] AgentSys (workflow automation, PR management, code review)..."
claude skill install "avifenesh/agentsys" 2>/dev/null || echo "  -> agentsys: install manually from https://github.com/avifenesh/agentsys"

# Fullstack dev skills (65 skills, Jira/Confluence workflows)
echo "[skills] Fullstack Dev (65 skills, Jira/Confluence integration)..."
claude skill install "jeffallan/claude-skills" 2>/dev/null || echo "  -> claude-skills: install manually from https://github.com/jeffallan/claude-skills"

# DevOps skills
echo "[skills] DevOps (infrastructure-as-code, CI/CD)..."
claude skill install "akin-ozer/cc-devops-skills" 2>/dev/null || echo "  -> cc-devops-skills: install manually from https://github.com/akin-ozer/cc-devops-skills"

# Security skills (Trail of Bits)
echo "[skills] Security (CodeQL, Semgrep, vulnerability detection)..."
claude skill install "trailofbits/skills" 2>/dev/null || echo "  -> trailofbits: install manually from https://github.com/trailofbits/skills"

echo ""

# -------------------------------------------------------
# 4. Finance & Business Skills
# -------------------------------------------------------
echo "=== Installing Finance & Business Skills ==="

echo "[skills] Finance & Business (financial analyst, CEO/CTO advisor, revenue ops, product strategy)..."
claude skill install "alirezarezvani/claude-skills" 2>/dev/null || echo "  -> alirezarezvani/claude-skills: install manually from https://github.com/alirezarezvani/claude-skills"

echo ""

# -------------------------------------------------------
# 5. Summary
# -------------------------------------------------------
echo "=== Setup Complete ==="
echo ""
echo "Next steps:"
echo "  1. Edit .env with your API keys (GITHUB_PERSONAL_ACCESS_TOKEN, etc.)"
echo "  2. Start Claude Code in this project:  claude"
echo "  3. Run /mcp to authenticate Vercel and Neon via OAuth"
echo "  4. Verify MCP connections:  /mcp"
echo ""
echo "Installed skill categories:"
echo "  - Developer & Engineering: web-artifacts, frontend-design, superpowers,"
echo "    agentsys, fullstack-dev, devops, security"
echo "  - Finance & Business: financial-analyst, ceo-advisor, cto-advisor,"
echo "    revenue-ops, product-strategy, campaign-analytics"
echo ""
echo "Model configured: claude-sonnet-4-5-20250929 (Sonnet 4.5)"
echo ""
