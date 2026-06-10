# Sample data — TRACE MVP

> **Status:** v1 · **Last updated:** 2026-06-10

**Synthetic data only.** Everything here is illustrative/fabricated for the hackathon MVP
(see `../prd/hackathon-mvp-prd-v2.md`). **No real client, customer, or production data — no PII.**
Coefficients are derived from *public* benchmarks (ML.Energy, SCI-for-AI, Electricity Maps).

## Files
| File | Shaped like | Contents |
|---|---|---|
| `generate.py` | — | Deterministic generator (`python3 generate.py`, seed=42) — regenerate the CSVs anytime, no AI credits |
| `llm_usage.csv` | **Langfuse / OpenTelemetry-GenAI** | Daily per-app LLM rollups: tokens (in/out/total), model, provider, region, cost, trace_count |
| `cloud_usage.csv` | **CCF** output | Daily per-app cloud rollups: service, region, usage_kwh, cost |
| `model_coefficients.csv` | SCI-for-AI inputs | Per-model `usd_per_1m_tokens`, `kwh_per_1m_tokens` (large/mid/small) |
| `grid_intensity.csv` | Electricity Maps | `g_co2e_per_kwh` by region (us-west 210, eu-west 290, us-east 380, ap-south 630) |
| `recommendations.json` | — | Optimization recs + **precomputed expected results** (validate the dashboard math) |
| `semgrep_findings.json` | `semgrep --json` | Synthetic code-risk findings for the Assess layer (stretch S2) |

## How carbon is computed (SCI-for-AI, transparent)
```
ai_carbon_g    = (total_tokens / 1e6) * kwh_per_1m * grid_g_per_kwh
ai_cost_usd    = (total_tokens / 1e6) * usd_per_1m
cloud_carbon_g = usage_kwh * grid_g_per_kwh
```
Location-based grid intensity; no offsets (offsets can't reduce an SCI score).

## The seeded "wow moment" (verified)
Over the 30-day period, AI inference totals ≈ **794 kg CO₂e / $31,300**, and **Support-Bot
alone is ~76% of carbon and ~77% of cost** (large model, ap-south, high volume) — the obvious
optimization target.

`rec-support-bot-rightsizing` (route ~70% of its summarization to a small model + shift
ap-south→us-west, keep 30% on the large model for complex tickets) cuts **total AI carbon ≈ −49%
and total AI cost ≈ −52%** — credible, not magical, because quality is protected on the hard 30%.

`rec-analytics-region` shows a **pure carbon win** (region shift, cost unchanged) — i.e.
carbon-aware decisions, not just cost-driven ones.

## Regenerate
```bash
cd docs/sample-data && python3 generate.py
```
`recommendations.json` and `semgrep_findings.json` are hand-authored (not regenerated); update
their `expected` values if you change the coefficients or app profiles in `generate.py`.
