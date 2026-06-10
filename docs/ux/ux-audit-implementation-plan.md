# TRACE UX Audit & Implementation Plan

**Date:** 2026-06-10  
**Source material:** Cognitive walkthrough (`docs/notes/6:10:26_12-31-cognitive walkthrough v1.rtf`) + full `app.py` code inspection + all data files  
**Status:** Awaiting implementation approval

---

## 1. Executive Summary

### Top 5 UX problems

| # | Problem | Impact |
|---|---|---|
| 1 | **Energy Debt is incomprehensible** | The score formula, progress bar, and badges are unexplained. A judge cannot understand what 0.74 means or why they should care. |
| 2 | **Agent Traces card icons are unreadable** | Cards show `🔡`, `⏱`, `💵`, `🌿`, `★` with no legend. Reviewer directly said "I don't know what these cards mean." |
| 3 | **Connect page has too many dead-end controls** | `⟳ Run Sync`, `↑ Upload File`, `📋 Norm Log` are toolbar buttons that do nothing. Source type buttons `Carbon Factors`, `Code / CI`, `Custom Source` are confusing noise for MVP. |
| 4 | **OpenTelemetry Collector and Webhook appear functional but are not** | Both connection methods appear as selectable radio options. Selecting either leads to a generic empty form. Reviewer noticed immediately. |
| 5 | **Methodology page coefficients have no provenance** | The table shows `kWh / 1M tokens` values with no explanation of where they come from. Reviewer explicitly said "I need to know where the model coefficients come from — I think they should be written out." |

### Top 5 fixes for judge understanding

| # | Fix |
|---|---|
| 1 | Add an `Energy Debt Explained` expander at the top of the Energy Debt tab with the formula, progress bar meaning, and badge definitions |
| 2 | Add a `Legend` panel above the Agent Graph: icon → meaning, color → severity |
| 3 | Disable `Run Sync`, `Norm Log`, `Upload File` toolbar buttons with clear `help=` text; remove `Carbon Factors`, `Code/CI`, `Custom Source` from drawer |
| 4 | Replace `OpenTelemetry collector` and `Webhook` radio options with a single `Coming soon` note |
| 5 | Add a `How these coefficients were derived` expander in Methodology with the 5-step derivation chain |

### Must-change before demo

- Disable/explain all dead-end buttons (Run Sync, Norm Log, Upload File, OpenTelemetry, Webhook)
- Add Agent Traces legend
- Add Energy Debt inline explainer
- Add "Assumptions behind this recommendation" section on each Optimize card
- Add coefficient provenance to Methodology page
- Rename `Methodology` in the sidebar nav to `Prove` to match the demo narrative (Connect → Observe → Optimize → Prove)

---

## 2. Question Inventory

