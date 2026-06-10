# TRACE Demo — User Journey

> **What this is:** A screen-by-screen walkthrough of every click and what appears in the app,
> mapped to the demo narrative. Use alongside `demo-script.md` (the presenter beat sheet).
> Client context loaded in the sidebar: **Northstar Bank — Digital Banking Modernization**.

---

## Before You Start

1. Run `streamlit run app.py` in the project folder.
2. Open the app full-screen in a browser.
3. Confirm the sidebar shows: **🌿 TRACE / AI GREENOPS DASHBOARD / 📁 Northstar Bank**.
4. The app opens on the **Connect** page by default. No data has been uploaded or changed yet.

---

## Stage 1 — Connect
**Story beat:** Show the judges that TRACE already knows where to find a client's data — and that connecting a new source is a deliberate, auditable step, not a black box.

### Step 1.1 — Land on Connect

**What the user sees:**
- Page title: **TRACE Connect: Data Sources**
- A row of five summary tiles: **7 Connected Systems · 3 Live API · 3 Static Uploads · 5 Healthy · 2 Warnings**
- Last normalization run: **12 minutes ago** · Total records ingested: **6,567**
- Three action buttons: **＋ Connect New System · ⟳ Run Sync · ↑ Upload File · 📋 Norm Log**
- A table of 7 connected systems with status badges:
  - 🟢 **AI/Works Control Plane** — API · Connected
  - 🟢 **Langfuse** — API · Connected
  - 🟡 **Datadog** — API · Warning
  - 🔵 **Cloudability Export** — Static CSV · Uploaded
  - 🟢 **Google Cloud Monitoring** — API · Connected
  - 🟢 **CCF Factors** — Static CSV · Active
  - 🟡 **Code Scan Findings** — Static JSON · Warning

**What to say:** *"This is Northstar Bank's data estate as TRACE sees it today. Seven sources already connected — live APIs pulling every 15–20 minutes, static exports uploaded. Two warnings tell us where data is stale or partially mapped. Everything is visible, nothing is hidden."*

---

### Step 1.2 — Demo the "Connect New System" flow

**Action:** Click **＋ Connect New System** (primary green button).

**What appears:** A drawer opens below the button with the heading **Connect New System**.

**Step A — Choose source type.** Seven source-type buttons appear in a row:
`AI/Works · LLM Observability · Cloud Monitoring · FinOps / Cloud Cost · Carbon Factors · Code / CI · Custom Source`

**Action:** Click **LLM Observability**.

**What appears:** The button highlights. Below it, the label **Source: `LLM Observability`** appears, along with four connection method radio buttons: `API connection · File upload · OpenTelemetry collector · Webhook`.

**Step B — Connection method.** The default selection is **API connection**.

**What appears:** A Langfuse-specific API form:
- Host URL field (`https://cloud.langfuse.com`)
- Public Key field (`pk-lf-...`)
- Secret Key field (password-masked, `sk-lf-...`)
- Project ID field (`proj_...`)
- Sync frequency dropdown: **Every 15 minutes / Every 30 minutes / Hourly**
- Data to ingest multiselect (pre-selected: Traces, Token usage, Cost, Latency, Eval scores)
- Prompt content storage radio: **Store metadata only** (pre-selected)

**What to say:** *"Adding Langfuse takes about 30 seconds — paste in an API key, choose what to ingest, decide whether to store prompt content or metadata only. That privacy control is intentional: clients keep sensitive prompt data in their own infrastructure."*

**Action:** Close the drawer by clicking **＋ Connect New System** again (toggles closed).

---

## Stage 2 — Observe
**Story beat:** Show the full cost + carbon + water picture, drill into the worst offender, inspect an agent trace, then rank apps by energy debt.

**Action:** Click **Observe** in the left sidebar.

---

### Step 2.1 — Dashboard tab

**What the user sees:**
- Page title: **TRACE Observe: AI Workload Dashboard**
- A yellow synthetic-data banner: *"⚠️ Synthetic client data — shaped like real AI/Works + Langfuse + CCF exports."*
- Four tabs: **📊 Dashboard · 🔍 AI Detail · 🔗 Agent Traces · ⚡ Energy Debt**
- The Dashboard tab is open by default.

