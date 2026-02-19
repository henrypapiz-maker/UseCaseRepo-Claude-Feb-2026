# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with this repository.

## Project Overview

This repository tracks Claude Code use cases, weekly adoption signals, and enterprise readiness across key dimensions. It serves as a living reference for evaluating the AI coding agent landscape.

## Model Configuration

- **Default Model:** Claude Sonnet 4.5 (`claude-sonnet-4-5-20250929`)
- Configured in `.claude/settings.json` and `.env.example`

## MCP Integrations

Three MCP servers are configured in `.mcp.json` (project root):

| Server   | Transport | Auth Method                        |
|----------|-----------|------------------------------------|
| Vercel   | HTTP      | OAuth (browser prompt on first use)|
| GitHub   | HTTP      | Personal Access Token (PAT)        |
| Neon     | HTTP      | OAuth (browser prompt on first use)|

On first session, run `/mcp` to authenticate Vercel and Neon via browser.

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
│   └── week-ending-2026-02-12.md
├── summaries/                       # Executive summaries
│   └── executive-summary-2026-02-12.md
└── use-case-log/                    # Key areas and use case tracking
    └── key-areas-and-use-cases.md
```

## Notes for Claude

- When making changes, prefer editing existing files over creating new ones
- Follow the established patterns in the codebase
- Ask clarifying questions if requirements are ambiguous
