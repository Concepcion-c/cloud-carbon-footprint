# 10 — Primary Sources Appendix

> **Summary:** Every source used to build TRACE — standards, frameworks, research papers, datasets, tools, and project documents. For each source: what it is, what it was used for, which part of the app or methodology it influenced, and its confirmation status.

---

## How to use this appendix

This document answers questions like:
- "Where did this formula come from?"
- "Is this methodology defensible?"
- "Which parts of TRACE are based on published standards?"
- "What is estimated versus verified?"

**Confirmation status labels:**
- ✅ **Confirmed in app** — the source directly drives a calculation, data value, or design decision visible in `app.py` or a data file
- 📄 **Confirmed in project docs** — cited in project research notes, PRDs, or the CHANGELOG; shapes the project thinking but may not be directly coded
- 🗺️ **Referenced as future integration** — mentioned in project docs as a planned source; not yet implemented
- ⚠️ **Recommended addition** — not currently cited in the repo; would strengthen the methodology

---

## Standards and frameworks

### SCI — Software Carbon Intensity (ISO/IEC 21031:2024)
| Attribute | Detail |
|---|---|
| **Type** | International standard |
| **Organisation** | Green Software Foundation (ratified as ISO/IEC 21031:2024) |
| **Status** | ✅ Confirmed in app |
| **What it defines** | A rate-based carbon metric: `SCI = (O + M) / R`, where O = operational carbon, M = embodied carbon, R = functional unit (e.g., per API call, per million tokens). Location-based, no offsets can reduce the score. |
| **How TRACE uses it** | The AI inference carbon formula is SCI-for-AI conformant: `tokens → energy → carbon` with location-based grid intensity and no offsets. The Prove > Methodology page explicitly lists SCI-for-AI as the primary standard. |
| **Where it appears** | `docs/research/trace-calculation-methodology.md`; `app.py` Prove page; `docs/prd/trace-prd.md` |
| **Caveats** | TRACE implements SCI-for-AI for the operational carbon (O) dimension. The embodied carbon (M) dimension is not yet implemented (Boavizta integration is planned). |

---

### SCI-for-AI (Green Software Foundation)
| Attribute | Detail |
|---|---|
| **Type** | Framework extension of SCI |
| **Organisation** | Green Software Foundation |
| **Status** | ✅ Confirmed in app |
| **What it defines** | Extends SCI to the AI lifecycle — training, fine-tuning, inference. Ratified Q4 2024; ISO-readiness Q1 2026. Built by 100+ organisations including Accenture, Google, Microsoft, IBM. Linked to EU AI Act environmental compliance. |
| **How TRACE uses it** | The core formula `(tokens / 1M) × kWh_per_1M_tokens × grid_gCO₂e_per_kWh` follows the SCI-for-AI approach for inference carbon. TRACE's methodology is described as "SCI-for-AI conformant" in the app. |
| **Where it appears** | `app.py` (Prove > Methodology > Standards Alignment table); `docs/research/trace-calculation-methodology.md` Section 11 |
| **Caveats** | TRACE implements inference carbon only. Training and fine-tuning carbon is out of scope for the MVP. |

---

### ISO/IEC 21031:2024 (the GHG accounting standard SCI resolves to)
| Attribute | Detail |
|---|---|
| **Type** | International standard |
| **Status** | ✅ Confirmed in app |
| **What it defines** | The GHG accounting boundary: operational boundary, location-based grid, no market-based offsets. |
| **How TRACE uses it** | TRACE's methodology is described as "ISO 21031 conformant" — location-based, no offsets, transparent assumptions. |
| **Where it appears** | `docs/research/trace-calculation-methodology.md`; `app.py` Prove page caption |

---

## Open-source tools and frameworks

