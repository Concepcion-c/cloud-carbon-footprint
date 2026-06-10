# PRD: TRACE — Hackathon MVP v3

> **Status:** Draft v3 · **Owner:** Concepcion-c · **Last updated:** 2026-06-10  
> Supersedes `hackathon-mvp-prd-v2(2).md`.  
> Same goal: a ≤5-minute demoable MVP that can be built quickly, uses synthetic/tool-shaped data, and proves the Phase 1–3 TRACE product story: **Connect → Observe → Optimize**.  
> Full product direction: TRACE becomes the cross-cloud, cross-model, client-facing control layer for AI workload observability, AI FinOps, GreenOps, carbon accounting, evidence lineage, and SDLC sustainability KPIs.

---

## 1. Product thesis

**TRACE is the AI Cost, Carbon, and Control Plane for software delivery.**

TRACE starts by connecting to the fragmented tools clients already have — LLM observability, cloud monitoring, FinOps/cloud cost, CCF, and AI/Works — then normalizes that telemetry into one shared cost + carbon + governance model.

Over time, TRACE becomes the system of record and system of action for AI workload management:

- Native LLM observability
- Token, cost, carbon, and quality per trace
- AI/Works / SDLC workflow attribution
- GreenOps and FinOps decisioning
- CCF-based carbon calculation extension
- Optimization recommendations
- Evidence packs for governance and reporting

### One-sentence MVP

A **Streamlit** dashboard that simulates enterprise onboarding, shows connected systems, ingests synthetic client exports shaped like real tools, normalizes them into a TRACE schema, observes AI workload cost/carbon by workflow and agent trace, recommends optimizations, and shows cost + CO₂e reductions with transparent evidence.

---

## 2. MVP positioning

### What this MVP proves

1. **TRACE Connect:** TRACE can ingest from fragmented enterprise tools and normalize their data into one schema.
2. **TRACE Observe:** TRACE can replace basic LLM observability for AI workloads by showing traces, agents, tokens, cost, carbon, latency, and quality signals.
3. **TRACE Optimize:** TRACE can recommend lower-cost/lower-carbon actions and show before/after impact.

### What this MVP does not claim

This MVP does **not** build full live integrations with every competitor tool. It shows:

- Functional ingestion from static JSON/CSV files shaped like real tool outputs
- Mocked API connectors to demonstrate the production integration path
- A credible connector adapter interface that supports live APIs, file uploads, OpenTelemetry, webhooks, and reference datasets

### Strategic wedge

TRACE should be described as:

> **The GreenOps intelligence layer and AI workload control plane for enterprise software delivery — connecting LLM observability, FinOps, cloud monitoring, AI/Works, and CCF-based carbon accounting into measurable optimization and governance outcomes.**

---

## 3. Product phases represented in the MVP

| Phase | Product goal | MVP proof |
|---|---|---|
| **Phase 1: TRACE Connect** | Ingest and normalize telemetry | Connector hub, file upload/API mock, validation, mapping, normalized schema |
| **Phase 2: TRACE Observe** | Replace LLM observability for AI workloads | AI workload dashboard, agent graph, trace details, cost/carbon per trace |
| **Phase 3: TRACE Optimize** | Become a system of action | Recommendations, what-if scenarios, before/after savings |

---

## 4. Core principle — reuse, do not rebuild

**We do not host or integrate these tools during the hackathon. We adopt their data shapes and show the integration path.** Only the unique TRACE logic is custom code.

| Layer | We BUILD | We ADOPT / SIMULATE | We ROADMAP |
|---|---|---|---|
| Connector hub | TRACE Connect UI + connector state model | Tool-shaped exports from AI/Works, Langfuse/LangSmith, FinOps, CCF | Live APIs, OTel collector, webhooks |
| Cloud carbon | TRACE calculation from CCF-shaped exports | CCF methodology/output shape | Full CCF ingestion from cloud billing |
| AI usage ledger | TRACE calculator | Langfuse/LangSmith/OpenTelemetry GenAI-shaped traces | Live LLM gateway / provider APIs |
| LLM observability | Basic trace + agent graph + trace metrics | Synthetic trace spans | Full native tracing SDK |
| FinOps | Cost allocation from static exports | Cloudability/Finout-style cost fields | Budgeting, showback/chargeback, anomaly detection |
| Optimization | Rule-based recommendations | Model substitution, prompt compression, caching, region shift | AI-assisted recommendation engine |
| Energy debt | Static code-scan findings | Semgrep-shaped JSON | Custom SDLC energy rules and CI gates |
| UI/storage | Streamlit + pandas | Local bundled CSV/JSON | Production UI and database |

