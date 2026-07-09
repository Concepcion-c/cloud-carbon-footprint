# Demo script — RECPT (≤5 min video, Round 1)

> **Status:** Draft v1 · **Last updated:** 2026-06-10
> For the MVP in `../prd/hackathon-mvp-prd-v2.md`, on the synthetic data in `../sample-data/`.
> Target: ≤5:00. One screen, one wow moment. Numbers below are pre-verified from the dataset.

## One-liner
**RECPT — carbon beside cost for cloud + AI, with optimizations that cut both. CCF, evolved for
the AI era. A tool clients buy and keep.**

## Setup before recording
- `streamlit run app.py` with the synthetic CSVs loaded; full-screen browser.
- Have the recommendation ready to click. Practice once so the "both numbers drop" lands clean.

## Beat sheet (target times)

**0:00–0:30 — Hook (the AI energy shock).**
> "AI data-centre electricity use jumped ~50% in 2025. Every token your agents burn has a cost
> *and* a carbon footprint — and today that carbon is invisible. Cloud carbon tools, including
> the one Thoughtworks open-sourced, CCF, measure infrastructure — not AI inference. RECPT closes
> that gap."

**0:30–1:00 — Load a client export (reuse, not rebuild).**
- Click "Upload client export" → loads the synthetic Langfuse-style LLM usage + CCF-style cloud usage.
> "RECPT ingests what clients already have — LLM usage from a gateway like LiteLLM or an
> observability tool like Langfuse, and cloud billing the way CCF does. No new instrumentation."

**1:00–1:45 — Cost beside carbon.**
- Show hero KPIs: **~$31.3k AI cost · ~794 kg AI carbon** (plus the cloud tab if built).
- Show the per-app / per-model / per-region breakdown.
> "Here's the month: cost and carbon, side by side, by app, model, and region. One app jumps out —
> **Support-Bot is ~76% of our AI carbon and ~77% of the cost**: a large model, high volume, running
> in ap-south, one of the dirtiest grids."

**1:45–2:30 — Assess: which app to fix first.**
- Show the Assess ranking (carbon + Semgrep code-risk). Support-Bot on top.
> "RECPT doesn't just measure — it ranks **energy debt**. It blends runtime carbon with a code scan
> (here, Semgrep) so you know *which app to modernize first* for the biggest cost-and-carbon return.
> That's the prioritization a consultancy can act on."

**2:30–3:30 — The wow moment: apply an optimization.**
- Click **Apply** on `rec-support-bot-rightsizing`.
- Totals animate down: **AI carbon −49% (794→406 kg), AI cost −52% ($31.3k→$15.1k).**
> "Route ~70% of Support-Bot's routine summarization to a small model and shift it to a cleaner grid —
> keep the hard 30% on the large model so quality holds. Watch both numbers drop: about **half the
> carbon and half the cost, gone, from one recommendation.**"
- (Optional) Click `rec-analytics-region`:
> "And carbon-aware isn't only about cost — this region shift cuts carbon with *zero* cost change."

**3:30–4:15 — Why it's credible and sellable.**
> "The method is open and **SCI-for-AI / ISO-21031 conformant** — every number traces to a public
> coefficient, no black box, no offset-washing. That's the audit-grade transparency a proprietary
> platform can't expose but an open tool can. And it's **independent** — a product the client buys
> and keeps, priced on outcomes: Baseline, Optimize, Transform, with carbon-linked gain-share."

**4:15–5:00 — The Thoughtworks wedge + roadmap.**
> "Thoughtworks co-founded the Green Software Foundation and created CCF — but its AI flagship has no
> sustainability story. RECPT is that story. We use **AI:works as client zero** to build greener
> software and prove the before/after — then sell the *measurement and the proof*, not the platform.
> Production plugs into CCF's ingestion, Langfuse, LiteLLM, and OpenTelemetry. **You can't manage what
> you can't measure — RECPT makes AI's cost and carbon, finally, measurable.**"

## Mapping to judging criteria
- **Innovation (30%)** — open-method AI-carbon + energy-debt Assess + carbon-aware optimization (not "carbon next to cost").
- **Tech feasibility (20%)** — reuses CCF/Langfuse/LiteLLM/Semgrep; transparent coefficients; credible roadmap.
- **Business impact (20%)** — ~50% cost+carbon cut shown; sellable to any client; outcome pricing.
- **Demo & storytelling (20%)** — one screen, one "both numbers drop" moment.
- **Responsible AI (10%)** — transparent, auditable, standards-aligned, honest quality trade-off, no offsets.

## Backup plan
If the live app fails: screen-recording of the same flow + the before/after numbers as static slides.
