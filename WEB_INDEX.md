# AI Use Cases Workbook - Web Navigation Index

## Overview

This document provides a hierarchical index of all views, lists, and data structures in the AI Use Cases workbook. Use this as a sitemap for developing web navigation.

---

## Site Hierarchy

```
/
├── dashboard/                      # Executive Summary
│   ├── stats                       # Key metrics and counts
│   ├── categorization             # Code Repos vs Vendor breakdown
│   └── sheet-index                # Quick links to all sections
│
├── use-cases/                      # AI Use Cases by Domain
│   ├── finance-accounting/        # Finance & Accounting
│   │   ├── code-repos             # GitHub repositories (9)
│   │   └── code-samples           # Working code examples
│   │
│   ├── pe-ma/                     # Private Equity & M&A
│   │   ├── code-repos             # Open source tools (10)
│   │   └── vendor-products        # Commercial platforms (15)
│   │
│   ├── legal-tech/                # Legal Technology
│   │   ├── code-repos             # Open source tools (10)
│   │   ├── vendor-products        # Commercial platforms (13)
│   │   └── use-cases              # 15 legal use cases
│   │
│   └── manufacturing/             # Manufacturing & Distribution
│       ├── code-repos             # Open source tools (10)
│       ├── vendor-products        # Commercial platforms (13)
│       └── use-cases              # 18 mfg finance use cases
│
├── platforms/                      # Enterprise Platforms
│   ├── erp/                       # ERP Systems
│   │   ├── use-cases              # Top 10 ERP AI use cases
│   │   └── api-integration        # API documentation
│   │
│   └── epm/                       # EPM Systems
│       ├── use-cases              # Top 5 EPM AI use cases
│       └── api-integration        # API documentation
│
├── research/                       # Research & Publications
│   ├── white-papers               # 24 AI research articles
│   └── strategy-roadmaps          # 31 downloadable PDFs
│
└── resources/                      # Implementation Resources
    └── learning                   # Tutorials, courses, docs
```

---

## Detailed View Specifications

### 1. Dashboard (`/dashboard`)

**Source:** `Executive Summary` sheet

| View | Description | Data Fields |
|------|-------------|-------------|
| `/dashboard/stats` | Key metrics | Total use cases, repos, vendors |
| `/dashboard/categorization` | Code vs Vendor breakdown | Domain, code count, vendor count |
| `/dashboard/sheet-index` | Navigation links | Sheet name, content, frequency |

**Filters:** None (static summary)

---

### 2. Finance & Accounting (`/use-cases/finance-accounting`)

**Sources:** `GitHub Repo Synopsis`, `Code Samples & Prompts`

#### 2.1 Code Repositories (`/use-cases/finance-accounting/code-repos`)

| Field | Type | Filterable | Sortable |
|-------|------|------------|----------|
| Repository | string | Yes | Yes |
| Last Update | date | Yes | Yes |
| Status | enum (ACTIVE/STALE/INACTIVE) | Yes | Yes |
| Stars | number | No | Yes |
| Models Used | string | Yes | No |
| Key Inputs | string | No | No |
| Highlights | string | No | No |
| URL | link | No | No |

**Filters:** Status, Models Used
**Sort:** Last Update (default), Stars

#### 2.2 Code Samples (`/use-cases/finance-accounting/code-samples`)

| Field | Type | Filterable |
|-------|------|------------|
| Repository | string | Yes |
| Use Case | string | Yes |
| Technology | string | Yes |
| Code/Prompt Sample | code block | No |
| Prerequisites | string | No |

---

### 3. PE & M&A (`/use-cases/pe-ma`)

**Source:** `PE & M&A AI Use Cases` sheet

#### 3.1 Code Repositories (`/use-cases/pe-ma/code-repos`)

| Field | Type | Filterable | Sortable |
|-------|------|------------|----------|
| Category | enum | Yes | Yes |
| Name | string | Yes | Yes |
| Description | string | No | No |
| Technical Details | string | Yes | No |
| URL/Source | link | No | No |
| Status/Activity | string | Yes | Yes |

**Categories:** Financial Modeling, Valuation, Due Diligence, M&A Analysis, OSS Due Diligence

#### 3.2 Vendor Products (`/use-cases/pe-ma/vendor-products`)

| Field | Type | Filterable | Sortable |
|-------|------|------------|----------|
| Category | enum | Yes | Yes |
| Name | string | Yes | Yes |
| Description | string | No | No |
| Technical Details | string | No | No |
| URL/Source | link | No | No |
| Status/Activity | string | Yes | No |

**Categories:** Deal Sourcing, Relationship Intelligence, Due Diligence, VDR, Portfolio, OSS Audit

---

### 4. Legal Tech (`/use-cases/legal-tech`)

**Sources:** `Legal Tech AI Repos`, `Legal Tech Use Cases`

