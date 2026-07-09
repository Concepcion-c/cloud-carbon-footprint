# 08 — Demo Guide

> **Summary:** How to present RECPT in a five-minute live demo. Includes the recommended walkthrough, key talking points, the wow moment, likely questions from judges or stakeholders, and suggested answers.

---

## The one-sentence pitch

*"RECPT shows the carbon and cost of your AI tools side by side — and then tells you exactly what to change to cut both."*

---

## Before the demo: setup

1. Run `streamlit run app.py` and open the app full-screen in a browser
2. Confirm the sidebar shows: **🌿 RECPT / AI GREENOPS DASHBOARD / 📁 Northstar Bank**
3. Confirm the app opens on the **Connect** page
4. Make sure no recommendations are applied (no green banner, no ↩ Reset all button visible)
5. Have the **Cloudability CSV file** ready at `docs/sample-data/finops_cloud_export.csv` in case you want to demo the file upload flow

---

## Recommended 5-minute walkthrough

### Opening hook (0:00–0:30)

**What to say:**
> "AI data-centre electricity consumption grew by approximately 50% in 2025. Every token your AI tools process has a carbon footprint — but today, that carbon is completely invisible. Cloud carbon tools measure your servers. AI billing tools measure your spend. Nobody shows you both in one place. RECPT closes that gap."

**What to show:** Nothing yet — this is the hook delivered to camera or audience.

---

### Stage 1: Connect (0:30–1:15)

**Action:** Land on the Connect page (it is the default).

**What to say:**
> "This is Northstar Bank's data estate as RECPT sees it today. Seven sources are already connected — live APIs from Langfuse, AI/Works, and Google Cloud Monitoring syncing every 15 minutes; static exports from Cloudability and CCF Factors. Two warnings tell us where the data is stale or partially mapped. Everything is visible, nothing is hidden."

**Optional — show the drawer:**

Click **＋ Connect New System**, then click **LLM Observability**, then select **API connection**.

> "Adding a new source takes about 30 seconds — paste in an API key, choose what to ingest, decide whether to store prompt content or metadata only. That last choice is intentional: clients keep sensitive prompt data in their own infrastructure."

Close the drawer.

**Key point to land:** *RECPT plugs into what clients already have — no new instrumentation required.*

---

### Stage 2: Observe — Dashboard (1:15–1:45)

**Action:** Click **Observe** in the sidebar.

**What to say:**
> "Here's May 2026 for Northstar Bank. Cost and carbon, side by side. $31,300 on AI inference. $20,700 on cloud infrastructure. Total carbon: over a thousand kilograms of CO₂e — about 72% from AI. The daily trend chart shows AI inference is the growth driver."

**What to point to:** Total Cost and Total Carbon KPI cards. The daily trend chart where the AI band is larger than the cloud band.

---

### Stage 3: Observe — AI Detail (1:45–2:30)

**Action:** Click the **🔍 AI Detail** tab.

**What to say:**
> "Here's where it gets interesting. One app is responsible for 76% of the AI carbon and 77% of the cost: **Support-Bot**. It is running a large model in Mumbai — one of the dirtiest electricity grids in our dataset. The charts make it obvious which app to fix."

**What to point to:** The yellow warning banner at the top of the tab. The Carbon by App bar chart (Support-Bot clearly dominates). The region charts showing ap-south as the tallest, reddest bar.

**Optional extra point:** Scroll down to the region comparison and say:
> "And it is not just carbon — the region with the dirtiest grid also has the highest water stress. Mumbai data centres consume 1.8 litres of water per kilowatt-hour of compute. Oregon uses 0.8. The same optimisation that cuts carbon also cuts water."

---

### Stage 4: Observe — Agent Traces (2:30–3:00)

**Action:** Click the **🔗 Agent Traces** tab.

**What to say:**
> "This is something no existing tool shows you. This is one workflow — step by step, agent by agent. Every node shows cost, carbon, water, latency, quality score, and retry count. That red card retried three times. Those retries are invisible in your billing dashboard, but each one burned extra tokens, energy, and carbon. Fix the prompt, and you eliminate that waste."