**Total Footprint row (5 KPI cards):**
| Card | Value |
|---|---|
| Total Cost | ~$52,000 (AI + cloud combined) |
| Total Carbon | ~1,100 kg CO₂e |
| Total Energy | ~X kWh — X% from AI inference |
| Total Water | ~X L — X% from AI inference |
| Total Tokens | ~X M across 4 apps · 3 models |

**AI Inference row (5 KPI cards):**
| Card | Value |
|---|---|
| AI Cost | ~$31,300 across 4 apps |
| AI Carbon | ~794 kg CO₂e (~72% of total) |
| AI Energy | ~X kWh · 3 models tracked |
| AI Water | ~X L (energy × WUE per region) |
| Traced Workflows | 3 from X total in ledger |

**Cloud Infrastructure row (4 KPI cards):**
| Card | Value |
|---|---|
| Cloud Cost | ~$20,700 |
| Cloud Carbon | ~X kg CO₂e (~28% of total) |
| Cloud Energy | ~X kWh |
| Cloud Water | ~X L (usage_kWh × WUE) |

**Daily Carbon Trend chart:** A stacked area chart over 30 days (May 2026), two bands — dark green (AI Inference) stacked above grey (Cloud Infra). AI inference is clearly the dominant and growing band.

**What to say:** *"Here's the full picture for May 2026 — cost and carbon, side by side, for AI inference and cloud infrastructure. About 72% of the carbon is coming from AI. The daily trend chart shows AI inference is the growth driver — cloud is relatively flat."*

---

### Step 2.2 — AI Detail tab

**Action:** Click the **🔍 AI Detail** tab.

**What appears at the top:** A yellow warning box:
> *"⚡ Support-Bot — 76% of AI carbon and 77% of AI cost. Top candidate for optimization."*

**Carbon by App chart (horizontal bar):** Support-Bot is the longest bar by far, followed by Analytics-Agent, Document-Processor, Code-Assistant.

**Cost by App chart:** Same pattern — Support-Bot dominates.

**Energy & Water by App (two charts side by side):** Support-Bot tops both.

**By Model (4 pie charts):** Carbon by Model · Cost by Model · Energy by Model (kWh) · Water by Model (L) — in all four, the `large` model class holds the biggest slice.

**By Region (3 bar charts, color-coded by intensity):**
- Carbon by Region: `ap-south` (630 gCO₂e/kWh) is the tallest, darkest red bar.
- Energy by Region: shows raw kWh consumption per region.
- Water by Region: `ap-south` (WUE 1.8 L/kWh) is the tallest blue bar.

**Caption below charts:** *"Dirtiest grids drive carbon; hottest/driest regions drive water. Region shift addresses both."*

**Full Detail table (App × Model × Region):** Sortable rows showing Cost, Carbon, Energy, Water, Tokens per combination.

**What to say:** *"One app, Support-Bot, is responsible for 76% of the AI carbon and 77% of the cost. It's running a large model in ap-south — Mumbai — which is on one of the dirtiest grids and has the highest water stress of any region we track. This is the lever. Let's go deeper."*

---

### Step 2.3 — Agent Traces tab

**Action:** Click the **🔗 Agent Traces** tab.

**What appears:**
- A dropdown labelled **Select workflow trace** with three options:
  - Customer Account Service Generation
  - Payment Processor Integration Test
  - Legacy Code Reverse Engineering

**Action:** Select **Customer Account Service Generation** (or whichever is pre-selected).

**Trace summary KPIs (5 cards):** Total Cost · Total Latency · Total Tokens · Total CO₂e · Total Water

**Agent Graph:** A horizontal flow diagram showing each agent step as a coloured card connected by arrows. Cards are colour-coded:
- Green border (🟢): clean run, no retries
- Amber border (🟡): 1–2 retries
- Red border (🔴): 3+ retries

