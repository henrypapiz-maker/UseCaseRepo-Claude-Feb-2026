---
name: daily-ai-update
description: Run daily AI Use Cases workbook update. Checks GitHub repos for activity, searches for new AI research articles, and updates the Excel workbook.
allowed-tools: Read, Write, Edit, Bash, WebSearch, WebFetch, Glob, Grep
argument-hint: [--full | --repos-only | --research-only]
---

# Daily AI Use Cases Workbook Update

You are running the daily automation routine to update the AI Use Cases Comprehensive 2026 workbook.

## Execution Steps

### Step 1: Check GitHub Repository Activity

Check the following repositories for updates (last push date, stars, activity):

**Finance AI Repos:**
1. AI4Finance-Foundation/FinRobot
2. vas3k/TaxHacker
3. hananedupouy/LLMs-in-Finance
4. georgezouq/awesome-ai-in-finance
5. The-AI-Alliance/deep-research-agent-for-finance
6. tinztwins/finllm-apps
7. kennethleungty/Finance-LLMs
8. firmai/financial-machine-learning

**Manufacturing/Distribution:**
9. frappe/erpnext
10. frePPLe/frepple

**Legal Tech:**
11. Open-Source-Legal/OpenContracts
12. LexPredict/lexpredict-lexnlp

For each repo, use WebFetch to check:
```
https://api.github.com/repos/{owner}/{repo}
```

Extract: pushed_at, stargazers_count, open_issues_count

Flag repos as:
- ACTIVE: pushed within last 30 days
- STALE: pushed 6-12 months ago
- INACTIVE: pushed >12 months ago

### Step 2: Search for New AI Research

Search for new articles published in the last 7 days:

**Search Queries:**
1. "generative AI enterprise 2026" site:deloitte.com OR site:mckinsey.com OR site:pwc.com
2. "AI agents finance accounting 2026"
3. "Microsoft Copilot research 2026"
4. "Google DeepMind paper 2025 2026"
5. "Anthropic Claude research 2026"
6. "Stanford HAI AI 2026"
7. "MIT CSAIL AI 2026"

For each new article found:
- Extract title, date, URL
- Write a 100-200 word synopsis
- Categorize as: Hyperscaler, Big 4, AI Studio, Academic, or Vendor

### Step 2b: Check Vendor Use Case Libraries

Search vendor use case libraries for new AI case studies:

**Cloud AI Platforms:**
- AWS Case Studies: https://aws.amazon.com/solutions/case-studies/ (filter: AI/ML)
- Google Cloud Customers: https://cloud.google.com/customers (filter: AI)
- Microsoft Customer Stories: https://customers.microsoft.com/en-us/search?sq=AI
- IBM Case Studies: https://www.ibm.com/case-studies (filter: AI)

**Enterprise Software:**
- Salesforce Customer Stories: https://www.salesforce.com/customer-stories/
- ServiceNow Customers: https://www.servicenow.com/customers.html
- Workday Customer Stories: https://www.workday.com/en-us/customer-stories.html
- SAP Customer Stories: https://www.sap.com/about/customer-stories.html

**RPA & Automation:**
- UiPath Case Studies: https://www.uipath.com/resources/automation-case-studies
- Automation Anywhere: https://www.automationanywhere.com/resources/customer-stories
- Blue Prism Case Studies: https://www.blueprism.com/resources/case-studies/
- Celonis Customers: https://www.celonis.com/customers/

**Data Platforms:**
- Snowflake Customers: https://www.snowflake.com/en/customers/
- Databricks Customers: https://www.databricks.com/customers
- Palantir Offerings: https://www.palantir.com/offerings/

**Finance-Specific:**
- BlackLine Case Studies: https://www.blackline.com/resources/case-studies/
- HighRadius Case Studies: https://www.highradius.com/resources/case-studies/
- Coupa Customers: https://www.coupa.com/customers

**AI Research Libraries:**
- Hugging Face Models: https://huggingface.co/models (filter: finance)
- Papers With Code: https://paperswithcode.com/ (search: finance, accounting)
- AI Multiple Research: https://research.aimultiple.com/

**Search queries for vendors:**
- "[Vendor] AI case study finance 2025 2026"
- "[Vendor] customer story automation accounting"
- "site:[vendor].com AI use case finance"

For relevant case studies found:
- Extract company name, vendor, use case description
- Note quantified benefits (%, hours saved, ROI)
- Categorize by functional area (AP, AR, Close, FP&A, etc.)

### Step 2c: Check PE & M&A AI Developments

