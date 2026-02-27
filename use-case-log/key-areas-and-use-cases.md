# Key Areas & Use Cases — Preview Log

**As of Week Ending 2/27/2026**

---

## Key Areas

| #  | Area                              | Maturity    | Enterprise Signal | Δ vs 2/12 |
|----|-----------------------------------|-------------|-------------------|-----------|
| 1  | Code Generation & Completion      | Mature      | Very High         | ↑         |
| 2  | Codebase Understanding & Navigation| Mature     | Very High         | ↑         |
| 3  | Debugging & Incident Response     | Mature      | High              | →         |
| 4  | Code Review & Quality             | Mature      | High              | →         |
| 5  | Testing & Test Generation         | Growing     | High              | ↑         |
| 6  | DevOps & CI/CD Automation         | Growing     | High              | ↑         |
| 7  | Security & Vulnerability Management| Mature     | Very High         | ↑↑        |
| 8  | Documentation & Knowledge Capture | Growing     | Medium-High       | ↑         |
| 9  | Multi-Agent Orchestration         | Growing     | High              | ↑         |
| 10 | Non-Developer / Citizen Automation| Growing     | High              | ↑↑        |
| 11 | Cross-Platform Agentic Workflows  | Growing     | Very High         | ↑↑        |
| 12 | Data Analysis & Financial Modeling| Growing     | High              | →         |
| 13 | Design-to-Code Workflows          | Emerging    | High              | NEW       |
| 14 | Enterprise Plugin Ecosystems      | Emerging    | Very High         | NEW       |

---

## Key Use Cases by Area

### 1. Code Generation & Completion
| Use Case | Description | Evidence |
|----------|-------------|----------|
| Feature implementation from natural language | Describe a feature, agent writes full implementation | Core Claude Code capability; universal adoption |
| Boilerplate & scaffolding | Generate project structure, configs, templates | High-frequency developer use |
| Code translation across languages | Convert code between languages/frameworks | Supported by Opus 4.6 context window |
| Refactoring at scale | Rename, restructure, modernize patterns across codebase | Subagent parallel work enables large-scale refactors |
| Large-scale code migrations | Describe migration in plain language, agent executes across thousands of services | Spotify case study (Feb 2026); "any engineer can kick off a large-scale migration" |

### 2. Codebase Understanding & Navigation
| Use Case | Description | Evidence |
|----------|-------------|----------|
| Codebase Q&A | Ask questions about how code works, find implementations | Core CLI capability |
| Architecture mapping | Understand system design, dependencies, data flow | Extended thinking enables deep reasoning |
| Onboarding acceleration | New developers get up to speed via conversational exploration | Enterprise adoption driver |
| Legacy code comprehension | Understand undocumented or complex legacy systems | Cited in enterprise case studies |

### 3. Debugging & Incident Response
| Use Case | Description | Evidence |
|----------|-------------|----------|
| Log analysis & root cause identification | Pipe logs into Claude Code, get diagnosis | Unix composability; CI/CD integration |
| Bug fix from issue description | Read GitHub issue, diagnose, fix, submit PR | GitHub/GitLab integration |
| Production incident triage | Analyze error patterns, suggest fixes under time pressure | Altana, HackerOne case studies |
| Regression detection | Identify what change introduced a bug | Git history analysis capability |

### 4. Code Review & Quality
| Use Case | Description | Evidence |
|----------|-------------|----------|
| Automated PR review | Review changed files for bugs, security issues, style | claude-code-action (5K GitHub stars) |
| Architectural review across services | Persistent reviewer tracking design decisions over time | Cited as underused enterprise capability |
| Standards enforcement | Enforce CLAUDE.md-defined coding standards | CLAUDE.md configuration system |
| Design decision tracking | Track and surface architectural decisions across dev cycles | Enterprise use case highlighted in reporting |

### 5. Testing & Test Generation
| Use Case | Description | Evidence |
|----------|-------------|----------|
| Unit test generation | Generate tests for existing code | Core capability |
| Test-driven development assist | Write tests first, then implement to pass | Plan Mode supports this workflow |
| Integration test scaffolding | Generate test harnesses for multi-service systems | Subagent orchestration enables complex test setups |
| Coverage gap identification | Analyze codebase for untested paths | Codebase understanding + test generation |

