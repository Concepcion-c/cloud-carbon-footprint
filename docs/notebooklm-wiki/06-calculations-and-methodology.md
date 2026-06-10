# 06 — Calculations & Methodology

> **Summary:** Every formula TRACE uses, where each one came from, the assumptions behind the numbers, worked examples in plain English, and an honest account of what is exact versus estimated.

---

## The big picture: what TRACE calculates

TRACE takes two types of raw data — **AI usage data** (token counts) and **cloud billing data** (kilowatt-hours) — and converts them into four metrics:

- **Cost** (USD)
- **Carbon** (kg CO₂e)
- **Energy** (kWh)
- **Water** (litres)

It does this using three lookup tables:
1. **Model coefficients** — how much energy and money does each model class consume per million tokens?
2. **Grid intensity** — how much carbon does the electricity grid in each region produce per kWh?
3. **WUE (Water Usage Effectiveness)** — how much water does a data centre in each region use per kWh?

---

## The five core formulas

### Formula 1: AI inference energy

```
ai_energy_kWh = (total_tokens / 1,000,000) × kWh_per_1M_tokens
```

**Plain English:** Count the tokens, divide by a million, multiply by how much electricity one million tokens consume for that model class.

**Source:** Derived from GPU hardware specifications (NVIDIA A100/H100), token throughput benchmarks (MLPerf), and server overhead estimates. See *Where the kWh/1M numbers come from* below.

**Implemented in:** `calc_ai()` function in `app.py`.

---

### Formula 2: AI inference carbon

```
ai_carbon_kg = ai_energy_kWh × grid_intensity_gCO₂e_per_kWh / 1000
```

**Plain English:** Take the energy used, multiply by how dirty the local electricity grid is (measured in grams of CO₂e per kWh), then divide by 1,000 to convert grams to kilograms.

**Source:** SCI-for-AI (Green Software Foundation); grid intensity values from Electricity Maps, EPA eGRID, ENTSO-E. This is a location-based calculation — it uses the actual carbon content of the grid where the computation runs, with no market-based renewable energy certificates or offsets applied.

**Why no offsets?** TRACE follows the ISO 21031 standard, which requires location-based accounting. This produces a more honest, auditable number. Claiming a model runs on renewable energy via offsets would reduce the reported carbon without actually changing the physical electricity used.

**Implemented in:** `calc_ai()` in `app.py`.

---

### Formula 3: AI inference cost

```
ai_cost_usd = (total_tokens / 1,000,000) × usd_per_1M_tokens
```

**Plain English:** Count the tokens, divide by a million, multiply by the model's published price per million tokens.

**Source:** Published pricing from Anthropic and OpenAI as of mid-2025.

**Implemented in:** `calc_ai()` in `app.py`.

---

### Formula 4: Cloud infrastructure carbon

```
cloud_carbon_kg = usage_kWh × grid_intensity_gCO₂e_per_kWh / 1000
```

**Plain English:** Take the kilowatt-hours from the cloud billing export (which already represents actual measured energy), multiply by grid intensity, and convert to kg.

**Note:** Cloud energy (kWh) comes directly from billing data — it is a measured value. AI energy (kWh) is *estimated* from token counts — it is a calculated proxy. This distinction matters for understanding confidence levels.

**Source:** Cloud Carbon Footprint methodology; same grid intensity values as formula 2.

**Implemented in:** `calc_cloud()` in `app.py`.

---

### Formula 5: Water consumption (AI and cloud)

```
water_liters = energy_kWh × WUE_liters_per_kWh
```

**Plain English:** Take the energy used, multiply by how many litres of water the data centre in that region consumes per kWh of energy delivered. The WUE (Water Usage Effectiveness) factor varies by region based on climate, cooling technology, and local water stress.

**Source:** The Green Grid WUE methodology; Li et al. (2023), *Making AI Less Thirsty*; Google Environmental Report 2023; Uptime Institute WUE survey data.

**Implemented in:** `calc_ai()`, `calc_cloud()`, and `load_trace_data()` in `app.py`.

---

### Formula 6: Energy Debt Score

```
energy_debt_score = (0.6 × carbon_rank) + (0.4 × code_risk_rank)
```

**Plain English:** Each app gets a score between 0 and 1. It is 60% based on how much carbon the app produces at runtime (relative to the worst offender) and 40% based on how many code-level inefficiency findings the code scan flagged. A score of 1.00 is the worst possible.

**Implemented in:** The Energy Debt tab calculation in `app.py`.

---

## The lookup tables

### Model coefficients

| Model class | Provider | USD / 1M tokens | kWh / 1M tokens |
|---|---|---|---|
| large | anthropic | $30.00 | 1.2 |
| mid | anthropic | $6.00 | 0.6 |
| small | anthropic | $1.00 | 0.3 |

