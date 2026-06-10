# 09 — Limitations, Roadmap & Risks

> **Summary:** What the TRACE MVP cannot do today, where the methodology has gaps, what would be needed for a real production deployment, and what the product roadmap looks like. Written honestly — this document does not oversell the current state.

---

## What TRACE is and is not

| TRACE is | TRACE is not |
|---|---|
| A working hackathon MVP demonstrating a real concept | A production-ready system |
| A proof-of-concept with defensible methodology | A certified emissions accounting system |
| A demo of how a real tool would work | A live integration with real data |
| A product with a clear production path | Available for client deployment today |

---

## Current technical limitations

### 1. All data is synthetic
Every number in the dashboard comes from `generate.py` — a deterministic random data generator. There are no real client connections, no live API calls, and no real billing or usage data. The dashboard looks and behaves like a real tool, but the underlying data is entirely fabricated.

**Impact:** Cannot be used for actual emissions reporting. All numbers are illustrative only.

### 2. No live connectors
The Connected Systems table on the Connect page shows seven data sources. None of them are live in the MVP. The status values ("12 min ago"), record counts, and normalization percentages are all hard-coded. Clicking "Run Sync" or "View" has no effect.

**Impact:** The Connect page demonstrates what the onboarding flow would look like, but no actual data ingestion occurs.

### 3. File upload is simulated
The file upload flow in the Connect drawer reads and validates an uploaded CSV (using pandas), but the Run Normalization step does not actually process the file into the dashboard metrics.

**Impact:** You can upload a file and see validation results, but the dashboard numbers do not change.

### 4. Four pages only (not five)
The v3 PRD describes a five-screen product including a dedicated Normalize page. The current app has four pages — Connect, Observe, Optimize, Prove. The Normalize functionality (field mapping, schema normalization, run history) is partially represented in the Connect drawer, but not as a standalone page.

**Impact:** The full data pipeline management experience described in the PRD is not yet built.

### 5. Two recommendations only
The Optimize page has exactly two recommendation cards, both hand-authored and tuned to the synthetic data. A production system would generate recommendations dynamically from the full data set using configurable rules.

**Impact:** The demo does not represent the variety of recommendations a real system would produce.

### 6. What-If Scenario Planner is static
The three scenarios in the What-If Planner (Current State, Balanced, Aggressive) use fixed percentage multipliers (−20.5%, −28%) applied to the baseline numbers. They are not driven by real recommendation logic.

**Impact:** The What-If table illustrates the concept but does not represent actual scenario modelling.

### 7. No authentication, multi-tenancy, or persistent storage
The app has no login, no user accounts, no data saved between sessions, and no support for multiple users or clients. Session state is in-memory only.

**Impact:** Cannot be deployed as a shared service without significant additional work.

### 8. PDF export not built
The Evidence Pack PDF export button is present in the Prove page but is disabled ("on roadmap"). Only CSV exports work.

### 9. Water confidence is Medium for all regions
The WUE (Water Usage Effectiveness) values in `grid_intensity.csv` are regional estimates from public data centre efficiency surveys. AWS does not publish region-level WUE with the same transparency as Google. All water figures carry Medium confidence.

---

## Methodology limitations

### 1. AI energy coefficients are blended estimates
The kWh/1M token values (0.3, 0.6, 1.2 for small/mid/large model classes) are derived from GPU hardware specifications and benchmark data — not from vendor measurements. No AI provider publishes per-call energy consumption.

**Consequence:** The AI carbon and energy figures carry Medium confidence. They are directionally correct and better than no measurement, but they are not precision measurements.

### 2. Coefficient granularity is low
TRACE uses three model classes (large, mid, small). A production system would have per-model coefficients for every named model across every provider. Models within the same class can vary significantly in actual energy use.

**Consequence:** Energy estimates for specific models (e.g., GPT-4o vs Claude Opus) are approximated by class membership, not measured per model.

### 3. No hardware or embodied emissions
TRACE measures operational emissions only (the energy used during inference). It does not measure embodied emissions — the carbon produced during manufacturing of servers and GPUs. Boavizta (a third-party API for embodied emissions) is referenced in the project documentation as a future integration but is not implemented.

**Consequence:** TRACE's carbon figures are Scope 2 operational only. A complete lifecycle assessment would require Scope 3 hardware data.

### 4. Location-based only
TRACE uses location-based grid intensity (the actual carbon content of the local grid). It does not support market-based accounting (where renewable energy certificates can reduce the reported carbon). This is intentional, not a gap — but some clients' sustainability teams may use market-based accounting and will need to reconcile the difference.

### 5. No provider-specific infrastructure data
Hyperscalers have internal infrastructure data (actual PUE per facility, actual hardware mix) that is not public. If providers published this data, TRACE's estimates would improve from Medium to High confidence for AI carbon.