**Decided build stack:** Streamlit + pandas + custom TRACE calculator + bundled synthetic CSV/JSON files.

---

# 5. MVP user and scenario

## Primary demo persona

**CIO / CTO / Head of Engineering at a financial services client**

They are using AI to accelerate modernization but need to answer:

- What is AI-enabled delivery costing us?
- What carbon impact is this creating?
- Which models, agents, workflows, regions, or code paths are driving waste?
- What should we optimize first?
- Can we produce transparent evidence behind the numbers?

## Demo scenario

A fictional financial services company, **Northstar Bank**, is modernizing a legacy digital banking platform with AI/Works-style workflows.

TRACE is onboarded to monitor:

- AI/Works usage
- LLM traces
- FinOps/cloud cost exports
- CCF carbon factors
- SDLC energy debt findings

---

# 6. MVP screens

## Screen 1: TRACE Connect — Data Sources

### Purpose

Show every connected system, whether it is a live API connection or a static file upload, the connection status, freshness, record counts, and normalization health.

### Top summary

```text
TRACE Connect

Connected systems: 7
Live API connections: 3
Static file uploads: 4
Healthy: 5
Warnings: 2
Failed: 0
Last normalization run: 12 minutes ago

[+ Connect New System] [Run Sync] [Upload File] [View Normalization Log]
```

### Connected systems table

| System | Category | Connection Type | Status | Last Sync | Records | Normalization | Owner | Actions |
|---|---|---|---|---|---:|---|---|---|
| AI/Works Control Plane | AI delivery | API / Mock API | Connected | 12 min ago | 1,248 | 98% mapped | Platform Team | View / Sync |
| Langfuse | LLM observability | Static JSON | Uploaded | 18 min ago | 842 | 94% mapped | AI Engineering | View / Replace |
| LangSmith | LLM observability | Static JSON | Available | — | — | — | AI Engineering | Connect |
| Datadog | LLM observability | API / Mock API | Warning | 1 hr ago | 493 | 81% mapped | SRE | Fix Mapping |
| New Relic | LLM observability | API / Mock API | Coming Soon | — | — | — | SRE | View Setup |
| Google Cloud Monitoring | Cloud monitoring | API / Mock API | Connected | 20 min ago | 1,876 | 92% mapped | Cloud Team | View / Sync |
| Cloudability Export | FinOps | Static CSV | Uploaded | Jun 10 | 2,104 | 89% mapped | FinOps | Replace File |
| CloudHealth | FinOps / GreenOps | API / Mock API | Coming Soon | — | — | — | FinOps | View Setup |
| Flexera | FinOps / ITAM | API / Mock API | Coming Soon | — | — | — | FinOps | View Setup |
| Vantage | Cloud cost | API / Mock API | Coming Soon | — | — | — | FinOps | View Setup |
| Finout | Unit economics | API / Mock API | Coming Soon | — | — | — | FinOps | View Setup |
| CCF Factors | Carbon methodology | Static CSV | Active | Jun 10 | 64 | 100% mapped | Sustainability | View |
| Code Scan Findings | SDLC sustainability | Static JSON | Warning | Jun 10 | 36 | 76% mapped | Engineering | Fix Mapping |

### Connector status types

| Status | Meaning |
|---|---|
| **Connected** | API connection is healthy and syncing |
| **Uploaded** | Static file was uploaded successfully |
| **Active** | Reference dataset is active, such as carbon factors |
| **Needs Mapping** | TRACE received data but fields need manual mapping |
| **Warning** | Data ingested, but incomplete, stale, or partially mapped |
| **Failed** | Connection or ingestion failed |
| **Paused** | Connector is configured but not syncing |
| **Available** | Connector can be configured in the MVP UI |
| **Coming Soon** | Connector tile exists but is not enabled |

### Connection type labels

| Type | Meaning |
|---|---|
| **API** | Live connection that syncs automatically |
| **Mock API** | Demo-only simulated API connector |
| **Static CSV** | One-time or periodic file upload |
| **Static JSON** | One-time or periodic trace/config upload |
| **Manual Upload** | User-provided file without active sync |
| **Reference Dataset** | Carbon factors, model factors, methodology file |
| **OpenTelemetry** | Streaming traces/events from apps or agents |
| **Webhook** | Event-based push from source system |