| Page | User question / confusion | Plain-English answer | UX fix | Priority | Effort |
|---|---|---|---|---|---|
| Connect | "Is the assessment authorization file active or roadmap?" | It is a future capability — TRACE does not currently have SSO/auth at MVP | Remove or add "Coming Soon" label to any auth-related UI | Must fix | Small |
| Connect | "I want to get rid of AI/Works, LLM Observability spin-ups" | MVP should only show the 7 already-connected sources; the drawer is for adding more | Streamline the source type buttons to only the 3 demo-relevant types (LLM Observability, FinOps/Cloud Cost, Cloud Monitoring) | Must fix | Small |
| Connect | "OpenTelemetry collector doesn't seem to work / Webhook doesn't seem to work" | Both are planned connectors, not implemented in MVP | Replace those two radio options with `Coming soon — contact team to set up` text | Must fix | Small |
| Connect | "Prompt content storage — I don't know what that is. Store full prompt and response, store metadata only, store redacted" | This controls what TRACE saves when it ingests your AI logs. Full = keeps the actual words sent/received (privacy risk). Metadata only = keeps counts and scores, no text (safer). Redacted = keeps structure, blanks sensitive content. | Add a `ℹ️` inline below each option with 1-sentence explanation; add a note that `metadata only` is the default for privacy | Must fix | Small |
| Connect | "Tell me what file I should be uploading" | The FinOps upload expects a Cloudability CSV export matching the TRACE schema. A sample file lives at `docs/sample-data/finops_cloud_export.csv` | Add a `📎 Download sample file` link button in the FinOps upload drawer step | Must fix | Small |
| Connect | "Normalization — please explain how that works" | Normalization = TRACE reads each row of the uploaded data and checks if all required fields (app name, region, token count) match TRACE's schema. Rows that match are ready to use; rows that don't are flagged as unmapped | Add a 2-sentence explainer above the field mapping table | Must fix | Small |
| Connect | "I don't know if I like the Owner column" | Owner = the team responsible for this data source (so the right person knows if it goes stale) | Add a column tooltip: `The team responsible for keeping this source healthy. Shown in alerts when data goes stale.` | Should fix | Small |
| Connect | "Run Sync, Norm Log, Blend Log — those don't work" | In the MVP, these are UI affordances showing what a production tool would offer. They are not wired up to real sync jobs | Disable all 3 with `disabled=True` and add `help="In production TRACE: triggers a live re-sync of this source."` | Must fix | Small |
| Connect | "Action links (View/Sync, Fix Mapping) — do those work?" | They are currently plain text rendered inside an HTML table, not real Streamlit buttons | Either convert to disabled `st.button` elements or replace with static badges labeled "Simulated" | Must fix | Small |
| Observe — Dashboard | "I'd like to see a date toggle — daily, last 30 days, monthly" | The data covers May 2026 (30 days). A toggle is feasible but adds complexity. At minimum, make the period prominent. | Add a period indicator at the top: `📅 Period: May 2026 (30 days) · All figures month-to-date` | Should fix | Medium |
| Observe — Dashboard | "What is 'total footprint'?" | The combined cost, carbon, energy, and water of all AI inference + cloud infrastructure in your data | Add subtitle to "Total Footprint" section header: `"AI inference + cloud infrastructure combined, for the selected period"` | Must fix | Small |
| Observe — Dashboard | "What's the difference between AI inference and cloud infrastructure?" | AI inference = the cost and carbon of calling AI models (Claude, GPT-4) token by token. Cloud infrastructure = the servers, databases, and storage that your apps run on. | Add a collapsible `ℹ️ What's the difference between AI inference and cloud?` info block at the top of the Dashboard tab | Must fix | Small |
| Observe — Dashboard | "What is kWh and why does it matter?" | A kilowatt-hour (kWh) is the unit of electricity consumption. TRACE uses it as the bridge between token counts and carbon — tokens → kWh → kg CO₂e | Add `sub` text to the Energy KPI: `"electricity consumed by AI inference"` | Should fix | Small |
| AI Detail | "Why is Support-Bot the top offender?" | Support-Bot uses a large model (the most energy-intensive class) AND runs in ap-south (Mumbai), which has the dirtiest electricity grid in the dataset (630 gCO₂e/kWh vs 210 for Oregon). Large model + dirty grid = high carbon. | Expand the warning banner: `"Support-Bot uses a large model in ap-south (630 gCO₂e/kWh — India's grid) — 3× dirtier than Oregon. Large model × dirty grid × high WUE = the top optimization target."` | Must fix | Small |
| AI Detail | "I don't understand what the region charts show" | Each bar is a cloud region. Taller = more carbon/energy/water used in that region. The bar color shows the grid intensity — red = dirty electricity. | Add subtitle to each region chart: `"Bars show total AI carbon by region. Color = grid carbon intensity. Red = dirtiest electricity."` | Must fix | Small |
| AI Detail | "Why is ap-south high for water too?" | Mumbai data centres consume 1.8 litres of cooling water per kWh of compute (high WUE), partly due to climate and cooling technology. Oregon uses only 0.8 L/kWh. | Add a caption below the region water chart: `"Mumbai (ap-south) has WUE 1.8 L/kWh — 2× more water-intensive than Oregon. Shifting to us-west cuts both carbon and water."` | Must fix | Small |
| Agent Traces | "I don't know what these cards mean — icons, colors, numbers" | Each card = one step in an AI agent workflow. Border color shows health: green = clean, amber = some retries, red = many retries. Icons: 🔡 = tokens in→out, ⏱ = time, 💵 = cost, 🌿 = carbon, ★ = quality score | Add a `Legend` panel above the graph using `st.expander("🗺️ How to read this graph", expanded=True)` | Must fix | Small |
| Agent Traces | "What are retries and why do they matter?" | A retry is when an AI agent step failed or produced a rejected output and had to try again. Each retry burns extra tokens, energy, and money — and the cost is invisible in billing dashboards. | Add to the legend: `"Retries = wasted compute. A step that retried 3 times consumed up to 4× the expected tokens, cost, and carbon."` | Must fix | Small |
| Agent Traces | "See Optimize in the error banner — does that navigate?" | Currently it's just text in an `st.error()` string — it doesn't navigate | Change `→ See Optimize.` to a real `st.button` that navigates | Should fix | Small |
| Agent Traces | "Accepted/Rejected — what does that mean?" | Accepted = the output was used by the next step. Rejected = the output was discarded (quality too low). A rejected output still consumed energy and carbon. | Add to legend: `"✓ Accepted = output used. ✗ Rejected = output discarded. Rejected outputs still consumed tokens and carbon."` | Must fix | Small |
| Energy Debt | "I don't know what Energy Debt means" | Energy Debt = the combination of (a) how much carbon an app produces every month, and (b) how many code-level inefficiency patterns are found in its source code. High on both = fix this app first. | Add an `st.info()` explainer at the top of the tab | Must fix | Small |
| Energy Debt | "I don't understand what the progress bar is showing" | The progress bar shows the app's Energy Debt Score as a proportion of the maximum possible score (1.00). | Add a label above each progress bar: `Score: 0.74 / 1.00 · Higher = more urgent to address` | Must fix | Small |
| Energy Debt | "What do the badges mean — 'energy-debt', 'other findings', 'no Semgrep findings'?" | `energy-debt` = code patterns that directly waste CPU/GPU cycles. `other findings` = broader code issues. `No Semgrep findings` = no code scan results available. | Add badge legend in the explainer | Must fix | Small |
| Energy Debt | "How is code risk evaluated? It doesn't tell us" | Semgrep scans source code for patterns known to cause inefficiency — polling loops, redundant model calls, large context windows. Each matching pattern is a `finding`. | Add to the section header caption: `"Code risk = findings from a Semgrep static analysis scan."` | Must fix | Small |
| Energy Debt | "60% carbon, 40% code risk — I don't really know what that means" | The Energy Debt Score = 60% of the app's carbon rank + 40% of its code-risk rank. It's a blended priority score. | Show the formula breakdown on each card as a small line below the score | Must fix | Small |
| Optimize | "I need a list of the assumptions" | Key assumptions: 70% of Support-Bot traffic is routine summarization; 30% kept on large model for quality; region shift is technically feasible; quality impact is estimated, not measured | Add an `st.expander("📋 Assumptions behind this recommendation")` on each rec card | Must fix | Medium |
| Optimize | "Is Apply simulated or real?" | Apply is a live what-if simulation — it recalculates all KPIs as if the recommendation were in production. It does not change any real infrastructure. | Add a caption below the Apply button explaining it is a simulation | Must fix | Small |
| Optimize | "Cost unchanged but carbon drops — why?" | The Analytics-Agent recommendation moves a workload to a cleaner electricity grid (Oregon) but keeps the same model and volume. The provider charges the same per token regardless of region. | Add this explanation to the second recommendation rationale | Must fix | Small |
| Optimize | Where do the What-if table percentage multipliers come from? | Balanced = both recommendations at stated fractions. Aggressive = + illustrative batch shift. Both are illustrative projections. | Add a footnote beneath the What-If table | Should fix | Small |
| Prove/Evidence Pack | "Normalization percentage — it doesn't tell me. I don't see any question marks or explanations" | Normalization % = the proportion of records successfully mapped to TRACE's schema. | Replace `title=` hover tooltip with a visible `ℹ️` expander | Must fix | Small |
| Prove/Evidence Pack | "Where does it say Medium confidence?" | Medium confidence label is in the Calculation Summary blocks but is easy to miss | Add a prominent `st.info()` callout at the top of the Evidence Pack | Must fix | Small |
| Prove/Evidence Pack | "Can this be taken to a sustainability team or auditor?" | The methodology is auditable; the demo uses synthetic data. Production TRACE with live connectors produces a fully traceable evidence pack. | Add an explicit audit readiness note | Should fix | Small |
| Methodology | "I need to know where the model coefficients come from" | Derived from: NVIDIA A100 TDP, MLPerf benchmark throughput, server overhead multiplier, PUE | Add a `How these coefficients were derived` expander with the 5-step derivation chain | Must fix | Small |
| Methodology | "Standards alignment table feels decorative" | The table exists but the "How TRACE uses it" column is too brief — a judge can't learn from it | Expand each row to 2–3 sentences; add a short plain-English intro before the table | Should fix | Medium |
| Global | "I don't really see any question mark, no explanation anywhere" | Most jargon terms have no hover tooltip or expander in the current app | Systematic tooltip pass: add `help=` text to all `st.metric`/`st.button` calls | Must fix | Medium |
| Sidebar | `Prove` is called `Methodology` in nav but the page inside is called `Evidence Pack` | Naming inconsistency creates confusion | Rename sidebar nav item to `Prove` | Must fix | Small |

