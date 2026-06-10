# PRD: TRACE — 6-hour Hackathon MVP

> **⚠️ SUPERSEDED by `./hackathon-mvp-prd-v2.md`** (open-source-tool-leveraged stack). Kept for history.

> **Status:** Draft v1 (superseded) · **Owner:** Concepcion-c · **Last updated:** 2026-06-10
> Scoped slice of `./trace-prd.md` for a **single ~6-hour build**. Optimized for a
> **≤5-min video demo** + the written form (Round 1 due 2026-06-12). PM / semi-technical
> friendly. No real client or AI:works data — **synthetic only**.

## 1. The one-sentence MVP
A working, single-screen web dashboard that ingests a **synthetic client AI-usage + cloud
export** and shows **carbon beside cost** per app/model/region, then lets you **apply an
optimization recommendation** and watch **both numbers drop live** — with a transparent,
SCI-for-AI methodology footnote.

## 2. Why this is the right 6-hour slice
- It demos the **core value** (cost+carbon together + actionable optimization) in one screen.
- It's the **sellable layer** (layer 3, independent of AI:works) → answers "can you sell this?".
- It's **buildable**: static front-end + pre-baked synthetic data + a simple coefficient table.
  No backend, no integrations, no live AI:works = no demo-day risk.
- Hits the judging rubric: Innovation (optimization + open method), Tech feasibility (credible
  pattern), Business impact (sellable, dual outcome), Demo (one "watch both drop" moment),
  Responsible AI (transparent, auditable, no offset-washing).

## 3. In scope (MUST — the demoable core)
- **M1. Dashboard screen** — hero KPIs: total **cost ($)** and **carbon (gCO₂e)** for the
  period, side by side.
- **M2. Breakdown** — a table/bars of cost + carbon by **app**, with model + region shown.
- **M3. Coefficient transparency** — a visible, plain-English methodology note + the coefficient
  table used (`carbon = tokens × energy/token × grid intensity`).
- **M4. Optimization recommendation** — at least one concrete rec (e.g. "route Support-Bot's
  summarization Opus-class → Haiku-class, shift ap-south → us-west"); an **Apply** button that
  recomputes and **animates both totals dropping**, showing **% cost and % carbon saved**.

## 4. Stretch (SHOULD — only if core is done early)
- **S1. Assess view** — rank apps by an "energy debt / intensity" score (carbon per 1K requests),
  flag the worst offender.
- **S2. Before/after toggle** — a "client-zero" legacy-vs-modernized comparison panel.
- **S3. Region/time carbon-aware hint** — show grid intensity by region to motivate a shift.

## 5. Explicitly OUT of scope (for the 6 hours)
Real data ingestion/connectors; live AI:works/Control-Plane integration; auth/multi-tenant;
self-hosted GPU telemetry; Boavizta/embodied; Azure; persistence/database; CAST-style real
static code analysis (Assess uses pre-scored synthetic data). These live in the roadmap slide.

## 6. Recommended build approach (fastest reliable path)
- **Single-page app, no backend.** Either a **single self-contained `index.html`** (HTML + JS +
  a light chart lib) or a minimal **Vite + React** app. Data is a **pre-baked JSON/CSV** bundled
  in — "ingest" is reading that file (optionally a fake "Upload export" button that loads it).
- **All math client-side** from a transparent coefficient table (below).
- **Vibe-code it** with an AI coding tool; keep one screen; style to read like a CCF / control-
  plane dashboard. Robustness for the *recording* beats feature count.
- Build in `~/projects/TRACE` (e.g. a `mvp/` or `packages/` subfolder); synthetic data spec
  belongs in `../sample-data/`.

## 7. Synthetic data spec (illustrative; derive from public benchmarks — label as synthetic)
**Apps (5):** Support-Bot, Doc-Summarizer, Code-Assistant, Search-RAG, Analytics-Agent.
**Models (cost $/1M tokens, energy kWh/1M tokens) — blended, illustrative:**
| Model class | $/1M tok | kWh/1M tok |
|---|---|---|
| Large ("Opus-class") | 30 | 1.2 |
| Mid ("Sonnet-class") | 6 | 0.6 |
| Small ("Haiku-class") | 1 | 0.3 |

**Regions (grid intensity gCO₂e/kWh — public Electricity Maps-style):**
us-west ≈ 210 · eu-west(Ireland) ≈ 290 · us-east ≈ 380 · ap-south ≈ 630.

**Formula:** `carbon_g = tokens_millions × kWh_per_million × grid_gPerkWh` ·
`cost_$ = tokens_millions × $_per_million`.

**Seed rows:** give each app a model, region, and monthly token volume so totals look real
(e.g. Support-Bot: Large, ap-south, 800M tokens → high cost *and* high carbon = the obvious
optimization target). Keep ~5–8 rows. Include one "before/after" pair for S2.

## 8. Acceptance criteria
- Open the app → hero **cost + carbon** render from the synthetic data. *(M1)*
- Per-app breakdown shows model + region and both metrics. *(M2)*
- Methodology + coefficient table visible on screen. *(M3)*
- Clicking **Apply** on the recommendation updates totals and shows **% saved on both**. *(M4)*
- Runs in a browser with no network/backend; reproducible for recording.

## 9. Hour-by-hour plan (~6h, single builder)
| Time | Task | Output |
|---|---|---|
| 0:00–0:30 | Scaffold app (index.html or Vite/React); repo subfolder | App opens, "hello" renders |
| 0:30–1:30 | Synthetic dataset + coefficient table + calc function | `carbon`/`cost` computed correctly |
| 1:30–3:00 | Dashboard: hero KPIs + per-app breakdown | M1, M2 done |
| 3:00–4:00 | Recommendation + **Apply** (recompute + animated deltas) | M4 done |
| 4:00–5:00 | Methodology note, branding, hero copy, polish | M3 + demo-ready look |
| 5:00–6:00 | Record ≤5-min demo + draft written form; buffer | Submission assets |
*(If ahead at 4:00, slot S1 Assess view before polish.)*

## 10. Demo beats (maps to `../demo/`)
Hook (AI energy shock; invisible AI cost+carbon) → "upload" synthetic client export → cost
**beside** carbon → point at the worst app → **Apply** the recommendation → **both numbers drop
live** (% saved) → methodology = open + SCI-for-AI → 10-sec roadmap (real ingest, AI:works as
client zero, gain-share pricing). One screen, one wow moment.

## 11. Risks (build-day)
| Risk | Mitigation |
|---|---|
| Scope creep | M1–M4 only; stretch strictly after core; out-of-scope list is law |
| Live-tool flakiness | Static app + bundled data; nothing depends on the network |
| Numbers look fake/too precise | Label synthetic; show ranges; cite public coefficient sources |
| "Obvious" critique | Lead the demo with **optimization that moves both numbers** + open method, not just display |
| Time lost to styling | Use a component/CSS kit; one screen; copy the CCF/control-plane look |

## 12. Definition of done
A browser-openable dashboard meeting all §8 acceptance criteria, a recorded ≤5-min demo, and a
drafted written submission — committed to `~/projects/TRACE` (private).