**File:** `docs/sample-data/model_coefficients.csv`

**Named model equivalents** (used for agent traces):
| Model name | kWh / 1M tokens |
|---|---|
| claude-opus-4-8 | 1.2 |
| claude-sonnet-4-6 | 0.6 |
| claude-haiku-4-5 | 0.3 |
| gpt-4.1 | 0.5 |
| gpt-4o | 0.6 |

---

### Grid intensity (carbon + water per region)

| Region | gCO₂e / kWh | WUE (L / kWh) | Real-world location |
|---|---|---|---|
| us-west | 210 | 0.8 | Oregon / Pacific Northwest |
| eu-west | 290 | 0.5 | Ireland |
| us-east | 380 | 1.2 | Virginia |
| ap-south | 630 | 1.8 | Mumbai |

**File:** `docs/sample-data/grid_intensity.csv`

**WUE explanation:** eu-west (Ireland) has the lowest WUE (0.5) because the cool, damp climate reduces the need for water-intensive evaporative cooling. ap-south (Mumbai) has the highest WUE (1.8) because the hot climate requires significantly more cooling water. Oregon (us-west) is moderate at 0.8 due to its cooler climate and hydro-heavy electricity mix.

---

## Where the kWh/1M token numbers come from

The energy-per-token coefficients cannot be looked up in a price list — they must be estimated from hardware benchmarks and inference performance data. Here is the derivation step by step.

**Step 1: GPU power draw**
An NVIDIA A100 or H100 running inference draws significant power:
- A100: up to ~400W at full load
- H100: up to ~700W at full load
- At ~70% utilisation (typical inference workload): ~280–490W continuously

**Step 2: Token throughput**
A large model (70 billion or more parameters) on an A100 produces approximately **500–1,500 tokens per second**, depending on batch size, quantisation, and serving configuration.

**Step 3: Energy per token (GPU level)**
Using a mid-range estimate of 400W and 1,000 tokens/second:
```
400W / 1,000 tokens/sec = 0.4 Wh / 1,000 tokens
                        = 0.4 kWh / 1M tokens (GPU only)
```

**Step 4: Server overhead**
The GPU is not the only component consuming power. Server-level overhead (CPU, RAM, networking, storage) adds approximately **1.3×–1.6×**. Using a midpoint of 1.5×:
```
0.4 × 1.5 = 0.6 kWh / 1M tokens (server level, mid-tier model)
```

**Step 5: Data centre PUE**
Hyperscalers (AWS, Google, Azure) operate with PUE (Power Usage Effectiveness) values around 1.1–1.2, meaning for every 1 kWh delivered to the server, roughly 1.2 kWh is consumed by the facility (cooling, lighting, power distribution). **This is folded into the coefficient**, not applied separately:
```
0.6 × 1.2 = 0.72 kWh / 1M tokens (full facility, mid-tier)
```

TRACE uses **0.6 kWh / 1M tokens** for mid-tier models — this represents the server-level estimate with PUE included in the blending. The final coefficient is a round number that sits within the range of published benchmark estimates.

**Small and large model scaling:**
- `small` models use approximately half the energy of `mid` → 0.3 kWh/1M
- `large` models use approximately twice the energy of `mid` (more parameters, more GPU memory, longer compute time per token) → 1.2 kWh/1M

**Supporting references:**
- Luccioni et al. (2023), *Power Hungry Processing* — benchmarked inference energy for various model sizes
- MLPerf Inference benchmarks — token throughput under various hardware conditions
- NVIDIA A100/H100 specification sheets — GPU TDP figures

---

## Confidence levels

TRACE uses three confidence levels, consistent with how CCF approaches measurement confidence:

| Level | Meaning | When it applies |
|---|---|---|
| **High** | All inputs are measured or directly sourced from provider data | Cloud kWh from billing data + confirmed regional grid factor |
| **Medium** | One or more inputs are estimated from benchmarks or averages | AI energy from token counts × model-class coefficient; WUE estimates for most regions |
| **Low** | Region or model is missing; a fallback average is used | Region not in lookup table; WUE defaulting to 1.0 L/kWh |

**The current MVP operates at Medium confidence throughout** — because the energy-per-token values are blended estimates, not vendor-measured figures.

---

## A worked example: Support-Bot on 1 May 2026

Support-Bot runs a `large` Anthropic model in `ap-south` (Mumbai).

**Input data:**
| Field | Value |
|---|---|
| Total tokens | 29,040,315 |
| kWh / 1M tokens | 1.2 (large model) |
| USD / 1M tokens | $30.00 |
| Grid intensity | 630 gCO₂e/kWh (ap-south) |
| WUE | 1.8 L/kWh (ap-south) |

**Step 1 — AI energy:**
```
(29,040,315 / 1,000,000) × 1.2 = 29.04 × 1.2 = 34.85 kWh
```