---

## 3. Page-by-Page UX Audit

### Connect

**What works**
- The 5 summary stat cards (7 systems, 4 live API, 3 static, 5 healthy, 2 warnings) give a fast orientation
- The status badge legend in the expander is good
- The FinOps file upload flow (upload → validate → field map → normalize) is the strongest demo flow
- Category tooltips on hover in the table are a nice touch
- The normalization success message is clear

**What is confusing**
- `⟳ Run Sync`, `↑ Upload File`, `📋 Norm Log` — three toolbar buttons that do nothing. No indication they're simulated.
- The Connect New System drawer shows 7 source type buttons. Three (`Carbon Factors`, `Code / CI`, `Custom Source`) have no plausible demo path.
- `OpenTelemetry collector` and `Webhook` appear as selectable radio options but lead to a generic empty form.
- No guidance on what file to upload for each source type until you're already in the flow.
- "Owner" column purpose isn't self-evident.
- "Normalization %" hover tooltip is invisible in most Streamlit modes.
- After uploading and normalizing, the Connected Systems table doesn't update.
- Prompt content storage options lack any explanation.

**What should be removed**
- `Carbon Factors` source type button from drawer
- `Code / CI` source type button from drawer
- `Custom Source` source type button from drawer
- `OpenTelemetry collector` and `Webhook` as selectable radio options