---

## Screen 1A: Connect New System drawer

### Purpose

Demonstrate that TRACE can connect to mature clients with live tooling and less mature clients with static exports.

```text
Connect New System

Choose source type:
[ AI/Works ] [ LLM Observability ] [ Cloud Monitoring ]
[ FinOps / Cloud Cost ] [ Carbon Factors ] [ Code / CI ]
[ Custom Source ]

Connection method:
( ) API connection
( ) File upload
( ) OpenTelemetry collector
( ) Webhook
```

### Example API connection flow

```text
System: Langfuse
Connection method: API

Required:
- Host URL
- Public key
- Secret key
- Project ID

Sync frequency:
[ Every 15 minutes v ]

Data to ingest:
[x] Traces
[x] Token usage
[x] Cost
[x] Latency
[x] Eval scores
[ ] Prompt / response content

Prompt content storage:
( ) Store full prompt/response
(x) Store metadata only
( ) Store redacted prompt/response
```

### Example static file upload flow

```text
System: Cloudability Export
Connection method: Static CSV

Upload file:
[ cloudability_export.csv ]

Expected fields:
- account
- service
- region
- cost_usd
- usage_type
- timestamp
- tags_project
- tags_workspace

Refresh cadence:
( ) One-time upload
(x) Monthly upload
( ) Weekly upload
```

Validation response:

```text
File validated.
2,104 records found.
184 records missing region.
91 records missing workspace tag.
Proceed to field mapping?
```

---

## Screen 1B: Field mapping

### Purpose

Show TRACE can handle messy enterprise data.

```text
Map source fields to TRACE schema
```

| Source field | TRACE field | Status |
|---|---|---|
| `model_name` | `model` | Mapped |
| `provider_name` | `provider` | Mapped |
| `workspace_name` | `workspace` | Mapped |
| `agent_id` | `agent` | Mapped |
| `input_tokens` | `input_tokens` | Mapped |
| `output_tokens` | `output_tokens` | Mapped |
| `total_cost_usd` | `cost_usd` | Mapped |
| `cloud_region` | `region` | Needs review |
| `run_id` | `trace_id` | Suggested |

Buttons:

```text
[Save Mapping] [Run Normalization]
```

---

## Screen 1C: Connector detail page

### Example: AI/Works Control Plane

```text
AI/Works Control Plane

Connection type: API / Mock API
Status: Connected
Last sync: 12 minutes ago
Sync frequency: Every 15 minutes
Records ingested: 1,248
Normalization success: 98%
Carbon calculation coverage: 91%
Data owner: Platform Team
```

Tabs:

1. Overview
2. Schema Mapping
3. Sync History
4. Data Quality
5. Normalized Records
6. Settings

### Data quality panel

```text
Data Quality

Token data completeness: 97%
Cost data completeness: 95%
Region completeness: 82%
Workflow attribution: 91%
Agent attribution: 88%
Carbon confidence: Medium
```

Warnings:

```text
50 records missing region.
23 records missing model name.
14 records missing workflow attribution.
```

---

## Screen 2: Normalize — TRACE shared schema

### Purpose

Show that TRACE turns fragmented telemetry into a common cost/carbon/governance model.

### Shared schema fields

```text
source_system
source_record_id
trace_id
span_id
parent_span_id
provider
model
region
workspace
workflow
agent
input_tokens
output_tokens
total_tokens
latency_ms
cost_usd
estimated_kwh
estimated_co2e_kg
eval_score
accepted_output
quality_risk
confidence_level
methodology_version
timestamp
business_unit
client_project
environment
sensitivity_flag
```

### Normalized table example

| source | provider | model | region | workspace | workflow | agent | input tokens | output tokens | latency | cost | kWh | CO₂e | confidence |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| AI/Works | Anthropic | Claude Sonnet | us-east | Digital Banking | Code generation | BuildAgent | 42,000 | 9,100 | 18s | $4.82 | 0.38 | 0.15kg | Medium |
| Langfuse | OpenAI | GPT-4.1 | us-central | Digital Banking | Test generation | TestAgent | 18,000 | 7,300 | 11s | $2.10 | 0.19 | 0.07kg | Medium |
| Cloudability | AWS | Bedrock | us-east-1 | Digital Banking | Batch summarization | SummaryAgent | 91,000 | 21,000 | 45s | $8.70 | 0.74 | 0.29kg | Low |

