# 03 — Functionality Guide

> **Summary:** A complete list of every feature in the TRACE MVP, what each one does, what data it uses, and what it produces. Distinguishes between fully implemented features, simulated demo features, and planned roadmap features.

---

## Feature status labels

Throughout this document, features are labelled as:
- **✅ Implemented** — the feature is fully working in the current app
- **🎭 Simulated** — the feature looks real in the demo but uses synthetic data or scripted behaviour
- **🗺️ Roadmap** — the feature is shown as coming soon or described in the PRD but not yet built

---

## Connect page features

### Connected systems dashboard ✅ Implemented

**What it does:** Displays all data sources as a live-status table, showing connection type, status, last sync time, record count, normalization percentage, and owner team.

**Data used:** Hard-coded `CONNECTOR_STATE` list in `app.py`. In a production deployment, this would be populated from live connector status APIs.

**Output:** A table of 7 systems with colour-coded status badges.

**Note:** The status values (12 min ago, 1 hr ago, etc.) are static strings in the demo. They do not update in real time.

---

### Summary health tiles ✅ Implemented

**What it does:** Calculates and displays five aggregate counts from the connector state list: total systems, live API count, static upload count, healthy count, warning count.

**Data used:** `CONNECTOR_STATE` list in `app.py`.

**Output:** Five summary cards at the top of the Connect page.

---

### Connect New System drawer ✅ Implemented

**What it does:** Opens a multi-step onboarding drawer for connecting a new data source.

**Steps:**
1. Source type selection (7 options)
2. Connection method selection (API connection, File upload, OpenTelemetry collector, Webhook)
3. Source-specific form (e.g., Langfuse API credentials form, or file upload with validation)
4. Field mapping table (shown after file upload)
5. Save Mapping and Run Normalization buttons

**Data used:** The Cloudability file upload path reads the uploaded CSV using `pandas.read_csv()` and counts records and missing fields. The Langfuse API path shows a form but does not make any real API calls.

**Output:** If Run Normalization is clicked, a success message appears and the drawer closes. This is a simulated completion in the demo.

---

### File upload with validation 🎭 Simulated

**What it does:** Accepts a CSV file upload, reads it with pandas, counts records, and flags missing required fields.

**Data used:** The uploaded file (if any). The `finops_cloud_export.csv` in the sample data folder is the file designed for this demo path.

**Output:** A validation summary showing record count and any missing field warnings.

**Note:** The normalization step (Run Normalization button) shows a spinner and success message but does not actually process the file into the dashboard.

---

### Available connectors roadmap tiles 🗺️ Roadmap

**What it does:** Displays 9 additional connector tiles marked "Coming Soon" — LangSmith, New Relic, CloudHealth, Flexera, Vantage, Finout, OpenTelemetry Collector, LiteLLM Gateway, Webhooks.

**Output:** A visual roadmap for stakeholders showing planned integrations.

---

### Status legend ✅ Implemented

**What it does:** Expandable reference explaining what each status badge colour means.

---

## Observe page features

### Total Footprint KPI cards ✅ Implemented

**What it does:** Displays five summary metrics for the combined AI + cloud footprint: Total Cost, Total Carbon, Total Energy, Total Water, Total Tokens.

**Data used:** `ai_curr` and `cloud_calc` DataFrames computed from the synthetic CSVs and the current recommendation state.

**Output:** Five KPI cards. If recommendations have been applied, the cost and carbon cards show before/after delta in green.

---

### AI Inference KPI cards ✅ Implemented

**What it does:** Displays five AI-specific metrics: AI Cost, AI Carbon, AI Energy, AI Water, Traced Workflows.

**Data used:** `ai_curr` (AI inference calculations), `trace_data` (for workflow count).

**Output:** Five KPI cards with optional delta display.

---

### Cloud Infrastructure KPI cards ✅ Implemented

**What it does:** Displays four cloud-specific metrics: Cloud Cost, Cloud Carbon, Cloud Energy, Cloud Water.

**Data used:** `cloud_raw` and `cloud_calc` DataFrames.

**Output:** Four KPI cards. Cloud metrics do not change when AI recommendations are applied.

---

### Daily Carbon Trend chart ✅ Implemented

**What it does:** Plots 30 days of carbon emissions as a stacked area chart with two bands: AI Inference and Cloud Infra.

**Data used:** Daily aggregates from `ai_curr` and `cloud_calc`.

**Output:** An interactive Plotly area chart. The chart updates when recommendations are applied (AI band shrinks).

---

### Worst-offender warning banner ✅ Implemented

**What it does:** Automatically identifies the app with the highest AI carbon footprint and displays it as a warning at the top of the AI Detail tab.