Each card shows: agent name · model name · tokens in → tokens out · latency · cost · CO₂e · eval score · Accepted ✓ or Rejected ✗ · retry badge.

**Red error banner (if any retries exist):**
> *"⚠️ [Agent Name] has the highest retry count (X retries). This step accounts for $X.XX of the trace cost and X.XXX kg CO₂e. Consider agent loop pruning or prompt compression. → See Optimize."*

**Span Details table:** One row per agent step — Agent, Model, Region, Input tokens, Output tokens, Latency, Cost, Energy (kWh), CO₂e (kg), Water (L), Eval, Retries, Accepted.

**What to say:** *"This is one traced workflow — the actual step-by-step path through Northstar's Customer Account Service agent. Every node shows cost, carbon, water, latency, and quality score. The red card is the expensive step — it retried three times. That retry loop is invisible in your billing dashboard, but it's right here. Fix the prompt, halve the cost and carbon for that step."*

**Action:** Use the dropdown to switch to **Payment Processor Integration Test** — shows a different trace topology, demonstrating the view works across workflow types.

---

### Step 2.4 — Energy Debt tab

**Action:** Click the **⚡ Energy Debt** tab.

**What appears at the top:** A red error banner:
> *"🔴 Support-Bot — Energy Debt Score X.XX / 1.00 · XXX kg CO₂e/mo · X findings"*

