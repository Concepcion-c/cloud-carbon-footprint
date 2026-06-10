# 11 — Glossary

> **Summary:** Plain-English definitions for every technical term used in TRACE. Organised alphabetically. Covers AI, carbon, cloud, and TRACE-specific terminology.

---

## A

**Agent** — An AI program that takes a sequence of steps to complete a task, often calling tools, retrieving information, or making decisions along the way. In TRACE, each step in an agent workflow is called a "span."

**Agent Graph** — The visualisation in TRACE's Observe > Agent Traces tab that shows an AI workflow as a flow diagram. Each node (box) is one agent step; arrows connect steps in sequence. Colour-coded by retry count: green (clean), amber (1–2 retries), red (3+ retries).

**ap-south** — The short name in TRACE's data for the Asia Pacific South region — specifically Mumbai, India. It has the highest grid carbon intensity (630 gCO₂e/kWh) and highest water stress (WUE 1.8 L/kWh) of any region in the demo data.

**Apply (button)** — The button on the Optimize page that triggers a live recalculation of the AI footprint with a recommendation's changes applied. Clicking it shows how much carbon and cost would drop if the recommended changes were made.

---

## B

**Baseline** — The starting state of the data before any recommendations are applied. All KPI cards and charts show baseline figures until a recommendation is applied.

**Batch shift** — A type of carbon optimisation where non-time-sensitive AI workloads are scheduled to run during times when the electricity grid is cleaner (e.g., at night or on weekends). Not yet implemented in the TRACE MVP.

**Blended estimate** — A number derived by combining data from multiple sources (hardware specs, benchmarks, industry averages) rather than from a direct measurement. TRACE's kWh/1M token coefficients are blended estimates. This is a Medium confidence data point.

**Boavizta** — An open-source project that provides a database of the carbon cost of manufacturing (embodied carbon) for server hardware, including GPUs. Referenced in TRACE's roadmap as a future integration for Scope 3 emissions.

---

## C

**Carbon-aware** — Making decisions (about which model to use, which region to run in, when to schedule a job) based on carbon impact, not just cost. TRACE's second recommendation (Analytics-Agent region shift) is a pure carbon-aware decision — it saves carbon with no cost change.

**Carbon intensity** — How much CO₂e is produced per unit of electricity in a given region. Measured in grams of CO₂e per kilowatt-hour (gCO₂e/kWh). A clean grid (e.g., Oregon, heavily hydro-powered) might be 210 gCO₂e/kWh. A coal-heavy grid might be 630 gCO₂e/kWh.

**CCF** — Short for Cloud Carbon Footprint. See full entry below.

**Cloud Carbon Footprint (CCF)** — An open-source tool created by Thoughtworks (and others) that measures the carbon emissions of cloud infrastructure (servers, storage, networking) across AWS, Google Cloud, and Azure. TRACE is built on a fork of CCF and extends it to cover AI inference. CCF is present in the TRACE repository but is not running in the TRACE MVP.

**CO₂e** — Carbon dioxide equivalent. A standard unit for expressing greenhouse gas emissions in terms of the equivalent amount of CO₂ that would have the same global warming effect. TRACE reports all carbon figures in kg CO₂e.

**Coefficient** — In TRACE, a number that converts one quantity into another. The model energy coefficient converts tokens into kWh. The grid intensity coefficient converts kWh into kg CO₂e.

**Confidence level** — TRACE labels data quality as High (measured or directly sourced), Medium (estimated from benchmarks), or Low (missing data, fallback used). Most AI carbon figures are Medium confidence.

**Connect (page)** — The first page in the TRACE app. Shows all connected data sources and allows new ones to be added.

---

## D

**Data normalisation** — The process of transforming data from different systems (with different field names and formats) into a single consistent schema that TRACE can process. In the demo, this is shown in the Connect drawer after a file upload.

**Demo persona** — The fictional client scenario used to make the demo concrete. TRACE uses "Northstar Bank — Digital Banking Modernisation" as its demo persona.