### Telemetry completeness score

```text
Token data: 94%
Cost data: 91%
Region data: 82%
Carbon confidence: Medium
Missing workflow attribution: 6 records
```

---

## Screen 3: Observe — AI workload dashboard

### Purpose

Show TRACE can replace basic LLM observability for AI workloads while adding carbon and governance context.

### Hero KPIs

- Total AI cost
- Total cloud cost
- Total estimated CO₂e
- Total tokens
- Average latency
- Average eval score
- Cost per accepted output
- CO₂e per accepted output

### Breakdown views

- Cost by model
- Carbon by model
- Cost + carbon by app
- Cost + carbon by region
- Top agents by token usage
- Top workflows by cost
- Top workflows by CO₂e
- Retry count by agent
- Eval score by workflow

### Trace detail / agent graph

Demo trace:

```text
SpecAgent → BuildAgent → TestAgent → ReviewAgent → FixAgent
```

Each node shows:

- model
- prompt/input tokens
- output tokens
- latency
- cost
- estimated CO₂e
- eval score
- retry count
- accepted output flag

Key demo message:

> TRACE does not only show that a workflow cost $18.42. It shows which agent step created the most cost and carbon, and whether that cost produced accepted output.

---

## Screen 4: Optimize — recommendations and what-if scenarios

### Purpose

Show TRACE can move from observability to action.

### Recommendation rules

| Recommendation | Trigger | Example |
|---|---|---|
| **Model substitution** | Low-risk workflow uses premium model | Move summarization from large model to small model |
| **Prompt compression** | Input tokens above threshold or repeated context | Compress architecture context |
| **Caching** | Same retrieval/policy context repeated across traces | Cache policy retrieval |
| **Region/time shifting** | High-carbon region for flexible workload | Move batch job to lower-carbon region/time |
| **Batch processing** | Many small calls for similar task | Batch summarization or test generation |
| **Agent loop pruning** | Retry count above threshold | Cap FixAgent retries at 2 |
| **Energy debt fix** | Static code-scan finding severity high | Fix repeated full-table scan |

### Recommendation card format

Each card must show:

- Action
- Why it was triggered
- Estimated cost saved
- Estimated CO₂e reduced
- Latency impact
- Quality risk
- Implementation effort
- Confidence level
- Apply button

Example:

```text
Recommendation: Prompt compression

BuildAgent is sending the same architecture context on every retry.
Estimated impact:
- 22,000 tokens saved per run
- $1,240/month saved
- 14.2kg CO₂e avoided/month
- Quality risk: Low
- Confidence: Medium

[Apply Recommendation]
```

---

## Screen 4A: What-if scenario planner

### Purpose

Show business tradeoffs.

| Scenario | Monthly AI cost | Estimated CO₂e | Avg latency | Quality risk |
|---|---:|---:|---:|---|
| Current | $12,400 | 410kg CO₂e | 12.8s | Low |
| Balanced optimization | $9,850 | 344kg CO₂e | 11.9s | Low-medium |
| Aggressive carbon mode | $8,900 | 301kg CO₂e | 14.2s | Medium |

Recommended scenario:

```text
Balanced optimization
20.5% cost reduction
16.1% CO₂e reduction
No major quality degradation
```

---

## Screen 5: Prove — evidence pack

### Purpose

Show transparent methodology and proof behind outcomes.

Evidence pack fields:

- Source telemetry
- Source system
- Trace IDs
- Token counts
- Model
- Provider
- Region
- Cost formula
- Energy formula
- Emissions factor
- Methodology version
- Assumptions
- Confidence level
- Before/after comparison
- Cost saved
- CO₂e reduced
- Quality/performance tradeoff
- Recommended next actions

MVP evidence pack should be a page/modal with export buttons:

```text
[Download CSV] [Download JSON] [Export Evidence Pack PDF - roadmap]
```

---

# 7. Functional connector scope

## Functional in hackathon MVP

These need to actually work using static uploads or bundled files.

| Connector | Type | MVP behavior |
|---|---|---|
| **AI/Works Control Plane** | Static JSON or mock API | Upload/read JSON and normalize workspace/workflow/agent/model/token/cost data |
| **Langfuse / LangSmith trace export** | Static JSON | Upload/read trace export and render agent graph |
| **Cloudability / FinOps export** | Static CSV | Upload/read cost data and join by workspace/project/region |
| **CCF Carbon Factors** | Static CSV | Upload/read carbon factors and calculate CO₂e |
| **Code Scan Findings** | Static JSON | Upload/read energy debt findings and surface recommendations |