### 6. DevOps & CI/CD Automation
| Use Case | Description | Evidence |
|----------|-------------|----------|
| CI pipeline creation & maintenance | Generate and update CI/CD configurations | GitHub Actions / GitLab CI integration |
| Infrastructure as code | Generate Terraform, CloudFormation, Kubernetes configs | Code generation capability |
| Deployment automation | Automate release workflows | CI composability (Unix philosophy) |
| Monitoring & alerting setup | Configure observability tooling | MCP integration with external tools |

### 7. Security & Vulnerability Management
| Use Case | Description | Evidence |
|----------|-------------|----------|
| Vulnerability scanning & response | Identify and fix security vulnerabilities | HackerOne: 44% reduction in response time |
| Reasoning-based vulnerability scanning | Context-aware scanning that traces data flows and maps component interactions | Claude Code Security (Feb 2026): 500+ unknown high-severity vulns found in open-source |
| Security code review | Review changes for OWASP top 10 and other risks | Automated PR review capability |
| Dependency audit | Analyze dependencies for known vulnerabilities | Codebase scanning + web search |
| Compliance code generation | Generate code meeting regulatory requirements | Compliance API for enterprise governance; PwC partnership for regulated industries |

### 8. Documentation & Knowledge Capture
| Use Case | Description | Evidence |
|----------|-------------|----------|
| API documentation generation | Generate docs from code | Code understanding capability |
| Architecture decision records | Document design decisions as they happen | Persistent architectural reviewer pattern |
| Runbook creation | Generate operational runbooks from code/configs | DevOps automation area |
| Knowledge base maintenance | Keep internal docs current with code changes | MCP integration with knowledge tools |

### 9. Multi-Agent Orchestration
| Use Case | Description | Evidence |
|----------|-------------|----------|
| Parallel feature development | Lead agent coordinates sub-agents on different modules | Native subagent support in Claude Code |
| Cross-layer changes | Coordinate frontend/backend/infrastructure changes simultaneously | Cited as underused enterprise capability |
| Large-scale migrations | Multiple agents handle different parts of a migration | Subagent + context compaction enables long-running work |
| Agent team composition | Mix Claude agents with other AI agents (Copilot, Codex, etc.) | Microsoft Agent Framework + GitHub Agent HQ (Feb 2026) |
| Platform-level multi-agent selection | Choose which agent handles each task from a unified platform | GitHub Agent HQ: Claude, Codex, Cognition, xAI agents in one workspace |

### 10. Non-Developer / Citizen Automation
| Use Case | Description | Evidence |
|----------|-------------|----------|
| Personal task automation | Book tickets, file taxes, manage household tasks | Fortune reporting; user testimonials |
| Business process automation | Non-technical staff automating workflows | Cowork enterprise launch (Feb 2026); Epic: >50% usage by non-developers |
| Department-specific AI agents | HR, finance, legal, design agents via Cowork plugins | 12 new MCP connectors; private enterprise marketplace (Feb 2026) |
| Data entry & form processing | Automate repetitive data tasks | General-purpose agent capability |
| Report generation | Create reports from data sources without coding | MCP + file management |
| Custom plugin creation | Build and distribute department-specific AI agents without coding | Cowork Plugin Create tool; enterprises building "hundreds to thousands" of plugins |

### 11. Cross-Platform Agentic Workflows
| Use Case | Description | Evidence |
|----------|-------------|----------|
| IDE-native autonomous coding | Agent works within Xcode/VS Code/JetBrains autonomously | Xcode 26.3 integration; GitHub Agent HQ (Feb 2026) |
| Mobile-to-desktop session continuity | Start task on phone, continue on laptop | Cross-device sessions feature |
| External tool orchestration | Connect to Jira, Slack, Google Drive, custom tools via MCP | 10,000+ MCP servers; 97M+ monthly downloads; Linux Foundation governance |
| Multi-framework agent composition | Compose Claude agents with other frameworks | Microsoft Agent Framework (Jan 2026); GitHub Agent HQ (Feb 2026) |
| Agent-as-MCP-server | Claude Code serves as an MCP server for other AI clients to invoke | Claude Code MCP server mode; enables agent-calling-agent orchestration |
| Interactive MCP UI components | Tools return dashboards, forms, charts rendered in conversation | MCP Apps (Jan 2026): co-built by Anthropic, OpenAI, and MCP-UI |

