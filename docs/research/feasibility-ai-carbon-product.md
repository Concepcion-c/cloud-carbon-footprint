# Feasibility one-pager — independent "carbon beside cost + optimization for AI" product

> **Status:** v1 · **Date:** 2026-06-10 · **Audience:** self (pressure-test before building)
> Companion to `../strategy/sustainability-strategy-analysis.md` (§7). Plain-English by design.
> All client examples are illustrative; no real client data is referenced.

## TL;DR — is it feasible?
**Yes, for a credible MVP — high confidence.** It's CCF's proven pattern (*ingest usage → apply
coefficients → show cost+carbon → recommend fixes*) **extended from cloud infrastructure to AI
inference**. The infra half already exists in CCF. The AI half is new but mechanically simple:
*tokens × energy-per-token × grid-carbon-intensity*. The hard parts are **data granularity** (how
finely we can attribute usage to apps/teams) and **coefficient accuracy** (closed models are
estimates) — both manageable and honestly disclosable. Transparency of method is the selling point.

## What we're building (recap)
A standalone tool the **client buys and keeps** that shows **carbon next to cost** for their
**cloud + AI inference**, ranks their **most inefficient apps** (energy debt), and recommends
**optimizations that cut both numbers**. SCI-for-AI / ISO 21031 conformant, open methodology.

---

## 1. Data inputs — what the client provides

### Tier 1 — minimum to deliver value (provider exports)
| Input | Source / format | Gives us | Ease |
|---|---|---|---|
| **Cloud billing** | AWS **CUR** (S3), GCP billing → **BigQuery**, Azure cost export (CSV) | Infra energy + carbon + cost (compute, storage, networking, embodied) | **Easy** — CCF already ingests AWS/GCP |
| **LLM usage/billing** | OpenAI usage export; Anthropic console usage; AWS **Bedrock** invocation logs (CloudWatch/S3); GCP **Vertex** usage | Tokens per model + spend → AI inference cost; carbon via coefficient | **Easy** for org totals; harder for per-app |

### Tier 2 — per-app / per-team attribution (the granularity that makes recs actionable)
| Input | Source | Gives us | Ease |
|---|---|---|---|
| **AI gateway / proxy logs** | LiteLLM, Portkey, Cloudflare AI Gateway, Kong AI, internal gateway | Per-**request** tokens + model + latency + app/user tags | **Medium** — best single source; only if they run a gateway |
| **Cost-allocation tags/labels** | Cloud + LLM spend tagged by app/team/env | Maps usage → applications | **Medium** — depends on their tagging hygiene |

> If the client has **no gateway**, that's a finding, not a blocker: recommending they route LLM
> calls through a gateway is itself a consulting hook (and improves their FinOps too).

### Tier 3 — self-hosted / fine-tuned models
| Input | Source | Gives us | Ease |
|---|---|---|---|
| **GPU instance-hours** | Cloud billing (already in Tier 1) | Rough energy from instance type × hours | **Medium** |
| **GPU utilization telemetry** | Prometheus + **DCGM exporter**, `nvidia-smi`, k8s metrics | Actual energy (better than instance-hours) | **Medium-hard** — needs their observability access |
| **Training/fine-tune job logs** | MLflow / W&B / pipeline logs | Training energy (often dwarfs inference per SCI-for-AI) | **Medium** |

### For the CAST-like "Assess" layer
- **Repo / source access** (read-only) → static energy-debt heuristics.
- **Runtime telemetry** (APM traces, cloud usage per service) → grounds static findings in real consumption. Static-only is approximate; **fusing the two** is the credible version.

---

## 2. Coefficients & methodology — *TW supplies these, not the client*

- **Energy per token** — from public benchmarks: **ML.Energy leaderboard**, **SCI-for-AI**,
  Greenpixie-style per-token figures, vendor disclosures. Ballpark anchor from research:
  LLM inference ≈ **0.5–1.3 kWh / million tokens** depending on model size + grid. Closed models
  (GPT-4-class) → estimated from open-model proxies of similar size/quantization.
- **Grid carbon intensity** by region/time — **Electricity Maps** (public averages; US 2024 avg
  ≈ 402 gCO₂e/kWh). Location-based per SCI (no offsets).
- **PUE** (data-centre overhead) and **embodied/Scope-3** hardware — CCF already uses **Boavizta**
  APIs for embodied; reuse for the infra half.
