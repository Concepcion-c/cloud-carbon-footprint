# CHANGELOG — RECPT decision log

A running log of meaningful decisions for the RECPT project. Newest first.
Format: `## YYYY-MM-DD` → `- **Decision** — why / context.`

After any notable decision (scope, architecture, tooling, naming), add an entry here.

## 2026-07-17

- **Removed the post-upload "Map source fields to RECPT schema" section (and its
  divider) from Connect New System** — after a file validates, the modal no
  longer shows the field-mapping table; "Files validated"/Save now follow
  directly. The content isn't lost — "Data Log" (Settings popover, added a
  few rounds ago) already shows the same table on demand via the shared
  `_render_field_mapping_table()` helper, confirmed still intact after this
  change; only the upload-flow call site was removed.

- **Connect New System catalog: top-aligned rows, no column stacking at narrow
  widths, doubled row spacing, all small buttons unified to outline style** —
  from a real screenshot review: the badge/button column was vertical-centering
  against the full two-line row (name + category caption) instead of the top
  line, fixed via `vertical_alignment="top"` on the row's `st.columns(...)`.
  Confirmed via direct viewport-resize testing (375px, sidebar collapsed) that
  Streamlit's columns don't switch `flex-direction` on narrow screens — they
  keep `flex-direction: row` but let `flex-wrap` drop the second column onto
  its own line once both can't fit; fixed by forcing `flex-wrap: nowrap` and
  giving the name/category column `flex:1 1 auto; min-width:0` (so its *text*
  shrinks/wraps) while the badge/button column gets `flex:0 0 auto` (sized to
  its own content, never squeezed) — verified side-by-side at 375px across all
  10 rows. Re-added the `margin-bottom:16px` removed two rounds ago — that
  removal correctly hit exactly 16px, but seeing it rendered, the user wanted
  16px *more* on top of that (32px total), so the same rule now serves a
  different, explicitly confirmed target. Also corrected an earlier "shrink but
  keep the solid color" call for "Download sample file"/"Browse files" — the
  user clarified *all* small enabled buttons in this modal should read as
  outline/secondary, so extended `_nav_icon_js()`'s existing outline-branch
  condition to cover them too, matching Select/Change/Cancel. _Why: this round
  was driven by an actual screenshot plus direct viewport-resize investigation,
  not assumptions about how Streamlit's responsive columns behave — the
  flex-wrap (not flex-direction) mechanism was confirmed empirically before
  writing the fix._

- **Connect New System polish: right-aligned row actions, no redundant post-selection
  "Source" line, small upload/download buttons, consistent 16px row spacing** —
  right-aligned the catalog list's badge/button column by targeting the actual flex
  container (`align-items`/`justify-content: flex-end` on the column's inner
  `stVerticalBlock`, not just `text-align` on the outer column — Streamlit's column
  layout is flex-based, so a button's own flex-item positioning ignores `text-align`
  from an ancestor; only the plain-HTML "Connected" badge respected that alone).
  Removed the `**Source:** category` line right after picking a system in Connect New
  System specifically (redundant — the catalog list just showed that same category);
  Update Data's own Source line is untouched, since there's no "just picked it" moment
  there. Shrank "Download sample file"/"Download Basic Template" and the native file
  uploader's "Browse files" to the same small size as the catalog's Select/Change
  buttons, explicitly leaving color alone (both already render solid purple/white via
  the existing button-color JS, unrelated to this change) — had to fix the download
  button's selector from a direct-child (`>`) to a descendant match once DOM
  inspection showed Streamlit wraps buttons with a `help=` tooltip in extra
  layers, which a direct-child selector doesn't reach. Removed an added
  `margin-bottom: 16px` between catalog rows once measurement showed Streamlit's own
  default block spacing there is already exactly 16px, so it was doubling the gap
  to 32px instead of hitting the requested 16px. _Why: user requested each of these
  after using the modal; the flex-vs-text-align and tooltip-wrapper issues were found
  by directly measuring/inspecting the live DOM, not assumed from the CSS alone._

