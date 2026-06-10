# CLAUDE.md — TRACE project onboarding

> **Read this first.** This file is the onboarding brief for anyone (human or Claude)
> joining the TRACE project. Think of it like onboarding a new teammate: it explains
> what we're building, how the repo is organized, where things live, and the rules we
> work by. Keep it current.

## What this is

**TRACE** is the private workspace for our **Cloud Carbon Footprint (CCF) / AI-emissions**
hackathon project (AI:Works Global Hackathon). It is built on a fork of the open-source
[Cloud Carbon Footprint](https://github.com/cloud-carbon-footprint/cloud-carbon-footprint)
codebase. We experiment here privately, then publish the finished result to the public fork.

Claude acts as a **PM teammate** here — drafting PRDs, synthesizing research, maintaining
the changelog, and helping ship code — always referencing the files in this repo.

## Repo & publishing model

| Remote | Repo | Purpose |
|---|---|---|
| `origin` | `Concepcion-c/TRACE` (**private**) | Day-to-day work. Push freely. |
| `public` | `Concepcion-c/cloud-carbon-footprint` (**public fork**) | Publish target for the final result. |
| `upstream` | `cloud-carbon-footprint/cloud-carbon-footprint` | Pull upstream CCF updates. |

**Publishing the final project to the public fork** (run only when ready to expose):

```bash
git checkout trunk
git checkout -B publish            # clean publish branch from trunk
git rm -r --cached docs            # strip internal PM docs from this branch only
git commit -m "Publish: strip internal docs"
git push public publish:trunk
git checkout trunk                 # back to work
```
> Before pushing: `git show publish:docs/` should error, confirming internal docs aren't published.
> `TRACE_Documents/` is git-ignored, so it can never be published regardless.

### 🔒 Golden rules
1. **No PII or client-confidential data** in anything tracked by git. Ever.
2. `TRACE_Documents/` is **local-only reference** (git-ignored). Never commit it; never quote
   its raw confidential content (sales calls, team chats) into tracked files. Distill
   **paraphrased, PII-free** insights into `docs/research/` instead.
3. The **public fork is world-visible** — only the curated `publish` branch reaches it.
4. New PRDs **start from `docs/prd/_TEMPLATE.md`**.
5. After any meaningful decision, **update `CHANGELOG.md`**.

## Folder map

```
TRACE/
├── CLAUDE.md            ← you are here (onboarding)
├── CHANGELOG.md         ← running log of decisions
├── docs/                ← all PM artifacts (internal; not published)
│   ├── prd/             ← PRDs (+ _TEMPLATE.md base)
│   ├── architecture/    ← technical architecture
│   ├── demo/            ← demo script
│   ├── assumptions/     ← assumptions & open questions
│   ├── sample-data/     ← SYNTHETIC sample data only
│   ├── research/        ← clean, PII-free research notes
│   └── notes/           ← running scratch notes
├── TRACE_Documents/     ← ⛔ local-only reference library (git-ignored)
└── (CCF codebase: packages/, microsite/, terraform/, …)
```

## How we work

- **PRDs:** copy `docs/prd/_TEMPLATE.md` → `docs/prd/<name>.md`, then fill in.
- **Decisions:** record in `CHANGELOG.md` (date · decision · why).
- **Research:** raw sources live in `TRACE_Documents/` (local). Synthesize them into
  `docs/research/` as clean Markdown with **no names, quotes, or confidential specifics**.
- **Architecture:** keep `docs/architecture/technical-architecture.md` updated so user
  stories and code can reference it.
- **Sample data:** only synthetic/illustrative data in `docs/sample-data/` — never real
  client or customer data.

## Project context (fill in as it firms up)

- **Problem we're solving:** _TBD — capture in the PRD._
- **Target users / personas:** _TBD._
- **Key differentiator vs. existing CCF:** _TBD (the AI-emissions angle)._
- **Success metric for the hackathon:** _TBD._

_Reference material to inform the above lives in `TRACE_Documents/` (see its README)._
