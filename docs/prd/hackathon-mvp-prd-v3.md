# PRD: RECPT — Hackathon MVP v3

> **Status:** Draft v3 · **Owner:** Concepcion-c · **Last updated:** 2026-06-10
> Supersedes `hackathon-mvp-prd-v2.md`. References ChatGPT v3 draft (`hackathon-mvp-CHAT-prd-v3-recpt.md`) as input.
> Same goal: a ≤5-minute demoable MVP that proves the Phase 1–3 RECPT product story: **Connect → Observe → Optimize**.
> Full product direction: RECPT becomes the cross-cloud, cross-model, client-facing control layer for AI workload observability, AI FinOps, GreenOps, carbon accounting, evidence lineage, and SDLC sustainability KPIs.

---

## 1. Product thesis

**RECPT is the AI Cost, Carbon, and Control Plane for software delivery.**

RECPT starts by connecting to the fragmented tools clients already have — LLM observability, cloud monitoring, FinOps/cloud cost, CCF, and AI/Works — then normalizes that telemetry into one shared cost + carbon + governance model.

Over time, RECPT becomes the system of record and system of action for AI workload management:

- Native LLM observability
- Token, cost, carbon, and quality per trace
- AI/Works / SDLC workflow attribution
- GreenOps and FinOps decisioning
- CCF-based carbon calculation extension
- Optimization recommendations
- Evidence packs for governance and reporting

### One-sentence MVP

A **Streamlit** dashboard that simulates enterprise onboarding, shows connected systems, ingests synthetic client exports shaped like real tools, normalizes them into a RECPT schema, observes AI workload cost/carbon by workflow and agent trace, recommends optimizations, and shows cost + CO₂e reductions with transparent evidence.

---

## 2. MVP positioning

### What this MVP proves

1. **RECPT Connect:** RECPT can ingest from fragmented enterprise tools and normalize their data into one schema.
2. **RECPT Observe:** RECPT can replace basic LLM observability for AI workloads by showing traces, agents, tokens, cost, carbon, latency, and quality signals.
3. **RECPT Optimize:** RECPT can recommend lower-cost/lower-carbon actions and show before/after impact.

### What this MVP does not claim

This MVP does **not** build full live integrations with every tool. It shows:

- Functional ingestion from static JSON/CSV files shaped like real tool outputs
- Mocked API connectors to demonstrate the production integration path
- A credible connector adapter interface that supports live APIs, file uploads, OpenTelemetry, webhooks, and reference datasets

The "Mock API" concept is an **implementation detail only** — it is never surfaced in the UI. The UI always shows "API" for live-style connectors and "Static CSV/JSON" for file-based connectors.

### Strategic wedge

> **RECPT connects to existing observability, cloud, and FinOps systems, then normalizes fragmented telemetry into one cost, carbon, and governance model.**

> **Static uploads let teams start measuring immediately, even before live integrations are configured.**

---

## 3. Product phases represented in the MVP

| Phase | Product goal | MVP proof |
|---|---|---|
| **Phase 1: RECPT Connect** | Ingest and normalize telemetry | Connector hub, file upload/API mock, validation, mapping, normalized schema |
| **Phase 2: RECPT Observe** | Replace LLM observability for AI workloads | AI workload dashboard, agent graph, trace details, cost/carbon per trace |
| **Phase 3: RECPT Optimize** | Become a system of action | Recommendations, what-if scenarios, before/after savings |

---

## 4. Core principle — reuse, do not rebuild

**We do not host or integrate these tools during the hackathon. We adopt their data shapes and show the integration path.** Only the unique RECPT logic is custom code.