Search for private equity and M&A AI developments:

**PE Deal Sourcing & Portfolio Platforms:**
- PitchBook: https://pitchbook.com/news/reports
- CB Insights: https://www.cbinsights.com/research/
- AlphaSense: https://www.alpha-sense.com/resources/
- Affinity: https://www.affinity.co/blog

**M&A Due Diligence AI Tools:**
- Kira Systems: https://www.litera.com/kira
- Datasite: https://www.datasite.com/en/resources
- DealRoom: https://dealroom.net/resources
- Hebbia: https://www.hebbia.ai/
- ToltIQ: https://toltiq.com/

**PE Thought Leadership:**
- BDO PE: https://www.bdo.com/insights/industries/private-equity
- EY Private Equity: https://www.ey.com/en_us/private-equity
- KPMG PE: https://kpmg.com/us/en/industries/private-equity.html
- Deloitte PE: https://www.deloitte.com/global/en/industries/private-equity.html

**Search queries for PE/M&A:**
1. "private equity AI due diligence 2026"
2. "M&A AI contract analysis tools"
3. "PE portfolio monitoring AI automation"
4. "deal sourcing AI 2026"
5. "VDR artificial intelligence"

For PE/M&A articles found:
- Extract use case type (deal sourcing, due diligence, portfolio monitoring, value creation)
- Note AI capabilities (NLP, ML, predictive analytics)
- Identify target platforms/tools
- Quantify benefits where available (% time reduction, deal acceleration)

### Step 2d: Check AI Strategy Roadmaps (Monthly)

Search for new AI strategy publications from major firms:

**Primary Sources:**
| Firm | URL | Focus |
|------|-----|-------|
| McKinsey | https://www.mckinsey.com/capabilities/quantumblack/our-insights | State of AI |
| Deloitte | https://www.deloitte.com/global/en/services/consulting/research/ | Tech Trends |
| Accenture | https://www.accenture.com/us-en/insights/technology | Technology Vision |
| BCG | https://www.bcg.com/capabilities/artificial-intelligence/insights | AI Radar |
| KPMG | https://kpmg.com/xx/en/our-insights/ai-and-technology.html | Global Tech Report |
| PwC | https://www.pwc.com/us/en/tech-effect/ai-analytics.html | AI Predictions |
| EY | https://www.ey.com/en_us/ai | AI Barometer |
| WEF | https://www.weforum.org/publications/ | Blueprint |

**Search queries:**
1. "[Firm] AI strategy PDF 2026"
2. "[Firm] AI roadmap report download"
3. "[Firm] generative AI enterprise PDF"

**Criteria for inclusion:**
- Free to download (no paywall)
- PDF or PPT format
- Minimum 5 pages
- Published within last 12 months

For qualifying documents:
- Record source firm, title, description
- Note page count and format
- Capture direct download URL
- Add to AI Strategy Roadmaps sheet

### Step 3: Update Excel Workbook

Use Python to update `AI_Use_Cases_Comprehensive_2026.xlsx`:

```python
from openpyxl import load_workbook

wb = load_workbook('AI_Use_Cases_Comprehensive_2026.xlsx')

# Update GitHub Repo Synopsis sheet
ws_repos = wb['GitHub Repo Synopsis']
# Update last update dates and status

# Add new research articles
ws_research = wb['AI Research & White Papers']
# Append new rows for new articles

# Update Executive Summary counts
ws_summary = wb['Executive Summary']

wb.save('AI_Use_Cases_Comprehensive_2026.xlsx')
```

### Step 4: Generate Summary Report

Create a summary of what was updated:

```
Daily Update Summary - {DATE}
==============================

GitHub Repos Checked: X
  - Active: X
  - Stale: X
  - New activity detected: [list repos]

Research Articles Found: X
  - Hyperscaler: X
  - Big 4: X
  - AI Studio: X
  - Academic: X

Excel Workbook: Updated
  - New rows added: X
  - Cells modified: X

Recommendations:
- [Any repos needing attention]
- [Any major announcements to highlight]
```

### Step 5: Commit Changes (if requested)

If changes were made:
```bash
git add AI_Use_Cases_Comprehensive_2026.xlsx
git commit -m "Daily update: {DATE} - {summary}"
git push
```

## Arguments

- `--full`: Run all steps (default)
- `--repos-only`: Only check GitHub repositories
- `--research-only`: Only search for new research articles
- `--no-commit`: Don't commit changes to git

## Output

The skill produces:
1. Updated Excel workbook
2. Console summary of changes
3. Git commit (unless --no-commit)
