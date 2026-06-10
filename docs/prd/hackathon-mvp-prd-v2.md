# PRD: TRACE — 6-hour Hackathon MVP (v2, OSS-leveraged)

> **Status:** Draft v2 (current) · **Owner:** Concepcion-c · **Last updated:** 2026-06-10
> Supersedes `./hackathon-mvp-prd.md`. Same goal — a ≤5-min-demoable MVP in ~6 hours — but
> **reuses mature open-source tools** for the expensive parts to spend the fewest AI credits.
> Full product: `./trace-prd.md`. Strategy: `../strategy/sustainability-strategy-analysis.md`.

## 1. The one-sentence MVP
A **Streamlit** dashboard that loads **synthetic client data shaped like real tool outputs**
(Langfuse-style LLM usage + CCF-style cloud usage), shows **carbon beside cost** for **cloud +
AI inference** by app/model/region, ranks the worst apps (**Assess**), and lets you **apply an
optimization recommendation** and watch **both numbers drop live** — on a transparent,
SCI-for-AI methodology.

## 2. Core principle — reuse, don't rebuild (this is the credit-saver)
**We do not host or integrate these tools during the hackathon. We adopt their data *shapes*
and show the integration path.** Only the unique TRACE logic is custom code.

| Layer | We BUILD | We ADOPT (schema/lineage) | We ROADMAP (slide only) |
|---|---|---|---|
| Cloud carbon | — (use synthetic, CCF-shaped) | **CCF** methodology + output shape | Full CCF ingestion (Athena/BigQuery) |
| AI usage ledger | TRACE calculator | **Langfuse** trace schema | Live Langfuse host |
| AI gateway | — | gateway-log shape | **LiteLLM** proxy |
| Telemetry standard | — | **SCI-for-AI**, **OpenTelemetry GenAI** fields | OTel ingestion |
| Risk/Assess | Assess score logic | **Semgrep** JSON shape | **Trivy**, custom energy rules |
| UI / storage | **Streamlit** + pandas | (DuckDB optional) | React polish |