## Visible but not functional in MVP

These appear in the connector hub to show product ambition.

- Datadog
- New Relic
- Google Cloud Monitoring
- CloudHealth
- Flexera
- Vantage
- Finout
- OpenTelemetry Collector
- Webhooks
- LiteLLM Gateway

---

# 8. Sample data spec

Place files in `../sample-data/`. Label clearly as synthetic.

## `aiworks_usage_export.json`

Purpose: proves AI/Works control plane ingestion.

Fields:

```text
workspace_id
workspace_name
project_name
workflow_id
workflow_name
agent_name
model_provider
model_name
region
input_tokens
output_tokens
total_cost_usd
latency_ms
retry_count
eval_score
accepted_output
timestamp
component
```

Components:

```text
CodeToSpec
DynamicSpec
SpectaCode
Evaluation
ControlPlane
```

## `llm_trace_export.json`

Purpose: proves native LLM observability ingestion.

Fields:

```text
trace_id
span_id
parent_span_id
workflow_id
workflow_name
agent_name
prompt_template
model_provider
model_name
region
input_tokens
output_tokens
latency_ms
error
retry_count
eval_score
accepted_output
timestamp
```

## `finops_cloud_export.csv`

Purpose: proves FinOps / cloud cost ingestion.

Fields:

```text
account
service
region
usage_type
cost_usd
usage_kwh
timestamp
tags_project
tags_workspace
business_unit
environment
```

## `carbon_factors.csv`

Purpose: proves CCF-style carbon calculation extension.

Fields:

```text
cloud_provider
region
carbon_intensity_kg_per_kwh
source
methodology_version
confidence_level
```

## `model_coefficients.csv`

Purpose: converts LLM token usage into estimated energy and cost.

Fields:

```text
model
provider
model_size_class
usd_per_1m_input_tokens
usd_per_1m_output_tokens
kwh_per_1m_tokens
methodology_version
confidence_level
```

Illustrative data:

| model | provider | class | blended usd_per_1m | kwh_per_1m |
|---|---|---|---:|---:|
| large | anthropic | premium | 30 | 1.2 |
| mid | anthropic | balanced | 6 | 0.6 |
| small | anthropic | efficient | 1 | 0.3 |

## `code_scan_findings.json`

Purpose: proves SDLC energy debt scanner.

Fields:

```text
repo
file_path
rule_id
severity
finding
recommendation
estimated_runtime_impact
confidence_level
workflow_id
agent_name
```

## Seeded wow moment

Make **Support-Bot** the top offender:

```text
Support-Bot
model: large
region: ap-south
tokens: ~800M/month
task: customer support summarization
```

Recommended optimization:

```text
large model → small model
ap-south → us-west
add caching for repeated policy retrieval
compress prompt context
```

Expected effect:

- Large cost reduction
- Large CO₂e reduction
- Low-medium quality risk

---

# 9. Calculation logic

## AI inference cost

```text
ai_cost =
(input_tokens / 1,000,000 × usd_per_1m_input_tokens)
+
(output_tokens / 1,000,000 × usd_per_1m_output_tokens)
```

If only a blended model cost is available:

```text
ai_cost = total_tokens / 1,000,000 × blended_usd_per_1m_tokens
```

## AI energy

```text
estimated_kwh = total_tokens / 1,000,000 × kwh_per_1m_tokens
```

## AI carbon

```text
estimated_co2e_kg = estimated_kwh × region_carbon_intensity_kg_per_kwh
```

## Cloud carbon

```text
cloud_carbon_kg = usage_kwh × region_carbon_intensity_kg_per_kwh
```

## Confidence logic

| Confidence | Criteria |
|---|---|
| **High** | Model, region, token counts, cost, and carbon factor are present |
| **Medium** | One key field is estimated or mapped from default |
| **Low** | Region, model class, or token counts are missing/approximated |

Add visible disclaimer:

> MVP uses synthetic data and transparent estimated factors. Production TRACE would support client-approved factors, provider-specific data, CCF methodology extensions, SCI-for-AI alignment, and confidence bands.

---

# 10. In scope

## Must-have