- **Methodology = SCI-for-AI / ISO 21031:** `SCI = (O + M) / R`, a *rate* per functional unit
  (here: per token / per request / per workflow). `O = energy × grid intensity` (location-based);
  `M = embodied`. **Offsets cannot reduce the score — only real elimination.** This conformance is
  the credibility bar *and* the differentiator vs black-box calculators.

---

## 3. What's real vs. approximate (be honest in the pitch)

| Claim | Confidence | Why |
|---|---|---|
| Cloud infra cost + carbon | **Solid** | CCF does this today on real billing data |
| AI inference **cost** | **Solid** | Comes straight from provider billing/usage |
| AI inference **carbon (totals)** | **Good** | Tokens are real; energy-per-token is benchmarked but model-dependent |
| AI inference carbon (closed models, fine-grained) | **Approximate** | Closed-model energy is estimated from open proxies — disclose the assumption |
| Per-app attribution | **Depends on data** | Solid with a gateway; coarse without |
| "Energy debt" static ranking | **Directional** | Static code can't read energy directly; proxy heuristics + runtime data needed |
| Optimization rec savings (e.g. model swap) | **Estimable** | Cost delta is exact; carbon delta uses the same coefficients — show ranges, not false precision |

**Principle:** lead with the numbers we can stand behind (cost, tokens, grid intensity), present
carbon as a transparent, methodology-cited estimate with ranges. Honesty *is* the moat here.

---

## 4. Reference architecture (plain English)
```
Client data (cloud billing + LLM usage [+ gateway logs] [+ repo/telemetry])
        │  ingest (connectors / file upload)
        ▼
Normalize → usage rows (compute, storage, tokens-by-model-by-app-by-region)
        │  apply coefficients (energy/token, grid intensity, PUE, embodied)
        ▼
Cost + carbon, side by side, sliced by app / model / team / region / time
        │
        ├── Assess:   rank apps by energy debt + cost/carbon (static + runtime)
        ├── Optimize: recommendations (right-size model, cache, batch, shift region/time, kill idle)
        └── Prove:    auditable SCI-for-AI ledger + before/after (client-zero / engagement)
```
This is **CCF's existing pipeline** with an added "tokens" usage type and an AI coefficient table.

---

## 5. The two AI:works-dependent layers (feasibility notes)
- **"Build green" (Green CodeRefiner analog):** add a green/efficiency pass to AI:works'
  spec-to-code agents (efficient algorithms, caching, right-sized models, efficient queries).
  *Real but partly marketing* — guaranteeing a precise % energy saving is hard. The **measurable**
  version is the **run-time** cost/carbon of the delivered app, computed by the independent product.
- **"Assess" via AI:works ingest (CAST analog):** reuse AI:works' reverse-engineering/ingest to
  also score energy debt. *Feasible, directional.* Pure-static energy is approximate (CAST infers
  from structure; Greenspector measures real device energy) — fuse static heuristics with runtime
  data for credibility. Strong fit with "which legacy apps to modernize first for cost+carbon ROI."

---

## 6. Risks & mitigations (technical)
| Risk | Mitigation |
|---|---|
| Closed-model coefficients are estimates | Cite sources, show ranges, conform to SCI-for-AI, disclose openly |
| No gateway → weak per-app attribution | Org/model-level first; recommend a gateway as a deliverable |
| Self-hosted GPU energy needs telemetry | Fall back to instance-hours; offer telemetry setup as a service step |
| Static energy-debt is approximate | Fuse with runtime data; frame as "prioritization," not exact accounting |
| Client reluctant to share billing/source | File-upload mode + read-only scoped access; nothing leaves their tenancy if self-hosted |
| Methodology disputes (audit) | Open, versioned coefficient table + evidence lineage; lead with GSF-founder credibility |

## 7. Open technical questions
1. **Gateway prevalence** — how many target clients already route LLM calls through a gateway (decides per-app feasibility out of the box)?
2. **Deployment model** — SaaS (client ships us exports) vs in-tenant (we run inside their cloud, à la CCF self-host)? Affects data-sharing comfort and sales motion.
3. **Coefficient maintenance** — who owns keeping the energy-per-token table current as models churn? (A small but ongoing job.)
4. **Embodied/Scope-3 for GPUs** — does Boavizta cover the GPU SKUs clients actually run, or do we need supplementary data?
5. **Assess accuracy bar** — what energy-debt precision do buyers expect before they trust a "fix this app first" recommendation?