### 12. Data Analysis & Financial Modeling
| Use Case | Description | Evidence |
|----------|-------------|----------|
| Investment-grade financial analysis | Institutional-quality financial modeling | NBIM case study |
| Analytics automation | Automate data analysis workflows | IG Group: 70 hrs/week saved in analytics |
| Data pipeline creation | Build ETL/data processing pipelines | Code generation + DevOps capabilities |
| Reporting dashboards | Generate visualization and reporting code | Full-stack code generation |

### 13. Design-to-Code Workflows
| Use Case | Description | Evidence |
|----------|-------------|----------|
| Bidirectional design-code sync | Push rendered UIs from Claude Code into Figma as editable design layers, and vice versa | Figma "Code to Canvas" (Feb 17, 2026) |
| Design system enforcement | Generate code that adheres to design tokens and component libraries | Figma MCP Server + Claude Code integration |
| Rapid UI prototyping loop | Build UI in Claude Code → capture in Figma → annotate → push back to code | Code to Canvas full bidirectional workflow |
| Cross-functional design review | Designers, developers, and PMs collaborate on live UI captures on Figma canvas | Figma blog: "Code is powerful for converging; the canvas is powerful for diverging" |

### 14. Enterprise Plugin Ecosystems
| Use Case | Description | Evidence |
|----------|-------------|----------|
| Private plugin marketplace | Enterprises build, distribute, and govern department-specific AI agents | Cowork enterprise marketplace (Feb 24, 2026) |
| Regulated industry deployment | Deploy AI agents within compliant governance frameworks (finance, healthcare) | PwC + Anthropic partnership (Feb 2026) |
| Custom connector development | Build MCP connectors to internal systems and proprietary data sources | 12 new MCP connectors added; Plugin Create tool |
| Department-level AI specialization | Pre-configured agents for HR, legal, finance, investment banking, equity research | Cowork plugins catalog; "mini apps" distributed internally |

---

## Update Notes

### Week Ending 2/27/2026

Major changes from the 2/12 scan:

- **Security moved to Mature** — Claude Code Security launch (reasoning-based vulnerability scanning) represents a product-grade capability, not just a feature. 500+ unknown vulns found in internal testing. Cybersecurity industry took notice (billions in market cap wiped).
- **Non-Developer / Citizen Automation moved to Growing** — Cowork's transition to enterprise-grade with plugins, marketplace, and 12 new connectors moves this from aspirational to operational. Epic confirms >50% of Claude Code usage is non-developers.
- **Multi-Agent Orchestration moved to Growing** — GitHub Agent HQ platformizes multi-agent selection; Claude Code as MCP server enables agent-calling-agent patterns.
- **Cross-Platform Agentic Workflows moved to Growing** — Figma Code to Canvas, GitHub Agent HQ, and 10K+ MCP servers (up from 3K+) demonstrate operational cross-platform integration.
- **Two new areas added:**
  - **Design-to-Code Workflows** (Emerging) — Figma Code to Canvas creates a new category of bidirectional design-engineering collaboration.
  - **Enterprise Plugin Ecosystems** (Emerging) — Cowork's private marketplace and department-specific plugins create a new enterprise platform category.

The highest-impact, most-underused use cases remain: **persistent architectural review**, **design decision tracking**, and **cross-layer coordination**. Newly emerging high-potential use cases: **reasoning-based security scanning**, **bidirectional design-code workflows**, and **enterprise plugin composition**.

---

### Week Ending 2/12/2026 (Initial Scan)

This log represents the initial scan of publicly evidenced use cases as of mid-February 2026. Key observations:

- **Mature areas** (Code Gen, Codebase Understanding, Debugging, Code Review) are well-established with broad adoption evidence.
- **Growing areas** (Testing, DevOps, Security, Documentation, Data Analysis) have strong momentum and specific enterprise proof points.
- **Emerging areas** (Multi-Agent, Citizen Use, Cross-Platform) represent the next wave — enabled by recent launches (Agent SDK, Xcode, Cowork) but still building adoption evidence.

---

*Last Updated: 2026-02-27*