- Connector hub with all supported systems visible
- Connection type and status shown for each system
- Connect New System drawer
- Static upload flow for CSV/JSON
- Field mapping screen
- Normalization summary
- Shared TRACE schema table
- Hero KPIs: cost, carbon, tokens, latency, quality
- AI workload dashboard by app/model/region/workflow/agent
- Trace detail with agent graph
- Token/cost/carbon per trace node
- Recommendation cards
- Apply recommendation to recalculate totals
- What-if scenario table
- Evidence pack page/modal
- Methodology note and coefficient table

## Should-have

- Data quality panel
- Telemetry completeness score
- Energy debt findings from code scan JSON
- Before/after modernization panel
- Export ledger as CSV/JSON
- Demo mode toggle to reset data

## Out of scope for hackathon

- Live Datadog, New Relic, Cloudability, CloudHealth, Flexera, Vantage, or Finout API integrations
- Live AI/Works integration
- Real CCF ingestion from cloud accounts
- Live OpenTelemetry collector
- Real Langfuse/LangSmith hosted setup
- Real LiteLLM proxy
- Real-time streaming
- Auth/multi-tenant
- Full enterprise FinOps replacement
- Full compliance reporting
- Production-grade carbon methodology
- PDF evidence pack generation unless time permits

---

# 11. User stories

## Connect

1. As a platform owner, I want to see all connected systems in one place so I know what telemetry TRACE is using.
2. As a FinOps analyst, I want to upload a static cloud cost export so I can start measuring before live APIs are configured.
3. As an AI engineer, I want to connect an LLM trace export so TRACE can show cost/carbon per workflow and agent.
4. As a sustainability lead, I want to upload carbon factors so TRACE can calculate CO₂e transparently.
5. As a delivery lead, I want to see connection status and data quality warnings so I know whether the numbers are trustworthy.

## Observe

1. As a CIO, I want to see AI cost and carbon together so I can govern AI growth.
2. As an engineering lead, I want to see the highest cost/carbon workflows so I know where to optimize first.
3. As an AI engineer, I want to inspect an agent trace so I can see which step is causing waste.
4. As a product owner, I want to see cost/carbon per accepted output so I can connect AI usage to delivery value.

## Optimize

1. As a platform team, I want recommendations for model substitution, prompt compression, caching, and agent loop pruning so I can reduce waste.
2. As a FinOps lead, I want what-if scenarios so I can compare cost, carbon, latency, and quality tradeoffs.
3. As a sustainability lead, I want evidence packs so I can explain the methodology and assumptions behind reported reductions.
4. As a delivery team, I want SDLC energy debt findings so I can fix sustainability issues before production.

---

# 12. Acceptance criteria

## Phase 1: Connect

- User can view a connector hub with at least 10 visible systems.
- Each connector shows category, connection type, status, last sync/upload, record count, normalization percentage, and owner.
- User can open a Connect New System drawer.
- User can choose API vs file upload connection method.
- User can upload/read at least 3 bundled sample files.
- User can view a field mapping screen.
- User can run normalization and see a normalized TRACE table.
- User can see data quality warnings and telemetry completeness.

## Phase 2: Observe

- Dashboard renders total cost and total CO₂e from normalized records.
- Dashboard shows cost and carbon by app/model/region/workflow/agent.
- User can open a trace detail page.
- Trace page shows an agent graph.
- Each trace node shows tokens, cost, CO₂e, latency, retry count, and eval score.
- User can identify the top cost/carbon workflow.

## Phase 3: Optimize

- System displays at least 4 recommendation cards.
- At least one recommendation can be applied.
- Applying a recommendation recalculates cost and CO₂e.
- What-if table shows Current vs Balanced Optimization vs Aggressive Carbon Mode.
- Evidence pack shows source telemetry, formula, factors, assumptions, methodology version, confidence, before/after cost, and before/after CO₂e.

## General

- Runs locally with `streamlit run app.py`.
- No network/cloud dependency.
- Uses synthetic data clearly labeled as synthetic.
- Demo can be completed in ≤5 minutes.

---

# 13. Demo walkthrough script

## Target length

5–7 minutes for internal walkthrough, compressible to ≤5 minutes for submission.

## Script