### Cloud Carbon Footprint (CCF)
| Attribute | Detail |
|---|---|
| **Type** | Open-source tool and methodology |
| **Organisation** | Thoughtworks (original authors); open-source community |
| **Repository** | github.com/cloud-carbon-footprint/cloud-carbon-footprint |
| **Status** | ✅ Confirmed in app |
| **What it provides** | Cloud infrastructure carbon measurement: converts AWS/GCP/Azure billing data → energy → carbon using location-based grid intensity. Proven pipeline, extensible architecture. |
| **How TRACE uses it** | (1) The cloud carbon formula `usage_kWh × grid_gCO₂e/kWh` mirrors CCF's approach. (2) The cloud usage CSV schema (`date, app, service, region, usage_kwh, cost_usd`) is shaped like a CCF billing export. (3) The CCF output schema is listed in the Standards Alignment table. (4) The TRACE repo is a fork of the CCF codebase. (5) The `carbon_factors.csv` values are labelled "CCF-v2.1 methodology." |
| **Where it appears** | Throughout `app.py`; `docs/research/feasibility-ai-carbon-product.md`; `CLAUDE.md`; `docs/strategy/sustainability-strategy-analysis.md` |
| **Caveats** | The CCF TypeScript codebase is present in the `packages/` folder but is not invoked at runtime by the TRACE MVP Python app. The relationship is methodological and structural, not a live code dependency. |

---

### Langfuse
| Attribute | Detail |
|---|---|
| **Type** | Open-source LLM observability platform |
| **Status** | ✅ Confirmed in app (schema used; API not live) |
| **What it provides** | Trace logging, token usage, cost tracking, eval scores, and prompt/response capture for LLM applications. |
| **How TRACE uses it** | The `llm_usage.csv` data is "Langfuse-shaped" — it follows the field structure of a Langfuse export. The Connect page's Langfuse connector form uses Langfuse's real API credential fields. The `llm_trace_export.json` data is shaped like Langfuse trace exports. |
| **Where it appears** | `docs/sample-data/llm_usage.csv`; `app.py` Connect page Langfuse form; `docs/langfuse/` reference folder |

---

### OpenTelemetry GenAI Semantic Conventions
| Attribute | Detail |
|---|---|
| **Type** | Open standard for observability |
| **Status** | ✅ Confirmed in app |
| **What it provides** | Standardised field names for LLM telemetry: `llm.usage.input_tokens`, `llm.usage.output_tokens`, etc. |
| **How TRACE uses it** | TRACE uses OpenTelemetry GenAI conventions for token field naming in the trace data schema. Listed in the Standards Alignment table. |
| **Where it appears** | `app.py` Prove > Methodology > Standards Alignment table |

---

### Semgrep
| Attribute | Detail |
|---|---|
| **Type** | Open-source static analysis tool |
| **Status** | ✅ Confirmed in app (output format used; tool not run live) |
| **What it provides** | Static code analysis with JSON output format. |
| **How TRACE uses it** | `semgrep_findings.json` follows the Semgrep JSON output format. The Energy Debt tab reads this file to count findings per app. Listed in the Standards Alignment table. |
| **Where it appears** | `docs/sample-data/semgrep_findings.json`; `app.py` Energy Debt calculation; Standards Alignment table |
| **Caveats** | The findings are synthetic. No real Semgrep scan was run. |

---

## Grid and energy intensity data sources

### Electricity Maps
| Attribute | Detail |
|---|---|
| **Type** | Real-time carbon intensity data provider |
| **Status** | ✅ Confirmed in app |
| **What it provides** | Location-based grid carbon intensity in gCO₂e/kWh for regions worldwide, in real time and historically. |
| **How TRACE uses it** | The grid intensity values in `grid_intensity.csv` are sourced from Electricity Maps data (along with EPA eGRID and ENTSO-E for regional cross-reference). |
| **Where it appears** | `docs/sample-data/carbon_factors.csv` (labelled as source); `docs/research/trace-calculation-methodology.md` Section 11 |

---

### EPA eGRID (US Environmental Protection Agency)
| Attribute | Detail |
|---|---|
| **Type** | US government emissions dataset |
| **Status** | ✅ Confirmed in app |
| **What it provides** | US regional electricity grid emissions factors (gCO₂e/kWh) by sub-region. |
| **How TRACE uses it** | US regional grid intensity values (us-east: 380, us-west: 210) are aligned to EPA eGRID data. |
| **Where it appears** | `docs/research/trace-calculation-methodology.md` Section 11; `docs/sample-data/carbon_factors.csv` |

---

### ENTSO-E Transparency Platform
| Attribute | Detail |
|---|---|
| **Type** | European Network of Transmission System Operators data |
| **Status** | ✅ Confirmed in app |
| **What it provides** | European electricity grid emissions factors. |
| **How TRACE uses it** | EU regional grid intensity value (eu-west: 290 gCO₂e/kWh) is aligned to ENTSO-E data. |
| **Where it appears** | `docs/research/trace-calculation-methodology.md` Section 11 |