| Layer | We BUILD | We ADOPT / SIMULATE | We ROADMAP |
|---|---|---|---|
| Connector hub | RECPT Connect UI + connector state model | Tool-shaped exports from AI/Works, Langfuse/LangSmith, FinOps, CCF | Live APIs, OTel collector, webhooks |
| Cloud carbon | RECPT calculation from CCF-shaped exports | CCF methodology/output shape | Full CCF ingestion from cloud billing |
| AI usage ledger | RECPT calculator | Langfuse/LangSmith/OpenTelemetry GenAI-shaped traces | Live LLM gateway / provider APIs |
| LLM observability | Basic trace + agent graph + trace metrics | Synthetic trace spans | Full native tracing SDK |
| FinOps | Cost allocation from static exports | Cloudability/Finout-style cost fields | Budgeting, showback/chargeback, anomaly detection |
| Optimization | Rule-based recommendations | Model substitution, prompt compression, caching, region shift | AI-assisted recommendation engine |
| Energy debt | Static code-scan findings | Semgrep-shaped JSON | Custom SDLC energy rules and CI gates |
| UI/storage | Streamlit + pandas | Local bundled CSV/JSON | Production UI and database |

**Decided build stack:** Streamlit + pandas + custom RECPT calculator + bundled synthetic CSV/JSON files.

---

## 5. MVP user and scenario

### Primary demo persona

**CIO / CTO / Head of Engineering at a financial services client**

They are using AI to accelerate modernization but need to answer:

- What is AI-enabled delivery costing us?
- What carbon impact is this creating?
- Which models, agents, workflows, regions, or code paths are driving waste?
- What should we optimize first?
- Can we produce transparent evidence behind the numbers?

### Demo scenario

A fictional financial services company, **Northstar Bank**, is modernizing a legacy digital banking platform with AI/Works-style workflows.

RECPT is onboarded to monitor:

- AI/Works usage
- LLM traces
- FinOps/cloud cost exports
- CCF carbon factors
- SDLC energy debt findings

---

## 6. MVP screens

---

### Screen 1: RECPT Connect: Data Sources

#### Purpose

Show every connected system — whether it is a live API-based or static file-based connection — its status, data freshness, record counts, and whether RECPT has successfully normalized it. This screen should feel like an **enterprise integration hub**, not a file upload page.

#### Top summary

```
RECPT Connect

Connected systems: 7
Live API connections: 3
Static file uploads: 4
Healthy: 5
Warnings: 2
Failed: 0
Last normalization run: 12 minutes ago

[+ Connect New System]   [Run Sync]   [Upload File]   [View Normalization Log]
```

`+ Connect New System` is the primary action button.
`Run Sync`, `Upload File`, and `View Normalization Log` are secondary actions.

#### Connected systems table

| System | Category | Connection Type | Status | Last Sync | Records | Normalization | Owner | Actions |
|---|---|---|---|---:|---:|---|---|---|
| AI/Works Control Plane | AI delivery | API | Connected | 12 min ago | 1,248 | 98% mapped | Platform Team | View / Sync |
| Langfuse | LLM observability | API | Connected | 18 min ago | 842 | 94% mapped | AI Eng | View / Sync |
| Datadog | LLM observability | API | Warning | 1 hr ago | 493 | 81% mapped | SRE | Fix Mapping |
| Cloudability Export | FinOps | Static CSV | Uploaded | Jun 10 | 2,104 | 89% mapped | FinOps | Replace File |
| Google Cloud Monitoring | Cloud monitoring | API | Connected | 20 min ago | 1,876 | 92% mapped | Cloud Team | View / Sync |
| CCF Factors | Carbon methodology | Static CSV | Active | Jun 10 | 64 | 100% mapped | Sustainability | View |
| Code Scan Findings | SDLC sustainability | Static JSON | Warning | Jun 10 | 36 | 76% mapped | Engineering | Fix Mapping |

#### Extended connector catalog (visible, not functional in MVP)

Show these connectors in a second table or an expandable section labeled "Available Connectors." Display them as roadmap tiles to prove platform ambition without overbuilding.

- LangSmith
- New Relic
- CloudHealth
- Flexera
- Vantage
- Finout
- OpenTelemetry Collector
- LiteLLM Gateway
- Webhooks

#### Status types