**Step 2 — AI carbon:**
```
34.85 × 630 / 1000 = 34.85 × 0.630 = 21.95 kg CO₂e
```

**Step 3 — AI cost:**
```
(29,040,315 / 1,000,000) × 30.00 = 29.04 × 30 = $871.21
```

**Step 4 — AI water:**
```
34.85 × 1.8 = 62.7 litres
```

**Monthly totals (×30 days):**
- **~605 kg CO₂e / month**
- **~$24,000 / month**
- **~1,881 litres of water / month** (approximately 12 bathtubs)

**What if Support-Bot ran in us-west instead?**
- Grid intensity: 210 gCO₂e/kWh (vs 630)
- Carbon would drop from 21.95 to 7.32 kg CO₂e/day — a **67% reduction** from the region change alone
- Water would drop from 62.7 L to 27.9 L/day — a **55% reduction**

---

## The recommendation calculation

When a recommendation is applied, TRACE does not use pre-computed numbers. It recomputes the entire AI footprint from scratch with the recommendation's changes applied.

**How it works:**
1. Take the full LLM usage DataFrame (30 days × 4 apps × multiple records)
2. For the target app (e.g., Support-Bot), split traffic according to the recommendation's `fraction` parameter (e.g., 0.7 = 70%)
3. Apply the model swap (e.g., `large` → `small`) to the 70% fraction
4. Apply the region shift (e.g., `ap-south` → `us-west`) to the same fraction
5. Keep the remaining 30% unchanged (on the original model and region)
6. Recalculate all energy, carbon, cost, and water metrics for the modified dataset
7. Update all KPIs, charts, and the before/after table

This is why the impact numbers in TRACE are not approximations — they are genuine recalculations of the model.

---

## How TRACE compares to other tools

**Compared to Greenpixie:**
- Both are estimate-based (neither reads an actual power meter)
- Greenpixie uses an explicit PUE multiplier at runtime: `total_facility_energy = IT_energy × PUE`
- TRACE folds PUE into the per-token coefficient — different approach, equivalent result
- TRACE adds water consumption; Greenpixie does not

**Compared to Cloud Carbon Footprint (CCF):**
- CCF measures infrastructure energy directly from billing kWh data (High confidence)
- TRACE estimates AI energy from token counts × coefficient (Medium confidence)
- Both use the same location-based grid intensity approach
- Both use the same grid intensity data sources (Electricity Maps, EPA eGRID, ENTSO-E)
- TRACE adds the AI inference layer that CCF does not have

---

## What is exact versus estimated

| Metric | How it is calculated | Confidence |
|---|---|---|
| Cloud cost | From billing data (direct) | High |
| Cloud energy (kWh) | From billing data (direct) | High |
| Cloud carbon | kWh × grid intensity (grid intensity is sourced, kWh is measured) | High/Medium |
| Cloud water | kWh × WUE (WUE is estimated for most regions) | Medium |
| AI cost | Tokens × published price (price is exact; token count from logs) | High |
| AI energy | Tokens × kWh/1M coefficient (coefficient is blended estimate) | Medium |
| AI carbon | AI energy × grid intensity | Medium |
| AI water | AI energy × WUE | Medium |

---

## Known methodology limitations

1. **Closed-model coefficients are estimates.** Anthropic and OpenAI do not publish per-model energy consumption. The kWh/1M values are derived from public hardware benchmarks and may not reflect the specific infrastructure these providers use.

2. **WUE values are estimated for most regions.** Google publishes facility-level WUE. AWS does not publish region-level WUE with the same transparency. The values in TRACE are estimates from industry surveys and climate-based reasoning.

3. **Hardware mix is blended.** The coefficients assume a typical mix of A100/H100 GPUs. Providers may use different hardware, quantisation, or batching strategies that alter per-token energy.

4. **PUE is an industry average.** Hyperscalers report PUE values between 1.1 and 1.2. TRACE uses 1.2 as a conservative estimate. Actual facility PUE varies.

5. **Token-to-energy scaling is approximate.** The relationship between model size and energy per token is not perfectly linear. The large/mid/small coefficient ratios (1.2 / 0.6 / 0.3) are reasonable approximations, not precision measurements.

---

## Key takeaways

- TRACE uses five core formulas: AI energy, AI carbon, AI cost, cloud carbon, and water — all traceable to published sources
- The kWh/1M token coefficients are derived from GPU specs and benchmark data, not vendor-measured — this is the primary source of uncertainty
- The methodology is aligned to SCI-for-AI and ISO 21031 — location-based, no offsets, transparent
- Medium confidence is the honest answer for AI inference carbon — and TRACE says so in the app itself
- The recommendation engine recalculates the full footprint from scratch — the impact numbers are genuine, not estimates on top of estimates
