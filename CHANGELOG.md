# CHANGELOG — TRACE decision log

A running log of meaningful decisions for the TRACE project. Newest first.
Format: `## YYYY-MM-DD` → `- **Decision** — why / context.`

After any notable decision (scope, architecture, tooling, naming), add an entry here.

## 2026-06-10

- **Generated the synthetic data package + demo script** — `docs/sample-data/` now has a deterministic
  `generate.py` (seed 42) producing Langfuse-shaped `llm_usage.csv`, CCF-shaped `cloud_usage.csv`,
  plus `model_coefficients.csv` / `grid_intensity.csv`, hand-authored `recommendations.json` (with
  precomputed expected results) and a sample `semgrep_findings.json` for the Assess layer. Verified
  the seeded wow-moment: Support-Bot ≈ 76% of AI carbon / 77% of cost; the right-sizing rec cuts total
  AI carbon ≈ −49% and cost ≈ −52%. Wrote the ≤5-min `docs/demo/demo-script.md`. _Why: pre-baking data
  removes a build block and spends zero AI credits; the demo script makes the story repeatable._
- **Evaluated an OSS stack + wrote MVP PRD v2** (`docs/prd/hackathon-mvp-prd-v2.md`, supersedes v1).
  Decision: reuse mature open-source tools (CCF, Langfuse, LiteLLM, SCI-for-AI, OpenTelemetry GenAI,
  Semgrep) by **adopting their data shapes and showing the integration path — not hosting/integrating
  them live** during the 6-hour build (which would cost more time + credits, not less). Decided build
  stack: **Streamlit + pandas (+ optional DuckDB) + a custom TRACE calculator + synthetic CSVs shaped
  on Langfuse/CCF/SCI**. Cut Trivy; demoted LiteLLM/OTel/Trivy to roadmap-slide only. _Why: spend the
  fewest AI credits by writing only the unique carbon-for-AI logic and reusing everything else as
  schema/lineage._
- **Wrote two PRDs** — the full product PRD (`docs/prd/trace-prd.md`, derived from strategy §7) and
  a ruthlessly-scoped **6-hour hackathon MVP PRD** (`docs/prd/hackathon-mvp-prd.md`): a single-screen,
  no-backend dashboard ingesting synthetic client data, showing carbon beside cost + an
  apply-a-recommendation interaction, with an hour-by-hour plan, synthetic data spec + coefficient
  table, acceptance criteria, and demo beats. _Why: convert the strategy into something buildable and
  demoable in one sitting for Round 1 (due 2026-06-12)._
- **Pivoted the strategy to an independent, sellable product** (v2 of the strategy doc) and added a
  feasibility one-pager → `docs/research/feasibility-ai-carbon-product.md`. _Why: TW cannot license
  AI:works to clients, so the AI:works-embedded recommendation wasn't sellable._ The lead product is
  now a standalone CCF-lineage tool (carbon beside cost + optimization + CAST-like energy-debt scan)
  the client buys and keeps; AI:works is repositioned as "client zero" + a build accelerator. Anchored
  on **run-time** carbon (the delivered app's footprint), not build-time. Documented exactly what the
  client must provide (cloud billing + LLM usage exports; gateway logs for per-app granularity) and
  what's real vs. estimated. Feasibility verdict: **high for an MVP**.
- **Ran the sustainability strategy analysis** → `docs/strategy/sustainability-strategy-analysis.md`.
  Synthesized the IT sustainability market analysis, AI:works + CCF docs, and team intent
  (local, PII-free) with public research on TW's FY26 direction (Looking Glass 2026, AI:works
  launch) and competitors (TechM Green CodeRefiner, CAST, Greenspector, Greenpixie). Scored 8
  ideas against a weighted rubric. **Recommendation: "Carbon Control Plane for AI:works"** —
  carbon beside cost in the Control Plane + optimization recommendations + modernization
  before/after, SCI-for-AI conformant. _Why: closes the gap that TW's FY26 AI narrative omits
  sustainability despite being a GSF founder + CCF originator; rides the AI-energy-shock
  narrative; tool-led, repeatable, gain-share-able._
- **Established PM doc structure** — added `CLAUDE.md` (onboarding), this `CHANGELOG.md`,
  and a `docs/` tree (prd, architecture, demo, assumptions, sample-data, research, notes),
  following the "Claude Code for PMs" workshop style. _Why: give Claude and teammates a
  consistent, referenceable structure._
- **Retired the interim `hackathon/` folder and `HACKATHON.md`** — their content (publish
  workflow, remotes model) now lives in `CLAUDE.md`. _Why: one clean home, no duplication._
- **Organized & protected `TRACE_Documents/`** — reference library sorted into themed folders
  (hackathon-admin, ccf-product, aiworks-platform, gsf-greenops, market-research, governance,
  claude-code-workshop); most sensitive items quarantined in `_confidential/`. Added
  `/TRACE_Documents/` to `.gitignore`. _Why: keep confidential/PII reference material local —
  it must never reach git or the public fork._
- **Created private workspace `Concepcion-c/TRACE`** — seeded from the public CCF fork; wired
  remotes `origin` (private), `public` (fork = publish target), `upstream` (org). Commits use
  the GitHub noreply email to satisfy email-privacy protection. _Why: experiment privately,
  publish only the finished result to the public fork._
