# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## Project Overview

This repository maintains a comprehensive AI Use Cases research workbook that tracks:
- Finance and Accounting AI use cases (80+ detailed use cases)
- GitHub repositories for finance, manufacturing, and legal tech AI
- Top 10 ERP and Top 5 EPM AI capabilities
- Latest AI research from hyperscalers, Big 4, AI studios, and academia

## Key Files

| File | Description |
|------|-------------|
| `AI_Use_Cases_Comprehensive_2026.xlsx` | Main workbook with all use cases and research |
| `DAILY_AUTOMATION_TASKS.md` | Documentation for daily update routine |
| `scripts/daily_update.py` | Python script for automated updates |

## Daily Automation

### Run Daily Update with Claude Code
```bash
# Use the daily-ai-update skill
/daily-ai-update
```

### Run Python Script Directly
```bash
pip install -r scripts/requirements.txt
python scripts/daily_update.py
```

### What Gets Updated
1. **GitHub Repos**: Check 16 repositories for activity status
2. **Research Articles**: Search for new AI papers and reports
3. **Excel Workbook**: Update dates, stats, add new articles

## Available Skills

| Skill | Description |
|-------|-------------|
| `/excel` | Work with Excel files (read, write, manipulate) |
| `/daily-ai-update` | Run daily workbook update routine |

## Project Structure

```
/
├── CLAUDE.md                              # This file
├── AI_Use_Cases_Comprehensive_2026.xlsx   # Main workbook (12+ sheets)
├── DAILY_AUTOMATION_TASKS.md              # Automation documentation
├── .claude/
│   └── skills/
│       ├── excel/SKILL.md                 # Excel skill
│       └── daily-ai-update/SKILL.md       # Daily update skill
├── scripts/
│   ├── daily_update.py                    # Python automation script
│   └── requirements.txt                   # Python dependencies
└── logs/                                  # Daily update logs
```

## Workbook Sheets

| Sheet | Content | Update Frequency |
|-------|---------|------------------|
| Executive Summary | Stats overview | Weekly |
| GitHub Repo Synopsis | 9 finance repos | Daily |
| Top 10 ERP AI Use Cases | ERP AI capabilities | Monthly |
| Top 5 EPM AI Use Cases | EPM AI capabilities | Monthly |
| Manufacturing & Distribution | 8 mfg/dist repos | Daily |
| Legal Tech AI Repos | 11 legal tech repos | Daily |
| AI Research & White Papers | 24+ articles with synopses | Daily |

## Development Guidelines

### Code Style
- Follow consistent formatting and naming conventions
- Write clear, self-documenting code
- Keep functions small and focused on a single responsibility

### Git Practices
- Use descriptive commit messages
- Create feature branches for new work
- Keep commits atomic and focused

## Notes for Claude

- When updating the workbook, use openpyxl library
- Preserve existing formatting when adding new rows
- Include 100-200 word synopses for new research articles
- Flag repos as ACTIVE/STALE/INACTIVE based on last push date
- Always verify URLs before adding to workbook
