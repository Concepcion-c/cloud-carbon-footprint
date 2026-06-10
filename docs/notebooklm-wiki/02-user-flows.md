# 02 — User Flows

> **Summary:** A plain-English, screen-by-screen walkthrough of everything a user can do in the TRACE app. This document explains what you see, what you can click, and what happens at each step.

---

## Overview of the app

The TRACE app has four pages, accessible from the left-hand sidebar:

| Page | Purpose |
|---|---|
| **Connect** | Shows all connected data sources; allows adding new ones |
| **Observe** | The main analytics dashboard — cost, carbon, energy, water by app, model, and region |
| **Optimize** | Recommendations for reducing cost and carbon; apply them live |
| **Prove** | Auditable evidence pack and methodology transparency |

The sidebar also shows the client context (**Northstar Bank — Digital Banking Modernization**) and a reset button (appears after applying recommendations).

Users move through the app in a natural left-to-right story: connect data → observe the footprint → optimise it → prove the results.

---

## Page 1: Connect

### What this page is for

The Connect page shows all the external systems that TRACE is drawing data from. It also lets you simulate adding a new data source — demonstrating how a real deployment would onboard a client's tools.

### What you see when you land on Connect

At the top of the page, five summary tiles show:
- **7 Connected Systems** — total number of active data sources
- **3 Live API** — systems connected via real-time API (AI/Works, Langfuse, Google Cloud Monitoring)
- **3 Static Uploads** — files that were manually uploaded (Cloudability Export, CCF Factors, Code Scan Findings)
- **5 Healthy** — sources that are connected and working normally
- **2 Warnings** — sources where data is incomplete, stale, or partially mapped (Datadog and Code Scan Findings)

Below the tiles, a line shows the last normalization run time and total records ingested.

### The connected systems table

A table lists all seven connected systems:

| System | Category | Type | Status |
|---|---|---|---|
| AI/Works Control Plane | AI delivery | API | Connected |
| Langfuse | LLM observability | API | Connected |
| Datadog | LLM observability | API | Warning |
| Cloudability Export | FinOps | Static CSV | Uploaded |
| Google Cloud Monitoring | Cloud monitoring | API | Connected |
| CCF Factors | Carbon methodology | Static CSV | Active |
| Code Scan Findings | SDLC sustainability | Static JSON | Warning |

Each row shows the system name, category, connection type, status badge, last sync time, number of records, normalization percentage, owner team, and an action link.

**Status colours mean:**
- Green (Connected/Active) — healthy and syncing
- Blue (Uploaded) — static file successfully loaded
- Yellow (Warning) — something needs attention
- Red (Failed) — not working (not shown in this demo)

### Adding a new data source (the Connect drawer)

Clicking **＋ Connect New System** opens a step-by-step drawer:

**Step 1 — Choose a source type.** Seven options: AI/Works, LLM Observability, Cloud Monitoring, FinOps / Cloud Cost, Carbon Factors, Code / CI, Custom Source.

**Step 2 — Choose a connection method.** Four options: API connection, File upload, OpenTelemetry collector, Webhook.

**What the Langfuse API flow looks like** (the most demo-relevant path):
- Click LLM Observability → API connection
- A form appears for: Host URL, Public Key, Secret Key (masked), Project ID
- Choose sync frequency (every 15 / 30 minutes, or hourly)
- Choose which data to ingest (Traces, Token usage, Cost, Latency, Eval scores, Prompt/response content)
- Choose prompt content storage (store full / metadata only / redacted) — this is the privacy control

**What the file upload flow looks like** (for the Cloudability / FinOps path):
- Click FinOps / Cloud Cost → File upload
- A form appears showing the expected fields
- Upload a CSV file
- TRACE validates the file, shows record count, flags missing fields
- A field mapping table appears showing how source fields map to the TRACE schema
- Click Save Mapping, then Run Normalization

**Available connectors (roadmap):** A collapsible section shows nine more connectors marked "Coming Soon": LangSmith, New Relic, CloudHealth, Flexera, Vantage, Finout, OpenTelemetry Collector, LiteLLM Gateway, Webhooks.

### Status reference

An expandable legend explains what each status badge means.

---

## Page 2: Observe

### What this page is for

Observe is the main analytics dashboard. It shows everything TRACE knows about the client's AI and cloud footprint, broken down in multiple ways. It has four tabs.

### Tab 1: Dashboard

**What you see:**

Three rows of summary tiles — Total Footprint, AI Inference, Cloud Infrastructure — each with metrics for cost, carbon, energy, water, and tokens.

**Example values from the demo data:**
- Total AI cost: ~$31,300/month
- Total AI carbon: ~794 kg CO₂e/month (approximately 72% of the combined total)
- AI water: calculated per region using data centre water efficiency factors