#### 4.1 Code Repositories (`/use-cases/legal-tech/code-repos`)

| Field | Type | Filterable |
|-------|------|------------|
| Category | enum | Yes |
| Name | string | Yes |
| Description | string | No |
| Technical Details | string | Yes |
| URL/Source | link | No |
| Status/Activity | string | Yes |

**Categories:** Contract Analysis, NLP Library, Document Analysis, Text Analytics, Legal Data

#### 4.2 Vendor Products (`/use-cases/legal-tech/vendor-products`)

| Field | Type | Filterable |
|-------|------|------------|
| Category | enum | Yes |
| Name | string | Yes |
| Description | string | No |
| Technical Details | string | No |
| URL/Source | link | No |
| Status/Activity | string | Yes |

**Categories:** Contract Analysis, Legal Research, Contract Management, Legal Drafting, E-Discovery

#### 4.3 Use Cases (`/use-cases/legal-tech/use-cases`)

| Field | Type | Filterable |
|-------|------|------------|
| Use Case Category | enum | Yes |
| Use Case | string | Yes |
| Description | string | No |
| Open Source Tools | string | Yes |
| Commercial Tools | string | Yes |
| Quantified Benefits | string | No |

---

### 5. Manufacturing & Distribution (`/use-cases/manufacturing`)

**Sources:** `Manufacturing & Distribution`, `Mfg & Dist Finance Use Cases`

#### 5.1 Code Repositories (`/use-cases/manufacturing/code-repos`)

| Field | Type | Filterable |
|-------|------|------------|
| Category | enum | Yes |
| Name | string | Yes |
| Description | string | No |
| Technical Details | string | Yes |
| URL/Source | link | No |
| Status/Activity | string | Yes |

**Categories:** ERP System, Production Planning, Supply Chain, Demand Forecasting, Inventory, Quality Control, Predictive Maintenance, Process Mining

#### 5.2 Vendor Products (`/use-cases/manufacturing/vendor-products`)

| Field | Type | Filterable |
|-------|------|------------|
| Category | enum | Yes |
| Name | string | Yes |
| Description | string | No |
| Technical Details | string | No |
| URL/Source | link | No |
| Status/Activity | string | Yes |

**Categories:** ERP, Planning, Demand Forecasting, Warehouse, Procurement, Quality, Process Mining

#### 5.3 Use Cases (`/use-cases/manufacturing/use-cases`)

| Field | Type | Filterable |
|-------|------|------------|
| Use Case Category | enum | Yes |
| Use Case | string | Yes |
| Description | string | No |
| Open Source Tools | string | Yes |
| ERP Integration | string | Yes |
| Quantified Benefits | string | No |

---

### 6. ERP Platforms (`/platforms/erp`)

**Sources:** `Top 10 ERP AI Use Cases`, `ERP API Integration`

#### 6.1 Use Cases (`/platforms/erp/use-cases`)

| Field | Type | Filterable | Sortable |
|-------|------|------------|----------|
| ERP System | enum | Yes | Yes |
| AI Product/Feature | string | Yes | No |
| Finance Use Cases | string | No | No |
| Key Capabilities | string | No | No |
| Quantified Benefits | string | No | No |
| URL | link | No | No |

**ERP Systems:** SAP S/4HANA, Oracle Fusion, Microsoft D365, Workday, NetSuite, Sage Intacct, Infor, Unit4, IFS, Epicor, Acumatica

#### 6.2 API Integration (`/platforms/erp/api`)

| Field | Type | Filterable |
|-------|------|------------|
| ERP System | enum | Yes |
| API Type | string | Yes |
| Documentation URL | link | No |
| Auth Method | string | Yes |
| Key Endpoints/Capabilities | string | No |

---

### 7. EPM Platforms (`/platforms/epm`)

**Sources:** `Top 5 EPM AI Use Cases`, `EPM API Integration`

#### 7.1 Use Cases (`/platforms/epm/use-cases`)

| Field | Type | Filterable |
|-------|------|------------|
| EPM System | enum | Yes |
| AI Product/Feature | string | Yes |
| Planning Use Cases | string | No |
| Key Capabilities | string | No |
| Quantified Benefits | string | No |
| URL | link | No |

**EPM Systems:** Oracle EPM, Anaplan, OneStream, Planful, SAP SAC

#### 7.2 API Integration (`/platforms/epm/api`)

| Field | Type | Filterable |
|-------|------|------------|
| EPM System | enum | Yes |
| API Type | string | Yes |
| Documentation URL | link | No |
| AI/ML Integration | string | No |
| Key Capabilities | string | No |

---

### 8. Research (`/research`)

**Sources:** `AI Research & White Papers`, `AI Strategy Roadmaps`

#### 8.1 White Papers (`/research/white-papers`)