---

## AI inference energy research

### Luccioni et al. (2023) — "Power Hungry Processing: Watts Driving the Cost of AI Deployment"
| Attribute | Detail |
|---|---|
| **Type** | Peer-reviewed research paper |
| **Authors** | Alexandra Sasha Luccioni, Yacine Jernite, Emma Strubell, Margaret Mitchell, Yoshua Bengio |
| **Status** | ✅ Confirmed in app |
| **What it provides** | Empirical measurements of inference energy for various LLM sizes and tasks. One of the first systematic benchmarks of deployment (not training) energy. |
| **How TRACE uses it** | The kWh/1M token coefficient derivation cites this paper as a primary source for inference energy estimation. |
| **Where it appears** | `docs/research/trace-calculation-methodology.md` Sections 5 and 11 |

---

### Patterson et al. (2022) — "Carbon Emissions and Large Neural Network Training"
| Attribute | Detail |
|---|---|
| **Type** | Research paper (Google) |
| **Status** | 📄 Confirmed in project docs |
| **What it provides** | Analysis of training vs inference carbon for large models. Context for why inference (not training) is the dominant ongoing emission source. |
| **How TRACE uses it** | Provides context for TRACE's focus on inference carbon (run-time) rather than training carbon (build-time). |
| **Where it appears** | `docs/research/trace-calculation-methodology.md` Section 11 |

---

### MLPerf Inference Benchmarks
| Attribute | Detail |
|---|---|
| **Type** | Industry benchmark suite |
| **Organisation** | MLCommons |
| **Status** | ✅ Confirmed in app |
| **What it provides** | Standardised benchmarks for LLM inference performance, including tokens per second under various hardware conditions. |
| **How TRACE uses it** | Token throughput figures (500–1,500 tokens/second for large models on A100) used in the coefficient derivation in `trace-calculation-methodology.md`. |
| **Where it appears** | `docs/research/trace-calculation-methodology.md` Section 5 |

---

### NVIDIA A100/H100 Specification Sheets
| Attribute | Detail |
|---|---|
| **Type** | Hardware manufacturer specifications |
| **Status** | ✅ Confirmed in app |
| **What it provides** | GPU Thermal Design Power (TDP): A100 up to ~400W, H100 up to ~700W. |
| **How TRACE uses it** | Step 1 of the coefficient derivation — GPU power draw is the starting point for the kWh/token calculation. |
| **Where it appears** | `docs/research/trace-calculation-methodology.md` Section 5 |

---

## Water consumption sources

### The Green Grid — Water Usage Effectiveness (WUE) Methodology
| Attribute | Detail |
|---|---|
| **Type** | Industry standard metric |
| **Organisation** | The Green Grid consortium |
| **Status** | ✅ Confirmed in app |
| **What it provides** | The WUE metric definition: litres of water consumed per kWh of IT equipment energy. |
| **How TRACE uses it** | The water formula `energy_kWh × WUE_liters_per_kWh` follows The Green Grid's WUE definition. |
| **Where it appears** | `docs/research/trace-calculation-methodology.md` Sections 8 and 11 |

---

### Li et al. (2023) — "Making AI Less Thirsty: Uncovering and Addressing the Secret Water Footprint of AI Models"
| Attribute | Detail |
|---|---|
| **Type** | Research paper |
| **Status** | ✅ Confirmed in app |
| **What it provides** | Analysis of AI model water consumption, including training and inference. Estimates that training GPT-3 consumed ~700,000 litres of water. Establishes the connection between AI inference energy and data centre cooling water. |
| **How TRACE uses it** | Provides the research basis for including water as a TRACE metric. Informs the regional WUE estimates. |
| **Where it appears** | `docs/research/trace-calculation-methodology.md` Sections 8 and 11 |

---

### Google Environmental Report 2023
| Attribute | Detail |
|---|---|
| **Type** | Corporate sustainability report |
| **Status** | ✅ Confirmed in app |
| **What it provides** | Google's published WUE figures for its facilities, including European data centres. Useful for calibrating the eu-west (Ireland) WUE estimate of 0.5 L/kWh. |
| **How TRACE uses it** | The eu-west WUE value (0.5) is described as "consistent with Google's reported EU West figures." |
| **Where it appears** | `docs/research/trace-calculation-methodology.md` Section 2 |