| Status | Meaning | UI treatment |
|---|---|---|
| **Connected** | API connection is healthy and syncing | Green check |
| **Uploaded** | Static file was uploaded successfully | Blue file icon |
| **Active** | Reference dataset is active, such as carbon factors | Green check |
| **Needs Mapping** | RECPT received data but fields need manual mapping | Yellow warning |
| **Warning** | Data ingested, but incomplete, stale, or partially mapped | Yellow warning |
| **Failed** | Connection or ingestion failed | Red alert |
| **Paused** | Connector is configured but not syncing | Gray pause |
| **Coming Soon** | Connector tile exists but is not enabled | Gray roadmap badge |

#### Connection type labels

Use these labels consistently across the UI. "Mock API" is never shown to the user — it is an implementation detail for the developer.

| Type | Meaning |
|---|---|
| **API** | Live connection that syncs automatically |
| **Static CSV** | One-time or periodic file upload |
| **Static JSON** | One-time or periodic trace/config upload |
| **Manual Upload** | User-provided file without active sync |
| **Reference Dataset** | Carbon factors, model factors, methodology file |
| **OpenTelemetry** | Streaming traces/events from apps or agents |
| **Webhook** | Event-based push from source system |

---

### Screen 1A: Connect New System drawer

#### Purpose

Demonstrate that RECPT can connect to mature clients with live tooling and less mature clients with static exports.

```
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

Then show source-specific options based on the selection.

#### Example: API connection flow

```
System: Langfuse
Connection method: API

Required:
- Host URL
- Public key
- Secret key
- Project ID

Sync frequency:
[ Every 15 minutes ▾ ]

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

#### Example: Static file upload flow

```
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

After upload, show:

```
File validated.
2,104 records found.
184 records missing region.
91 records missing workspace tag.
Proceed to field mapping?
```

---

### Screen 1B: Field mapping

#### Purpose

Show RECPT can handle messy enterprise data.

```
Map source fields to RECPT schema
```

| Source field | RECPT field | Status |
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

```
[Save Mapping]   [Run Normalization]
```

---

### Screen 1C: Connector detail page

#### Example: AI/Works Control Plane

```
AI/Works Control Plane

Connection type: API
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

#### Data quality panel

```
Data Quality

Token data completeness: 97%
Cost data completeness: 95%
Region completeness: 82%
Workflow attribution: 91%
Agent attribution: 88%
Carbon confidence: Medium
```

Warnings:

```
50 records missing region.
23 records missing model name.
14 records missing workflow attribution.
```

This panel shows that RECPT handles messy enterprise data without pretending it is clean. The confidence level reflects data completeness, not a performance judgment.

---

### Screen 2: Normalize — RECPT shared schema

#### Purpose

Show that RECPT turns fragmented telemetry into a common cost/carbon/governance model.

#### Shared schema fields

```
source_system          provider               eval_score
source_record_id       model                  accepted_output
trace_id               region                 quality_risk
span_id                workspace              confidence_level
parent_span_id         workflow               methodology_version
input_tokens           agent                  timestamp
output_tokens          latency_ms             business_unit
total_tokens           cost_usd               client_project
                       estimated_kwh          environment
                       estimated_co2e_kg      sensitivity_flag
```

#### Normalized table example

| source | provider | model | region | workspace | workflow | agent | input tokens | output tokens | latency | cost | kWh | CO₂e | confidence |
|---|---|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| AI/Works | Anthropic | Claude Sonnet | us-east | Digital Banking | Code generation | BuildAgent | 42,000 | 9,100 | 18s | $4.82 | 0.38 | 0.15 kg | Medium |
| Langfuse | OpenAI | GPT-4.1 | us-central | Digital Banking | Test generation | TestAgent | 18,000 | 7,300 | 11s | $2.10 | 0.19 | 0.07 kg | Medium |
| Cloudability | AWS | Bedrock | us-east-1 | Digital Banking | Batch summarization | SummaryAgent | 91,000 | 21,000 | 45s | $8.70 | 0.74 | 0.29 kg | Low |

#### Telemetry completeness score

```
Token data: 94%
Cost data: 91%
Region data: 82%
Carbon confidence: Medium
Missing workflow attribution: 6 records
```

