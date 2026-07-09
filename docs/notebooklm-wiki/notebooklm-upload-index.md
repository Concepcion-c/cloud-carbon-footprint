# NotebookLM Upload Index

> **How to use this file:** Upload all 13 documents in the RECPT NotebookLM wiki to a single NotebookLM notebook, in the order listed below. This index tells you what each file covers, the best order to add them, and ready-to-use prompts for asking NotebookLM questions. Paste the briefing prompt at the top into the notebook chat first.

---

## Recommended upload order

Add files to NotebookLM in this sequence. The order matters: NotebookLM builds context progressively, and later files reference concepts from earlier ones.

| # | File | What it covers |
|---|---|---|
| 1 | `00-start-here.md` | What RECPT is, who it is for, where everything lives |
| 2 | `01-product-overview.md` | The product vision, target users, business model |
| 3 | `02-user-flows.md` | How users navigate the app, step by step |
| 4 | `03-functionality-guide.md` | What every page and feature actually does |
| 5 | `04-architecture.md` | How the system is built and why |
| 6 | `06-calculations-and-methodology.md` | How every number is calculated |
| 7 | `07-data-dictionary.md` | What every data field means |
| 8 | `05-ccf-integration.md` | The relationship with Cloud Carbon Footprint |
| 9 | `08-demo-guide.md` | How to run and present the demo |
| 10 | `09-limitations-roadmap-risks.md` | What RECPT cannot do today and what comes next |
| 11 | `10-primary-sources-appendix.md` | Where every number and standard comes from |
| 12 | `11-glossary.md` | Plain-English definitions of all technical terms |
| 13 | `notebooklm-upload-index.md` | This file — overview, prompts, and question guide |

**Important:** `10-primary-sources-appendix.md` should be uploaded even if you do not read it manually. NotebookLM will draw on it to answer questions about methodology credibility, formula origins, and what is estimated versus measured.

---

## What each file covers

### `00-start-here.md`
The entry point for anyone new to RECPT. Explains what problem RECPT solves (AI carbon and cost are currently invisible), who the key stakeholders are, and where to find things in the documentation. Read this first before asking detailed questions about any other file.

### `01-product-overview.md`
The product's full story: why it exists, who it is for, what makes it different from existing tools like Cloud Carbon Footprint or FinOps platforms, and how it would be sold. Covers the three-tier pricing model (Baseline / Optimize / Transform), the gain-share option, and Thoughtworks' competitive advantages (CCF co-creator, Green Software Foundation co-founder, AI:works platform).

### `02-user-flows.md`
A step-by-step walkthrough of the four pages in the app — Connect, Observe, Optimize, and Prove. Describes what a user does, what they see, and what decisions they can make on each page. Useful for understanding the intended user experience without having the app open.

### `03-functionality-guide.md`
A detailed feature-by-feature breakdown: what every tab, chart, metric, and button does in the live app. Goes deeper than the user flow — explains why each element is there and what information it conveys. The reference to use when someone asks "what does the Energy Debt tab show?" or "what happens when you click Apply?"

### `04-architecture.md`
How the system is actually built: the tech stack (Python, Streamlit, pandas, Plotly), the data flow from CSV files through calculation functions to dashboard, the file and folder structure, and a Mermaid diagram showing the component relationships. Explains why a simple single-file architecture was chosen for the MVP and what would change in a production deployment.

### `05-ccf-integration.md`
The relationship between RECPT and Cloud Carbon Footprint (CCF). Explains what CCF is, how RECPT uses CCF's approach without invoking its code, and the four-phase path for a future production integration. Useful for stakeholders asking "is this built on CCF?" or "how is this different from CCF?"

### `06-calculations-and-methodology.md`
The mathematical core of RECPT. Documents every formula used to calculate carbon, energy, cost, and water from token counts and cloud usage data. Includes the worked example (29M tokens → 34.85 kWh → 21.95 kg CO₂e → $871.21 → 62.7L water), all coefficient values, and the standards the methodology aligns to (SCI-for-AI, ISO 21031). The companion to `10-primary-sources-appendix.md`.

### `07-data-dictionary.md`
Defines every data field, file, and calculated metric in the RECPT dataset. Tells you what each CSV and JSON file contains, where the values come from (synthetic, sourced, or calculated), and the exact formulas used for all derived metrics. The reference when someone asks "what does this column mean?" or "where does this number come from?"

### `08-demo-guide.md`
The complete five-minute demo playbook: setup checklist, recommended narration for each stage, key numbers to know, the wow moment (clicking Apply on the Optimize page), and prepared answers for likely tough questions. Written so anyone who has read it once can present the demo confidently.

### `09-limitations-roadmap-risks.md`
An honest account of what RECPT cannot do today: all data is synthetic, no live connectors exist, energy coefficients are estimated not measured, only two recommendations are implemented. Also covers the product roadmap (short, medium, long term) and known risks (coefficient credibility challenge, "this is just a demo" objection). This document demonstrates the project's intellectual honesty.

