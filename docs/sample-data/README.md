# Sample data — RECPT MVP

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
| `model_coefficients_named.csv` | SCI-for-AI inputs | Per **named Claude model** (haiku/sonnet/opus), split `usd_per_1m_input/output`, `kwh_per_1m_input/output`, `kwh_per_1m_cache_read`, plus a `g_co2e_per_kwh_default` fallback and a `notes_confidence` provenance string. Energy figures for Sonnet are derived from Jegham et al. 2025's measured per-query energies; Haiku/Opus are extrapolated by model-size proxy (no public Anthropic energy disclosure) — see `docs/notebooklm-wiki/06-calculations-and-methodology.md`. |
| `grid_intensity.csv` | Electricity Maps | `g_co2e_per_kwh` and `wue_liters_per_kwh` by region (us-west 210/0.8, eu-west 290/0.5, us-east 380/1.2, ap-south 630/1.8) |
| `aiworks_usage_export.json` | **AI/Works Control Plane export** | Per-call records with real-shaped fields (`model_provider`, `model_name`, `input_tokens`, `output_tokens`, `total_cost_usd`, `agent_name`, `workflow_name`, `eval_score`, …) — 10 of 1,248 total records included (see file's own `_note`). Consumed by `app.py`'s `calc_ai_named()` and shown on Observe → "Anthropic (Real Data)". |
| `anthropic_console_export_sample.csv` | **Anthropic Console / Admin-API usage export** | `date,model,workspace,input_tokens,cache_read_input_tokens,output_tokens,cost_usd` — a sample file matching the tolerant import schema the Connect page's "AI/Works" → File upload flow accepts (see `normalize_anthropic_upload()` in `app.py`). Download it directly from that flow to see the expected shape. |
| `recommendations.json` | — | Optimization recs + **precomputed expected results** (validate the dashboard math) |
| `semgrep_findings.json` | `semgrep --json` | Synthetic code-risk findings for the Assess layer (stretch S2) |

## How carbon is computed (SCI-for-AI, transparent)
```
ai_carbon_g    = (total_tokens / 1e6) * kwh_per_1m * grid_g_per_kwh
ai_cost_usd    = (total_tokens / 1e6) * usd_per_1m
cloud_carbon_g = usage_kwh * grid_g_per_kwh
```
Location-based grid intensity; no offsets (offsets can't reduce an SCI score).

### Named-model variant (real Anthropic usage)
The bucketed formula above assumes a `large/mid/small` model class. For usage sources that
report a *real* model name and split input/output token counts (`aiworks_usage_export.json`,
or an uploaded Anthropic Console/Admin-API export), `app.py`'s `calc_ai_named()` uses:
```
ai_energy_kwh = (input_tokens/1e6)*kwh_per_1m_input
              + (output_tokens/1e6)*kwh_per_1m_output
              + (cache_read_input_tokens/1e6)*kwh_per_1m_cache_read
ai_carbon_kg  = ai_energy_kwh * region_carbon_kg_per_kwh
ai_cost_usd   = the source's own billed cost, when present — else the same
                usd_per_1m_input/output split as above
```
Cost is preferred from the real source (Anthropic tells you what it billed); energy, carbon,
and water are always estimates, since Anthropic does not publish per-model energy
consumption. An unrecognized model name falls back to the Sonnet row's coefficients. See
Observe → "Anthropic (Real Data)" in the running app.

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
`recommendations.json`, `semgrep_findings.json`, `aiworks_usage_export.json`,
`llm_trace_export.json`, `finops_cloud_export.csv`, and `anthropic_console_export_sample.csv`
are hand-authored (not regenerated). Update `recommendations.json`'s `expected` values if you
change the coefficients or app profiles in `generate.py`; update
`model_coefficients_named.csv`'s values by editing `MODELS_NAMED` in `generate.py`, not the
CSV directly, so they stay reproducible.