**App ranking cards (5 cards, ranked #1–#5):** Each card shows:
- Rank number in red/amber/grey
- App name and monthly carbon/cost
- Energy Debt Score (large number, colour-coded)
- A filled progress bar showing the score as a proportion
- Badges: `X energy-debt` (red), `X other findings` (amber), or `No Semgrep findings` (grey)

Support-Bot is #1. The score is a blend: 60% runtime carbon + 40% code-risk findings from the code scan.

**Code Scan Findings section:** The top 4 findings from the code scan, each showing:
- Severity badge (HIGH / MEDIUM / LOW)
- Finding description (truncated to 80 characters)
- Fix recommendation
- File path · Agent name · Component

**What to say:** *"Energy Debt combines two things: how much carbon the app produces at runtime, and how many inefficiency findings the code scan flagged. Support-Bot scores highest on both. This is the CAST-style ranking that tells a modernization team exactly where to focus — not 'fix everything', but 'fix this app first, and here's why'."*

---

## Stage 3 — Optimize
**Story beat:** The wow moment. Apply a recommendation and watch both numbers drop live.

**Action:** Click **Optimize** in the left sidebar.

---

### Step 3.1 — Read the recommendation

**What the user sees:**
- Page title: **TRACE Optimize: Recommendations**
- Caption: *"Apply a recommendation — watch AI cost and carbon drop live"*
- Section heading: **AI Workload Recommendations**

**Recommendation card 1 — Support-Bot right-sizing:**
> **⚡ Right-size Support-Bot summarization + shift region**
>
> Support-Bot is ~76% of AI carbon and ~77% of AI cost. ~70% of its traffic is routine summarization that runs fine on a small model; the rest stays on the large model for complex tickets. Also shift ap-south (630 gCO₂e/kWh) → us-west (210).
>
> Pills: `model: large → small (70% traffic)` `region: ap-south → us-west (70% traffic)`
>
> `Carbon −64.2% for Support-Bot` `Cost −67.7%`
>
> *Quality trade-off: 30% of traffic kept on the large model in-region to protect answer quality on complex tickets (honest trade-off, not a blanket downgrade).*

**Recommendation card 2 — Analytics-Agent region shift:**
> **⚡ Carbon-aware region shift for Analytics-Agent**
>
> Same workload, cleaner grid: move Analytics-Agent us-east (380) → us-west (210). Cost unchanged (token price is region-independent) — a pure carbon win.
>
> Pill: `region: us-east → us-west (100% traffic)`
>
> `Carbon −44.7% for Analytics-Agent` `Cost unchanged (carbon-only win)`

**SDLC Energy Debt Fixes section:** Two code-scan findings shown as cards with HIGH/MEDIUM badges and fix recommendations.

**What-If Scenario Planner table (static, at the bottom):**
| Scenario | AI Cost | CO₂e | AI Water | Latency | Quality Risk |
|---|---|---|---|---|---|
| Current state | $31,300 | ~1,100 kg | ~X L | 12.8s | Low |
| ⭐ Balanced (recommended) | $24,900 −20.5% | ~920 kg −16.1% | ~X L −16.1% | 11.9s | Low-medium |
| Aggressive carbon mode | $22,500 −28.0% | ~810 kg −26.5% | ~X L −28.0% | 14.2s | Medium |

**What to say:** *"TRACE is specific about the trade-off — 70% of Support-Bot's traffic shifts to a smaller model because that traffic is routine summarization. The hard 30% stays on the large model. We're not doing a blanket downgrade. Quality is an explicit variable, not a footnote."*

---

### Step 3.2 — Apply the recommendation (the wow moment)

**Action:** Click **⚡ Apply** on the Support-Bot card.

**What happens:** A spinner appears for ~0.6 seconds: *"Computing optimized footprint…"*

**What appears immediately after:**

A green success banner at the top of the page:
> **Optimizations applied.** AI carbon: **−49%** (−390 kg) · AI cost: **−52%** (−$16,240)

Four before/after metric tiles:
| Tile | Value |
|---|---|
| AI Cost — before | $31,300 |
| AI Cost — after | $15,060 ↓ −51.9% |
| AI Carbon — before | 794 kg |
| AI Carbon — after | 406 kg ↓ −48.9% |

The Support-Bot card now shows a green background and a ✅ icon. The **Apply** button has changed to **↩ Undo**.

**What to say:** *"Half the carbon and half the cost — from one recommendation, applied live. No new infrastructure, no re-architecture. Routing and region. And if the quality doesn't hold, there's an Undo button."*

**Optional — Apply the second recommendation:**

**Action:** Click **⚡ Apply** on the Analytics-Agent card.

**The success banner updates:** AI carbon drops a further ~25 kg. Cost stays unchanged.

**What to say:** *"And this one is carbon-only — same workload, cleaner grid, zero cost impact. Carbon-aware decisions aren't always about saving money. Sometimes they're just the right thing to do."*

---

## Stage 4 — Prove
**Story beat:** Close with credibility. Show the open methodology, the auditable evidence pack, and the before/after comparison that becomes a client deliverable.

**Action:** Click **Prove** in the left sidebar.

---

### Step 4.1 — Evidence Pack tab

**What the user sees:**
- Page title: **TRACE Prove: Evidence Pack**
- Two tabs: **📋 Evidence Pack · 📐 Methodology**
- The Evidence Pack tab is open by default.

**Left column — Source Telemetry:**
A block listing all 7 connected sources with record counts and normalization percentages:
- 🟢 AI/Works Control Plane — 1,248 records · 98% mapped
- 🟢 Langfuse — 842 records · 94% mapped
- 🟡 Datadog — 493 records · 81% mapped
- 🔵 Cloudability Export — 2,104 records · 89% mapped
- 🟢 Google Cloud Monitoring — 1,876 records · 92% mapped
- 🟢 CCF Factors — 64 records · 100% mapped
- 🟡 Code Scan Findings — 36 records · 76% mapped

**Left column — Calculation Summary:** Two evidence blocks showing the exact formulas used:
- **AI Inference Carbon:** `(total_tokens / 1,000,000) × kWh_per_1M_tokens × grid_kg_CO₂e_per_kWh` · Scope: 4 apps · 3 models · 4 regions · Period: May 2026 · Confidence: Medium
- **Cloud Infrastructure Carbon:** `usage_kWh × regional_grid_kg_CO₂e_per_kWh` · Methodology: Location-based, no RECs or offsets

**Right column — Before / After Comparison** (live, reflecting any optimizations applied):
| Metric | Before | After | Δ |
|---|---|---|---|
| AI Cost | $31,300 | $15,060 | −51.9% |
| AI Carbon | 794 kg | 406 kg | −48.9% |
| AI Energy | X kWh | X kWh | −X% |
| AI Water | X L | X L | −X% |
| Cloud Cost | $20,700 | $20,700 | — |
| Cloud CO₂e | X kg | X kg | — |
| Cloud Water | X L | X L | — |
| Total Cost | $52,000 | $35,760 | −X% |

**Right column — Applied Optimizations:** Lists the recommendations that were applied with ✅ checkmarks.

**Export buttons:**
- **📥 Download AI Ledger CSV** — downloads `trace_ai_ledger.csv`
- **📥 Download Cloud Ledger CSV** — downloads `trace_cloud_ledger.csv`
- **📄 Evidence Pack PDF** — greyed out, labelled "PDF export on roadmap"

**What to say:** *"Every number traces back to a source. The formula is here. The data sources are here. The confidence level is honest — Medium, because we don't have the provider's actual power meter, but we have public GPU benchmarks and regional grid data. This is the audit pack. A client can take this to their sustainability team or their auditor."*

---

### Step 4.2 — Methodology tab

**Action:** Click the **📐 Methodology** tab.

**What appears:**

**Left column:**

SCI-for-AI Carbon Formula — a dark code block showing all formulas:
```
AI carbon (gCO₂e)    = (tokens / 1,000,000) × kWh_per_1M_tokens × grid_gCO₂e_per_kWh
AI cost (USD)        = (tokens / 1,000,000) × USD_per_1M_tokens
Cloud carbon (gCO₂e) = usage_kWh × grid_gCO₂e_per_kWh
Energy Debt Score    = 0.6 × carbon_rank + 0.4 × code_risk_rank
```

Standards Alignment table:
| Standard | How TRACE uses it |
|---|---|
| SCI-for-AI (Green Software Foundation) | Primary formula |
| ISO 21031 | GHG accounting: operational boundary, location-based, no offsets |
| OpenTelemetry GenAI | Token field names |
| Langfuse trace schema | LLM usage log shape |
| CCF output schema | Cloud usage log shape |
| Semgrep JSON | Energy Debt layer |

Honest Caveats section — four bullets about coefficient estimation, location-based grid, synthetic data, and explicit quality trade-offs.

**Right column:**

Model Coefficients table (live data from `model_coefficients.csv`):
| Model | Provider | USD / 1M tokens | kWh / 1M tokens |
|---|---|---|---|
| large | anthropic | $30.00 | 1.2 |
| mid | anthropic | $6.00 | 0.6 |
| small | anthropic | $1.00 | 0.3 |

Grid Intensity bar chart — horizontal bars, colour-coded green → amber → red:
- us-west: 210 gCO₂e/kWh (green)
- eu-west: 290 (green-amber)
- us-east: 380 (amber)
- ap-south: 630 (red)

Grid Intensity table below the chart showing Region + gCO₂e/kWh values.

**What to say:** *"Thoughtworks co-founded the Green Software Foundation. We're not aligning to SCI-for-AI as a box-check — we helped write it. The coefficients are public, the grid intensity is public, the formula is right there. That's the transparency a proprietary black-box calculator can't offer. Clients can challenge any number, and we can defend every one."*

---

## End State Checklist

After the full journey, the app shows:
- [ ] Connect: 7 systems visible, drawer demo complete
- [ ] Observe Dashboard: total footprint KPIs loaded, daily trend chart visible
- [ ] Observe AI Detail: Support-Bot flagged as #1 offender, region breakdown showing ap-south in red
- [ ] Observe Agent Traces: at least one trace stepped through, retries highlighted
- [ ] Observe Energy Debt: Support-Bot ranked #1, code scan findings visible
- [ ] Optimize: at least rec-1 applied, before/after numbers showing ~−49% carbon, ~−52% cost
- [ ] Prove Evidence Pack: before/after table updated, applied optimizations listed, CSV download available
- [ ] Prove Methodology: formula, standards alignment, and coefficient table visible

**Total clock time for a rehearsed run: 4–5 minutes.**

---

## Reset Between Runs

Click **↩ Reset all** in the sidebar (appears when any recommendation is applied) to return to the baseline state. All before/after numbers revert instantly.