---

### Screen 3: Observe — AI workload dashboard

#### Purpose

Show RECPT can replace basic LLM observability for AI workloads while adding carbon and governance context.

#### Hero KPIs

- Total AI cost
- Total cloud cost
- Total estimated CO₂e
- Total tokens
- Average latency
- Average eval score
- Cost per accepted output
- CO₂e per accepted output

#### Breakdown views

- Cost by model
- Carbon by model
- Cost + carbon by app
- Cost + carbon by region
- Top agents by token usage
- Top workflows by cost
- Top workflows by CO₂e
- Retry count by agent
- Eval score by workflow

#### Trace detail / agent graph

Demo trace:

```
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

> RECPT does not only show that a workflow cost $18.42. It shows which agent step created the most cost and carbon, and whether that cost produced accepted output.

---

### Screen 4: Optimize — recommendations and what-if scenarios

#### Purpose

Show RECPT can move from observability to action.

#### Recommendation rules

| Recommendation | Trigger | Example |
|---|---|---|
| **Model substitution** | Low-risk workflow uses premium model | Move summarization from large model to small model |
| **Prompt compression** | Input tokens above threshold or repeated context | Compress architecture context |
| **Caching** | Same retrieval/policy context repeated across traces | Cache policy retrieval |
| **Region/time shifting** | High-carbon region for flexible workload | Move batch job to lower-carbon region/time |
| **Batch processing** | Many small calls for similar task | Batch summarization or test generation |
| **Agent loop pruning** | Retry count above threshold | Cap FixAgent retries at 2 |
| **Energy debt fix** | Static code-scan finding severity high | Fix repeated full-table scan |

#### Recommendation card format

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

```
Recommendation: Prompt compression

BuildAgent is sending the same architecture context on every retry.
Estimated impact:
- 22,000 tokens saved per run
- $1,240/month saved
- 14.2 kg CO₂e avoided/month
- Quality risk: Low
- Confidence: Medium