```text
Hi, I’m Chinwe, and this is TRACE: the AI Cost, Carbon, and Control Plane for software delivery.

The problem we’re solving is simple: enterprises are adopting AI faster than they can govern it. AI is helping teams modernize systems, generate code, write tests, and operate software faster, but most organizations cannot clearly answer three questions: What is this AI usage costing us? What carbon impact is it creating? And what should we change to reduce waste without slowing delivery?

TRACE is designed to answer those questions.

For this demo, we’re using a fictional financial services client, Northstar Bank, modernizing a legacy digital banking platform. The team is using AI/Works-style workflows to reverse engineer legacy code, generate specs, create services, and test the new application. TRACE sits across that delivery lifecycle and turns fragmented telemetry into cost, carbon, and optimization decisions.

We start in the onboarding flow.

I create a new TRACE workspace called Digital Banking Modernization. TRACE asks what we want to monitor: LLM usage, cloud cost, carbon impact, SDLC sustainability KPIs, and optimization opportunities.

Now TRACE shows the available data sources. In a real client environment, these could include Datadog, New Relic, LangSmith, Langfuse, Google Cloud Monitoring, Apptio Cloudability, CloudHealth, Flexera, Vantage, Finout, AI/Works, and Cloud Carbon Footprint.

For the MVP, we’ll connect three sources.

First, I connect an AI/Works control plane export. This gives TRACE workspace, workflow, model, token, cost, and agent activity data.

Second, I connect an LLM observability trace export. This gives TRACE the step-by-step trace of prompts, model calls, retrieval steps, agent loops, latency, and eval signals.

Third, I connect a cloud and FinOps export. This gives TRACE cloud service, region, cost, and infrastructure usage data.

Once I click ingest, TRACE validates the files, maps the fields, and shows a telemetry completeness score. We can see token data, cost data, region data, and workflow attribution. Some records have high confidence, while others have medium or low confidence because the source data is incomplete. That is important because TRACE is not pretending the data is perfect. It shows where the evidence is strong and where more instrumentation is needed.

Next, TRACE normalizes the data into a shared schema.

Now records from AI/Works, Langfuse-style traces, and Cloudability-style cost exports all appear in one model. Each row has a provider, model, region, workspace, workflow, agent, input tokens, output tokens, latency, cost, estimated kilowatt-hours, estimated CO₂e, confidence level, and methodology version.

This is the TRACE Connect layer: ingest and normalize.

Now we move into TRACE Observe.

Here we can see the AI workload dashboard. At the top, we see total AI cost, total estimated CO₂e, total tokens, average latency, and quality score. Below that, TRACE breaks down cost and carbon by model, workflow, agent, and region.

The most important view is the workflow trace.

I open the customer account service generation workflow. TRACE shows the full agent path: SpecAgent, BuildAgent, TestAgent, ReviewAgent, and FixAgent. For each step, we can see model used, prompt tokens, output tokens, cost, carbon, latency, retry count, and eval score.

This is where TRACE becomes more than a dashboard. We can see that BuildAgent and FixAgent are driving most of the cost and carbon. We can also see that FixAgent retries multiple times before human review. That is a sustainability signal, a cost signal, and an engineering workflow signal.

Now we move into TRACE Optimize.

TRACE generates recommendations based on the telemetry.

The first recommendation is model substitution. TRACE has identified that low-risk summarization tasks are using a premium model when a smaller model could likely perform the task with lower cost and lower carbon impact.

The second recommendation is prompt compression. The BuildAgent is sending the same architecture context repeatedly on every retry. TRACE estimates that compressing and caching that context could save thousands of tokens per workflow.

The third recommendation is caching. The same policy retrieval step is repeated across most agent runs. TRACE recommends caching that retrieval output and shows the estimated cost and CO₂e savings.

The fourth recommendation is agent loop pruning. FixAgent averages more than four retries before human review. TRACE recommends capping retries at two and escalating earlier when confidence is low.

The fifth recommendation is an energy debt finding. TRACE scanned the generated service and found a repeated full-table query pattern that may increase runtime compute once the application is deployed. That gives the team a sustainability KPI inside the SDLC, not after the fact.

Now we open the what-if scenario view.

TRACE compares the current model mix to an optimized model mix and an aggressive carbon reduction mode. The balanced optimization scenario reduces estimated AI cost by about 20% and estimated CO₂e by about 16%, while keeping quality risk low to medium.

Finally, we generate an evidence pack.

The evidence pack shows the source telemetry, trace IDs, calculation formula, emission factors, assumptions, methodology version, confidence level, before-and-after comparison, estimated cost saved, and estimated CO₂e reduced.

That is the proof layer. TRACE gives leaders a way to govern AI delivery with the same seriousness they apply to cost, security, and quality.

The bigger vision is that TRACE can start by ingesting from the tools clients already have, but over time it becomes the cross-cloud, cross-model control layer for AI workload observability, GreenOps, FinOps, and SDLC sustainability.

TRACE helps enterprises build with AI faster, while proving they are controlling the cost and carbon impact of that AI.
```

