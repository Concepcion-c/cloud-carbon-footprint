# 01 — Product Overview

> **Summary:** What TRACE is, the problem it solves, who it is for, the demo story, and the key outcomes it demonstrates. Start here to understand the product before going into detail.

---

## The problem TRACE solves

AI tools — chatbots, coding assistants, agent workflows, document summarisers — are becoming a standard part of how companies operate. Every time these tools run, they consume energy. That energy has a cost (reflected in your cloud or API bill) and a carbon footprint (reflected in the greenhouse gas emissions produced by the data centres running the models).

The problem today is that **cost is visible, but carbon is invisible.** Your CFO can see the AI spend on the monthly bill. Your sustainability team has no equivalent number. No existing enterprise tool connects these two views.

At the same time, **AI energy use is growing fast.** According to the International Energy Agency, AI data centre electricity consumption grew approximately 50% in 2025. For companies that have committed to sustainability targets, this is a growing blind spot that is getting harder to ignore.

TRACE closes this gap. It ingests the same usage data that companies already collect for billing purposes, adds a carbon and energy calculation layer, and shows cost and carbon side by side — with recommendations for how to reduce both.

---

## What TRACE is

**TRACE** stands for **Token-level Realtime AI Carbon Estimation**.

It is a dashboard and optimisation tool for understanding and reducing the carbon footprint of AI workloads. In the hackathon MVP, it does the following:

1. **Connects** to data sources — LLM observability tools, cloud billing exports, AI gateway logs, and carbon factor reference data
2. **Observes** cost, carbon, energy, and water use — broken down by app, model, region, and individual agent workflow step
3. **Optimises** — recommends concrete actions (swap to a more efficient model, shift to a cleaner grid region) and shows the before/after impact live
4. **Proves** — produces an auditable evidence pack showing every formula, data source, and assumption behind the numbers

TRACE is positioned as an **independent, sellable product** in the lineage of Cloud Carbon Footprint (the open-source tool Thoughtworks co-created). It does not require the client to buy or use any other Thoughtworks platform.

---

## The three-layer product vision

The full TRACE product vision has three layers:

| Layer | Name | What it does | Sellable independently? |
|---|---|---|---|
| 1 | **Assess** | Scans the client's application estate and ranks apps by "energy debt" — a blend of runtime carbon and code-level inefficiency | Yes |
| 2 | **Build Green** | Thoughtworks modernises the priority apps using AI:works, resulting in more efficient software | No — this is TW's delivery engine, not a client purchase |
| 3 | **Prove & Manage** | Measures the run-time cost and carbon of the delivered apps on an ongoing basis; recommends optimisations; produces auditable before/after reports | Yes |

**The hackathon MVP demonstrates layers 1 and 3.** Layer 2 is referenced in the demo context (AI:works as "client zero") but is not part of the purchasable product.

---

## What TRACE measures

TRACE measures four things for AI inference workloads and cloud infrastructure:

| Metric | What it is | Unit |
|---|---|---|
| **Cost** | How much money was spent on AI API calls or cloud compute | USD per month |
| **Carbon** | Greenhouse gas emissions from the energy used | kg CO₂e per month |
| **Energy** | Electricity consumed by the AI inference or cloud workload | kWh per month |
| **Water** | Water consumed by data centre cooling systems | Litres per month |

These are calculated using token counts (for AI inference) or kilowatt-hours from billing data (for cloud infrastructure), combined with regional grid intensity and data centre efficiency factors.

---

## Target users

| User | Role | What they care about |
|---|---|---|
| **VP Engineering / Platform / Cloud** | Owns the infrastructure bill | Cutting AI cost while meeting sustainability targets |
| **Sustainability / ESG Lead** | Owns carbon reporting | Accurate, auditable AI emissions data for disclosures |
| **Engineering Team** | Builds and runs the AI apps | Knowing which apps to optimise and how |
| **Thoughtworks (internally)** | Using TRACE on its own AI:works engagements | Demonstrating carbon-aware delivery ("client zero") |

---

## The demo story

The demo runs a fictional client scenario: **Northstar Bank**, which is undergoing a Digital Banking Modernisation project. The bank is running five AI applications in production.

**The hook:** The bank's AI tools are costing $31,300 per month and producing 794 kg of CO₂e — but nobody knows this. The sustainability team sees the cloud bill but not the AI inference spend. The AI team sees the API costs but not the emissions. TRACE shows both in the same place, for the first time.

**The reveal:** One application, **Support-Bot**, is responsible for 76% of the AI carbon footprint and 77% of the AI cost. It is running an expensive large-language model in Mumbai (ap-south), one of the dirtiest electricity grids in the data set. Nobody flagged this because carbon was never measured.

**The action:** TRACE recommends shifting 70% of Support-Bot's traffic to a smaller model (appropriate for routine summarisation tasks) and moving that traffic to Oregon (us-west), a cleaner grid. The 30% of complex customer support queries stay on the large model, in-region, to preserve quality.

**The result:** Applying this one recommendation drops AI carbon by approximately 49% and AI cost by approximately 52% — live, in front of the audience, in a single click.

**The proof:** The Prove page shows the auditable evidence: every data source, every formula, every assumption, and the before/after comparison — downloadable as a CSV ledger.

---

## Key value propositions

1. **Carbon beside cost** — the only view that shows both in the same dashboard, broken down by app, model, and region
2. **Optimisations that cut both** — not a reporting tool but an action tool; every recommendation quantifies the impact on cost *and* carbon
3. **Open and auditable methodology** — every number traces to a published source; no black boxes; transparent about confidence levels
4. **Independent product** — clients buy and keep it without depending on any other Thoughtworks platform
5. **Standards-aligned** — built on SCI-for-AI (Green Software Foundation) and ISO 21031; the same standard Thoughtworks helped create

---

## What makes TRACE different from existing tools

| Existing tool | What it does | What it misses |
|---|---|---|
| Cloud Carbon Footprint (CCF) | Measures cloud infrastructure carbon | Does not measure AI inference tokens |
| LLM observability tools (Langfuse, Datadog) | Tracks token usage, cost, latency | Does not calculate carbon |
| FinOps tools (Cloudability, Apptio) | Tracks cloud spend | No sustainability layer |
| Generic carbon calculators | Estimates emissions | Not connected to live AI usage data; opaque methodology |

TRACE sits at the intersection of all of these — pulling data from each source type and producing a unified cost + carbon view that none of them provides alone.

---

## Demo context: synthetic data notice

Every number in the TRACE demo is **synthetic** — generated artificially using a deterministic data generator (`docs/sample-data/generate.py`). The data is shaped to look like real Langfuse, CCF, and cloud billing exports, but contains no actual client information.

This is clearly labelled in the app with a yellow banner: *"⚠️ Synthetic client data — shaped like real AI/Works + Langfuse + CCF exports. All numbers illustrative."*

---

## Key takeaways

- TRACE solves a real problem: AI carbon is invisible today, and it is growing fast
- The product has three layers; the MVP demonstrates two (Assess and Prove/Manage)
- The demo story (Northstar Bank, Support-Bot, −49% carbon in one click) is the central narrative
- TRACE is differentiated by showing cost and carbon together, with an open and auditable methodology
- All demo data is synthetic; this is disclosed in the app