- **Connect New System's catalog buttons are now genuinely small/secondary, "Other
  system" is a real list row (no divider), and Delete Source's Cancel reads as subtle
  while staying full-size** — the prior round's fix only removed `use_container_width`,
  which changes width, not the visual weight buttons actually needed; the real blocker
  turned out to be a JS snippet (`_nav_icon_js()`, app.py) that force-applies inline
  `!important` styles to every secondary button on a fixed 0/150/600ms delay after each
  rerun — inline `!important` always beats stylesheet `!important` regardless of
  selector specificity, so a plain CSS override could never win. Extended that JS's
  existing outline-vs-solid branch (previously only for the Connect table's "See More"
  buttons) to also cover Connect New System's catalog/Change buttons and Delete
  Source's Cancel, and replaced the fixed-delay-only approach with a `MutationObserver`
  that reactively restyles new buttons as they appear — needed because the System Name
  list only renders after an Owner is picked, later than the JS's original 600ms
  window, so the one-shot retries alone permanently missed it. Removed the "Other
  system" divider so it reads as the last row of the same list, not a separate section.
  _Why: user pointed out the buttons still looked full-weight and asked for "Other
  system" to be merged into the list — investigating the "why doesn't my new CSS
  apply" question surfaced the actual root cause above, not a guess._

- **Follow-up polish on the catalog work above: deferred system picker, top-of-table
  ordering, a real Anthropic Last Sync bug fix, a new "Data Log" option, and Webhook as a
  third connection method** — after testing the catalog UI, tightened it per feedback: the
  System Name row-list now only renders once an Owner is picked (less visual noise up
  front), and its "Select" buttons dropped `use_container_width=True` for natural,
  text-sized sizing, since Streamlit has no way to disable individual `st.selectbox` options
  or badge them, so the row-list (not a native dropdown) is the only way to show the green
  "Connected" badge next to already-connected systems. `get_visible_connectors()` now puts
  `custom_connectors` (newest first) ahead of the alphabetized `CONNECTOR_STATE` block, so a
  freshly-connected system surfaces at the top of the Connected Systems table instead of the
  bottom. Root-caused and fixed a real pre-existing bug: a per-rerun Anthropic patch block
  (predating the catalog work, written back when Anthropic had no way to become a visible
  connector at all) was overwriting Anthropic's Last Sync column with
  `st.session_state.uploaded_file_name`, which after a multi-file upload literally reads
  `"2 file(s) uploaded"` — removed those two override lines so Last Sync stays whatever the
  Save handler wrote ("just now"), matching every other connector. Moved the "Map source
  fields to RECPT schema" table out of Update Data (not relevant when just changing how an
  already-connected system is fed data) into a new "Data Log" option in the Settings
  popover, between "Update Data" and "Delete Source" — deliberately named differently from
  the page-level, still-unimplemented "Norm Log" placeholder button, which is a distinct,
  broader concept. Added "Webhook" as a third connection method (alongside API connection
  and File upload) in both dialogs — it was already promised in the Connect page's own
  description text ("connect via API, file upload, OpenTelemetry, or webhook") but never
  actually selectable; follows the same "simulated in this demo" convention as the generic
  API-connection branch. _Why: user tested the previous round live and asked for these
  specific adjustments; the Anthropic Last Sync bug was found while investigating the
  reported "shows file count instead of a timestamp" symptom, not something guessed at._

