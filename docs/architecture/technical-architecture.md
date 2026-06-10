# Technical architecture — TRACE

> **Status:** Draft · **Last updated:** 2026-06-10
> Keep this current so PRDs, user stories, and code can reference it. Ask Claude to
> update it whenever an architectural decision is made (and log the decision in
> `../../CHANGELOG.md`).

## Context
TRACE builds on the open-source **Cloud Carbon Footprint (CCF)** codebase (this repo is a
fork). CCF is a monorepo (`packages/`) — `app`, `api`, `client`, `cli`, plus cloud-provider
packages. Our work extends it toward **AI / LLM emissions**.

## Where our changes live
_TBD — list the packages/files we touch and any new modules._

## Key components
| Component | Responsibility | Status |
|---|---|---|
| _TBD_ | _TBD_ | _planned_ |

## Data flow
_TBD — how AI-usage/emissions data enters, is calculated, and is surfaced._

## Integration points (existing CCF)
_TBD — estimation engine, data ingestion, frontend dashboards, etc._

## Open technical questions
_TBD (cross-reference `../assumptions/assumptions.md`)._
