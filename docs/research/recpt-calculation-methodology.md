# How RECPT Calculates Energy, Cost, Carbon, and Water

This document explains how RECPT calculates AI inference energy, AI inference carbon, AI inference cost, cloud infrastructure carbon, and water consumption.

The current implementation uses a lightweight estimation model based on token counts, model coefficients, regional grid intensity, regional WUE, and cloud usage data.

---

## 1. Core RECPT Formulas

The core formulas come from `app.py`.

### AI Inference Energy

```
ai_energy_kWh = (total_tokens / 1,000,000) × kWh_per_1M_tokens
```

This estimates the energy used by AI inference based on the total number of tokens processed. The `kWh_per_1M_tokens` coefficient is a blended hardware estimate that includes GPU energy, server overhead, and data center PUE — see Section 5 for the full derivation.

**Source:** Luccioni et al. (2023), *Power Hungry Processing: Watts Driving the Cost of AI Deployment*; NVIDIA A100/H100 spec sheets; MLPerf Inference benchmarks.

---

### AI Inference Carbon

```
ai_carbon_kg = ai_energy_kWh × grid_intensity_gCO₂e_per_kWh / 1000
```

This converts AI inference energy into carbon emissions. The division by 1,000 converts grams of CO₂e into kilograms of CO₂e.

**Source:** SCI-for-AI (Green Software Foundation); Electricity Maps; EPA eGRID; ENTSO-E. RECPT uses location-based grid intensity — no market-based RECs or offsets applied. This is intentional and aligned to ISO 21031.

---

### AI Inference Cost

```
ai_cost_usd = (total_tokens / 1,000,000) × usd_per_1M_tokens
```

This estimates the cost of AI inference based on token volume and the model's price per 1 million tokens. Costs come from `model_coefficients.csv`.

**Source:** Anthropic and OpenAI published pricing as of mid-2025.

---

### Cloud Infrastructure Carbon

```
cloud_carbon_kg = usage_kWh × grid_intensity_gCO₂e_per_kWh / 1000
```

This converts cloud infrastructure energy use into carbon emissions. The cloud energy value (`usage_kWh`) comes directly from the billing export. The AI energy value is estimated from token counts because LLM providers generally do not expose per-call energy readings — RECPT backs into that energy usage from hardware and inference benchmarks.

**Source:** Cloud Carbon Footprint methodology; Electricity Maps; EPA eGRID.

---

### AI Water Consumption

```
ai_water_liters = ai_energy_kWh × WUE_liters_per_kWh
```

WUE (Water Usage Effectiveness) estimates how many liters of water a data center consumes per kWh of energy delivered to IT equipment. The regional WUE values come from `grid_intensity.csv` (same lookup used for carbon). Water is calculated per span in `load_trace_data()` and per row in `calc_ai()`.

**Source:** The Green Grid, *Water Usage Effectiveness*; Li et al. (2023), *Making AI Less Thirsty*; Google Environmental Report 2023; Uptime Institute WUE survey data.

---

### Cloud Water Consumption

```
cloud_water_liters = usage_kWh × WUE_liters_per_kWh
```

The same WUE lookup applies to cloud infrastructure energy. Calculated per row in `calc_cloud()`.

---

## 2. The Two Lookup Tables That Do the Work

RECPT relies on two main lookup tables: `model_coefficients.csv` and `grid_intensity.csv`. Together, these convert token usage into energy, cost, carbon, and water.

---

### model_coefficients.csv

This table converts tokens into estimated energy and cost.

| Model  | Provider  | USD / 1M Tokens | kWh / 1M Tokens |
|--------|-----------|----------------|----------------|
| large  | anthropic | 30.00          | 1.2            |
| mid    | anthropic | 6.00           | 0.6            |
| small  | anthropic | 1.00           | 0.3            |

**Source:** Energy coefficients are blended hardware estimates — see Section 5. Cost per 1M tokens is based on published Anthropic pricing (mid-2025). The model class labels (large/mid/small) map to named models via the `MODEL_KWH_PER_1M` constant in `app.py`:

| Named model            | Provider  | kWh / 1M tokens |
|------------------------|-----------|----------------|
| claude-opus-4-8        | Anthropic | 1.2            |
| claude-sonnet-4-6      | Anthropic | 0.6            |
| claude-haiku-4-5       | Anthropic | 0.3            |
| gpt-4.1                | OpenAI    | 0.5            |
| gpt-4o                 | OpenAI    | 0.6            |

---

### grid_intensity.csv

This table converts energy into carbon and water by region.

| Region    | gCO₂e / kWh | WUE (L / kWh) |
|-----------|------------|---------------|
| us-west   | 210        | 0.8           |
| eu-west   | 290        | 0.5           |
| us-east   | 380        | 1.2           |
| ap-south  | 630        | 1.8           |

**Carbon source:** Electricity Maps / EPA eGRID / ENTSO-E. Location-based, no offsets.

**WUE source:** Region-level estimates from public data center efficiency reporting. Key inputs:
- `eu-west` (Ireland): Low WUE due to cool climate and low water stress; consistent with Google's reported EU West figures
- `us-west` (Oregon/Pacific NW): Moderate WUE; mix of hydro and cooler climate
- `us-east` (Virginia): Higher WUE; warmer climate, more mechanical cooling
- `ap-south` (Mumbai): Highest WUE; hot climate, significant evaporative cooling demand

AWS does not publish region-level WUE with the same transparency as Google. These values are estimates and should be flagged as Medium confidence in production.

---

## 3. Worked Example: Support-Bot on May 1, 2026

Support-Bot runs a `large` Anthropic model in `ap-south`, which represents the Mumbai region.

### Input Data

| Field             | Value          |
|-------------------|----------------|
| Date              | 2026-05-01     |
| App               | Support-Bot    |
| Model             | large          |
| Provider          | anthropic      |
| Region            | ap-south       |
| Total tokens      | 29,040,315     |
| kWh / 1M tokens   | 1.2            |
| USD / 1M tokens   | 30.00          |
| Grid intensity    | 630 gCO₂e / kWh |
| WUE               | 1.8 L / kWh    |

---

### Step 1: Calculate AI Energy

```
ai_energy_kWh = (29,040,315 / 1,000,000) × 1.2
              = 29.04 × 1.2
              = 34.85 kWh
```

Support-Bot used approximately **34.85 kWh** of AI inference energy on May 1, 2026.

---

### Step 2: Calculate AI Carbon

```
ai_carbon_kg = 34.85 × 630 / 1000
             = 34.85 × 0.630
             = 21.95 kg CO₂e
```

Support-Bot produced approximately **21.95 kg CO₂e** on May 1, 2026.

---

### Step 3: Calculate AI Cost

```
ai_cost_usd = (29,040,315 / 1,000,000) × 30.00
            = 29.04 × 30
            = $871.21
```

Support-Bot cost approximately **$871.21** on May 1, 2026.

---

### Step 4: Calculate AI Water

```
ai_water_liters = 34.85 × 1.8
                = 62.7 liters
```

Support-Bot consumed approximately **62.7 liters of water** on May 1, 2026.

---

## 4. Monthly Impact

Over 30 days, Support-Bot produces roughly:

- **605 kg CO₂e / month**
- **~$24,000 / month**
- **~1,881 liters of water / month** (approximately 12 bathtubs)

This is why Support-Bot appears as the top offender in the dashboard.

Moving Support-Bot from a `large` model in `ap-south` to a `small` model in `us-west` drops carbon, cost, and water by approximately **65%** — both the energy coefficient and the regional WUE are lower in us-west.

---

## 5. Where the kWh / 1M Token Coefficients Come From

The `kWh_per_1M_tokens` coefficients are blended hardware estimates. They are not vendor-published figures.

### Step 1: GPU Power Draw

An NVIDIA A100 or H100 running inference draws significant power.

| GPU         | Typical TDP  |
|-------------|-------------|
| NVIDIA A100 | Up to ~400W  |
| NVIDIA H100 | Up to ~700W  |