[Apply Recommendation]
```

---

### Screen 4A: What-if scenario planner

#### Purpose

Show business tradeoffs.

| Scenario | Monthly AI cost | Estimated CO₂e | Avg latency | Quality risk |
|---|---:|---:|---:|---|
| Current | $12,400 | 410 kg CO₂e | 12.8s | Low |
| Balanced optimization | $9,850 | 344 kg CO₂e | 11.9s | Low-medium |
| Aggressive carbon mode | $8,900 | 301 kg CO₂e | 14.2s | Medium |

Recommended scenario:

```
Balanced optimization
20.5% cost reduction
16.1% CO₂e reduction
No major quality degradation
```

---

### Screen 5: Prove — evidence pack

#### Purpose

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

MVP evidence pack should be a page or modal with export buttons:

```
[Download CSV]   [Download JSON]   [Export Evidence Pack PDF — roadmap]
```

---

## 7. Functional connector scope

### Functional in hackathon MVP

These need to actually work using static uploads or bundled files.

| Connector | Type | MVP behavior |
|---|---|---|
| **AI/Works Control Plane** | Static JSON | Upload/read JSON and normalize workspace/workflow/agent/model/token/cost data |
| **Langfuse / LangSmith trace export** | Static JSON | Upload/read trace export and render agent graph |
| **Cloudability / FinOps export** | Static CSV | Upload/read cost data and join by workspace/project/region |
| **CCF Carbon Factors** | Static CSV | Upload/read carbon factors and calculate CO₂e |
| **Code Scan Findings** | Static JSON | Upload/read energy debt findings and surface recommendations |

### Visible but not functional in MVP

Show these as available or coming soon in the connector hub to prove platform vision without overbuilding.

- Datadog
- New Relic
- Google Cloud Monitoring
- CloudHealth
- Flexera
- Vantage
- Finout
- OpenTelemetry Collector
- LiteLLM Gateway
- Webhooks

---

## 8. Suggested demo moment

During the live walkthrough, use this framing:

> "RECPT can start in two modes. For mature clients, it connects to live systems through APIs like AI/Works, Datadog, Langfuse, Google Cloud Monitoring, or FinOps tools. For clients who are earlier in their journey, RECPT can ingest static exports like CSV or JSON files. In both cases, the connector adapter normalizes the data into the same RECPT schema."

Then walk through these steps:

1. Click **+ Connect New System**
2. Choose **Cloudability Export**
3. Select **File Upload**
4. Upload the sample CSV
5. Show validation warnings (missing region, missing workspace tag)
6. Open field mapping screen
7. Click **Run Normalization**
8. Watch the dashboard update with new cost + carbon totals

This is the cleanest way to demonstrate ingestion in under 2 minutes.

---

## 9. Sample data spec

Place files in `../sample-data/`. Label clearly as synthetic.

### `aiworks_usage_export.json`

Purpose: proves AI/Works control plane ingestion.

Fields: `workspace_id`, `workspace_name`, `project_name`, `workflow_id`, `workflow_name`, `agent_name`, `model_provider`, `model_name`, `region`, `input_tokens`, `output_tokens`, `total_cost_usd`, `latency_ms`, `retry_count`, `eval_score`, `accepted_output`, `timestamp`, `component`

Components: `CodeToSpec`, `DynamicSpec`, `SpectaCode`, `Evaluation`, `ControlPlane`

### `llm_trace_export.json`

Purpose: proves native LLM observability ingestion.

Fields: `trace_id`, `span_id`, `parent_span_id`, `workflow_id`, `workflow_name`, `agent_name`, `prompt_template`, `model_provider`, `model_name`, `region`, `input_tokens`, `output_tokens`, `latency_ms`, `error`, `retry_count`, `eval_score`, `accepted_output`, `timestamp`

### `finops_cloud_export.csv`

Purpose: proves FinOps / cloud cost ingestion.

Fields: `account`, `service`, `region`, `usage_type`, `cost_usd`, `usage_kwh`, `timestamp`, `tags_project`, `tags_workspace`, `business_unit`, `environment`

### `carbon_factors.csv`

Purpose: proves CCF-style carbon calculation extension.

Fields: `cloud_provider`, `region`, `carbon_intensity_kg_per_kwh`, `source`, `methodology_version`, `confidence_level`

### `model_coefficients.csv`

Purpose: converts LLM token usage into estimated energy and cost.

Fields: `model`, `provider`, `model_size_class`, `usd_per_1m_input_tokens`, `usd_per_1m_output_tokens`, `kwh_per_1m_tokens`, `methodology_version`, `confidence_level`

Illustrative data:

| model | provider | class | blended usd_per_1m | kwh_per_1m |
|---|---|---|---:|---:|
| large | anthropic | premium | 30 | 1.2 |
| mid | anthropic | balanced | 6 | 0.6 |
| small | anthropic | efficient | 1 | 0.3 |

### `code_scan_findings.json`

Purpose: proves SDLC energy debt scanner.

Fields: `repo`, `file_path`, `rule_id`, `severity`, `finding`, `recommendation`, `estimated_runtime_impact`, `confidence_level`, `workflow_id`, `agent_name`

### Seeded wow moment

Make **Support-Bot** the top offender:

```
Support-Bot
model: large
region: ap-south
tokens: ~800M/month
task: customer support summarization
```

Recommended optimization: `large → small model` + `ap-south → us-west` + caching for repeated policy retrieval + prompt compression.

Expected effect: large cost reduction, large CO₂e reduction, low-medium quality risk.

---

## 10. Calculation logic

### AI inference cost

```
ai_cost =
  (input_tokens / 1,000,000 × usd_per_1m_input_tokens)
  + (output_tokens / 1,000,000 × usd_per_1m_output_tokens)