Below the tiles, a **Daily Carbon Trend chart** shows 30 days of carbon emissions as a stacked area chart. The dark green band is AI inference; the grey band is cloud infrastructure. The AI inference band is larger and growing.

**What changes after applying a recommendation:** The tiles update with before/after deltas in green (costs and carbon going down are shown as good news).

### Tab 2: AI Detail

**What you see first:** A yellow warning box identifying the worst offender:
> *"⚡ Support-Bot — 76% of AI carbon and 77% of AI cost. Top candidate for optimization."*

**Charts in this tab:**
- Carbon by App (horizontal bar chart) — Support-Bot dominates
- Cost by App (horizontal bar chart) — Support-Bot dominates
- Energy by App (horizontal bar chart)
- Water by App (horizontal bar chart)
- Carbon by Model / Cost by Model / Energy by Model / Water by Model (four pie charts)
- Carbon by Region / Energy by Region / Water by Region (three bar charts, colour-coded from green to red by grid intensity or WUE)

The region charts show why location matters: the Mumbai region (ap-south) has a grid intensity of 630 gCO₂e/kWh and a water intensity of 1.8 litres/kWh — the highest in the data set. Oregon (us-west) is 210 gCO₂e/kWh and 0.8 litres/kWh.

A caption reads: *"Dirtiest grids drive carbon; hottest/driest regions drive water. Region shift addresses both."*

**Full Detail table:** A sortable table showing every combination of App × Model × Region with cost, carbon, energy, water, and token counts.

### Tab 3: Agent Traces

**What this tab is for:** This tab shows individual AI agent workflows as step-by-step diagrams — like an X-ray of a single AI workload.

**What you see:**
- A dropdown to select a workflow trace (three available: Customer Account Service Generation, Payment Processor Integration Test, Legacy Code Reverse Engineering)
- Five summary tiles for the selected trace: Total Cost, Total Latency, Total Tokens, Total CO₂e, Total Water
- An **Agent Graph** — a horizontal flow diagram showing each step in the workflow as a coloured card connected by arrows

**What each card in the Agent Graph shows:**
- Agent name and model used
- Tokens in → tokens out
- Latency (seconds)
- Cost (USD)
- CO₂e (kg)
- Water (litres)
- Quality eval score
- Whether the output was accepted or rejected
- Retry count badge (green = clean, amber = 1–2 retries, red = 3+ retries)

**The retry alert:** If any agent step had retries, a red error banner appears identifying the worst offender and explaining the cost/carbon impact.

**Span Details table:** A full breakdown of every agent step with all metrics in a sortable table.

**Why this matters:** Agent retries are invisible in billing dashboards. Every retry burns extra tokens, energy, and carbon. TRACE surfaces them and quantifies the waste.

### Tab 4: Energy Debt

**What this tab is for:** Energy Debt ranks the client's applications by a combined score of runtime carbon waste and code-level inefficiency. It is TRACE's version of a "which app should we fix first?" prioritisation tool.

**The Energy Debt Score formula:**
> Score = 60% × runtime carbon rank + 40% × code-risk findings rank

**What you see:**
- A red banner identifying the worst-scoring app (Support-Bot)
- Five ranked app cards, each showing: rank number, app name, monthly carbon and cost, Energy Debt score (0–1.00), a score bar, and coloured badges for energy-debt findings and other code findings
- A Code Scan Findings section showing the top 4 findings from the code scan, with severity badges (HIGH / MEDIUM / LOW), fix recommendations, and file references

This tab answers the question: "If we had to modernise one app this quarter to get the best return on carbon and cost, which one is it?"

---

## Page 3: Optimize

### What this page is for

Optimize is where TRACE turns observations into actions. It shows specific recommendations and lets you apply them — with the dashboard updating live to show the impact.

### What you see before applying anything

**Two recommendation cards:**

**Card 1 — Right-size Support-Bot summarisation + shift region:**
- The rationale: Support-Bot is 76% of AI carbon and 77% of cost. 70% of its traffic is routine summarisation that works fine on a smaller, cheaper model. The remaining 30% (complex queries) stays on the large model.
- The actions: Swap 70% of traffic from `large` model to `small` model. Shift 70% of traffic from `ap-south` (Mumbai, 630 gCO₂e/kWh) to `us-west` (Oregon, 210 gCO₂e/kWh).
- Projected impact: Carbon −64.2% for Support-Bot, Cost −67.7%
- Quality trade-off (shown explicitly): *"30% of traffic kept on the large model in-region to protect answer quality on complex tickets."*