---

# 14. Demo flow checklist

1. Start with empty or partially configured workspace.
2. Open **TRACE Connect**.
3. Show connected systems table with API/static status.
4. Click **Connect New System**.
5. Select **Cloudability Export** or **LLM Trace Export**.
6. Choose **Static CSV/JSON Upload**.
7. Upload bundled sample file.
8. Show validation response.
9. Open field mapping screen.
10. Save mapping.
11. Run normalization.
12. Show telemetry completeness and warnings.
13. Open normalized table.
14. Open dashboard.
15. Show cost + carbon KPIs.
16. Open workflow trace and agent graph.
17. Show top cost/carbon agent.
18. Apply one recommendation.
19. Show before/after cost + CO₂e reduction.
20. Generate evidence pack.

---

# 15. Hour-by-hour plan

| Time | Task | Output |
|---|---|---|
| 0:00–0:20 | Set up Streamlit app, folder structure, sample data folder | App runs locally |
| 0:20–0:50 | Create/generate synthetic CSV/JSON data | Sample data available |
| 0:50–1:30 | Implement loader + connector state model | Connector table works |
| 1:30–2:15 | Implement field mapping and normalization | Shared TRACE schema table |
| 2:15–3:00 | Implement carbon/cost calculator | Numbers render |
| 3:00–3:45 | Build dashboard KPIs and breakdowns | Observe view works |
| 3:45–4:30 | Build trace detail / agent graph | Trace view works |
| 4:30–5:15 | Build recommendations and Apply logic | Optimize view works |
| 5:15–5:45 | Build evidence pack page/modal | Prove view works |
| 5:45–6:30 | Polish, labels, demo reset button, record walkthrough | Submission-ready |

---

# 16. Build requirements

## Folder structure

```text
TRACE/
  app.py
  requirements.txt
  README.md
  sample-data/
    aiworks_usage_export.json
    llm_trace_export.json
    finops_cloud_export.csv
    carbon_factors.csv
    model_coefficients.csv
    code_scan_findings.json
  src/
    connectors.py
    normalize.py
    calculate.py
    recommendations.py
    evidence.py
```

## Connector state fields

```text
connector_id
system_name
category
connection_type
status
last_sync_at
sync_frequency
records_ingested
records_normalized
normalization_success_rate
data_owner
auth_type
source_format
created_at
updated_at
```

## Static upload fields

```text
file_name
file_type
file_size
uploaded_at
uploaded_by
refresh_cadence
```

## API connector fields

```text
api_base_url
auth_status
token_expiration
sync_enabled
last_successful_sync
last_failed_sync
```

---

# 17. Risks and mitigations

| Risk | Mitigation |
|---|---|
| MVP becomes too big | Only 3–5 connectors actually work; rest are visible placeholders |
| Looks like just a dashboard | Make onboarding, normalization, recommendation application, and evidence pack central |
| Numbers seem fake | Label synthetic data and show formula/methodology/confidence |
| Too much focus on FinOps replacement | Lead with AI workload control plane wedge; position enterprise FinOps replacement as roadmap |
| Live integrations fail | Do not use live APIs in MVP; use static tool-shaped exports |
| Carbon methodology challenged | Use transparent assumptions, methodology version, and confidence bands |
| Demo takes too long | Use demo reset and preloaded sample workspace |
| Streamlit UI feels basic | Use strong labels, tabs, metric cards, tables, and a clean scripted flow |

---

# 18. Definition of done

The MVP is done when:

- `streamlit run app.py` launches without network dependencies.
- TRACE Connect shows all supported systems with status and connection type.
- At least 3 sample sources can be loaded or are bundled as loaded.
- Data can be normalized into the TRACE shared schema.
- Dashboard shows cost + carbon together.
- Trace view shows agent steps with tokens, cost, CO₂e, latency, retry count, and eval score.
- Recommendation engine shows at least 4 recommendations.
- Applying at least 1 recommendation updates cost and CO₂e.
- What-if scenario table shows Current vs Optimized states.
- Evidence pack shows source data, formula, assumptions, methodology version, confidence, and before/after results.
- Demo can be completed in ≤5 minutes.
- Written submission can describe TRACE as a tool-led, repeatable AI GreenOps service.