- **Connect New System now has a specific-systems catalog with connected-state badges;
  both connector modals are dismiss-safe and reconciled for consistency** — Anthropic had
  become unreachable through the modal (its `CONNECTOR_STATE` row was removed in a prior
  change, and the System Name picker only ever listed rows already in
  `get_visible_connectors()`). Introduced `SYSTEM_CATALOG`, a fixed list of systems
  independent of connection state, and replaced the System Name `st.selectbox` with a custom
  row list (`st.columns`-based, no native Streamlit widget supports per-option
  disable+badge): each catalog system shows the existing green `status_badge("Connected")`
  pill and no button if already connected, or a "Select" button if not. Anthropic is now
  catalogued with category "AI Model Provider" (correcting its previous accidental
  "Custom Source" default), and a generic "Other system" row — visually separated by a
  divider — covers anything not in the catalog. Separately, root-caused the reported
  "modal reopens when just navigating around" bug to Streamlit's `st.dialog` defaulting to
  `on_dismiss="ignore"` (X/outside-click/ESC triggers no rerun at all) combined with two of
  the three connector dialogs having no Cancel button — so the *only* way to ever reset
  `show_connect_modal`/`show_update_modal` was clicking Save; any other dismissal left it
  stuck `True` until the next unrelated rerun reopened it. Fixed by passing a same-purpose
  `on_dismiss` callback to all three dialogs. While reconciling Update Data's Save handler to
  match Connect New System's (same button layout/gating/spinner/field-mapping table, per the
  "add vs. modify should behave consistently" ask), found and fixed a real gap: Update Data
  never refreshed `records`/`norm_pct` even after a genuine new upload — fixed with an
  `n_records = None` sentinel so a bare connection-method flip (no new upload) can no longer
  clobber a connector's real record count with a computed 0. Also replaced the old
  `norm_done` page banner and Update Data's rerun-swallowed `st.success(...)` (which never
  actually rendered, since `st.success` doesn't survive a rerun) with a single page-agnostic
  `pending_toast` session-state flag consumed via `st.toast()`. _Why: user reported Anthropic
  was unreachable and both modals behaved inconsistently with each other and with basic modal
  UX expectations (unwanted reopening); fixing the literal reports required first
  distinguishing "connectable" from "connected," which didn't exist as a concept in the code
  before this change._

## 2026-07-16