**What to point to:** An agent card with a red border and retry badge. The error banner below the graph.

---

### Stage 5: Observe — Energy Debt (3:00–3:15)

**Action:** Click the **⚡ Energy Debt** tab.

**What to say:**
> "RECPT doesn't just measure — it prioritises. The Energy Debt score combines runtime carbon with code-level inefficiency findings. Support-Bot scores highest on both. If you had to tell an engineering team which app to modernise first for the best return, this is the answer."

---

### Stage 6: Optimize — The wow moment (3:15–4:00)

**Action:** Click **Optimize** in the sidebar.

**Pause. Let the audience read the first recommendation card.**

**What to say:**
> "RECPT found that 70% of Support-Bot's traffic is routine summarisation — the kind of work a smaller, cheaper model handles just as well. Shift that 70% to a small model and move it to Oregon. The 30% of complex queries stays on the large model, in-region, to protect quality. That trade-off is stated explicitly — RECPT doesn't do blanket downgrades."

**Action:** Click **⚡ Apply** on the Support-Bot card.

**Wait for the spinner. Then pause again on the result.**

**What to say:**
> "Half the carbon. Half the cost. From one recommendation. No new infrastructure. No re-architecture. Routing and region. And if the quality doesn't hold, there's an Undo button."

**If time allows — apply the second recommendation:**

**Action:** Click **⚡ Apply** on the Analytics-Agent card.

> "This one is carbon-only — same workload, cleaner grid, zero cost impact. Carbon-aware decisions aren't always about saving money. Sometimes they're just the right thing to do."

---

### Stage 7: Prove (4:00–4:45)

**Action:** Click **Prove** in the sidebar.

**What to say:**
> "The Prove page is what RECPT produces for the client's sustainability team or auditor. Every number traces back to a source. The formula is here. The data sources are here. The confidence level is honest — Medium, because we're working from hardware benchmarks, not a power meter. This isn't a black box. Clients can challenge any number, and we can defend every one."

**What to point to:** The Before/After Comparison table (with green deltas). The Calculation Summary evidence blocks with the formula and confidence level.

**Click the Methodology tab:**

> "Thoughtworks co-founded the Green Software Foundation. We're not aligning to SCI-for-AI as a box-check — we helped write it. The coefficients and the grid intensity values are all published here."

**What to point to:** The Standards Alignment table. The Model Coefficients table.

---

### Close (4:45–5:00)

**What to say:**
> "AI is the new forcing function. It is driving energy, cost, and the urgent need to measure and control both. Thoughtworks created Cloud Carbon Footprint, helped write the Green Software Foundation standards, and built RECPT — a product that any client can buy and keep, that shows their AI footprint in plain numbers, and that tells them what to do about it. You can't manage what you can't measure. RECPT makes AI's cost and carbon, finally, measurable."

---

## Key numbers to know

| Number | Context |
|---|---|
| ~50% | AI data centre energy growth in 2025 (IEA) |
| 7 | Connected data sources in the Northstar Bank demo |
| ~$31,300 | Monthly AI inference cost at baseline |
| ~794 kg | Monthly AI carbon at baseline |
| 76% / 77% | Support-Bot's share of AI carbon / cost |
| 630 gCO₂e/kWh | Grid intensity in Mumbai (ap-south) — the dirtiest region |
| 210 gCO₂e/kWh | Grid intensity in Oregon (us-west) — the cleanest region |
| ~49% | AI carbon reduction after applying the Support-Bot recommendation |
| ~52% | AI cost reduction after applying the Support-Bot recommendation |
| 1,881 L/month | Water consumption for Support-Bot at baseline (~12 bathtubs) |

---

## Likely questions and suggested answers

### "Is this data real?"

*"No — all the data in this demo is synthetic, generated specifically for the hackathon. The numbers are shaped to look like real Langfuse, CCF, and billing exports, and the relationships between them are realistic. The yellow banner in the Observe page says so explicitly. In a real deployment, RECPT would ingest the client's own data."*