**Data used:** `by_app` DataFrame (aggregated from `ai_curr`).

**Output:** A yellow warning box naming the top offender and its share of total AI carbon and cost.

---

### Carbon, cost, energy, and water by app (bar charts) ✅ Implemented

**What it does:** Four horizontal bar charts showing each metric broken down by application name.

**Data used:** `by_app` DataFrame.

**Output:** Four interactive Plotly charts. Bars reorder when recommendations are applied.

---

### Carbon, cost, energy, and water by model (pie charts) ✅ Implemented

**What it does:** Four donut charts showing each metric broken down by model class (large, mid, small).

**Data used:** `by_model` DataFrame (aggregated from `ai_curr`).

**Output:** Four interactive Plotly pie charts.

---

### Carbon, energy, and water by region (bar charts) ✅ Implemented

**What it does:** Three colour-coded bar charts showing each metric by cloud region. Bars are coloured by grid intensity (carbon) or WUE (water) — green for clean/efficient, red for dirty/water-intensive.

**Data used:** `by_region` DataFrame (merged with `grid` lookup table).

**Output:** Three interactive Plotly charts plus a summary table.

---

### Full Detail table (App × Model × Region) ✅ Implemented

**What it does:** A sortable, full breakdown table showing every combination of app, model, and region with cost, carbon, energy, water, and token counts.

**Data used:** `ai_curr` grouped by app, model, region.

**Output:** A Streamlit DataFrame widget.

---

### Workflow trace selector ✅ Implemented

**What it does:** A dropdown allowing the user to select one of three synthetic agent workflow traces to inspect.

**Data used:** `trace_data` loaded from `llm_trace_export.json`.

**Output:** Populates the trace summary KPIs and Agent Graph for the selected workflow.

---

### Agent Graph (trace visualisation) ✅ Implemented

**What it does:** Renders a horizontal flow diagram showing each agent step in the selected workflow as a colour-coded card connected by arrows.

**Card colours:**
- Green border — no retries (clean run)
- Amber border — 1–2 retries
- Red border — 3+ retries

**Each card shows:** agent name, model, token counts, latency, cost, CO₂e, water, eval score, accepted/rejected status, retry badge.

**Data used:** `spans` array from the selected trace in `llm_trace_export.json`. CO₂e and water per span are calculated using `MODEL_KWH_PER_1M` and `REGION_CARBON_KG` constants in `app.py`.

**Output:** An HTML flow diagram rendered with `unsafe_allow_html=True`.

---

### Retry alert banner ✅ Implemented

**What it does:** Identifies the agent step with the highest retry count and displays a red error banner naming it, its cost and carbon impact, and a recommendation to investigate.

**Data used:** `spans` array from the selected trace.

**Output:** A red Streamlit error box with specific numbers.

---

### Span Details table ✅ Implemented

**What it does:** A full per-step table for the selected trace, showing agent name, model, region, token counts, latency, cost, energy, CO₂e, water, eval score, retries, and accepted status.

**Data used:** `spans` array from the selected trace.

**Output:** A Streamlit DataFrame.

---

### Energy Debt ranking ✅ Implemented

**What it does:** Calculates a 0–1.00 Energy Debt Score for each app (60% runtime carbon rank + 40% code-risk findings rank) and displays them as ranked cards.

**Data used:** `ai_base` DataFrame for runtime carbon; `semgrep_findings.json` for code-risk findings; path-to-app mapping logic in `app.py`.

**Output:** Five ranked app cards with score bars and finding badges.

---

### Code Scan Findings list ✅ Implemented

**What it does:** Displays the top 4 code scan findings from the synthetic code scan data, with severity badges, finding descriptions, fix recommendations, and file references.

**Data used:** `code_scan_findings.json` (synthetic data).

**Output:** Four finding cards with HIGH/MEDIUM/LOW severity badges.

**Note:** These are synthetic findings, not the result of a real Semgrep scan on any codebase.

---

## Optimize page features

### Recommendation cards ✅ Implemented

**What it does:** Displays each recommendation as a card showing the rationale, the specific actions (model swap and/or region shift), the projected carbon and cost impact for the target app, and the quality trade-off.

**Data used:** `recommendations.json` (hand-authored synthetic data); `ai_base`, `coeffs`, `grid` DataFrames for real-time impact calculation.

**Output:** Two recommendation cards with action pills and projected impact labels. The impact percentages are calculated live from the data — not hardcoded.

---

### Apply recommendation ✅ Implemented

**What it does:** When the Apply button is clicked, TRACE recalculates the entire AI footprint with the recommendation's actions applied, then updates all affected metrics across the app.