**What should be renamed**
- "Owner" column → "Responsible Team"
- "Normalization" column header → "Mapped %" with tooltip
- Action text links → disabled buttons

**Tooltips / helper text to add**
- Inline below section header: `"TRACE connects to your existing AI and cloud data sources. No new instrumentation required."`
- Each dead-end toolbar button: `disabled=True, help="In production TRACE, this triggers a live re-sync. Simulated in this MVP."`
- Prompt content storage: inline explanation per option
- Sample file download link in FinOps upload flow

---

### Observe — Dashboard tab

**What works**
- Three-section layout (Total Footprint, AI Inference, Cloud Infrastructure) is logical
- Daily carbon trend stacked area chart is effective
- Live updates when recommendations are applied
- KPI delta display (good = green) is clear

**What is confusing**
- No date filter — "May 2026" in the caption is easy to miss
- "Total Footprint" header has no subtitle
- "AI Inference" vs "Cloud Infrastructure" distinction is not explained
- "Traced Workflows" KPI sub-text `"from X total in ledger"` — "ledger" is unexplained
- Water KPI sub-text `"energy × WUE per region"` is a formula, not an explanation

**What should be renamed**
- "Traced Workflows" sub-text → `"sample workflows selected for agent-level analysis"`

**Tooltips/helper text**
- `st.info()` with `"📅 Showing: May 2026 (30 days) · Synthetic Northstar Bank data"` at the top
- Subtitle to Total Footprint section: `"Combined AI inference + cloud infrastructure for the period"`
- Water KPI sub-text → `"data centre cooling water used by AI inference"`

---

### AI Detail tab

**What works**
- Warning banner calling out Support-Bot by % is good
- Side-by-side Carbon/Cost bar charts are immediately legible
- Region chart with color scale (green→red) is effective
- Region data table at bottom is useful
- Caption `"Dirtiest grids drive carbon; hottest/driest regions drive water."` — keep it

**What is confusing**
- Warning banner says "Top candidate for optimization" but doesn't say WHY
- "By Model" section: 4 pie charts is too many for a 5-minute demo
- Region labels like `ap-south (630 g/kWh)` — a judge may not know what `g/kWh` means
- No caption explaining WHY ap-south has high water alongside high carbon

**What should be compressed**
- Compress "By Model" to 2 charts: Carbon by Model + Cost by Model only

**Tooltips/helper text**
- Expand warning banner to include: `"Support-Bot uses a large model in ap-south (630 gCO₂e/kWh — India's grid) — 3× dirtier than Oregon. Large model × dirty grid × high WUE = the top optimization target."`
- Add caption below water region chart: `"Mumbai (ap-south) data centres use 1.8 L of cooling water per kWh — more than double Oregon (0.8 L/kWh). The same region shift that cuts carbon also cuts water."`

---

### Agent Traces tab

**What works**
- Workflow selector dropdown is clear
- KPI row at the top is good
- Error banner calling out the highest-retry step is good
- Span Details table captures the right columns

**What is confusing**
- No legend — card icons (🔡, ⏱, 💵, 🌿, ★) are unexplained
- Border colors (green/amber/red) are not labeled
- `✓ Accepted` / `✗ Rejected` on cards — not explained
- `★ 0.91` — eval score, not labeled as such on the card
- `→ See Optimize.` in the error banner is static text, doesn't navigate
- Span Details `CO₂e (kg)` shows 4 decimal places with very small numbers
- No explanation of what a "workflow trace" is

**What should be renamed**
- `CO₂e (kg)` in span table → `Carbon CO₂e (kg)`

**Tooltips/helper text**
- Full legend expander (expanded=True) — see Section 5
- Tab caption: `"Each row below is one step in an AI agent workflow — showing the exact cost, carbon, and quality of every model call."`

**Buttons/flows to fix**
- Replace `→ See Optimize.` text with a real `st.button("→ Go to Optimize")` that navigates

---

### Energy Debt tab

**What works**
- Ranked card list (1–5) with color coding creates urgency hierarchy
- Code scan findings show actionable specifics (severity, file, fix)
- Error banner calling out the worst app score is good

**What is confusing**
- The entire tab needs an intro explaining what "Energy Debt" means — there is none
- Progress bar has no label — a judge sees a partial bar with no reference
- Score `0.74` next to label `ENERGY DEBT` means nothing without explanation
- Badges (`3 energy-debt`, `5 other findings`, `No Semgrep findings`) need a legend
- Formula `60% carbon rank + 40% code-risk rank` is in the caption but too cryptic
- "SDLC Energy Debt" — `SDLC` is jargon
- Connection between the ranked cards and the code scan findings below is not obvious

**What should be renamed**
- `"Code Scan Findings (SDLC Energy Debt)"` → `"Code Inefficiency Findings — What to Fix"` with subtitle `"From a Semgrep static analysis scan of the apps' source code"`

**Tooltips/helper text**
- Full `st.info()` explainer at top — see Section 5
- `Score: X.XX / 1.00 · Higher = more urgent` label below each progress bar
- Formula breakdown on each card: `"60% from carbon rank · 40% from code risk rank"`

