# PRD: TRACE — carbon beside cost + optimization for AI

> **Status:** Draft v1 · **Owner:** Concepcion-c · **Last updated:** 2026-06-10
> Derived from `../strategy/sustainability-strategy-analysis.md` (§7, v2) and
> `../research/feasibility-ai-carbon-product.md`. This is the **full product** PRD.
> For the 6-hour hackathon build, see `./hackathon-mvp-prd.md`.

## 1. Problem statement
AI usage creates real **cost and carbon** that are largely **invisible** to the enterprises
buying it. Cloud carbon tools (incl. CCF) measure infrastructure, not **AI inference**. As the
**AI energy shock** drives data-centre demand up sharply, buyers are shifting from *"what's our
cloud carbon?"* to *"what's the carbon of our AI workloads, per app, and how do we cut it?"* —
and they want **finance-grade, auditable** answers tied to action, not another report.

Thoughtworks co-founded the Green Software Foundation and originated CCF, yet its flagship AI
story (AI:works, *Looking Glass 2026*) contains no sustainability narrative. There is no
sellable, tool-led TW product that closes this gap.

## 2. Goals & non-goals
**Goals**
- A **standalone, sellable product** (client buys and keeps) that shows **carbon next to cost**
  for a client's **cloud + AI inference**, ranks their most inefficient apps, and recommends
  optimizations that cut both.
- **SCI-for-AI / ISO 21031 conformant**, with an **open, auditable methodology**.
- **Repeatable across any client**, regardless of whether they use AI:works.
- Underwrites **outcome / carbon-linked pricing**.

**Non-goals**
- Not selling, exposing, or depending on AI:works (it is "client zero" + an internal accelerator).
- Not a bespoke advisory engagement; not a one-off report.
- Not (v1) Circular IT / hardware e-waste, deep Scope-3 supply chain, or Azure-first coverage.
- Not offset brokering — we measure and reduce; offsets don't reduce the SCI score.

## 3. Target users & personas
- **Primary buyer — VP Engineering / Platform / Cloud (or Head of FinOps):** owns the cloud + AI
  bill; wants cost down and a defensible carbon number. Pays when carbon rides on cost savings.
- **Sustainability / ESG lead:** needs auditable, standards-aligned data for disclosure (CSRD/
  ISSB/California), without black-box methodology.
- **Engineering teams:** need carbon at the same granularity/cadence they already see cost, or
  they won't act.
- **TW internal (client zero):** proves the product on TW's own AI:works delivery (before/after).

## 4. Success metrics
- **Client outcome:** measured % reduction in AI+cloud **cost and gCO₂e** after acting on
  recommendations (target: a credible double-digit % on at least one workload).
- **Adoption:** time-to-first-insight after data connect (target: < 1 day).
- **Trust:** methodology accepted by the client's audit/assurance function.
- **Commercial:** convertible into a priced bundle / gain-share; repeatable across ≥ N clients.

## 5. Proposed solution
A CCF-lineage tool that extends CCF's proven pipeline (*ingest usage → apply coefficients →
show cost+carbon → recommend fixes*) from cloud infrastructure to **AI inference**
(`tokens × energy-per-token × grid-carbon-intensity`). Three layers:

1. **Assess** *(CAST-like; optionally via AI:works ingest)* — rank apps by **energy debt** +
   estimated cost/carbon; prioritize what to fix.
2. **Build green** *(via AI:works — internal accelerator)* — TW builds/modernizes the priority
   apps more efficiently; benefit proven by this product.
3. **Prove & manage** *(the product the client keeps)* — measure run-time cost + carbon,
   before/after, ongoing; recommend optimizations; auditable SCI-for-AI ledger.

**Anchor on run-time carbon** (the delivered app's ongoing footprint), not build-time (TW's
delivery cost). See architecture in `../research/feasibility-ai-carbon-product.md` §4.

## 6. User stories / requirements
- As a **platform lead**, I connect cloud billing + LLM usage and see **cost beside carbon**
  sliced by app / model / region / team / time.
- As a **platform lead**, I receive **optimization recommendations** (right-size model, cache,
  batch, shift region/time, kill idle) each quantifying **$ and gCO₂e** saved.
- As an **ESG lead**, I export an **auditable SCI-for-AI ledger** with evidence lineage and a
  versioned coefficient table.
- As an **engineer**, I see the **most inefficient apps** ranked by energy debt + cost/carbon.
- As a **TW seller**, I show a **before/after** proof from a real (client-zero) modernization.

**Functional requirements**
- Ingest: cloud billing exports (AWS CUR, GCP BigQuery, Azure); LLM usage (OpenAI/Anthropic/
  Bedrock/Vertex); optional AI gateway logs + cost-allocation tags; optional repo/runtime
  telemetry (Assess).
- Compute: transparent coefficients (energy/token by model, grid intensity by region, PUE,
  embodied via Boavizta); SCI-for-AI `SCI=(O+M)/R`, location-based, no offsets.
- Present: cost+carbon dashboard with drill-down; recommendation engine; auditable export.

**Non-functional**
- Open/versioned methodology; deployable SaaS or in-client-tenant; performance acceptable on
  large billing sets (CCF's slow-load issue is a known constraint to fix).

## 7. Data & client inputs
**Floor to deliver value:** client's **cloud billing export + LLM usage export.**
Per-app granularity needs **AI gateway logs** or good cost tags. Self-hosted models need GPU
instance-hours or utilization telemetry. **TW supplies coefficients**, not the client. Full
detail + ease ratings in `../research/feasibility-ai-carbon-product.md` §1.

## 8. Pricing / commercial model
- **Maturity bundles** on top of existing pricing: **Baseline** (measure) / **Optimize**
  (recommend + implement) / **Transform** (embed + govern).
- **Carbon-linked / gain-share** option tied to measured cost+carbon savings (white space —
  no peer publicly offers this).
- Transparency contrast: open methodology + integrated software+services vs opaque competitors.

## 9. Scope for the hackathon (MVP)
See `./hackathon-mvp-prd.md` — a 6-hour, demoable slice of **layer 3** (Prove & manage) on
synthetic client data, plus a lightweight Assess view and a client-zero before/after.

## 10. Assumptions & open questions
See `../strategy/sustainability-strategy-analysis.md` §8 and
`../research/feasibility-ai-carbon-product.md` §7. Key opens: gateway prevalence (per-app
feasibility), deployment model (SaaS vs in-tenant), coefficient maintenance ownership.

## 11. Risks
Closed-model coefficients are estimates (disclose, cite, show ranges); weak per-app attribution
without a gateway; static energy-debt is directional; regulatory tailwind softening in EU/US
(anchor on cost/risk, not compliance). Mitigations in the feasibility doc §6.
