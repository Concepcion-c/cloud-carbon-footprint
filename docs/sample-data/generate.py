#!/usr/bin/env python3
"""
RECPT — synthetic sample data generator (deterministic).

Produces tool-shaped synthetic data for the hackathon MVP (see
../prd/hackathon-mvp-prd-v2.md). NO real client data. Re-run anytime:

    python3 generate.py

Outputs (this folder):
  - llm_usage.csv                 Langfuse / OpenTelemetry-GenAI shaped (daily per-app rollups)
  - cloud_usage.csv               CCF-shaped (daily per-app rollups)
  - model_coefficients.csv        energy + price per 1M tokens, bucketed large/mid/small (illustrative)
  - model_coefficients_named.csv  energy + price per 1M tokens, by real Claude model name,
                                   with a split input/output/cache-read rate (see
                                   docs/notebooklm-wiki/06-calculations-and-methodology.md)
  - grid_intensity.csv            gCO2e/kWh + water-use-efficiency by region (public Electricity-Maps-style)
Companion (hand-authored, not generated here): recommendations.json, semgrep_findings.json,
  aiworks_usage_export.json, llm_trace_export.json, finops_cloud_export.csv,
  anthropic_console_export_sample.csv
"""
import csv, random, datetime

random.seed(42)  # deterministic

DAYS = [datetime.date(2026, 5, 1) + datetime.timedelta(days=i) for i in range(30)]

# model -> (provider, usd_per_1m, kwh_per_1m)   illustrative, blended
MODELS = {
    "large": ("anthropic", 30.0, 1.2),
    "mid":   ("anthropic", 6.0,  0.6),
    "small": ("anthropic", 1.0,  0.3),
}
# named model -> (provider, usd_in, usd_out, kwh_in, kwh_out, kwh_cache_read,
#                 g_co2e_per_kwh_default, confidence note)
# kwh_in/out from Jegham et al. 2025 (Sonnet, measured) and model-size-proxy
# extrapolation (Haiku/Opus); usd_in/out anchored to published per-tier Anthropic
# API pricing; kwh_cache_read = kwh_in * 0.1 (cache reads skip most prefill compute).
MODELS_NAMED = {
    "claude-haiku-4-5":  ("anthropic", 0.80, 4.00,  0.182, 1.039, 385,
                          "Medium - energy extrapolated by model-size proxy (no public Anthropic energy disclosure); cost anchored to published Haiku-tier pricing"),
    "claude-sonnet-4-6": ("anthropic", 3.00, 15.00, 0.494, 2.961, 385,
                          "Medium - energy derived from Jegham et al. 2025 measured per-query energies; cost anchored to published Sonnet-tier pricing"),
    "claude-opus-4-8":   ("anthropic", 15.00, 75.00, 1.039, 6.234, 385,
                          "Medium - energy extrapolated by model-size proxy (no public Anthropic energy disclosure); cost anchored to published Opus-tier pricing"),
}
# region -> (gCO2e/kWh, water-use-efficiency L/kWh)
GRID = {
    "us-west":  (210, 0.8),
    "eu-west":  (290, 0.5),
    "us-east":  (380, 1.2),
    "ap-south": (630, 1.8),
}

# app -> (model, region, monthly_tokens, cloud_service, monthly_cloud_kwh, monthly_cloud_cost)
APPS = {
    "Support-Bot":     ("large", "ap-south", 800_000_000, "Compute",    400, 3000),
    "Search-RAG":      ("small", "us-west",  400_000_000, "Storage",    700, 8000),
    "Doc-Summarizer":  ("mid",   "eu-west",  300_000_000, "Compute",    250, 2000),
    "Code-Assistant":  ("mid",   "us-east",  250_000_000, "Compute",    350, 4000),
    "Analytics-Agent": ("large", "us-east",  120_000_000, "Analytics",  800, 12000),
}

def daily_split(total, n):
    """Split `total` across n days with +-20% jitter, summing back to `total`."""
    factors = [random.uniform(0.8, 1.2) for _ in range(n)]
    s = sum(factors)
    out = [total * f / s for f in factors]
    return out

# --- llm_usage.csv ---
with open("llm_usage.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["date","app","model","provider","region",
                "input_tokens","output_tokens","total_tokens","cost_usd","trace_count"])
    for app,(model,region,monthly,_,_,_) in APPS.items():
        provider, usd_per_1m, _ = MODELS[model]
        for d, tok in zip(DAYS, daily_split(monthly, len(DAYS))):
            total = int(round(tok))
            inp = int(round(total * 0.6)); out = total - inp
            cost = round(total/1e6 * usd_per_1m, 2)
            traces = max(1, int(round(total / random.uniform(20000, 40000))))
            w.writerow([d.isoformat(), app, model, provider, region, inp, out, total, cost, traces])

# --- cloud_usage.csv ---
with open("cloud_usage.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["date","app","service","region","usage_kwh","cost_usd"])
    for app,(_,region,_,service,mk,mc) in APPS.items():
        for d, (kwh, cost) in zip(DAYS, zip(daily_split(mk, len(DAYS)), daily_split(mc, len(DAYS)))):
            w.writerow([d.isoformat(), app, service, region, round(kwh,3), round(cost,2)])

# --- model_coefficients.csv ---
with open("model_coefficients.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["model","provider","usd_per_1m_tokens","kwh_per_1m_tokens"])
    for m,(p,usd,kwh) in MODELS.items():
        w.writerow([m,p,usd,kwh])

# --- model_coefficients_named.csv ---
with open("model_coefficients_named.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["model_name","provider","usd_per_1m_input","usd_per_1m_output",
                "kwh_per_1m_input","kwh_per_1m_output","kwh_per_1m_cache_read",
                "g_co2e_per_kwh_default","notes_confidence"])
    for m,(p,usd_in,usd_out,kwh_in,kwh_out,grid_default,note) in MODELS_NAMED.items():
        w.writerow([m,p,usd_in,usd_out,kwh_in,kwh_out,round(kwh_in*0.1,4),grid_default,note])

# --- grid_intensity.csv ---
with open("grid_intensity.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["region","g_co2e_per_kwh","wue_liters_per_kwh"])
    for r,(g,wue) in GRID.items():
        w.writerow([r,g,wue])

print("Wrote llm_usage.csv, cloud_usage.csv, model_coefficients.csv, "
      "model_coefficients_named.csv, grid_intensity.csv")