### "How accurate is the carbon estimate?"

*"The methodology is honest about this: we label it Medium confidence. The cloud carbon figures are High confidence because we have measured kWh from billing data. The AI inference carbon is Medium confidence because we estimate energy from token counts using hardware benchmarks — no AI provider publishes per-call energy data. We show the formula and the coefficients in the Prove tab so anyone can review them. It is more accurate than not measuring at all, and it is transparent about where the uncertainty is."*

### "Where do the kWh-per-token numbers come from?"

*"They are derived from publicly available hardware specs — specifically NVIDIA A100 and H100 GPU power ratings, combined with token throughput benchmarks from MLPerf. We also cite Luccioni et al. (2023), a peer-reviewed paper that benchmarked inference energy for various model sizes. The derivation is documented in full in our methodology notes. These are estimates, not vendor measurements — we are transparent about that."*

### "Why doesn't RECPT use carbon offsets?"

*"RECPT follows the ISO 21031 standard, which requires location-based accounting. This means we use the actual carbon content of the electricity grid where the computation runs. Market-based offsets — like renewable energy certificates — don't change the physical electricity that powers a data centre. Claiming them would reduce the reported number without reducing the actual impact. We believe the honest number is the useful number."*

### "How is this different from Cloud Carbon Footprint?"

*"CCF measures cloud infrastructure — servers, storage, networking. It does not measure AI inference at all. When you call the Claude or GPT API, CCF sees nothing. RECPT fills that gap by adding an AI inference measurement layer using token counts and model-class energy coefficients. It also adds water consumption tracking, agent-level trace visibility, and a recommendation engine — none of which exist in CCF today."*

### "Could this work with a real client's data?"

*"Yes — and the architecture is designed for it. In a real deployment, RECPT would connect to the client's cloud billing exports (AWS CUR, GCP BigQuery billing, Azure cost export) and their LLM usage data (from an AI gateway like LiteLLM or an observability tool like Langfuse). The Connect page shows exactly what those connectors would look like. For the hackathon, we used synthetic data shaped like those exports."*

### "What would it take to make this production-ready?"

*"A few key steps: live API connectors to replace the static files, client-specific energy coefficients where providers publish data, and a proper deployment model. On the methodology side, per-model hardware data from providers like Boavizta would sharpen the AI carbon estimates from Medium to High confidence. The full roadmap is documented."*

### "Why Thoughtworks? What's the competitive advantage?"

*"Three things: we co-created CCF (so we know this domain deeply), we co-founded the Green Software Foundation (so we helped write the SCI-for-AI standard this product is built on), and we have AI:works (so we can demonstrate carbon-aware AI delivery, not just measure it). We can use AI:works as client zero — build greener software using it, then prove the before-and-after carbon reduction with RECPT. That combination — build it green and prove it — is something no other firm can offer today."*

---

## If something goes wrong

**App won't start:** Check Python and Streamlit are installed (`pip install -r requirements.txt`). Run from the project root directory.

**Numbers look wrong:** Run `cd docs/sample-data && python3 generate.py` to regenerate the CSV files. Note: recommendations.json is hand-authored and won't regenerate.

**Applied recommendations and now the demo state is messy:** Click **↩ Reset all** in the sidebar to instantly restore the baseline.

**Live demo fails entirely:** The key numbers are all in `docs/demo/demo-script.md` and can be presented from static slides as a fallback.

---

## Key takeaways

- The wow moment is on the Optimize page — clicking Apply and watching both numbers drop ~50% is the single most memorable moment in the demo
- Frame RECPT as a product the client buys and keeps — not a consulting deliverable, not a platform dependency
- Lead with the AI energy shock (50% growth in 2025) before opening the app — the hook needs to land before the numbers
- Be honest about what is synthetic and what is estimated — the transparency is part of the value proposition
- The Support-Bot story (76% of carbon from one app, in one region, fixable with one recommendation) is the narrative spine of the entire demo