---

### Uptime Institute Annual Global Data Center Survey
| Attribute | Detail |
|---|---|
| **Type** | Industry survey |
| **Status** | 📄 Confirmed in project docs |
| **What it provides** | Industry-average PUE (Power Usage Effectiveness) values and data centre efficiency benchmarks, including WUE data. |
| **How TRACE uses it** | Informs the PUE assumption (≈1.2) used in the coefficient derivation, and provides context for WUE regional estimates. |
| **Where it appears** | `docs/research/trace-calculation-methodology.md` Sections 5 and 11 |

---

## Future / planned sources

### Boavizta
| Attribute | Detail |
|---|---|
| **Type** | Open-source hardware embodied emissions API |
| **Status** | 🗺️ Referenced as future integration |
| **What it provides** | GPU-SKU-level embodied emissions data (carbon cost of manufacturing hardware). Enables Scope 3 hardware emissions measurement. |
| **How TRACE plans to use it** | Future integration to add the embodied carbon (M) dimension to the SCI score, upgrading from Scope 2 operational only. |
| **Where it appears** | `docs/research/feasibility-ai-carbon-product.md`; `docs/strategy/sustainability-strategy-analysis.md` |

---

### ML.Energy Leaderboard
| Attribute | Detail |
|---|---|
| **Type** | Research initiative and dataset |
| **Status** | ⚠️ Recommended addition |
| **What it provides** | Energy benchmarks for LLM inference across a wide range of models, serving frameworks, and hardware. More up-to-date than Luccioni et al. for newer models. |
| **How it would improve TRACE** | Would allow TRACE to expand from three model classes to named model coefficients with benchmark-backed values. |
| **Note** | Referenced in `docs/research/feasibility-ai-carbon-product.md` but not formally cited in `trace-calculation-methodology.md`. |

---

## Internal project documents

### TRACE Project Strategy Analysis
| Attribute | Detail |
|---|---|
| **Type** | Internal strategy document |
| **File** | `docs/strategy/sustainability-strategy-analysis.md` |
| **Status** | 📄 Confirmed in project docs |
| **What it covers** | Market analysis, Thoughtworks competitive positioning, CCF revival context, AI:works relationship, hackathon MVP recommendation, commercial model options. |
| **How it shaped TRACE** | The pivot from an AI:works-embedded tool to an independent, sellable product is documented here. The "build green + prove it" two-layer product vision originated in this document. |

---

### TRACE Feasibility Analysis
| Attribute | Detail |
|---|---|
| **Type** | Internal technical feasibility document |
| **File** | `docs/research/feasibility-ai-carbon-product.md` |
| **Status** | ✅ Confirmed in app |
| **What it covers** | Data tier requirements, coefficient sources, confidence levels, reference architecture, seven open technical questions. |
| **How it shaped TRACE** | Defined the three data tiers (cloud billing, gateway logs, GPU telemetry), the confidence level framework (High/Medium/Low), and the reference architecture used in the MVP. |

---

### TRACE Calculation Methodology
| Attribute | Detail |
|---|---|
| **Type** | Internal technical reference |
| **File** | `docs/research/trace-calculation-methodology.md` |
| **Status** | ✅ Confirmed in app |
| **What it covers** | All formulas, coefficient derivation, worked examples, WUE values, water calculation, Greenpixie comparison, PUE handling, full sources list. |
| **How it shaped TRACE** | This is the single authoritative reference for all calculations in `app.py`. The code implements exactly what this document specifies. |

---

## Key takeaways

- The core TRACE methodology rests on well-established published sources: SCI-for-AI (ISO 21031), Electricity Maps/EPA eGRID grid intensity, and Luccioni et al. for inference energy
- The energy-per-token coefficients are estimated, not measured — this is the primary uncertainty, and it is disclosed
- Water consumption is a newer addition with Medium confidence; the sources (The Green Grid, Li et al., Google) are credible but the regional WUE values are estimates
- The CCF codebase and methodology are the structural and intellectual ancestors of TRACE's cloud carbon layer
- Boavizta (embodied emissions) and ML.Energy (per-model coefficients) would strengthen the methodology if added