---

### Optimize page

**What works**
- Pill badges (model swap, region shift with fraction) are clear
- Carbon % and Cost % pills are effective
- Quality trade-off note is a good design choice — keep it prominent
- Undo button per recommendation is correct
- Reset all in sidebar works
- Applied state summary (banner + metrics) is well done
- What-if table structure is good

**What is confusing**
- No "Assumptions behind this recommendation" section
- Apply button has no clarification that it's a simulation
- SDLC Energy Debt Fixes section — where do these come from? Not explained
- What-if percentage multipliers have no source explanation
- "Batch shift" in Aggressive row — unexplained

**Tooltips/helper text**
- `st.caption()` below Apply button (see Section 5)
- `st.expander("📋 Assumptions behind this recommendation")` per card
- Caption above SDLC section: `"These code fixes come from a Semgrep scan of the apps' source code. Fixing them reduces wasted compute at the code level, complementing the model/region optimizations above."`
- Footnote to What-if table: `"Balanced = both AI recommendations applied. Aggressive = + illustrative batch shift of off-peak workloads."`

---

### Prove / Evidence Pack tab

**What works**
- Before/After Comparison table is clear and live
- Applied Optimizations list (✅ with title) is clear
- Assumptions & Confidence block is comprehensive
- Download buttons (AI Ledger CSV, Cloud Ledger CSV) work correctly
- PDF export is correctly disabled with tooltip

**What is confusing**
- "Source Telemetry" section header — jargon
- Normalization % `title=` tooltip is invisible in most Streamlit modes
- "Medium" confidence is buried in a dense text block
- Before/After table when no recs applied — before and after show same numbers, looks broken
- "Audit readiness" is not explicitly addressed

**What should be renamed**
- "Source Telemetry" → "Connected Data Sources"

**Tooltips/helper text**
- `st.info()` at top: `"This Evidence Pack shows exactly where every number comes from — the formula, the data source, and the confidence level. It's what you'd share with a sustainability team or external auditor."`
- Replace nested `title=` tooltip on normalization % with visible `ℹ️` expander
- Medium confidence highlighted callout — see Section 5
- Explicit audit readiness note — see Section 5

---

### Methodology tab

**What works**
- Formula code block is clean and comprehensive
- Standards Alignment table has live links
- Honest Caveats section is appropriate
- Model Coefficients table is present
- Grid Intensity bar chart with color scale is effective

**What is confusing**
- Formula code block shows raw formulas with no plain-English explanation alongside them
- Standards Alignment "How TRACE uses it" column is too brief (1 phrase each)
- Model Coefficients `kWh / 1M tokens` values have no derivation explanation
- "Illustrative · blended from public GPU benchmarks" caption is too brief
- The page doesn't directly answer: "Can I trust these numbers?"

**What to add**
- Plain-English formula explainer box before the code block
- `How these coefficients were derived` expander (5-step chain) — see Section 5
- Expand each row of Standards Alignment to include a sentence of context

---

### Global / Navigation

**What works**
- Sidebar is clean and dark
- Synthetic data warning in sidebar footer is visible
- `✓ N recs applied` + `↩ Reset all` sidebar state is good
- Overall visual polish is high

**What is confusing**
- Sidebar nav shows `Methodology` but the page is called "Evidence Pack" internally
- No breadcrumb or story arc visible on any page
- The narrative `Connect → Observe → Optimize → Prove` is not visible anywhere

**Fixes**
- Rename nav item `Methodology` → `Prove`
- Add one-line story arc at the top of each page (current page highlighted)

---

## 4. Recommended App Updates

### P0 — Must fix for demo clarity

| ID | Change | Page |
|---|---|---|
| P0-1 | Disable `Run Sync`, `Norm Log`, `Upload File` with `disabled=True` + `help=` text | Connect |
| P0-2 | Remove `OpenTelemetry collector` and `Webhook` from connection method radio; replace with `Coming soon` note | Connect |
| P0-3 | Remove `Carbon Factors`, `Code / CI`, `Custom Source` from drawer source type buttons | Connect |
| P0-4 | Add `📎 Download sample file` link for FinOps upload | Connect |
| P0-5 | Add Agent Traces legend (expanded by default) | Observe → Agent Traces |
| P0-6 | Add `Energy Debt Explained` info block at top of Energy Debt tab | Observe → Energy Debt |
| P0-7 | Add progress bar label: `Score: X.XX / 1.00 · Higher = more urgent` | Observe → Energy Debt |
| P0-8 | Add score formula per card: `60% carbon rank · 40% code risk rank` | Observe → Energy Debt |
| P0-9 | Add `Assumptions behind this recommendation` expander per rec card | Optimize |
| P0-10 | Add caption below Apply button explaining it's a simulation | Optimize |
| P0-11 | Rename sidebar nav `Methodology` → `Prove` | Global |
| P0-12 | Add story arc line on each page: `Connect → Observe → Optimize → Prove` | Global |
| P0-13 | Add `Medium confidence` highlighted callout to Evidence Pack | Prove |
| P0-14 | Add coefficient derivation expander to Methodology tab | Methodology |
| P0-15 | Expand Support-Bot warning banner to explain WHY (model + region combination) | Observe → AI Detail |