- **Connect New System is now a real modal; connectors persist for the session; detail
  pages got a Settings menu (Update Data / Delete Source)** — replaced the inline `.drawer`
  panel with an `st.dialog` (first use of Streamlit's native modal in this app; no existing
  React-style "modal component" exists here since this is a single-file Streamlit prototype).
  Added System Name / Owner fields with a select-existing-or-type-new pattern, and a unified
  "Basic Template" CSV (AI-usage + cloud-usage shapes, `system_type` discriminator column)
  for any system without its own dedicated sample file — real ingestion via
  `classify_basic_template_upload()`/`calc_basic_template_upload()`, running through the same
  `calc_ai_named()`/`calc_cloud()` paths as everything else. New/updated/deleted connectors
  now genuinely persist within a session via `st.session_state` (`custom_connectors`,
  `connector_overrides`, `deleted_connector_systems`), merged through a new
  `get_visible_connectors()` that every read site (table, summary tiles, detail dispatch,
  Prove page's evidence list) now goes through — `CONNECTOR_STATE` itself is rebuilt from
  scratch every Streamlit rerun and can't hold state on its own. Caught two bugs the literal
  ask would've introduced: a new connector's "See More" crashing with `KeyError` in
  `fabricate_connector_records()` (no fallback for an unseeded name), and Basic-Template
  cloud rows silently getting zero carbon/water because their AWS-style region codes
  (`us-west-2`) don't match `grid_intensity.csv`'s abstract names — extended the existing
  Cloudability region-map adapter to cover both. _Why: user asked to refactor the Connect
  flow into a modal with real data-management actions; the app had no existing modal
  convention to reuse, so `st.dialog` was the correct native tool rather than extending the
  static, non-interactive `.sref-*` overlay._

- **Scenario Planner table: fixed CO₂e/Water period labels and scope mismatch** — the "Total
  CO₂e" and "AI Water" columns showed no time-period qualifier (only "Monthly AI Cost" did),
  even though all three figures are computed over the same monthly window. "Total CO₂e" also
  mixed in `base_cloud_carbon` while Cost and Water stayed AI-only. Renamed all three headers
  to "AI {Cost,CO₂e,Water}/mo" (matching the existing "/mo" convention used on the Energy Debt
  tab) and dropped the cloud-carbon addition so all three columns
  share the same AI-only scope, matching what the recommendations actually affect (cloud is
  unchanged by any of them). Org-wide (AI+cloud) totals remain visible in the KPI header
  elsewhere on the page. _Why: the mixed scope made the −16.1%/−26.5% deltas not match the
  displayed kg values; AI-only-everywhere keeps the table internally consistent._

- **Anthropic real-model-name mapping now has a tier-inference fallback, guaranteeing
  100% of real uploaded rows match a coefficient row** — previously, any model
  identifier not in the hand-maintained `ANTHROPIC_REAL_MODEL_MAP` (e.g. a model
  released after that list was last updated) fell through untranslated and was
  counted as "unmapped," dragging the displayed normalization % below 100% even
  though the record still got an estimate. Added `map_anthropic_model_name()`
  (`app.py`, near `ANTHROPIC_REAL_MODEL_MAP`): exact matches still use the precise
  lookup; anything else is matched by tier via substring ("opus"/"sonnet"/"haiku" —
  always present in Anthropic's real naming) to the latest real coefficient row for
  that tier. Deliberately did not hand-enumerate exact historical/future model IDs
  to avoid inventing date-slug strings that can't be verified. _Why: user asked why
  their upload showed only 65% normalized and wanted a guarantee of 100%, not a
  one-off patch for today's specific file._ Verified live with a synthetic
  never-before-seen model slug (still containing a tier word) — it correctly folded
  into the matching tier's real coefficient row rather than just suppressing the
  unmapped warning.

- **Anthropic detail page's "Add more usage files" now requires an explicit commit
  button** — previously it silently ingested and committed new files the instant they
  were selected, with no deliberate confirmation step, which read as "there's no way to
  actually upload." Now matches the Connect drawer's existing two-step pattern: selecting
  files only validates/previews; a new "Add these files to the connection" button is what
  actually commits them (calls `finalize_anthropic_calc()`), with a persistent success
  message afterward instead of a message that flashed for 1.2s before reloading. Verified
  live that the commit correctly propagates to the Connect page's Anthropic row and the
  Prove page's Evidence Pack panel. _Why: user-reported confusion that no upload action
  existed on that page._ Confirmed with the user that uploaded data remains
  session-only (not persisted across a browser refresh or app restart) — same as the
  existing Connect-drawer upload; no storage layer was added.

## 2026-07-09

- **Renamed the product from TRACE to RECPT** — updated `app.py`, `CLAUDE.md`, and all `docs/`
  content/filenames that referenced the old brand name (`trace-prd.md` → `recpt-prd.md`,
  `trace-calculation-methodology.md` → `recpt-calculation-methodology.md`,
  `hackathon-mvp-CHAT-prd-v3-trace.md` → `hackathon-mvp-CHAT-prd-v3-recpt.md`). Generic
  telemetry/tracing terminology (Agent Traces, `trace_id`, `llm_trace_export.json`, CSS/JS
  identifiers like `.trace-arrow`, `load_trace_data()`) was left untouched — it refers to
  LLM/agent tracing, not the product name. The private GitHub repo (`Concepcion-c/TRACE`) and
  the local project folder were **not** renamed. _Why: RECPT is the name going forward._

## 2026-06-10

### Session status & forward look

**Where we are:** workspace, strategy, feasibility, PRDs, synthetic data, and demo script are
complete and pushed to the private repo (`Concepcion-c/TRACE`, commit `04a6ad0c`). Ready to build
the MVP for Round 1 (video + written form due **2026-06-12**).

**Key decisions at a glance**
- **Product = an independent, sellable CCF-lineage tool** (carbon beside cost + optimization +
  CAST-like energy-debt Assess) the client buys and keeps — *not* an AI:works-embedded module.
  AI:works = "client zero" + build accelerator only.
- **Anchor on run-time carbon** (the delivered app's ongoing footprint), not build-time.
- **Build stack = Streamlit + pandas (+ optional DuckDB) + a custom RECPT calculator + synthetic
  CSVs.** Reuse OSS (CCF, Langfuse, LiteLLM, SCI-for-AI, OpenTelemetry GenAI, Semgrep) by *adopting
  their data shapes and showing the integration path*, not hosting them live. Trivy cut.
- **Methodology = SCI-for-AI / ISO 21031, open & auditable** (location-based grid intensity, no offsets).
- **MVP scope frozen to M1–M5** (hero cost+carbon, AI breakdown, visible methodology, apply-a-
  recommendation that drops both numbers); cloud tab / Assess / before/after / ledger are stretch.

**Open questions (to confirm with stakeholders)**
1. **Client data path [biggest]** — will clients share cloud-billing + LLM-usage exports, and at
   what granularity (AI gateway logs vs org/model totals)?
2. **Deployment model** — SaaS (client ships us exports) vs in-tenant (runs inside their cloud, à la
   CCF self-host)?
3. **Gain-share appetite** — put price at risk on measured carbon, or lead with the outcome narrative only?
4. **Coefficient rigor** — is approximate-but-transparent acceptable, or are defensible per-model numbers required?
5. **Scope ambition** — AI-inference carbon only vs unified cloud + AI GreenOps?
6. Secondary (feasibility §7): coefficient-maintenance owner; Boavizta GPU-SKU coverage; Assess accuracy bar.

**Next recommended steps**
1. **Build the MVP** per `docs/prd/hackathon-mvp-prd-v2.md` — scaffold Streamlit `app.py` that loads
   the synthetic CSVs and renders cost-beside-carbon + the Apply-recommendation interaction (M1–M5).
   Use the Stitch mockups in `docs/design/stitch-dashboard/` for layout + design tokens.
2. Wire the **Assess** view from `semgrep_findings.json` (stretch S2) if time allows.
3. **Record the ≤5-min demo** per `docs/demo/demo-script.md`; draft the written Round-1 submission.
4. Optional credibility artifacts: one real **Langfuse** trace export; a **CCF demo-mode** screenshot
   for the cloud tab.
5. **Get stakeholder answers** to the open questions (especially #1 client data path and #2 deployment).

---

- **Committed & pushed the batch to the private repo** (commit `04a6ad0c` on `trunk`) — strategy v2,
  both PRDs, feasibility one-pager, synthetic data package, demo script. Extracted the Stitch UI export
  to `docs/design/stitch-dashboard/` (screen mockups + `DESIGN.md` tokens) and git-ignored the original
  `.zip`. Verified no `RECPT_Documents/` leak and that the CCF `.gitignore` `*.csv` rule did not drop
  the sample data. _Why: keep the private workspace current and design assets browsable._
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
  stack: **Streamlit + pandas (+ optional DuckDB) + a custom RECPT calculator + synthetic CSVs shaped
  on Langfuse/CCF/SCI**. Cut Trivy; demoted LiteLLM/OTel/Trivy to roadmap-slide only. _Why: spend the
  fewest AI credits by writing only the unique carbon-for-AI logic and reusing everything else as
  schema/lineage._
- **Wrote two PRDs** — the full product PRD (`docs/prd/recpt-prd.md`, derived from strategy §7) and
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
- **Organized & protected `RECPT_Documents/`** — reference library sorted into themed folders
  (hackathon-admin, ccf-product, aiworks-platform, gsf-greenops, market-research, governance,
  claude-code-workshop); most sensitive items quarantined in `_confidential/`. Added
  `/RECPT_Documents/` to `.gitignore`. _Why: keep confidential/PII reference material local —
  it must never reach git or the public fork._
- **Created private workspace `Concepcion-c/TRACE`** — seeded from the public CCF fork; wired
  remotes `origin` (private), `public` (fork = publish target), `upstream` (org). Commits use
  the GitHub noreply email to satisfy email-privacy protection. _Why: experiment privately,
  publish only the finished result to the public fork._