### `10-primary-sources-appendix.md`
A complete catalogue of every external source behind RECPT's methodology — standards (ISO 21031, SCI-for-AI), open-source tools (CCF, Langfuse, OpenTelemetry), grid intensity datasets (Electricity Maps, EPA eGRID, ENTSO-E), research papers (Luccioni et al., Patterson et al., Li et al.), and hardware specs (NVIDIA A100/H100, MLPerf). Each entry shows how the source was used, its confirmation status, and any caveats. **Upload this file so NotebookLM can answer methodology credibility and sourcing questions accurately.**

### `11-glossary.md`
Plain-English definitions for 50+ technical terms used in RECPT and AI carbon accounting — from "token" and "inference" through "SCI-for-AI," "WUE," "location-based accounting," and "Energy Debt Score." Organised alphabetically. Upload this so NotebookLM can explain jargon clearly when teammates ask.

### `notebooklm-upload-index.md`
This file. Contains the upload order, file descriptions, the notebook briefing prompt, and suggested questions. Upload it last so NotebookLM can reference it as the meta-document for the wiki set.

---

## Notebook briefing prompt

Copy and paste this into the NotebookLM chat **immediately after uploading all files**, before asking any other questions. It orients the notebook to the project context.

---

**Paste this into NotebookLM chat:**

> I have uploaded a complete documentation set for RECPT — a Python/Streamlit hackathon MVP that measures and optimises the carbon and cost of AI inference workloads. RECPT was built by Thoughtworks for the AI:Works Global Hackathon. The documentation covers the product overview, all four app pages (Connect / Observe / Optimize / Prove), the calculation methodology (SCI-for-AI / ISO 21031), the Cloud Carbon Footprint relationship, the demo playbook, all data sources, limitations, roadmap, and a glossary.
>
> The fictional client in the demo is Northstar Bank. All demo data is synthetic. The app is built with Python, Streamlit, pandas, and Plotly. There are no live data connectors in the MVP.
>
> Please index all 13 documents and confirm you have done so. When answering questions, please cite which document you are drawing from.

---

## Suggested questions to ask NotebookLM

These questions are written to test different parts of the wiki. Use them as starting points.

### Understanding the product
- "What problem does RECPT solve, and who is it for?"
- "How is RECPT different from Cloud Carbon Footprint?"
- "What is the Energy Debt Score and how is it calculated?"
- "What are the four pages in the RECPT app and what does each one do?"
- "What is the 'wow moment' in the RECPT demo?"

### Understanding the calculations
- "How does RECPT calculate the carbon footprint of an AI inference call?"
- "Where do the kWh-per-million-token coefficients come from?"
- "Why does Mumbai (ap-south) have higher carbon and water figures than Oregon (us-west)?"
- "What is WUE and how does RECPT use it?"
- "What is location-based accounting and why does RECPT use it instead of market-based accounting?"

### Understanding the demo
- "Walk me through the recommended five-minute demo script."
- "What numbers should I know before presenting the RECPT demo?"
- "What happens when you click Apply on the Optimize page?"
- "How should I answer if a judge asks whether the accuracy of the carbon estimates can be trusted?"

### Understanding the data
- "What data files does RECPT use and where do they come from?"
- "What is synthetic data and is all of RECPT's demo data synthetic?"
- "What is a Langfuse export and why does RECPT use that format?"
- "What are the five synthetic applications in the Northstar Bank demo?"

### Understanding limitations and future direction
- "What are the most important limitations of the RECPT MVP?"
- "What would it take to make RECPT production-ready?"
- "What is the roadmap for integrating RECPT with the real Cloud Carbon Footprint codebase?"
- "Why are the AI carbon figures labelled Medium confidence rather than High confidence?"

### For non-technical teammates
- "Explain RECPT as if I have never heard of carbon footprinting or AI observability."
- "What is a token and why does it matter for calculating AI carbon?"
- "Can you explain the Support-Bot recommendation in plain English?"
- "What is the relationship between Thoughtworks, CCF, and the Green Software Foundation?"

---

## Suggested doc summary prompt

Use this prompt to get NotebookLM to produce a briefing summary — useful for sharing with teammates who have not read the wiki.

---

**Paste into NotebookLM chat:**

> Please produce a one-page briefing about RECPT for a non-technical business audience. Include: (1) what problem it solves in one sentence, (2) what the demo shows in three bullet points, (3) what makes the methodology defensible, (4) the single biggest limitation, and (5) why Thoughtworks is the right firm to build this. Draw from all documents. Keep it under 400 words.

---

## A note on the primary sources appendix

`10-primary-sources-appendix.md` is the most important file for methodology questions. It is the only document in the wiki that explicitly lists every external source behind RECPT's numbers — standards, research papers, hardware specs, and grid intensity datasets — with their confirmation status (directly coded in the app, cited in project docs, planned for future integration, or recommended addition).

If a teammate asks "is this methodology credible?" or "where did that number come from?" — the appendix is where NotebookLM will find the most precise answer. Do not skip uploading it.

---

## Key takeaways

- Upload all 13 files; all are needed for complete coverage
- Upload `10-primary-sources-appendix.md` even if you do not read it — it is essential for NotebookLM to answer methodology questions
- Paste the briefing prompt immediately after uploading to orient the notebook
- The wiki is written for non-technical teammates — the language is plain English throughout, with technical details explained rather than assumed
- All RECPT demo data is synthetic; nothing in the wiki contains real client or personal data