**Decided build stack:** Streamlit + pandas (+ optional DuckDB) + custom TRACE calculator +
bundled synthetic CSVs. **Why Streamlit:** fastest credible data dashboard for a semi-technical
builder — Python, no front-end build, charts included. (Revises v1's static-HTML call.)

## 3. In scope (MUST — demoable core)
- **M1. Load synthetic data** — a fake "upload client export" that reads bundled CSVs
  (`llm_usage.csv` Langfuse-shaped, `cloud_usage.csv` CCF-shaped, `model_coefficients.csv`,
  `grid_intensity.csv`).
- **M2. Hero KPIs** — total **cost ($)** and **carbon (gCO₂e)** side by side (cloud + AI combined).
- **M3. AI inference breakdown** — cost + carbon by **app / model / region**, from
  `tokens × energy/token × grid intensity`.
- **M4. Optimization recommendation + Apply** — ≥1 concrete rec (model swap / region shift /
  caching / prompt compression); **Apply** recomputes and **animates both totals dropping**,
  showing **% cost and % carbon saved**.
- **M5. Methodology transparency** — visible SCI-for-AI note + the coefficient table on screen.

## 4. Stretch (SHOULD — only after core)
- **S1. Cloud tab** — CCF-shaped cloud cost + carbon by service/region (mostly reuses M3 logic).
- **S2. Assess ranking** — rank apps by an energy-debt/intensity score; **import a real Semgrep
  JSON** to blend code-risk into the score (credibility booster).
- **S3. Before/after** — "client-zero" legacy-vs-modernized panel (AI:works as accelerator proof).
- **S4. Exportable carbon ledger** — download the SCI-for-AI table as CSV/PDF.
- **S5. One real Langfuse trace export** displayed to prove the production data path.

## 5. OUT of scope (the 6 hours)
Hosting Langfuse; running LiteLLM proxy live; real CCF ingestion; OpenTelemetry implementation;
Trivy; auth/multi-tenant; database beyond local files/DuckDB; real static energy analysis; live
AI:works. **All of these are roadmap-slide material, not build material.**

## 6. Synthetic data spec (tool-shaped; deterministic — no AI credits to generate)
Place in `../sample-data/`. Label clearly as synthetic; coefficients derive from public benchmarks.

**`llm_usage.csv` — Langfuse / OpenTelemetry-GenAI shaped**
`trace_id, timestamp, app, model, provider, region, task_type, input_tokens, output_tokens, total_tokens, cost_usd`

**`cloud_usage.csv` — CCF-shaped**
`timestamp, app, service, region, usage_kwh, cost_usd`

**`model_coefficients.csv`** *(illustrative, blended)*
| model | provider | usd_per_1m | kwh_per_1m |
|---|---|---|---|
| large | anthropic | 30 | 1.2 |
| mid | anthropic | 6 | 0.6 |
| small | anthropic | 1 | 0.3 |

**`grid_intensity.csv`** *(public Electricity-Maps-style, gCO₂e/kWh)*
`us-west,210` · `eu-west,290` · `us-east,380` · `ap-south,630`

**Formulas:** `ai_carbon_g = (total_tokens/1e6) × kwh_per_1m × grid_g_per_kwh` ·
`ai_cost = (total_tokens/1e6) × usd_per_1m` · cloud: `cloud_carbon_g = usage_kwh × grid_g_per_kwh`.

**Seed for the wow-moment:** make **Support-Bot = large model, ap-south, ~800M tokens/mo** → top
cost *and* carbon. The recommendation swaps it to **small model + us-west** → big drop in both.
Include a before/after row pair for S3.

## 7. Acceptance criteria
- App loads → hero **cost + carbon** render from the CSVs. *(M1, M2)*
- AI breakdown by app/model/region shows both metrics. *(M3)*
- Methodology + coefficient table visible. *(M5)*
- **Apply** updates totals and shows **% saved on both**. *(M4)*
- Runs locally (`streamlit run app.py`), no network/cloud, reproducible for recording.

## 8. Hour-by-hour plan (~6h, single builder)
| Time | Task | Output |
|---|---|---|
| 0:00–0:20 | `pip install streamlit pandas`; `app.py` hello; repo subfolder | App runs |
| 0:20–0:50 | Drop in the 4 synthetic CSVs (pre-generated); load with pandas | Data loads |
| 0:50–1:40 | TRACE calculator (AI + cloud carbon/cost) | Numbers correct |
| 1:40–3:00 | Dashboard: hero KPIs + AI breakdown (table + bar charts) | M2, M3 |
| 3:00–4:15 | Recommendation + **Apply** (recompute + delta display) | M4 |
| 4:15–5:00 | Methodology note + coefficient view + branding; (S1 cloud tab / S2 Assess if ahead) | M5 + polish |
| 5:00–6:00 | Record ≤5-min demo + draft written form; buffer | Submission |

## 9. Demo flow (maps to `../demo/`)
Hook (AI energy shock; invisible AI cost+carbon) → "upload" synthetic client export → **cost
beside carbon** (cloud + AI) → AI breakdown by model/app/region → **Assess**: worst app by
energy debt → **Apply** a recommendation (Support-Bot large→small, ap-south→us-west) → **both
numbers drop live** → methodology = open, SCI-for-AI, ingests Langfuse/LiteLLM/OTel/provider
exports → close: *"This is CCF evolved for AI GreenOps — a tool clients buy and keep; AI:works
is how we build it, client zero."*

## 10. Risks (build-day)
| Risk | Mitigation |
|---|---|
| OSS-stack scope creep | Build NONE of the tools live; adopt shapes only; §5 is law |
| Streamlit unfamiliarity | It's ~20 lines for a dashboard; lean on `st.metric`, `st.bar_chart`, `st.dataframe` |
| Tools look bolted-on | The schema-alignment table (§2) + roadmap slide makes reuse the *story*, not a hack |
| Numbers too precise/fake | Label synthetic; cite public coefficient sources; show ranges |
| "Just a carbon dashboard" critique | Lead with **Apply-moves-both-numbers** + Assess (Semgrep) + open method |
| Credits burned vibe-coding | Pre-generate data (done outside the build); keep one screen; minimal custom code |

## 11. Definition of done
A `streamlit run`-able dashboard meeting §7, a recorded ≤5-min demo, and a drafted written
submission — committed to `~/projects/TRACE` (private). Production integration (CCF/Langfuse/
LiteLLM/OTel/Semgrep) shown as a roadmap slide, not built.