| Field | Type | Filterable | Sortable |
|-------|------|------------|----------|
| Source Type | enum | Yes | Yes |
| Organization | string | Yes | Yes |
| Title | string | Yes | No |
| Date | date | Yes | Yes |
| Synopsis | string | No | No |
| URL | link | No | No |

**Source Types:** Hyperscaler, Big 4, Consulting, AI Studio, Academic

#### 8.2 Strategy Roadmaps (`/research/strategy-roadmaps`)

| Field | Type | Filterable | Sortable |
|-------|------|------------|----------|
| Source | enum | Yes | Yes |
| Document Title | string | Yes | No |
| Description | string | No | No |
| Pages/Length | string | No | Yes |
| Format | enum (PDF/PPT/Web) | Yes | No |
| Year | number | Yes | Yes |
| Download Link | link | No | No |

**Sources:** McKinsey, Deloitte, Accenture, BCG, KPMG, PwC, EY, WEF, C3.ai, Info-Tech, RTS Labs, 3Cloud, Microsoft, Applied AI

---

### 9. Resources (`/resources`)

**Source:** `Implementation Resources`

| Field | Type | Filterable |
|-------|------|------------|
| Resource Type | enum | Yes |
| Name | string | Yes |
| URL | link | No |
| Description | string | No |

**Resource Types:** Documentation, Tutorial, Course, Tool, Framework

---

## Global Navigation Components

### Primary Navigation Bar
```
Dashboard | Use Cases ▼ | Platforms ▼ | Research ▼ | Resources
```

### Use Cases Dropdown
```
Use Cases
├── Finance & Accounting
├── PE & M&A
├── Legal Tech
└── Manufacturing
```

### Platforms Dropdown
```
Platforms
├── ERP Systems (10)
└── EPM Systems (5)
```

### Research Dropdown
```
Research
├── White Papers (24)
└── Strategy Roadmaps (31)
```

---

## Filter Components

### Global Filters (appear on multiple views)
- **Type Toggle:** Code Repos | Vendor Products | All
- **Status Filter:** Active | Stale | Inactive
- **Search:** Full-text search across Name, Description

### Domain-Specific Filters
- **Category Dropdown:** Dynamic based on current view
- **Technology Filter:** Python, JavaScript, etc.
- **Date Range:** For research/updates

---

## Data Relationships

```
Executive Summary
    └── aggregates counts from all sheets

GitHub Repo Synopsis
    └── links to → Code Samples & Prompts

PE & M&A AI Use Cases
    ├── Code Repos section
    └── Vendor Products section

Legal Tech AI Repos
    ├── Code Repos section
    ├── Vendor Products section
    └── links to → Legal Tech Use Cases

Manufacturing & Distribution
    ├── Code Repos section
    ├── Vendor Products section
    └── links to → Mfg & Dist Finance Use Cases

Top 10 ERP AI Use Cases
    └── links to → ERP API Integration

Top 5 EPM AI Use Cases
    └── links to → EPM API Integration

AI Research & White Papers
    └── external links to sources

AI Strategy Roadmaps
    └── download links to PDFs
```

---

## API Endpoints (for future REST API)

```
GET /api/v1/dashboard/stats
GET /api/v1/dashboard/categorization

GET /api/v1/use-cases/finance?status=ACTIVE
GET /api/v1/use-cases/pe-ma?type=code-repos
GET /api/v1/use-cases/legal-tech?category=Contract+Analysis
GET /api/v1/use-cases/manufacturing?type=vendor-products

GET /api/v1/platforms/erp?system=SAP
GET /api/v1/platforms/epm

GET /api/v1/research/white-papers?source=McKinsey
GET /api/v1/research/roadmaps?format=PDF&year=2025

GET /api/v1/resources?type=Tutorial
```

---

## Update Frequencies

| Section | Update Frequency | Automation |
|---------|-----------------|------------|
| GitHub Repos | Daily | Automated via GitHub API |
| Research/White Papers | Daily | Web search |
| ERP/EPM Use Cases | Monthly | Manual review |
| Strategy Roadmaps | Monthly | Web search |
| Use Cases | As needed | Manual addition |

---

## File Locations

| Asset | Path |
|-------|------|
| Main Workbook | `AI_Use_Cases_Comprehensive_2026.xlsx` |
| Automation Tasks | `DAILY_AUTOMATION_TASKS.md` |
| Daily Update Skill | `.claude/skills/daily-ai-update/SKILL.md` |
| Excel Skill | `.claude/skills/excel/SKILL.md` |
| Python Script | `scripts/daily_update.py` |
| This Index | `WEB_INDEX.md` |

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total Sheets | 15 |
| Total Use Cases | 80+ |
| Code Repositories | 39 |
| Vendor Products | 41 |
| ERP Platforms | 10 |
| EPM Platforms | 5 |
| Research Articles | 24 |
| Strategy Roadmaps | 31 |
| Unique Sources | 50+ |