**Card 2 — Carbon-aware region shift for Analytics-Agent:**
- The rationale: The same workload, moved to a cleaner grid region.
- The action: Shift 100% of Analytics-Agent traffic from `us-east` (380 gCO₂e/kWh) to `us-west` (210 gCO₂e/kWh).
- Projected impact: Carbon −44.7%, Cost unchanged (token pricing is region-independent)
- This card demonstrates that carbon-aware decisions are not always about saving money — sometimes they are purely about doing the right thing.

**SDLC Energy Debt Fixes section:** Two code-level findings from the Energy Debt scan, with HIGH/MEDIUM severity badges and specific fix recommendations.

**What-If Scenario Planner table (read-only):** A three-row table comparing Current State, Balanced Optimisation (recommended), and Aggressive Carbon Mode — showing projected AI cost, total CO₂e, AI water, latency, and quality risk for each scenario.

### Applying a recommendation

**Action:** Click the **⚡ Apply** button on any recommendation card.

**What happens:**
1. A brief spinner appears ("Computing optimised footprint…")
2. The page reloads with:
   - A green success banner showing the total impact (e.g., "AI carbon: −49%, AI cost: −52%")
   - Four before/after metric tiles (AI Cost before/after, AI Carbon before/after)
   - The applied card turns green with a ✅ icon
   - The Apply button changes to an **↩ Undo** button

**What changes across the app:** Because the app recalculates all metrics when a recommendation is applied, the Observe Dashboard and Prove pages also update to reflect the new numbers. This shows that TRACE is not just showing static projections — it is recomputing the entire footprint with the optimisation applied.

**Undoing:** Clicking ↩ Undo on any card reverses its effect. The **↩ Reset all** button in the sidebar resets everything to the baseline in one click.

---

## Page 4: Prove

### What this page is for

Prove is the evidence and transparency layer. It is the auditable record that a client could share with their sustainability team, auditor, or board.

### Tab 1: Evidence Pack

**Left column — Source Telemetry:** A list of all 7 connected data sources with record counts and normalization percentages. This shows where every number came from.

**Left column — Calculation Summary:** Two evidence blocks showing the exact formulas used for AI inference carbon and cloud infrastructure carbon, with scope (number of apps, models, regions), time period, and confidence level.

**Right column — Before / After Comparison:** A live table (updates when recommendations are applied) showing before and after values for: AI Cost, AI Carbon, AI Energy, AI Water, Cloud Cost, Cloud CO₂e, Cloud Water, Total Cost — with percentage change in each row.

**Right column — Applied Optimizations:** A list of any recommendations that were applied, with ✅ checkmarks.

**Export buttons:**
- **📥 Download AI Ledger CSV** — exports the AI inference data with all calculated fields
- **📥 Download Cloud Ledger CSV** — exports the cloud infrastructure data with carbon figures
- **📄 Evidence Pack PDF** — marked as "on roadmap" (not yet built)

### Tab 2: Methodology

**Left column — SCI-for-AI Carbon Formula:** A dark code block showing all four formulas in the app:
```
AI carbon  = (tokens / 1,000,000) × kWh_per_1M_tokens × grid_gCO₂e_per_kWh
AI cost    = (tokens / 1,000,000) × USD_per_1M_tokens
Cloud carbon = usage_kWh × grid_gCO₂e_per_kWh
Energy Debt Score = 0.6 × carbon_rank + 0.4 × code_risk_rank
```

**Left column — Standards Alignment table:** Shows six standards TRACE aligns to (SCI-for-AI, ISO 21031, OpenTelemetry GenAI, Langfuse trace schema, CCF output schema, Semgrep JSON).

**Left column — Honest Caveats:** A bulleted list acknowledging what is estimated, what is approximate, and what would be different in a production deployment.

**Right column — Model Coefficients table:** Live data from `model_coefficients.csv` showing energy and cost per million tokens for each model class.

**Right column — Grid Intensity chart and table:** A horizontal bar chart (colour-coded green to red) and table showing the gCO₂e/kWh value for each region.

---

## The reset flow

The sidebar shows an **↩ Reset all** button whenever any recommendation has been applied. Clicking it instantly resets all metrics to the baseline state — useful for repeating the demo.

---

## Key takeaways

- The app tells a story from left to right: Connect (data in) → Observe (understand it) → Optimize (act on it) → Prove (show the evidence)
- Every page is navigable from the sidebar; users can move freely between pages
- The "wow moment" is on the Optimize page — one click drops both cost and carbon by approximately half
- The Agent Traces tab is distinctive — it makes individual AI workflow steps visible with cost, carbon, and water per step
- The Prove page is designed to be a client-shareable deliverable, not just an internal view
