# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## Project Overview

This repository tracks Claude Code use cases, weekly adoption signals, and enterprise readiness across key dimensions. It serves as a living reference for evaluating the AI coding agent landscape.

## Model Configuration

- **Default Model:** Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)
- Configured in `.claude/settings.json` and `.env.example`

## MCP Integrations

Three MCP servers are configured in `.mcp.json` (project root):

| Server | Transport | Endpoint | Auth Method |
|--------|-----------|----------|-------------|
| Vercel | HTTP | `https://mcp.vercel.com` | API Token (`VERCEL_API_KEY` in `.env`) |
| GitHub | HTTP | `https://api.githubcopilot.com/mcp/` | Personal Access Token (`GITHUB_PERSONAL_ACCESS_TOKEN` in `.env`) |
| Neon | HTTP | `https://mcp.neon.tech/mcp` | OAuth (browser prompt on first use) |

**Setup:** Copy `.env.example` to `.env` and fill in your tokens. On first session, run `/mcp` to authenticate Neon via browser.

## Skills

Skills are installed via `./setup-skills.sh`. Below is the full catalog:

### Developer & Engineering Skills

| Skill | Source | Description |
|-------|--------|-------------|
| web-artifacts-builder | `anthropics/skills` | Build web artifacts and components |
| frontend-design | `anthropics/skills` | Frontend design assistance |
| mcp-builder | `anthropics/skills` | Build and scaffold MCP servers |
| webapp-testing | `anthropics/skills` | Web application testing |
| Superpowers | `obra/superpowers` | 20+ battle-tested skills: planning, reviewing, testing, debugging |
| AgentSys | `avifenesh/agentsys` | Task-to-production workflows, PR management, code review |
| Fullstack Dev | `jeffallan/claude-skills` | 65 skills including Jira/Confluence integration |
| DevOps | `akin-ozer/cc-devops-skills` | Infrastructure-as-code, CI/CD pipelines |
| Security | `trailofbits/skills` | CodeQL, Semgrep, vulnerability detection |

### Finance & Business Skills

| Skill | Source | Description |
|-------|--------|-------------|
| Financial Analyst | `alirezarezvani/claude-skills` | Financial analysis and reporting |
| CEO/CTO Advisor | `alirezarezvani/claude-skills` | Executive strategy guidance |
| Revenue Ops | `alirezarezvani/claude-skills` | Revenue operations optimization |
| Product Strategy | `alirezarezvani/claude-skills` | Product roadmap and strategy |
| Campaign Analytics | `alirezarezvani/claude-skills` | Marketing campaign analysis |

## Development Guidelines

### Code Style
- Follow consistent formatting and naming conventions
- Write clear, self-documenting code
- Keep functions small and focused on a single responsibility

### Git Practices
- Use descriptive commit messages
- Create feature branches for new work
- Keep commits atomic and focused

### Testing
- Write tests for new functionality
- Ensure existing tests pass before committing

## Common Commands

```bash
# First-time setup (MCP servers, skills, env file)
./setup-skills.sh

# Set model to Sonnet 4.5
export CLAUDE_MODEL=claude-sonnet-4-5-20250929

# Check MCP server status (inside Claude Code)
/mcp
```

## Project Structure

```
/
├── CLAUDE.md                        # This file - guidance for Claude Code
├── .mcp.json                        # MCP server config (Vercel, GitHub, Neon)
├── .env.example                     # API key templates (copy to .env)
├── .claude/settings.json            # Claude Code project settings (model)
├── setup-skills.sh                  # One-time setup script for skills & MCP
├── weekly-records/                  # Weekly scan records by date
│   ├── week-ending-2026-02-12.md
│   └── week-ending-2026-02-27.md
├── summaries/                       # Executive summaries
│   ├── executive-summary-2026-02-12.md
│   └── executive-summary-2026-02-27.md
└── use-case-log/                    # Key areas and use case tracking
    └── key-areas-and-use-cases.md
```

## Notes for Claude

- When making changes, prefer editing existing files over creating new ones
- Follow the established patterns in the codebase
- Ask clarifying questions if requirements are ambiguous