### P1 — Should fix for judge confidence

| ID | Change | Page |
|---|---|---|
| P1-1 | Add `AI inference vs cloud infrastructure` explainer info box on Dashboard | Observe |
| P1-2 | Add date period indicator `📅 May 2026 · 30 days · Synthetic Northstar Bank data` | Observe |
| P1-3 | Make `→ See Optimize` a real navigation button in Agent Traces error banner | Agent Traces |
| P1-4 | Add caption to water region chart (Mumbai WUE explanation) | AI Detail |
| P1-5 | Add normalization % visible tooltip (not just `title=` hover) | Connect + Prove |
| P1-6 | Add audit readiness note to Evidence Pack | Prove |
| P1-7 | Rename "Source Telemetry" → "Connected Data Sources" | Prove |
| P1-8 | Rename "SDLC Energy Debt Fixes" → "Code Inefficiency Fixes" with Semgrep explainer | Optimize |
| P1-9 | Expand Standards Alignment table rows to 2–3 sentences each | Methodology |
| P1-10 | Add prompt content storage option explanations | Connect |
| P1-11 | Add `Responsible team` tooltip on Owner column | Connect |
| P1-12 | Compress "By Model" section to 2 charts (Carbon + Cost only) | AI Detail |

### P2 — Polish if time allows

| ID | Change | Page |
|---|---|---|
| P2-1 | Add daily/monthly period toggle | Observe |
| P2-2 | Add badge legend to Energy Debt badges | Observe |
| P2-3 | Add plain-English formula explainer before the code block | Methodology |
| P2-4 | Add What-if table footnote explaining Balanced vs Aggressive scenarios | Optimize |
| P2-5 | Rename "Owner" column → "Responsible Team" | Connect |
| P2-6 | Convert action column links to styled disabled buttons | Connect |

---

## 5. Proposed Copy

### Agent Traces legend (P0-5)

```
🗺️ How to read this graph

Each box is one step in an AI agent workflow — one call to a model.

Border color shows health:
  🟢 Green border   = Clean run (0 retries)
  🟡 Amber border   = Some retries (1–2)
  🔴 Red border     = High retries (3+)

Inside each box:
  🔡  Tokens in → Tokens out (input → output)
  ⏱   Latency (how long the step took)
  💵  Cost in USD for this step
  🌿  Carbon in kg CO₂e for this step
  ★   Eval score — output quality (0 = poor, 1 = perfect)
  ✓ Accepted / ✗ Rejected — was the output used?

⚠️ Retries = wasted compute.
A step that retried 3 times consumed up to 4× the expected tokens, cost, and carbon.
Retries are invisible in billing dashboards — TRACE surfaces them so you can fix the prompt.
```

### Energy Debt explainer info box (P0-6)

```
⚡ What is Energy Debt?

Energy Debt measures two things at once for each AI application:

1. Runtime carbon — how much CO₂e does this app's AI inference produce every month?
   (From Langfuse token data + regional grid intensity)

2. Code risk — how many energy-inefficiency patterns does the app's code contain?
   (From a Semgrep static analysis scan)

These two scores are blended:
   Energy Debt Score = 60% × carbon rank + 40% × code risk rank

A score of 1.00 = worst possible. The ranking tells your modernization team
exactly where to focus first — not "fix everything," but "start here."
```

### Assumptions expander — Support-Bot rec (P0-9)

```
📋 Assumptions behind this recommendation

• Traffic split: Analysis of Support-Bot's trace logs shows ~70% of requests are 
  routine one-step summarizations of customer support tickets. The remaining ~30% 
  involve complex multi-turn reasoning that benefits from a larger model.

• Model right-sizing: The small model class (0.3 kWh/1M tokens) handles summarization 
  tasks at equivalent quality to the large model class (1.2 kWh/1M tokens) for this 
  use case. Quality trade-off is stated explicitly: 30% of traffic stays on the large 
  model to protect complex-query accuracy.

• Region availability: The small model class is available in us-west-2 (Oregon) via 
  the same provider. No re-architecture is required — only routing configuration.

• Cost model: Token pricing applies equally in both regions. Cost reduction comes 
  entirely from the model swap (large → small = 30× cheaper per token for the 70% 
  shifted). Region shift alone would not affect cost.

• These are estimates. Production TRACE would validate these assumptions with the 
  engineering team before applying changes.
```

### Assumptions expander — Analytics-Agent rec (P0-9)