```

If only blended cost is available:

```
ai_cost = total_tokens / 1,000,000 × blended_usd_per_1m_tokens
```

### AI energy

```
estimated_kwh = total_tokens / 1,000,000 × kwh_per_1m_tokens
```

### AI carbon

```
estimated_co2e_kg = estimated_kwh × region_carbon_intensity_kg_per_kwh
```

### Cloud carbon

```
cloud_carbon_kg = usage_kwh × region_carbon_intensity_kg_per_kwh
```

### Confidence logic

| Confidence | Criteria |
|---|---|
| **High** | Model, region, token counts, cost, and carbon factor are all present |
| **Medium** | One key field is estimated or mapped from a default |
| **Low** | Region, model class, or token counts are missing or approximated |

Add visible disclaimer on the methodology page:

> MVP uses synthetic data and transparent estimated factors. Production RECPT would support client-approved factors, provider-specific data, CCF methodology extensions, SCI-for-AI alignment, and confidence bands.

---

## 11. In scope

### Must-have

- Connector hub with all supported systems visible
- Connection type and status shown for each system
- Connect New System drawer
- Static upload flow for CSV/JSON
- File validation with warnings
- Field mapping screen
- Normalization summary
- Shared RECPT schema table
- Hero KPIs: cost, carbon, tokens, latency, quality
- AI workload dashboard by app/model/region/workflow/agent
- Trace detail with agent graph
- Token/cost/carbon per trace node
- Recommendation cards
- Apply recommendation to recalculate totals
- What-if scenario table
- Evidence pack page/modal
- Methodology note and coefficient table

### Should-have

- Data quality panel per connector
- Telemetry completeness score
- Energy debt findings from code scan JSON
- Before/after modernization panel
- Export ledger as CSV/JSON
- Demo mode toggle to reset data

### Out of scope for hackathon

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

## 12. User stories

### Connect

1. As a platform owner, I want to see all connected systems in one place so I know what telemetry RECPT is using.
2. As a FinOps analyst, I want to upload a static cloud cost export so I can start measuring before live APIs are configured.
3. As an AI engineer, I want to connect an LLM trace export so RECPT can show cost/carbon per workflow and agent.
4. As a sustainability lead, I want to upload carbon factors so RECPT can calculate CO₂e transparently.
5. As a delivery lead, I want to see connection status and data quality warnings so I know whether the numbers are trustworthy.

### Observe

1. As a CIO, I want to see AI cost and carbon together so I can govern AI growth.
2. As an engineering lead, I want to see the highest cost/carbon workflows so I know where to optimize first.
3. As an AI engineer, I want to inspect an agent trace so I can see which step is causing waste.
4. As a product owner, I want to see cost/carbon per accepted output so I can connect AI usage to delivery value.

### Optimize

1. As a platform team, I want recommendations for model substitution, prompt compression, caching, and agent loop pruning so I can reduce waste.
2. As a FinOps lead, I want what-if scenarios so I can compare cost, carbon, latency, and quality tradeoffs.
3. As a sustainability lead, I want evidence packs so I can explain the methodology and assumptions behind reported reductions.
4. As a delivery team, I want SDLC energy debt findings so I can fix sustainability issues before production.

---

## 13. Acceptance criteria

### Phase 1: Connect

- User can view a connector hub with at least 7 visible systems.
- Each connector shows category, connection type, status, last sync/upload, record count, normalization percentage, and owner.
- User can open a Connect New System drawer.
- User can choose API vs file upload connection method.
- User can upload or read at least 3 bundled sample files.
- User can view a field mapping screen.
- User can run normalization and see a normalized RECPT table.
- User can see data quality warnings and telemetry completeness.

### Phase 2: Observe

- Dashboard renders total cost and total CO₂e from normalized records.
- Dashboard shows cost and carbon by app/model/region/workflow/agent.
- User can open a trace detail page.
- Trace page shows an agent graph.
- Each trace node shows tokens, cost, CO₂e, latency, retry count, and eval score.
- User can identify the top cost/carbon workflow.

### Phase 3: Optimize

- System displays at least 4 recommendation cards.
- At least one recommendation can be applied.
- Applying a recommendation recalculates cost and CO₂e.
- What-if table shows Current vs Balanced Optimization vs Aggressive Carbon Mode.
- Evidence pack shows source telemetry, formula, factors, assumptions, methodology version, confidence, and before/after results.

### General

- Runs locally with `streamlit run app.py`.
- No network/cloud dependency.
- Uses synthetic data clearly labeled as synthetic.
- Demo can be completed in ≤5 minutes.

---

## 14. Demo walkthrough script

### Target length

5–7 minutes for internal walkthrough, compressible to ≤5 minutes for submission.

### Script

```
Hi, I'm Chinwe, and this is RECPT: the AI Cost, Carbon, and Control Plane for software delivery.