**Doc-Summarizer** — One of the five synthetic AI applications in the TRACE demo data. Runs a mid-tier model in eu-west (Ireland).

---

## E

**Embodied carbon** — The carbon emitted during the manufacture of hardware (servers, GPUs, chips). This is distinct from operational carbon (the energy used while running). TRACE currently measures operational carbon only. Embodied carbon would be added via Boavizta in a future version.

**Energy Debt** — TRACE's term for the accumulated inefficiency in an application — the combination of high runtime carbon (from using expensive models in dirty regions) and code-level inefficiency (from energy-debt findings in the code scan). Quantified as the Energy Debt Score.

**Energy Debt Score** — A 0–1.00 number that ranks apps by combined inefficiency: 60% from runtime AI carbon rank + 40% from code-risk findings rank. A score of 1.00 is the worst possible. Used on the Observe > Energy Debt tab and Optimize > SDLC Energy Debt Fixes section.

**eu-west** — The short name for the Europe West region in TRACE's data — specifically Ireland. It has the lowest WUE (0.5 L/kWh) of any region in the demo because Ireland's cool, damp climate minimises cooling water needs.

**Eval score** — A quality score (0–1) assigned to an AI agent's output. Used in the Agent Traces tab to show whether each step produced a high-quality result. An output may be rejected (not used) even if it was generated.

---

## F

**FinOps** — Financial Operations — the practice of managing and optimising cloud costs. Cloudability is a FinOps tool. TRACE extends FinOps thinking by adding carbon alongside cost.

**Fork** — In software, a copy of an open-source project that someone creates to develop independently. The TRACE repository is a fork of Cloud Carbon Footprint — it started as a copy of CCF with the intent to build on top of it.

**Fraction** — In a TRACE recommendation, the proportion of an application's traffic that the recommendation applies to. A fraction of 0.7 means 70% of traffic shifts to the new model or region; 30% stays on the original.

---

## G

**gCO₂e/kWh** — Grams of CO₂e per kilowatt-hour. The unit used to express grid carbon intensity. To convert to kg CO₂e, divide by 1,000.

**Green Software Foundation (GSF)** — A non-profit organisation, co-founded by Thoughtworks, that develops standards and tools for reducing the carbon impact of software. Authored the SCI-for-AI standard that TRACE is built on.

**Grid intensity** — See carbon intensity.

**GreenOps** — The practice of applying operational efficiency principles specifically to reducing the environmental impact of technology systems. TRACE's tagline is "AI GreenOps Dashboard."

---

## H

**High confidence** — In TRACE's confidence labelling system, a figure where all inputs are measured or directly sourced from provider data. Cloud kWh from billing data combined with a regional grid factor is High confidence.

---

## I

**Inference** — Running an already-trained AI model to produce an output (an answer, a summary, a code suggestion). This is distinct from training a model. TRACE measures inference carbon — the energy used every time an AI tool generates a response.

**Input tokens** — The words and symbols sent to an AI model as part of a request. Together with output tokens, they determine how much energy and cost an AI call consumes.

**ISO/IEC 21031:2024** — The international standard that defines Software Carbon Intensity (SCI). Specifies location-based accounting, operational boundary, and no offsets. TRACE's methodology is described as "ISO 21031 conformant."

---

## K

**kWh** — Kilowatt-hour. The unit of electricity consumption. One kWh is the energy consumed by a 1,000-watt appliance running for one hour. TRACE uses kWh as the intermediate unit in all carbon calculations.

**kWh/1M tokens** — Kilowatt-hours per million tokens. The energy coefficient for a model class. Small model: 0.3. Mid model: 0.6. Large model: 1.2. These are blended estimates from hardware benchmarks.

---

## L

**Langfuse** — An open-source LLM observability platform that tracks token usage, cost, latency, eval scores, and agent traces. TRACE's `llm_usage.csv` data is "Langfuse-shaped" — it follows the format of a Langfuse export.

**Large language model (LLM)** — An AI model trained on large amounts of text, capable of generating, summarising, translating, and answering questions in natural language. Claude, GPT-4, and similar models are LLMs.