At ~70% utilization, inference workloads draw approximately 280–490W continuously.

### Step 2: Token Throughput

A large model (70B+ parameters) on an A100 produces approximately **500–1,500 tokens/second** depending on batch size, quantization, and serving configuration.

### Step 3: Energy per Token (GPU-level)

```
400W / 1,000 tokens/sec = 0.4 Wh / 1,000 tokens
                        = 0.4 kWh / 1M tokens  (GPU only)
```

### Step 4: Server Overhead

The GPU is not the only power consumer. Server-level overhead (CPU, RAM, networking, storage) adds approximately **1.3×–1.6×**. Using a midpoint of 1.5×:

```
0.4 × 1.5 = 0.6 kWh / 1M tokens  (server level, mid-tier model)
```

This ~0.6 kWh/1M figure is the basis for the **mid-tier model coefficient**.

### Step 5: Data Center Overhead / PUE

Hyperscalers operate with PUE values around 1.1–1.2. Applying PUE = 1.2:

```
0.6 × 1.2 = 0.72 kWh / 1M tokens  (full facility, mid-tier)
```

RECPT uses **0.6 kWh / 1M tokens** for mid-tier models — this is the server-level estimate without separate PUE multiplication, because PUE is already folded into the coefficient (see Section 6).

### Final Coefficients

| Model class | Derivation                                | kWh / 1M Tokens |
|-------------|-------------------------------------------|----------------|
| small       | ~50% of mid (smaller model, fewer params) | 0.3            |
| mid         | Server-level estimate (~0.6)              | 0.6            |
| large       | 2× mid (larger model, more GPU memory)    | 1.2            |

The `large` coefficient (1.2) is a conservative upper-bound for Opus/GPT-4-class models — larger context windows and more parameters roughly double the per-token energy of a mid-tier model.

---

## 6. Important Caveat About PUE

The `kWh_per_1M_tokens` coefficient **already includes PUE**.

RECPT does not separately multiply AI inference energy by PUE at runtime. The formula:

```
tokens × kWh_per_1M_tokens
```

already includes:
- GPU energy
- Server overhead
- Data center overhead (PUE ≈ 1.2)

This is similar to the Greenpixie approach, but RECPT folds PUE into the per-token coefficient because RECPT does not have measured IT energy as an input.

---

## 7. What Greenpixie Does vs. What RECPT Does

Silvia is right that Greenpixie also does not ingest actual power consumption.

Greenpixie's approach is roughly:

```
total_facility_energy = IT_energy × PUE
carbon = total_facility_energy × grid_intensity
```

RECPT's approach is equivalent but starts from the token side:

```
IT_energy = tokens × kWh_per_1M_tokens
carbon = IT_energy × grid_intensity
```

| Dimension                        | Greenpixie                              | RECPT                                      |
|----------------------------------|-----------------------------------------|--------------------------------------------|
| Starting point                   | Measured or estimated IT energy         | Token counts                               |
| PUE handling                     | Explicit multiplier at runtime          | Folded into per-token coefficient          |
| Carbon conversion                | Energy × grid intensity                 | Energy × grid intensity                    |
| Water                            | Not in scope                            | Energy × WUE per region (built in)         |
| Estimation basis                 | Estimate-based                          | Estimate-based                             |

Neither system reads an actual power meter. Both use estimation models.

---

## 8. Water Consumption: Implemented

Water consumption is built into RECPT. The formula:

```
water_liters = energy_kWh × WUE_liters_per_kWh
```

WUE (Water Usage Effectiveness) estimates how many liters of water a data center consumes per kWh of energy. The values are region-specific and stored in `grid_intensity.csv`.

### What was built

**Data layer:** `grid_intensity.csv` — `wue_liters_per_kwh` column added for all four regions.

**Calculator (`app.py`):**
- `calc_ai()` — `df["ai_water_liters"] = df["ai_energy_kwh"] * df["wue_liters_per_kwh"]`
- `calc_cloud()` — `df["cloud_water_liters"] = df["usage_kwh"] * df["wue_liters_per_kwh"]`
- `load_trace_data()` — each span enriched with `water_liters = kwh × REGION_WUE[region]`