The problem we're solving is simple: enterprises are adopting AI faster than they can govern it.
AI is helping teams modernize systems, generate code, write tests, and operate software faster,
but most organizations cannot clearly answer three questions: What is this AI usage costing us?
What carbon impact is it creating? And what should we change to reduce waste without slowing delivery?

RECPT is designed to answer those questions.

For this demo, we're using a fictional financial services client, Northstar Bank, modernizing a
legacy digital banking platform. The team is using AI/Works-style workflows to reverse engineer
legacy code, generate specs, create services, and test the new application. RECPT sits across
that delivery lifecycle and turns fragmented telemetry into cost, carbon, and optimization decisions.

We start in RECPT Connect: Data Sources.

RECPT can start in two modes. For mature clients, it connects to live systems through APIs like
AI/Works, Datadog, Langfuse, Google Cloud Monitoring, or FinOps tools. For clients who are
earlier in their journey, RECPT can ingest static exports like CSV or JSON files. In both cases,
the connector adapter normalizes the data into the same RECPT schema.

I click Connect New System and choose Cloudability Export. I select File Upload and upload the
sample CSV. RECPT validates the file and immediately shows me what's wrong: 184 records are
missing region data, and 91 records are missing a workspace tag. That is important — RECPT is
not pretending the data is clean. It shows where the evidence is strong and where more
instrumentation is needed.

I open the field mapping screen and map source fields to RECPT schema fields. Then I run
normalization. RECPT now has records from AI/Works, LLM traces, and cloud cost exports all
in one model — with provider, model, region, workspace, workflow, agent, tokens, cost,
estimated kilowatt-hours, estimated CO₂e, and confidence level per row.

Now we move into RECPT Observe.

At the top, total AI cost, total estimated CO₂e, total tokens, average latency, and quality score.
Below that, cost and carbon broken down by model, workflow, agent, and region.

I open the customer account service generation workflow. RECPT shows the full agent path:
SpecAgent, BuildAgent, TestAgent, ReviewAgent, FixAgent. For each step, I can see model used,
tokens, cost, carbon, latency, retry count, and eval score.

This is where RECPT becomes more than a dashboard. BuildAgent and FixAgent are driving most of
the cost and carbon. FixAgent retries multiple times before human review. That is a sustainability
signal, a cost signal, and an engineering workflow signal at the same time.

Now we move into RECPT Optimize.

RECPT generates four recommendations: model substitution for low-risk summarization tasks, prompt
compression for BuildAgent's repeated architecture context, caching for repeated policy retrieval
across agent runs, and agent loop pruning to cap FixAgent retries and escalate earlier when
confidence is low.

I apply the prompt compression recommendation. RECPT recalculates cost and CO₂e and shows the
before/after delta live.

The what-if scenario view compares the current model mix to a balanced optimization and an
aggressive carbon reduction mode. The balanced scenario reduces AI cost by about 20% and CO₂e
by about 16% with low to medium quality risk.

Finally, RECPT generates an evidence pack with source telemetry, calculation formula, emission
factors, assumptions, methodology version, confidence level, and before/after comparison.

That is the proof layer. RECPT gives leaders a way to govern AI delivery with the same seriousness
they apply to cost, security, and quality.