**How it works (simplified):** The `apply_all_recs()` function in `app.py` takes the LLM usage DataFrame, splits the affected app's traffic according to the recommendation's `fraction` parameter, applies the model swap and/or region shift to the specified fraction, recalculates all energy/carbon/cost/water metrics, and returns a new DataFrame. All downstream KPIs and charts use this recalculated DataFrame.

**Data used:** `llm_raw`, `coeffs`, `grid`, `recommendations.json`.

**Output:** Updated KPI tiles, success banner with delta percentages, card turns green.

---

### Undo recommendation ✅ Implemented

**What it does:** Removes a recommendation from the applied set and recalculates the footprint without it.

**Output:** Metrics revert to the state before that recommendation was applied.

---

### Reset all ✅ Implemented

**What it does:** Clears all applied recommendations and resets all metrics to baseline.

**Output:** All cards revert to unapplied state; all metrics return to baseline values.

---

### SDLC Energy Debt fix cards ✅ Implemented

**What it does:** Shows the top 2 code-level findings as actionable fix cards with severity, description, recommendation, and file path.

**Data used:** `code_scan_findings.json`.

**Output:** Two fix cards.

---

### What-If Scenario Planner table ✅ Implemented

**What it does:** Displays a static three-row comparison table for Current State, Balanced Optimisation, and Aggressive Carbon Mode — showing projected AI cost, CO₂e, water, latency, and quality risk.

**Data used:** Hardcoded percentage multipliers (balanced: cost −20.5%, carbon −16.1%; aggressive: cost −28%, carbon −26.5%) applied to the baseline numbers.

**Output:** A formatted HTML table.

**Note:** This table is static (not affected by the Apply buttons). It is a planning view, not a live recalculation.

---

## Prove page features

### Source Telemetry block ✅ Implemented

**What it does:** Lists all 7 connected sources with their record counts and normalization percentages, with coloured status icons.

**Data used:** `CONNECTOR_STATE` list in `app.py`.

**Output:** A formatted evidence block.

---

### Calculation Summary block ✅ Implemented

**What it does:** Shows the exact formulas used for AI inference carbon and cloud infrastructure carbon, with scope, time period, and confidence level.

**Data used:** Formula strings and counts from `llm_raw` and `cloud_raw` DataFrames.

**Output:** Two evidence blocks with formula, scope, and confidence information.

---

### Before / After Comparison table ✅ Implemented

**What it does:** A live table showing before and after values for eight metrics (AI Cost, AI Carbon, AI Energy, AI Water, Cloud Cost, Cloud CO₂e, Cloud Water, Total Cost) with percentage change. Updates in real time when recommendations are applied.

**Data used:** `base_*` and `curr_*` variables computed throughout `app.py`.

**Output:** A formatted comparison table. Delta values are green for improvements (reductions in cost/carbon/water) and red for increases.

---

### Applied Optimizations list ✅ Implemented

**What it does:** Lists the titles of all recommendations that have been applied, with ✅ checkmarks.

**Output:** A list or a "No optimisations applied yet" message.

---

### Download AI Ledger CSV ✅ Implemented

**What it does:** Generates a downloadable CSV of the AI inference data with all calculated fields (date, app, model, provider, region, tokens, cost, energy, CO₂e).

**Data used:** `ai_curr` DataFrame with renamed columns and a "source" column added.

**Output:** `trace_ai_ledger.csv` download.

---

### Download Cloud Ledger CSV ✅ Implemented

**What it does:** Generates a downloadable CSV of the cloud infrastructure data with carbon figures.

**Data used:** `cloud_calc` DataFrame with renamed columns and a "source" column added.

**Output:** `trace_cloud_ledger.csv` download.

---

### Evidence Pack PDF 🗺️ Roadmap

**What it does:** Would generate a PDF export of the full evidence pack.

**Current state:** Button is present but disabled, labelled "PDF export on roadmap."

---

### Methodology tab ✅ Implemented

**What it does:** Shows the full SCI-for-AI formula, standards alignment table, honest caveats, model coefficients table, and grid intensity chart and table.

**Data used:** `coeffs` and `grid` DataFrames (from `model_coefficients.csv` and `grid_intensity.csv`).

**Output:** A two-column methodology reference page.

---

## Key takeaways

- All core features (data loading, calculations, recommendation engine, charts, downloads) are fully implemented
- The connector status and the Run Normalization flow are simulated for the demo — they look real but do not make live API calls
- The What-If Scenario Planner uses static multipliers, not live recalculation
- Code scan findings are synthetic and hand-authored, not the output of a real scan
- The PDF export and several planned connectors are roadmap items
