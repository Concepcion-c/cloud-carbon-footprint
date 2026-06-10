# Sustainability as a Thoughtworks Differentiator — Strategy & Ranked Hackathon Ideas

> **Status:** v2 analysis (independent-product pivot) · **Date:** 2026-06-10 · **Audience:** self (evaluation)
> **v2 change:** the lead recommendation is now an **independent, sellable product** (CCF-lineage), *not* an AI:works-embedded module — because TW does not license AI:works to clients. AI:works is repositioned as "client zero" + an accelerator. See §1, §6 (note), §7.
> **Lenses applied:** Product Manager (buildable) · TW executive (sellable, on-strategy) · Head of Sustainability (credible, outcome-backed).
> **Sources:** local `TRACE_Documents/` (IT Sustainability Market Analysis; AI/Works platform docs; CCF revival/roadmap docs; team check-ins — paraphrased, no PII) + public web research on TW FY26 / AI:works / competitors. Confidential material is distilled, never quoted.

---

## 1. Executive summary

**The thesis.** Thoughtworks' FY26 flagship narrative — *Looking Glass 2026* and the **AI:works** agentic delivery platform — **contains no sustainability story at all**, even though TW *co-founded the Green Software Foundation* and *originated Cloud Carbon Footprint (CCF)*. That gap is the opportunity. The market is simultaneously being reshaped by the **AI energy shock** (IEA: AI data-centre electricity use surged ~50% in 2025; hyperscaler emissions are *rising* again), which is pushing buyers from "what's our cloud carbon?" to **"what's the carbon of our AI workloads, per agent, and how do we cut it?"**

**The move.** Make **carbon a standalone, sellable product** in CCF's lineage — an *independent* "GreenOps for AI" tool the client buys and keeps, that shows **carbon beside cost** for their cloud *and* their AI inference and recommends optimizations. It must **not** depend on owning AI:works (which TW does not license to clients). AI:works instead plays two supporting roles: **"client zero"** (TW dogfoods it) and an **accelerator** that *builds greener software*, whose benefit the independent product then *proves* to the client. **We sell the outcome + the proof, never the platform.**