The bigger vision: RECPT starts by ingesting from the tools clients already have, but over time
it becomes the cross-cloud, cross-model control layer for AI workload observability, GreenOps,
FinOps, and SDLC sustainability. RECPT helps enterprises build with AI faster, while proving
they are controlling the cost and carbon impact of that AI.
```

---

## 15. Demo flow checklist

1. Start with empty or partially configured workspace.
2. Open **RECPT Connect: Data Sources**.
3. Show connected systems table with API/static status.
4. Click **+ Connect New System**.
5. Select **Cloudability Export**.
6. Choose **File Upload**.
7. Upload bundled sample CSV.
8. Show validation response (missing region, missing workspace tag).
9. Open field mapping screen.
10. Save mapping and click **Run Normalization**.
11. Show telemetry completeness score and data quality warnings.
12. Open normalized RECPT schema table.
13. Open dashboard.
14. Show cost + carbon KPIs.
15. Open workflow trace and agent graph.
16. Show top cost/carbon agent node.
17. Apply one recommendation.
18. Show before/after cost + CO₂e reduction.
19. Open what-if scenario table.
20. Generate evidence pack.

---

## 16. Hour-by-hour plan

| Time | Task | Output |
|---|---|---|
| 0:00–0:20 | Set up Streamlit app, folder structure, sample data folder | App runs locally |
| 0:20–0:50 | Create/generate synthetic CSV/JSON data | Sample data available |
| 0:50–1:30 | Implement loader + connector state model | Connector table renders |
| 1:30–2:15 | Implement file validation, field mapping, and normalization | Shared RECPT schema table |
| 2:15–3:00 | Implement carbon/cost calculator | Numbers render |
| 3:00–3:45 | Build dashboard KPIs and breakdowns | Observe view works |
| 3:45–4:30 | Build trace detail / agent graph | Trace view works |
| 4:30–5:15 | Build recommendations and Apply logic | Optimize view works |
| 5:15–5:45 | Build evidence pack page/modal | Prove view works |
| 5:45–6:30 | Polish, labels, demo reset button, record walkthrough | Submission-ready |

---

## 17. Build requirements

### Folder structure

```
RECPT/
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

### Connector state fields

For all connectors:

```
connector_id          normalization_success_rate
system_name           data_owner
category              auth_type
connection_type       source_format
status                created_at
last_sync_at          updated_at
sync_frequency
records_ingested
records_normalized
```

For static uploads, also store:

```
file_name
file_type
file_size
uploaded_at
uploaded_by
refresh_cadence
```

For API connections, also store:

```
api_base_url
auth_status
token_expiration
sync_enabled
last_successful_sync
last_failed_sync
```

---

## 18. Risks and mitigations

| Risk | Mitigation |
|---|---|
| MVP becomes too big | Only 3–5 connectors actually work; rest are visible placeholders |
| Looks like just a dashboard | Make onboarding, normalization, recommendation application, and evidence pack central |
| Numbers seem fake | Label synthetic data and show formula/methodology/confidence |
| Carbon methodology challenged | Use transparent assumptions, methodology version, and confidence bands |
| "Mock API" confuses demo | Never show "Mock API" in the UI — it is an implementation detail only |
| Demo takes too long | Use demo reset and preloaded sample workspace; 8-step connector moment is ≤2 min |
| Streamlit UI feels basic | Use strong labels, tabs, metric cards, tables, and a clean scripted flow |
| Live integrations fail | Do not use live APIs in MVP; use static tool-shaped exports |

---

## 19. Definition of done

The MVP is done when:

- `streamlit run app.py` launches without network dependencies.
- RECPT Connect shows at least 7 systems with status, connection type, records, normalization %, and owner.
- At least 3 sample sources can be loaded or are bundled as loaded.
- File upload shows validation warnings and field mapping screen.
- Data can be normalized into the RECPT shared schema.
- Dashboard shows cost + carbon together.
- Trace view shows agent steps with tokens, cost, CO₂e, latency, retry count, and eval score.
- Recommendation engine shows at least 4 recommendation cards.
- Applying at least 1 recommendation updates cost and CO₂e live.
- What-if scenario table shows Current vs Optimized states.
- Evidence pack shows source data, formula, assumptions, methodology version, confidence, and before/after results.
- Demo can be completed in ≤5 minutes.
- Written submission can describe RECPT as a tool-led, repeatable AI GreenOps service.
