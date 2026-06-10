# CHANGELOG — TRACE decision log

A running log of meaningful decisions for the TRACE project. Newest first.
Format: `## YYYY-MM-DD` → `- **Decision** — why / context.`

After any notable decision (scope, architecture, tooling, naming), add an entry here.

## 2026-06-10

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