Anchor on the carbon the client actually pays for — **run-time** (the delivered app's ongoing cloud + AI-inference footprint) — not **build-time** (the AI credits TW spends building it). Measure it **SCI-for-AI / ISO 21031 conformant** with an **open, auditable methodology** — the trust differentiator vs black-box calculators, and the one a proprietary platform can't expose but an open tool can.

**The recommended hackathon MVP:** an **independent "carbon beside cost + optimization for AI" product** (codename **TRACE**), demoed on *synthetic client* cloud-billing + LLM-usage data — with a **CAST-like "which apps are inefficient" scan** as the attention-grabber and **AI:works shown as client-zero proof** (before/after a modernization). This is *more* sellable than an AI:works-embedded module and directly answers the judges' "can you actually sell this?".

**Why it wins as a *service* (not advisory):** packaged, tool-backed, and **repeatable across any client** — regardless of whether they ever touch AI:works; produces a per-engagement **auditable carbon ledger + savings recommendations**; and underwrites **carbon-linked gain-share pricing** no peer publicly offers.

---

## 2. Market evaluation

### 2.1 Where the bar is moving
- **Reporting → decision/action.** AI is what turns sustainability software from a reporting tool into an *operational system*: recommendations, what-if/scenario modeling, and sustainability embedded in procurement/ops workflows. "Actionability beyond reporting" is a top buyer demand.
- **Toward finance-grade / audit-grade data.** Buyers now scrutinize the *integrity of the underlying data process*, not just the reported number — controls, traceability, anomaly detection, evidence lineage. Auditability is becoming a maturity marker even in IT carbon tools.
- **Productized, tool-led, repeatable — not bespoke advisory.** "The market increasingly rewards services that are packaged, tool-backed, and repeatable." But *tooling alone is insufficient — integration is the real product* (connectors, pipelines, operating model, adoption).

### 2.2 Biggest drivers of client *spend* (now and next)
1. **Dual-outcome cost + carbon** ("one action, two wins"): cloud/AI efficiency, right-sizing, idle elimination — *"sustainability survives when it behaves like operational excellence."*
2. **Short-term ROI / cost takeout** — the dominant filter in NA; the AI energy *cost* shock makes this urgent.
3. **Regulatory readiness** — strongest, most durable in EU/APAC; softening in US.
4. **Risk / resilience** — climate risk now extends to physical risk to IT assets (extreme heat on data centres), converging with BCP.
5. **AI as a monetizable value-add** — buyers pay an AI premium *only* when tied to measurable efficiency/speed/ROI.

ACV signal from the analysis: enterprise platform deals typically **$75K–$150K**, complex/Scope-3 **$250K–$1M+**; buyers accept higher ACVs when **pricing scales with scope/value, not seats.**

### 2.3 Disruptors (the forces to ride)
- **AI energy shock** *(confirmed externally: IEA — AI DC consumption +~50% in 2025; data-centre demand doubling by 2030, AI-specific tripling; Microsoft energy +168% since 2020).* This is the durable narrative.
- **Built-in / enterprise-suite sustainability** displacing bolt-on point tools (buyer fatigue with fragmented tools → consolidation).
- **Productization / tool-led services** replacing bespoke advisory.
- **Climate risk + physical resilience** as a new buying trigger.
- **Assurance/auditors shaping acceptable methods** — proof and governance win.

### 2.4 The credibility bar: standards
- **SCI (Software Carbon Intensity) = ISO/IEC 21031:2024**, the anchor standard. `SCI = (O + M)/R` — a *rate* per functional unit (API call, user, ML training run…); location-based; **offsets can't reduce the score, only real elimination**.
- **SCI for AI** extends it across the AI lifecycle; ratified Q4 2024, ISO-readiness Q1 2026, ISO submission Q2 2026; built by 100+ orgs (Accenture chairs; Google, Microsoft, IBM). GSF explicitly links it to **EU AI Act** environmental compliance.
- **Implication:** any TW product should be **SCI-for-AI-conformant by design** — and TW's **GSF-founder status is an underused trust asset** to lead with.

### 2.5 Regulatory nuance (don't over-anchor on compliance)
- **EU:** CSRD in force but the **Omnibus simplification (Mar 2026)** cut in-scope companies ~80%.
- **US:** SEC climate rule paused; **California SB 253** (Scope 1+2 by Aug 2026) still live; SB 261 enjoined.
- **APAC:** *hardening* — ISSB convergence (Singapore, Japan SSBJ, Australia phased from Jan 2025).
- **Takeaway:** regulation is **softening in EU/US, hardening in APAC** → anchor the value prop on **AI-energy cost + risk + brand/efficiency**, with compliance as a *secondary, region-dependent* driver.

---

## 3. Thoughtworks + AI:works + CCF fit

### 3.1 TW direction (FY26+)
- **Private since Nov 2024** (Apax, $1.75B) → thesis of **margin expansion via AI-led delivery leverage** (more software output per consultant). Last hard financials: FY2023 $1.16B (+19%).
- Core 2026 frame: **AI-First Software Delivery (AIFSD)** — generative/agentic systems across the full SDLC. *Looking Glass 2026*'s five lenses (AI & delivery, rewiring for agents, evolving interactions, data ecosystems, responsible foundations) **omit sustainability entirely** — the white space.
- Stated ambition (internal): **~50% of revenue from data & AI by 2029**; commercial shift from rate-cards to **solution/output-based selling** with value-sharing.

### 3.2 AI:works (the flagship)
- **Launched 20 Jan 2026**; targets **legacy modernization** in messy hybrid estates. Six components incl. the **Control Plane** (orchestrates agents with **cost transparency, guardrails, compliance tracking, spend/anomaly detection, consumption billing**). **3-3-3** delivery (3 days concept / 3 weeks prototype / 3 months production MVP).
- Internally framed as **"how we sell & deliver, not what we sell"** — *not* yet licensed to clients (IP-protection guardrail). No public pricing; client sandbox not yet available (GA ~mid-2026).
- **Strategic hook:** the Control Plane already meters per-agent **cost** → carbon telemetry is a natural, low-friction extension on existing plumbing, **not** a bolt-on.

### 3.3 CCF (the asset to evolve)
- Open-source; converts **AWS/GCP** usage → energy + carbon, surfaced **alongside cost**, with a regional carbon-intensity map and a **read-only FinOps recommendation engine**. Includes embodied/Scope-3 hardware emissions (now via **Boavizta** APIs).
- **Revived to baseline** (deps, methodology refresh) by a team that has since moved on — **no active dev resource**; known **performance** limits (slow loads).
- **Does not yet measure AI inference** — but that's the explicit roadmap ("Evolve CCF"): take **token-usage data × a carbon-intensity coefficient** (lean on GSF SCI-for-AI), target early AI footprint detection ~Q4 2026. Documented intent to embed into **AI:works** + EMPC/DAMO offerings.

### 3.4 Asset synergy & gaps
- **Synergy:** Control Plane = the socket (token cost/usage); CCF = the open, auditable measurement + recommendation DNA; TW = GSF credibility + modernization delivery. CCF's **open methodology inside AI:works' proprietary platform** gives clients defensible CSRD/audit numbers without exposing AI:works IP.
- **Gaps:** AI-inference measurement not built yet; **Control Plane cost data is internal-only** (a client-facing data path is unresolved); no CCF dev resource; Azure/multi-cloud and **Circular IT / Scope-3 depth** under-served; commercial model (free feature vs paid add-on) undecided.

---

## 4. Positioning & proof story

**Lead narrative (exec messaging):** *"AI is the new forcing function: it drives energy → cost → the need to measure and control. Thoughtworks — which co-founded the Green Software Foundation and created Cloud Carbon Footprint — is the partner that makes your AI build **measurably** efficient, with an **open, auditable** method, inside the very platform that delivers your software."*

**The "Green AI operating model" = measurement + governance + optimization**, with concrete artifacts:
- **Measurement:** per-token/per-workload/per-agent carbon, SCI-for-AI conformant.
- **Governance:** an auditable carbon ledger with evidence lineage (transparent open methodology).
- **Optimization:** recommendations that quantify cost *and* carbon (model/region/scheduling trade-offs).

**Transparency contrast:** explicitly position TW's *open, integrated software + services + transparent commercials* against opaque/fragmented competitor pricing and black-box AI-carbon calculators.

**Proof beats messaging:** standards participation (GSF/SCI-for-AI), **measurable client outcomes** (before/after modernization), and **tool-backed methodology** — the three things the analysis says the innovation bar now demands.

---

## 5. Idea catalog

Each idea: problem → what it does → CCF + AI:works use → productization/pricing → proof artifact → demo concept.

**I1 — Carbon Control Plane for AI:works** *(carbon beside cost + optimization recs).*
AI carbon is invisible. Add a carbon view to the Control Plane: per-agent/workflow gCO₂e (SCI-for-AI), and **optimization recommendations** ("route this step Opus→Haiku: −68% cost, −71% gCO₂e, negligible quality delta"). *CCF* = methodology + recommendation engine; *AI:works* = token/cost telemetry. **Packaged module**, priced as add-on or bundled; underwrites gain-share. Proof: per-engagement carbon ledger. Demo: live Control Plane mock with a Carbon tab + a recommendation that moves both numbers.

**I2 — Green SDLC / Energy-Debt Detection** *(green code in modernization).*
AI-assisted code/static analysis flags "energy debt"/leaks; SDLC-embedded sustainability KPIs + enforcement gates; before/after green-code report. Competes with TechM Green CodeRefiner & CAST but **carbon-native + tied to AI:works modernization**. Harder to build credibly in a hackathon.

**I3 — Unified GreenOps+FinOps control plane (cloud *and* AI).**
Extend CCF to unify cloud carbon + AI-inference carbon with cost; carbon-aware region/model/vendor decisions. Strong, but broader scope = more to build for a demo.

**I4 — Carbon-linked outcome pricing + maturity bundles** *(commercial wrapper).*
Productize **Baseline / Optimize / Transform** bundles on existing pricing; flagship **carbon-linked / net-neutral / gain-share** contracts powered by CCF measurement. Genuine white space (no peer publicly offers gain-share on carbon) — but it's a *commercial model*, not a buildable tool demo on its own.

**I5 — SCI-for-AI auditable attestation ledger** *(proof layer).*
An auditable, transparent per-engagement carbon ledger with evidence lineage — open method inside the proprietary platform; CSRD/EU-AI-Act-ready. Strongest on proof/credibility/differentiation; needs I1's telemetry to be tangible.

**I6 — Modernization before/after carbon story generator.**
Quantify legacy-app emissions vs AI:works-rebuilt app: cost + carbon reduction as a reusable **sales proof artifact** that justifies premium/outcome pricing. Excellent demo + business-impact; pairs naturally with I1.

**I7 — Circular IT / Scope-3 extension.**
Addresses TW's gap, but doesn't fit the AI:works/CCF AI-inference focus; weak hackathon fit.

**I8 — Carbon-aware agent orchestration** *(auto-routing).*
Control Plane auto-routes agent workloads to lower-carbon models/regions/times. High innovation/differentiation; hard to build for real in a hackathon (mock only).

---

## 6. Ranked shortlist

Scores 1–5 per criterion. Weights: Strategic fit ×3 · Market pull ×3 · Productization ×3 · Proof/credibility ×2 · Outcome-pricing ×2 · Differentiation ×2 · MVP feasibility ×3. Max = 90.

| Rank | Idea | SF×3 | MP×3 | Prod×3 | Proof×2 | Price×2 | Diff×2 | Feas×3 | **Total** |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **I1 Carbon Control Plane (+optimization)** | 5 | 5 | 5 | 4 | 4 | 4 | 5 | **84** |
| 2 | I3 Unified GreenOps+FinOps (cloud+AI) | 5 | 5 | 5 | 4 | 4 | 3 | 3 | 76 |
| 3 | I6 Modernization before/after story | 5 | 4 | 4 | 4 | 4 | 4 | 4 | 75 |
| 4 | I5 SCI-for-AI auditable ledger | 5 | 4 | 4 | 5 | 3 | 5 | 3 | 74 |
| 5 | I8 Carbon-aware agent orchestration | 5 | 5 | 4 | 3 | 3 | 5 | 2 | 70 |
| 6 | I2 Green SDLC / energy-debt | 4 | 4 | 4 | 4 | 3 | 3 | 3 | 65 |
| 6 | I4 Carbon-linked outcome pricing | 4 | 4 | 3 | 3 | 5 | 5 | 2 | 65 |
| 8 | I7 Circular IT / Scope-3 | 2 | 3 | 3 | 3 | 2 | 3 | 2 | 46 |

**Read (raw scores):** I1 leads on the rubric as written.

**Read (v2 re-weight — the decisive correction):** I1 is **AI:works-embedded**, so it fails the hard constraint *we cannot sell AI:works to clients*. Re-weighting **Productization** for true sellable independence collapses I1's score and elevates the **independent product**. The lead recommendation is now a **standalone tool fusing I3 (unified cloud+AI GreenOps) + I5 (auditable SCI-for-AI ledger) + I2 (CAST-like energy-debt scan) + I6 (before/after proof)** — none of which require the client to own AI:works. **I1 is demoted to a *client-zero proof* supporting role.** See §7.

---

## 7. Recommended hackathon MVP — the independent product

### Concept
**TRACE — "carbon beside cost + optimization for AI."** A standalone, CCF-lineage product the **client buys and keeps**. It ingests the client's own usage data, shows **carbon next to cost** for their **cloud *and* AI inference**, and recommends optimizations that cut both. It does **not** require the client to own or use AI:works. *(Backronym: Token-level Realtime AI Carbon Estimation.)*

### Two carbons — be crisp about which we sell
- **Build-time carbon/cost** = the AI credits/energy TW spends *while building* the software (what the AI:works Control Plane meters). Weak client story — it's our delivery cost.
- **Run-time carbon/cost** = the *delivered application's* ongoing footprint in production (its cloud bill + its own AI-feature inference). **This is what the client pays for forever — anchor the product here.**

### The three-layer product (resolves "we can't sell AI:works")
1. **Assess** *(CAST-like, optionally via AI:works ingest/reverse-engineering)* — scan the client estate, rank apps by **energy debt** + estimated cost/carbon, prioritize what to fix.
2. **Build green** *(Green CodeRefiner-like, via AI:works)* — TW modernizes/builds the priority apps more efficiently. **AI:works lives here — as our engine, not their purchase.**
3. **Prove & manage** *(CCF-like, the **independent product**)* — measure run-time cost + carbon, before/after, ongoing; recommend optimizations; the **auditable dashboard the client buys and keeps**.

**Sellable product = layers 1 + 3** (no AI:works dependency). **AI:works = layer 2** (client zero + accelerator). We sell the outcome + the proof.

### Feasibility & what the client must provide
The product is **CCF extended from cloud to AI inference** — same proven pattern (ingest usage → apply coefficients → dashboard + recs). **Verdict: high feasibility for an MVP** built on provider usage exports + public coefficients.

| What it measures | Client provides | Feasibility |
|---|---|---|
| Cloud infra cost + carbon | Cloud billing exports — AWS CUR (S3), GCP billing→BigQuery, Azure cost export | **High** — CCF already does this |
| AI inference cost + carbon (totals) | LLM usage/billing exports — OpenAI/Anthropic console, AWS Bedrock invocation logs, GCP Vertex usage (tokens per model) | **High** |
| Per-app / per-team attribution | AI **gateway/proxy logs** (LiteLLM, Portkey, Cloudflare AI Gateway…) — per-request tokens + model + tags; or cost-allocation tags | **Medium** — if absent, recommending a gateway is itself a consulting hook |
| Self-hosted / fine-tuned models | GPU instance-hours (billing) or utilization telemetry (Prometheus/DCGM, nvidia-smi); training-job logs | **Medium** |
| "Which apps are inefficient" (Assess) | Repo/source access + ideally runtime telemetry (APM, cloud usage) to ground static findings | **Medium** — static energy is approximate; fuse static heuristics + runtime data |

**TW supplies the coefficients, not the client:** energy-per-token by model (public benchmarks — ML.Energy, SCI-for-AI; estimates for closed models), grid carbon intensity by region (Electricity Maps), PUE. The open, transparent methodology **is** the differentiator. **Floor to deliver value: cloud billing export + LLM usage export.** Honest caveat — closed-model coefficients are estimates; disclose openly (transparency is the sell).

### Why this scores against the judging rubric
*(Innovation 30 / Tech feasibility 20 / Business impact 20 / Demo & storytelling 20 / Responsible AI 10)*
- **Innovation (the team's risk):** the *independent SCI-for-AI product + CAST-like energy-debt scan + carbon-aware optimization* is well beyond "carbon next to cost." It's a sellable Green AI operating model.
- **Tech feasibility:** reuses CCF's proven ingest→coefficient→recommend pattern; runs on public coefficients + synthetic client exports. Credible.
- **Business impact:** dual cost+carbon outcome, **sellable to any client** (not gated on AI:works), premium/gain-share pricing, board-level AI-energy concern.
- **Demo & storytelling:** ingest a client export → "watch cost and carbon side by side" → apply a rec → both drop → before/after client-zero proof.
- **Responsible AI:** transparent, auditable, standards-aligned, no offsets-washing.

### Demo narrative (≤5 min)
Hook (AI energy shock; the client's invisible AI carbon + cost) → upload a **synthetic client** LLM-usage + cloud-billing export → dashboard shows **cost beside carbon** per app/model/region → **Assess** view ranks the client's most inefficient apps (energy debt) → apply an **optimization rec** (e.g. route a summarization step Opus→Haiku, or shift region): **both numbers drop live** → **client-zero proof**: AI:works before/after on a modernization → close on the commercial model (Baseline/Optimize/Transform + carbon-linked gain-share) and the roadmap to wire CCF's AI-inference engine in for real.

### Synthetic data needed (all illustrative — no real client data)
- A fabricated **client LLM-usage export** (tokens per model/app/region/time) + a fabricated **cloud-billing export**.
- Model **energy-per-token** coefficients from *public* benchmarks (ML.Energy, SCI-for-AI, Greenpixie-style figures).
- **Grid carbon intensity** by region (public Electricity Maps averages).
- A legacy-vs-modernized app profile for the before/after.

### Build approach (PM/non-technical-friendly)
Vibe-coded front-end that **ingests a small synthetic client export** and renders cost-beside-carbon + an Assess ranking + a scripted optimization interaction, over a transparent coefficient table. Show *how it plugs into real client data*, backed by a credible technical roadmap. Ship a plain-English methodology one-pager (SCI-for-AI = energy × grid intensity, per token). See the deeper feasibility write-up in `docs/research/feasibility-ai-carbon-product.md`.

---

## 8. Assumptions & open questions

### Assumptions (stated; challenge any)
- **A1.** Audience = you, for evaluation; goal is a *credible demo + pitch + roadmap*, not a production build. *(high)*
- **A2.** AI:works Control Plane meters per-agent token **cost** and could expose token **usage** — the input carbon estimation needs. *(high — confirmed in docs/public)*
- **A3.** SCI-for-AI is the methodology to align to; precise coefficients can be approximated from public benchmarks for the demo. *(high)*
- **A4.** No real AI:works sandbox/client data is available in the hackathon window → mock/synthetic only. *(high)*
- **A5.** Target buyer = enterprise modernization clients already buying (or piloting) AI:works; secondary = TW as "client zero." *(med)*
- **A6.** Primary value anchor = AI-energy **cost + risk + efficiency**, with compliance secondary/region-dependent. *(med-high)*
- **A7.** CCF can be *positioned* as the engine even without new dev resource in the hackathon. *(med)*

### Open questions (answers that would most change the recommendation)
> **v2 note:** the pivot to an **independent product** resolves the two biggest original questions — the client supplies *their own* cloud/LLM data (Q1), and AI:works is *not* sold to clients (Q2). They remain listed as assumptions to confirm with stakeholders.
1. *(largely resolved)* **Data source for the client-facing AI carbon number** — now: the **client's own** cloud-billing + LLM-usage exports (see §7 table), not the internal Control Plane. Confirm clients can/will share these and at what granularity (gateway vs totals).
2. *(largely resolved)* **Commercial intent for AI:works** — now: AI:works stays internal (client zero + accelerator); the sellable thing is the independent product. Confirm exec alignment on this split.
3. **Gain-share appetite** — is TW willing to put price at risk on measured carbon outcomes, or is "outcome-linked narrative" enough for now?
4. **Coefficient rigor for the demo** — is approximate-but-transparent acceptable, or do judges/stakeholders expect defensible SCI-for-AI numbers?
5. **Scope ambition** — AI-inference carbon only (focused, feasible) vs. unified cloud+AI GreenOps (broader, stronger strategically, heavier to build)?
6. **Circular IT / Scope-3** — worth a nod for completeness, or explicitly out of scope for this MVP?

---

## 9. Risks & mitigations

| Risk | Mitigation |
|---|---|
| **"Carbon next to cost" reads as obvious** (innovation score) | Lead with *optimization that moves both numbers* + open-method-in-proprietary-platform + gain-share pricing; frame as a *Green AI operating model*, not a dashboard. |
| **AI:works inaccessible / no sandbox** | Build a faithful *mock*; ship a credible integration **roadmap**; position as "how it plugs in," not a live integration. |
| **Methodology credibility challenged** | Anchor explicitly to **SCI-for-AI / ISO 21031**; transparent coefficient table; lead with TW's GSF-founder status. |
| **Data-ownership / audit mismatch** (internal-only cost data) | Surface as the #1 open question; propose a client-billing-data path (as CCF does for cloud). |
| **Regulatory tailwind softening (EU/US)** | Anchor value on cost/risk/efficiency, not compliance; treat compliance as APAC-led upside. |
| **No CCF dev resource** | Hackathon is the awareness/championing vehicle; deliverable feeds the exec buy-in + AI:works roadmap effort already underway. |
| **CCF performance / Boavizta volatility** | Out of demo scope; note in roadmap; demo runs on a small curated synthetic set. |

---

*Next actions if you greenlight: (a) ✅ feasibility one-pager → `docs/research/feasibility-ai-carbon-product.md`; (b) turn §7 into `docs/prd/trace-prd.md`; (c) draft the ≤5-min demo script in `docs/demo/`; (d) spec the synthetic client export + coefficient table in `docs/sample-data/`.*