```
📋 Assumptions behind this recommendation

• Carbon-only optimization: This recommendation moves Analytics-Agent from us-east-1 
  (Virginia, 380 gCO₂e/kWh) to us-west-2 (Oregon, 210 gCO₂e/kWh). The same model, 
  the same volume. The grid is simply 45% cleaner.

• No cost impact: Token pricing for this model class is identical in both regions. 
  Cost is unchanged.

• No quality impact: This is a pure infrastructure routing change — the model and 
  workload are unchanged. Quality risk: None.

• Water reduction: Oregon's WUE (0.8 L/kWh) vs Virginia's (1.2 L/kWh) means this 
  shift also reduces water consumption by ~33%.

• Carbon-aware decisions aren't always about saving money. Sometimes the right move 
  is simply choosing the cleaner grid.
```

### Apply button caption (P0-10)

```
⚡ Apply runs a live what-if simulation — it recalculates all metrics as if this 
change were in production. Nothing in your real infrastructure changes. 
Use ↩ Reset all in the sidebar to restore the baseline.
```

### Energy Debt progress bar label (P0-7)

```
Score: {score:.2f} / 1.00  ·  {score*100:.0f}% of maximum Energy Debt
Higher score = more urgent to address
```

### Coefficient derivation expander (P0-14)

```
📐 How these coefficients were derived

Step 1 — GPU power draw
  NVIDIA A100 GPU: ~400W TDP (max power under load)
  NVIDIA H100 GPU: ~700W TDP
  Source: NVIDIA published hardware specifications

Step 2 — Token throughput
  Large model on A100: ~1,000 tokens/second (inference)
  Source: MLPerf Inference Benchmark Suite (MLCommons, 2023)

Step 3 — Energy per token
  400W ÷ 1,000 tokens/sec = 0.4 Wh/token = 0.0004 kWh/token
  Per million tokens = 400 kWh

Step 4 — Server overhead + PUE
  × 1.5 (server overhead: cooling, memory, other components)
  × 1.2 (Power Usage Effectiveness — data centre overhead)
  = ~720 kWh per million tokens for a large model on A100

Step 5 — Blended estimate
  Blending A100 and H100 fleets, utilization ~80%:
  Large model class: 1.2 kWh / 1M tokens  ✓
  Mid model class:   0.6 kWh / 1M tokens  (half of large)
  Small model class: 0.3 kWh / 1M tokens  (quarter of large)

Why "Medium confidence"?
  No AI provider publishes per-call energy data. These are benchmarked estimates.
  When providers publish real data, TRACE can replace these with measured values.
  Until then, the estimates are documented, reproducible, and challengeable.
```

### Dashboard — AI vs Cloud explainer (P1-1)

```
ℹ️ What's the difference between AI inference and cloud infrastructure?

AI inference = the energy and carbon of calling an AI model — 
every prompt sent to Claude, GPT-4, or similar. Measured in tokens; 
tracked via Langfuse or an AI gateway.

Cloud infrastructure = the servers, databases, and networking that 
your applications run on — the "compute and storage" layer. Measured 
in kWh from cloud billing exports; tracked via CCF methodology.

They're tracked separately because they have different optimization levers:
  AI inference  → model choice, routing, prompt efficiency
  Cloud infra   → right-sizing, region, reserved capacity
```

### Evidence Pack — Medium confidence callout (P0-13)

```
ℹ️ Confidence: Medium for AI carbon estimates

AI inference carbon is estimated, not metered. Here's why:

• We know the token counts precisely (from Langfuse / AI billing).
• We estimate energy using GPU benchmarks (kWh per million tokens).
• We apply regional grid intensity from Electricity Maps / EPA eGRID.

The uncertainty is in step 2 — no AI provider publishes per-call energy data.
"Medium confidence" means: the methodology is sound, the inputs are real, 
but the energy conversion is a calibrated estimate, not a power-meter reading.

This is a stronger basis than most sustainability reporting, which uses 
Scope 2 market-based estimates that can be offset to near-zero.
TRACE uses location-based accounting — no offsets, just physics.
```

### Evidence Pack — Audit readiness note (P1-6)

```
📋 Audit readiness

What you CAN take to a sustainability team:
  ✓ The methodology (formula, coefficients, sources)
  ✓ The confidence level and its explanation
  ✓ The before/after comparison showing optimization impact
  ✓ The standards alignment (SCI-for-AI, ISO 21031, GHG Protocol)

What requires production TRACE (live data):
  ⚠️ This demo uses synthetic Northstar Bank data — not real usage logs
  ⚠️ Production TRACE with live connectors produces a fully traceable 
     evidence pack with actual token counts, timestamps, and model names

A production audit pack carries the same methodology with real data,
making it defensible to a GHG Protocol-aligned sustainability audit.
```

### Connect — Prompt content storage explanations (P1-10)

```
Store full prompt / response
  TRACE saves the complete text of every AI request and response.
  ⚠️ Only use this if prompt content is non-sensitive and your data 
  governance policy permits it.

Store metadata only  (default — recommended)
  TRACE saves token counts, model, latency, cost, and eval scores — 
  but NOT the actual text. All carbon and cost calculations work with 
  metadata only. Best choice for most teams.

Store redacted prompt / response
  TRACE saves the text with PII automatically removed (names, 
  account numbers, etc.). Requires a redaction filter to be configured.
```