**Latency** — How long an AI call takes from request to response, measured in milliseconds. Shown per agent step in the Agent Traces tab.

**LiteLLM** — An open-source AI gateway (proxy) that sits in front of multiple AI providers and standardises token usage, cost, and routing. Listed as a planned future connector in TRACE.

**Location-based accounting** — The approach of using the actual carbon content of the electricity grid where computation runs, rather than adjusting for renewable energy certificates. TRACE uses location-based accounting, aligned to ISO 21031. This produces the honest physical carbon figure.

---

## M

**Market-based accounting** — An alternative to location-based accounting where organisations can claim lower carbon figures by purchasing renewable energy certificates (RECs). TRACE intentionally does not use market-based accounting.

**Medium confidence** — In TRACE's confidence labelling system, a figure where one or more inputs are estimated from benchmarks or averages. Most AI carbon figures in TRACE are Medium confidence because the kWh/1M token coefficients are blended estimates.

**Model class** — TRACE groups AI models into three classes based on their capability and energy use: `large` (1.2 kWh/1M tokens), `mid` (0.6 kWh/1M), and `small` (0.3 kWh/1M). These map to real models: large ≈ Claude Opus, mid ≈ Claude Sonnet, small ≈ Claude Haiku.

**Model swap** — A type of recommendation in TRACE that routes some or all of an application's AI traffic from a more expensive/energy-intensive model to a more efficient one. The Support-Bot recommendation includes a large → small model swap for 70% of traffic.

---

## N

**Northstar Bank** — The fictional client in the TRACE demo. Represents a financial services organisation running a Digital Banking Modernisation project with five AI applications.

---

## O

**Observe (page)** — The second page in the TRACE app. The main analytics dashboard with four tabs: Dashboard, AI Detail, Agent Traces, and Energy Debt.

**Offset** — A carbon credit that represents a reduction in emissions elsewhere, used to compensate for emissions produced by a company. TRACE does not use offsets — it reports the actual physical carbon of AI workloads.

**OpenTelemetry GenAI** — A set of standard field names for capturing LLM telemetry (token counts, model name, region, latency). TRACE's trace data follows these conventions.

**Operational carbon** — The carbon produced by running software (during inference, while servers are running). Distinct from embodied carbon (manufacturing). TRACE measures operational carbon only.

**Optimize (page)** — The third page in the TRACE app. Shows recommendations and lets you apply them to see the impact on cost and carbon.

**Output tokens** — The words and symbols an AI model generates in response to a request. Together with input tokens, they determine energy and cost.

---

## P

**PUE (Power Usage Effectiveness)** — A measure of data centre energy efficiency. PUE = total facility energy / IT equipment energy. A PUE of 1.2 means that for every 1 kWh used by servers, 1.2 kWh is consumed in total (the extra 0.2 kWh goes to cooling, lighting, etc.). Hyperscalers typically achieve PUE of 1.1–1.2. In TRACE, PUE is folded into the kWh/1M token coefficient rather than applied separately.

**Prove (page)** — The fourth page in the TRACE app. Shows the evidence pack (before/after comparison, data sources, formulas) and the methodology tab.

---

## R

**REC (Renewable Energy Certificate)** — A certificate proving that a unit of energy was produced from a renewable source. Companies buy RECs to claim renewable energy use. TRACE does not adjust for RECs — it uses location-based accounting.

**Recommendation** — In TRACE, a specific, quantified suggestion for reducing AI cost and carbon. Each recommendation has: a rationale, specific actions (model swap, region shift), projected impact percentages, and an explicit quality trade-off statement.

**Region shift** — A type of recommendation in TRACE that moves AI workloads from a high-carbon-intensity region (e.g., Mumbai at 630 gCO₂e/kWh) to a lower-carbon-intensity region (e.g., Oregon at 210 gCO₂e/kWh). The same model running the same workload produces less carbon in a cleaner grid region.

**Retry count** — The number of times an AI agent step was re-executed before producing an acceptable output. Retries increase cost, energy, and carbon. Highlighted in TRACE's Agent Traces tab.