### 6. AI cost figures depend on token-based pricing
TRACE assumes all AI inference is priced by token count (input + output). Some providers and deployment models use other pricing structures (per-second, per-request flat fee, reserved capacity). These would not be correctly estimated by TRACE's current cost formula.

---

## Product risks

### 1. Coefficient credibility challenge
A technically sophisticated audience may challenge the kWh/1M estimates. Mitigation: the Prove > Methodology tab shows the derivation chain explicitly. The Honest Caveats section acknowledges the estimates. TRACE is transparent, not defensive. See `08-demo-guide.md` for suggested responses.

### 2. "This is just a demo" objection
The app looks polished but runs on synthetic data. Mitigation: be upfront about this (the yellow synth banner is there for a reason). Frame the demo as "what TRACE will do with your data" — the architecture is real, the calculations are real, the data is synthetic.

### 3. No active CCF development resource
The project documentation notes that CCF's codebase was revived to a baseline but has no active engineering team maintaining it. The production integration path (Phase 1–4 described in `05-ccf-integration.md`) requires a developer committed to the CCF codebase.

### 4. AI energy transparency may improve and invalidate estimates
If major providers (Anthropic, OpenAI, Google) begin publishing per-call energy data — as regulatory pressure increases — TRACE's estimated coefficients would be superseded by measured values. This is a positive risk (the estimates become more accurate) but requires the methodology to be updated.

---

## Responsible AI and sustainability considerations

### 1. No greenwashing
TRACE explicitly does not use carbon offsets in its calculations. It reports the physical energy and carbon of AI workloads, not offset-adjusted figures. This is intentional and aligned to ISO 21031.

### 2. Honest confidence levels
The app labels all AI carbon figures as Medium confidence and explains why. It does not present estimates as measured values.

### 3. Quality trade-offs are explicit
Every recommendation in TRACE shows an explicit quality trade-off statement ("30% of traffic kept on the large model to protect answer quality on complex tickets"). TRACE does not recommend blanket model downgrades without acknowledging the quality implication.

### 4. No real client data in the repo
The project uses only synthetic data in tracked files. The CLAUDE.md governance rules explicitly prohibit PII or client-confidential data from being committed to the repository.

### 5. Open methodology
All formulas, coefficients, and assumptions are documented in the Prove > Methodology tab and in `docs/research/trace-calculation-methodology.md`. Any stakeholder can review and challenge the methodology.

---

## What would be needed for production readiness

| Requirement | What it involves |
|---|---|
| **Live connectors** | Build API integrations for Langfuse, LiteLLM, OpenTelemetry, AWS Bedrock, GCP Vertex, Azure OpenAI, and cloud billing APIs |
| **Real data pipeline** | Replace static CSVs with a proper ETL pipeline (ingest, validate, normalise, store) |
| **Per-model coefficients** | Expand the model coefficient table from 3 classes to named models across all major providers |
| **CCF integration** | Implement the Phase 1–4 CCF extension (see `05-ccf-integration.md`) |
| **Authentication and multi-tenancy** | Add user accounts, client isolation, and role-based access |
| **Deployment infrastructure** | Database, API server, scheduled sync jobs, alerting |
| **Methodology validation** | Commission a third-party review of the coefficients; engage with Boavizta for embodied emissions; update WUE with provider-published figures |
| **PDF export** | Build the evidence pack PDF generation |
| **Dynamic recommendations** | Replace hand-authored JSON recommendations with a rules engine that generates recommendations from any client dataset |

---

## Product roadmap

Based on `docs/prd/trace-prd.md` and `docs/strategy/sustainability-strategy-analysis.md`:

### Short term (post-hackathon to production MVP)
- Live Langfuse connector
- Live cloud billing connector (AWS CUR first)
- Real data pipeline replacing static CSV
- Named model coefficient table
- Dynamic recommendation generation
- Per-client deployment

### Medium term
- CCF Phase 1–2 integration (LLM estimator + cloud provider AI service connectors)
- Multi-cloud support (Azure OpenAI, GCP Vertex)
- Boavizta embodied emissions integration
- Evidence Pack PDF
- AI:works Control Plane carbon telemetry connector

### Long term
- Full CCF extension (all four phases)
- Carbon-linked gain-share pricing model
- Client-approved coefficient factors
- Real-time optimisation (carbon-aware routing)
- Scope 3 / Circular IT layer

---

## Key takeaways

- The TRACE MVP is a well-executed proof of concept, not a production system
- The primary limitations are (1) synthetic data, (2) no live connectors, and (3) blended energy coefficient estimates
- These limitations are disclosed honestly in the app itself and in this documentation
- The production path is well-defined; none of the limitations are blockers — they are sequenced engineering work
- The methodology is transparent about its confidence levels, which is a strength, not a weakness
- No actual client or sensitive data is in the repository
