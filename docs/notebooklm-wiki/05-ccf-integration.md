# 05 — Cloud Carbon Footprint & TRACE

> **Summary:** What Cloud Carbon Footprint (CCF) is, how TRACE relates to it, what was reused versus built from scratch, and the path for TRACE to eventually grow into a proper CCF extension. Written in plain English.

---

## What is Cloud Carbon Footprint?

**Cloud Carbon Footprint (CCF)** is an open-source tool created by Thoughtworks (with contributions from others) that helps organisations measure the carbon emissions of their cloud infrastructure. It connects to AWS, Google Cloud, and Azure billing data, applies carbon intensity factors for each region, and produces a dashboard showing how much CO₂e their servers, storage, and networking are producing.

CCF answers the question: *"How much carbon does my cloud spend create?"*

It is well-established, open-source, trusted by enterprises, and was co-created by Thoughtworks, which also co-founded the Green Software Foundation. This gives Thoughtworks strong credibility in the carbon measurement space.

**What CCF does not do:** CCF measures cloud infrastructure — the servers and services. It does not measure AI inference carbon. When you call the OpenAI API or run a Claude model on Bedrock, CCF does not see those tokens or calculate their energy and carbon footprint. That gap is exactly what TRACE is designed to fill.

---

## What is the relationship between TRACE and CCF?

The TRACE repository is a **fork of the CCF codebase**. This means that when the project started, Thoughtworks took a complete copy of the CCF source code and began building on top of it.

However, at the hackathon MVP stage, the relationship is primarily **conceptual, not technical**. Here is the honest breakdown:

| Aspect | Reality |
|---|---|
| **CCF code in the repo?** | Yes — the full CCF TypeScript codebase is present in the `packages/` folder (~82,500 lines across 742 files) |
| **CCF code running in the MVP?** | No — the TRACE Python app does not invoke any CCF code at runtime |
| **CCF methodology used?** | Yes — TRACE borrows CCF's carbon calculation approach for cloud infrastructure |
| **CCF data formats used?** | Yes — the cloud usage data in TRACE is shaped like CCF's billing export format |
| **CCF grid intensity values?** | Yes — the regional gCO₂e/kWh values in TRACE are sourced from the same public datasets CCF uses (Electricity Maps, EPA eGRID, ENTSO-E), and the values are labelled as "CCF-v2.1" methodology |

The simplest way to explain this: **TRACE borrows CCF's ideas and data; the code is waiting to be connected.**

---

## The microwave analogy

Think of CCF as a fully equipped professional kitchen. TRACE is currently a microwave sitting on the counter next to it.

- The microwave (TRACE MVP) works great and does exactly what it was designed to do
- It is not using the kitchen (the CCF codebase)
- The long-term plan is to actually cook in the kitchen — to wire TRACE into CCF's existing infrastructure so the two become one product

This was the right call for the hackathon: building directly on CCF's TypeScript codebase would have taken weeks and required deep technical investment. The Python prototype proved the concept fast without that overhead.

---

## What CCF already provides that TRACE would use in production

CCF has a modular architecture with well-defined extension points:

| CCF component | What it does | How TRACE would use it |
|---|---|---|
| `@cloud-carbon-footprint/core` | Core estimation interfaces and algorithms | TRACE would add a new `LLMInferenceEstimator` implementing CCF's `IFootprintEstimator` interface |
| `@cloud-carbon-footprint/aws` | AWS billing connectors and service estimators | TRACE would add Bedrock (AWS's AI service) as a new `ICloudService` implementation |
| `@cloud-carbon-footprint/gcp` | Google Cloud connectors | TRACE would add Vertex AI as a new service |
| `@cloud-carbon-footprint/azure` | Azure connectors | TRACE would add Azure OpenAI as a new service |
| `@cloud-carbon-footprint/api` | REST API server | TRACE would add new endpoints for AI footprint data |
| `@cloud-carbon-footprint/client` | React dashboard | TRACE would add the Observe/Optimize/Prove pages |

This is a well-defined, buildable path. The CCF architecture was designed for this kind of extension — it has clear interfaces and a proven pipeline.

---

## What TRACE built that CCF does not have

Everything TRACE does with AI inference is net new — not present in any form in the existing CCF codebase:

| New capability | Description |
|---|---|
| **LLM inference carbon calculation** | `(tokens / 1M) × kWh_per_1M_tokens × grid_intensity` — a new formula not in CCF |
| **Model energy coefficients** | A lookup table mapping model classes (large/mid/small) to kWh per million tokens — entirely new data |
| **LLM observability connector** | Ingesting Langfuse-shaped trace data with token counts, latency, eval scores, retries — new schema |
| **Agent trace visualisation** | The step-by-step agent graph showing cost/carbon/water per workflow step — new UI concept |
| **Water consumption calculation** | `energy_kWh × WUE_liters_per_kWh` using region-specific Water Usage Effectiveness factors — new metric |
| **Energy Debt Score** | The combined 60%/40% runtime + code-risk ranking — new concept |
| **Recommendation engine** | Model swap + region shift recommendations with live recalculation — new logic |
| **Evidence pack** | The before/after audit report format — new output type |

---

## What TRACE directly borrowed from CCF

| Borrowed element | How it appears in TRACE |
|---|---|
| **Cloud carbon formula** | `usage_kWh × grid_gCO₂e/kWh` — the same location-based approach CCF uses |
| **Grid intensity values** | The `gCO₂e/kWh` values in `grid_intensity.csv` are sourced from the same datasets CCF uses (Electricity Maps, EPA eGRID, ENTSO-E), with the same regional coverage |
| **Cloud usage data schema** | The `cloud_usage.csv` file is shaped like a CCF billing export: `date, app, service, region, usage_kwh, cost_usd` |
| **Methodology label** | The `carbon_factors.csv` file labels values as "CCF-v2.1" methodology |
| **Location-based, no offsets principle** | CCF's philosophical position — that location-based grid intensity with no market-based offsets is the honest approach — is directly adopted by TRACE |

---

## The full production path

For TRACE to become a proper CCF extension (rather than a parallel Python app), the engineering work would proceed in roughly four phases:

**Phase 1 — Extend CCF core (~2–3 weeks):**
Add an `LLMInferenceEstimator` to `packages/core`, with a `llm-constants.ts` file containing the kWh/1M token coefficients.

**Phase 2 — Add cloud provider AI service connectors (~4–6 weeks):**
Add Bedrock (in `packages/aws`), Vertex AI (in `packages/gcp`), and Azure OpenAI (in `packages/azure`) as new service classes.

**Phase 3 — Add LLM observability connectors (~3–4 weeks):**
Create a new `packages/llm` package with connectors for Langfuse, OpenTelemetry GenAI, and LiteLLM.

**Phase 4 — Extend the API and client (~3–4 weeks):**
Add new API endpoints and React dashboard pages replicating the Observe/Optimize/Prove functionality currently in the Streamlit app.

Total estimated effort: approximately 12–17 weeks for a proper production integration. The hackathon MVP is a proof of concept that validates the idea; the production path is well-defined.

---

## Why is the CCF codebase in the repo if it's not used?

Three reasons:

1. **Forking was the intended starting point.** The project intended to build on CCF from the beginning. The fork was created so that CCF updates could eventually be pulled in, and so the final product could be published back to the CCF community.

2. **It is the inheritance model for the publishing workflow.** When the project is ready to share publicly, it will be published to a public CCF fork (`Concepcion-c/cloud-carbon-footprint`), not as a separate repository. The fork relationship makes this clean.

3. **The full CCF codebase would be available for Phase 1–4 integration** the moment a developer needs it. There is no setup overhead — all the code is already there.

---

## Key takeaways

- CCF is Thoughtworks' existing open-source cloud carbon tool, and TRACE is its natural evolution into the AI era
- The TRACE MVP is currently a parallel Python app inspired by CCF's methodology, not an extension of CCF's code
- The connection between the two is primarily methodological (shared formulas, shared data sources) and strategic (TW's GSF credibility)
- The production path to a proper CCF extension is well-defined and does not require starting over — it requires wiring the new AI estimators into CCF's existing extension points
- For hackathon purposes, the CCF relationship is a **credibility anchor** ("built by the people who invented CCF") and a **vision** ("this is what CCF becomes in the AI era"), not a technical dependency