---

## S

**SCI** — Software Carbon Intensity. The metric defined by ISO/IEC 21031:2024. A rate expressed per functional unit (e.g., per million tokens, per API call). See SCI-for-AI.

**SCI-for-AI** — An extension of SCI that applies to AI workloads including training, fine-tuning, and inference. Ratified by the Green Software Foundation in Q4 2024. TRACE's AI inference carbon formula is SCI-for-AI conformant.

**Scope 2 emissions** — In the GHG Protocol, Scope 2 covers indirect emissions from purchased electricity. TRACE measures Scope 2 operational emissions for AI inference and cloud infrastructure.

**Scope 3 emissions** — Indirect emissions in a company's value chain — including the carbon cost of manufacturing the hardware used (embodied carbon). TRACE does not currently measure Scope 3.

**Semgrep** — A static code analysis tool. TRACE's Energy Debt tab reads Semgrep-formatted findings to count code-level inefficiency issues per application.

**Span** — One step in an AI agent workflow trace. Each span represents one model call with its own token counts, latency, cost, carbon, and quality score.

**Streamlit** — The Python web framework used to build the TRACE dashboard. It handles all the web UI complexity — layouts, charts, interactive widgets, routing — without requiring a separate frontend codebase.

**Support-Bot** — The synthetic AI application in the TRACE demo that dominates the carbon and cost figures. It runs a large model in ap-south (Mumbai), making it the top target for optimisation.

**Synthetic data** — Data generated artificially for testing or demonstration purposes, not sourced from real systems. All data in the TRACE demo is synthetic, generated by `docs/sample-data/generate.py`.

---

## T

**Token** — The basic unit of text that AI models process. A token is roughly 3–4 characters or about ¾ of a word in English. AI providers charge by the number of input and output tokens. TRACE uses token counts as the starting point for all AI inference calculations.

**TRACE** — Token-level Realtime AI Carbon Estimation. The name of the Thoughtworks hackathon project that extends Cloud Carbon Footprint to cover AI inference carbon, cost, energy, and water.

**TDP (Thermal Design Power)** — The maximum heat a CPU or GPU can produce under sustained load, effectively indicating maximum power draw. An NVIDIA A100's TDP is ~400W; an H100's TDP is ~700W. Used in TRACE's coefficient derivation.

---

## U

**USD/1M tokens** — US dollars per million tokens. The cost coefficient for a model class. Small model: $1.00. Mid model: $6.00. Large model: $30.00. Based on published provider pricing as of mid-2025.

**us-east** — The short name for the US East region in TRACE's data — specifically Virginia. Grid intensity: 380 gCO₂e/kWh. WUE: 1.2 L/kWh.

**us-west** — The short name for the US West region in TRACE's data — specifically Oregon/Pacific Northwest. The cleanest and most water-efficient region in the demo: 210 gCO₂e/kWh, WUE 0.8 L/kWh.

---

## W

**What-If Scenario Planner** — A table on the Optimize page comparing three scenarios (Current State, Balanced Optimisation, Aggressive Carbon Mode) with projected cost, carbon, water, latency, and quality risk.

**WUE (Water Usage Effectiveness)** — A data centre efficiency metric. WUE = total facility water used / IT equipment energy consumed. Measured in litres per kWh. A lower WUE means less water per unit of compute. TRACE uses region-specific WUE values to calculate water consumption. Ireland (eu-west): 0.5 L/kWh. Oregon (us-west): 0.8. Virginia (us-east): 1.2. Mumbai (ap-south): 1.8.

---

## Key takeaways

- The most important terms for the demo are: token, carbon intensity (gCO₂e/kWh), WUE, model class (large/mid/small), Energy Debt Score, and SCI-for-AI
- "Location-based" and "no offsets" are key differentiators — they make TRACE's numbers honest and auditable
- "Medium confidence" is not a weakness — it is the honest label for estimates derived from benchmarks, and TRACE says so openly
- All carbon in TRACE is CO₂e (CO₂ equivalent), covering all greenhouse gases, not just carbon dioxide