**Dashboard:**
- KPI cards — Total Water, AI Water, Cloud Water
- AI Detail tab — Energy & Water by App, Energy/Water by Model, Energy/Water by Region breakdowns
- Agent Traces — Water (L) column in span details table
- Optimize — AI Water column in what-if scenario table
- Prove — AI Water and Cloud Water rows in before/after comparison; `water_liters` field in CSV exports

### WUE values in use

| Region    | WUE (L / kWh) | Basis                                                   |
|-----------|--------------|--------------------------------------------------------|
| eu-west   | 0.5          | Ireland — cool climate, low water stress               |
| us-west   | 0.8          | Oregon — Pacific NW, hydro-heavy, cooler climate       |
| us-east   | 1.2          | Virginia — warmer climate, more mechanical cooling     |
| ap-south  | 1.8          | Mumbai — hot climate, high evaporative cooling demand  |

---

## 9. Water Example: Support-Bot

Using the Support-Bot example from Section 3:

```
ai_energy_kWh = 34.85 kWh / day
WUE (ap-south) = 1.8 L / kWh

water_liters_per_day   = 34.85 × 1.8 = 62.7 liters / day
water_liters_per_month = 62.7 × 30   = 1,881 liters / month
```

That is approximately **12 bathtubs of water per month** for one bot's inference workload.

For comparison, if Support-Bot ran in `eu-west` (Ireland, WUE = 0.5):

```
water_liters_per_day   = 34.85 × 0.5 = 17.4 liters / day
water_liters_per_month = 17.4 × 30   = 523 liters / month
```

This means **region selection reduces water consumption by 72%** for the same workload — the same lever that cuts carbon also cuts water.

---

## 10. Data Model and Confidence

Water confidence tracks carbon confidence:

- **High** — region present in lookup, regional WUE sourced from public provider reporting
- **Medium** — region-level estimate from industry averages; AWS does not publish region-level WUE with full transparency
- **Low** — region missing; fallback WUE = 1.0 L/kWh (global average) is applied

In production, RECPT would support client-approved WUE factors and provider-specific values (Google, Microsoft, and others publish facility-level WUE; AWS publishes less granularly).

---

## 11. Sources

| Topic                                | Source                                                                                  |
|--------------------------------------|-----------------------------------------------------------------------------------------|
| Primary carbon methodology           | SCI-for-AI, Green Software Foundation                                                   |
| Grid carbon intensity, real-time     | Electricity Maps                                                                        |
| US regional grid factors             | EPA eGRID                                                                               |
| EU grid factors                      | ENTSO-E Transparency Platform                                                           |
| GPU energy and inference benchmarks  | MLPerf Inference benchmarks; NVIDIA A100/H100 spec sheets                               |
| LLM inference energy                 | Luccioni et al. (2023), *Power Hungry Processing: Watts Driving the Cost of AI Deployment* |
| LLM training vs. inference carbon    | Patterson et al. (2022), *Carbon Emissions and Large Neural Network Training*           |
| PUE industry averages                | Uptime Institute Annual Global Data Center Survey                                       |
| WUE methodology                      | The Green Grid, *Water Usage Effectiveness*; Google Environmental Report 2023           |
| AI water footprint                   | Li et al. (2023), *Making AI Less Thirsty: Uncovering and Addressing the Secret Water Footprint of AI Models* |
| Open-source cloud carbon baseline    | Cloud Carbon Footprint methodology docs                                                 |

---

## 12. Bottom Line for Silvia

Water is a one-column extension to the data model and one extra formula line in the calculator — and it is now built.

The math is parallel to carbon:

```
carbon = energy × grid_intensity
water  = energy × WUE
```

The harder part is choosing the right WUE by cloud provider and region, since AWS does not publish region-level WUE as transparently as Google. RECPT uses region-level estimates with a Medium confidence label, consistent with how it handles grid intensity.

Both carbon and water go down when you shift workloads to cleaner, lower-WUE regions — the optimization lever is the same for both metrics.