### Page story arc (P0-12)

Add this as a single styled line at the top of each page, with the current page highlighted.  
Example HTML for the Connect page:

```html
<div style="font-size:11px;color:#94a3b8;margin-bottom:16px;">
  <b style="color:#4edea3;">Connect</b>
  <span style="color:#334155"> → Observe → Optimize → Prove</span>
</div>
```

---

## 6. Implementation Plan

### Phase 1 — Quick clarity fixes (< 2 hours, zero risk)
*Labels, captions, `disabled=True`, `help=` text. Touches only additive lines in `app.py`.*

- Rename sidebar nav `Methodology` → `Prove`
- Add page story arc line to all 4 pages
- Disable `Run Sync`, `Norm Log`, `Upload File` with `help=` text
- Add Apply button caption (simulation warning)
- Add date period indicator to Observe Dashboard
- Rename "Source Telemetry" → "Connected Data Sources" on Prove tab
- Add Medium confidence `st.info()` to Evidence Pack
- Rename "SDLC Energy Debt Fixes" section header in Optimize
- Add audit readiness note to Evidence Pack
- Add `📎 Download sample file` link for FinOps upload

### Phase 2 — Page-level explainers (2–3 hours, low risk)
*New `st.info()`, `st.expander()`, `st.caption()` blocks. No logic changes.*

- Add Agent Traces legend expander (`expanded=True`)
- Add Energy Debt explainer `st.info()` at top of tab
- Add Energy Debt score formula to each card
- Add progress bar label
- Expand Support-Bot warning banner (WHY explanation)
- Add AI vs Cloud explainer `st.expander()` on Dashboard
- Add prompt content storage explanations inline
- Add Mumbai WUE caption to water region chart

### Phase 3 — Interaction cleanup (1–2 hours, low risk)
*Removing/simplifying source type buttons and radio options.*

- Remove `Carbon Factors`, `Code / CI`, `Custom Source` from drawer source type buttons
- Replace `OpenTelemetry collector` and `Webhook` radio options with `st.info("Coming soon")`
- Convert action column links to disabled buttons (or static badge text)
- Add `→ Go to Optimize` navigation button in Agent Traces error banner

### Phase 4 — Methodology/Evidence credibility (2–3 hours, medium risk)
*New expanders, expanding existing text blocks. Only additive changes.*

- Add `How these coefficients were derived` expander (full derivation chain)
- Expand Standards Alignment rows to 2–3 sentences each
- Add plain-English formula explainer before the code block
- Add assumptions expanders to both recommendation cards

### Phase 5 — Demo polish (1 hour, low risk)

- Compress "By Model" section to 2 charts
- Add badge legend to Energy Debt badges
- Add What-if table footnote
- Final walkthrough check: read every page cold as if you're a judge

---

## 7. Files to Modify

| File | What needs to change | Why it matters | Risk |
|---|---|---|---|
| `app.py` | All changes above — labels, `st.info()`, `st.expander()`, `disabled=True`, removed buttons, new captions | Only file in the entire app | Medium — 1,430 lines but all changes are additive; no calculation or data loading logic changes |
| `docs/sample-data/recommendations.json` | Add `assumptions` array to each recommendation object | Assumptions expander can read structured data from JSON instead of being hardcoded | Low |

All `app.py` changes are **additive** — inserting new Streamlit UI elements without touching calculation logic or data loading. The only structural changes are removing 3 source type buttons from the drawer and 2 radio options from the connection method list.

---

## 8. Acceptance Criteria

The UX update is done when all of the following are true:

- [ ] Every question from the cognitive walkthrough is answered somewhere visible in the app
- [ ] All 5 KPI labels on Dashboard have helper sub-text or tooltip
- [ ] `Run Sync`, `Norm Log`, and `Upload File` toolbar buttons are disabled with explanatory `help=` text
- [ ] `OpenTelemetry collector` and `Webhook` connection options are replaced with a `Coming soon` note
- [ ] Agent Traces graph has a visible legend (expanded by default) explaining all icons and colors
- [ ] Energy Debt tab has an intro explainer that a non-technical judge can read in 30 seconds
- [ ] Each Energy Debt card shows the score formula (`60% carbon rank + 40% code risk rank`) and a labeled progress bar
- [ ] Both Optimize recommendation cards have an `Assumptions` expander
- [ ] Apply button has a caption explaining it is a what-if simulation
- [ ] Support-Bot warning banner explains WHY (large model + dirty grid + high WUE), not just THAT it's the top offender
- [ ] Methodology tab has a `How these coefficients were derived` expander with the 5-step chain
- [ ] Medium confidence is prominently explained (not buried in a text block) on the Evidence Pack tab
- [ ] Sidebar nav reads `Prove` (not `Methodology`)
- [ ] Story arc `Connect → Observe → Optimize → Prove` is visible on every page
- [ ] A judge can complete the 5-minute demo walkthrough without clicking a dead-end button or asking "what does this mean?"
