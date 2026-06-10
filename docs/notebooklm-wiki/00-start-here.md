# 00 — Start Here: TRACE Wiki Introduction

> **Summary:** This is the entry point for the TRACE NotebookLM wiki. Read this first to understand what TRACE is, who this wiki is for, and how to get the most out of these documents.

---

## What is TRACE?

**TRACE** (Token-level Realtime AI Carbon Estimation) is a dashboard that shows organisations how much their AI tools cost, how much carbon they produce, how much energy they consume, and how much water they use — all in one place, alongside their cloud infrastructure costs and emissions.

It was built as a **hackathon MVP** (Minimum Viable Product) for the AI:Works Global Hackathon 2026 by a Thoughtworks team. It is a working demo, not a production system.

The core idea: AI is becoming a major and rapidly growing source of energy consumption and carbon emissions, but today's tools only show you the *cost* — not the environmental impact. TRACE makes both visible at the same time, and then tells you what to do about it.

---

## Who is this wiki for?

This wiki is written for **non-technical teammates** — people who want to understand, explain, or demo TRACE without needing to read code. It is equally useful for:

- **Hackathon judges** who want to understand what was built and why
- **Thoughtworks teammates** preparing for client conversations or internal presentations
- **Product and strategy people** who need to explain the methodology or answer tough questions
- **Future developers** who want to understand the project before looking at the code

Technical detail is included where it helps, but plain-English explanations always come first.

---

## What is in this wiki?

| File | What it covers |
|---|---|
| **00 — Start Here** (this file) | Introduction, how to use the wiki |
| **01 — Product Overview** | What TRACE is, who it's for, the demo story |
| **02 — User Flows** | Step-by-step walkthrough of every page and screen |
| **03 — Functionality Guide** | Every feature explained in plain English |
| **04 — Architecture** | How the app is built and how it runs |
| **05 — CCF Integration** | How TRACE relates to Cloud Carbon Footprint |
| **06 — Calculations & Methodology** | Every formula and where it came from |
| **07 — Data Dictionary** | Every data field, what it means, and where it comes from |
| **08 — Demo Guide** | How to present TRACE in 5 minutes |
| **09 — Limitations, Roadmap & Risks** | What the MVP can't do and what comes next |
| **10 — Primary Sources Appendix** | Every source used to build TRACE |
| **11 — Glossary** | Plain-English definitions of technical terms |
| **NotebookLM Upload Index** | How to use this wiki in NotebookLM |

---

## Important things to know before asking questions

1. **All data in the demo is synthetic.** Every number you see in the dashboard was generated artificially for demonstration purposes. It is shaped to look like real data but contains no actual client information.

2. **TRACE is a hackathon MVP.** It demonstrates a concept with real potential, but it is not a production-ready product. Some features are simulated for the demo.

3. **The app is built entirely in Python.** It runs as a local web application using a tool called Streamlit. It does not require a server, database, or cloud service to run.

4. **The methodology is open and documented.** Every formula and assumption is written down and traceable to a published source. This transparency is intentional — it is one of TRACE's key differentiators.

5. **The client in the demo is fictional.** The app shows "Northstar Bank — Digital Banking Modernization" as the client context. This is synthetic.

---

## Suggested questions to ask NotebookLM

These questions are designed to help you get useful answers quickly. Upload all files for the best results.

**Understanding the product:**
- "What problem does TRACE solve?"
- "Who are TRACE's target users?"
- "What is the demo story for TRACE?"
- "What is the difference between TRACE and Cloud Carbon Footprint?"
- "What does TRACE measure that existing tools don't?"

**Understanding the demo:**
- "What happens when you click Apply on a recommendation?"
- "What is Support-Bot and why is it important in the demo?"
- "What is the Energy Debt score?"
- "What does the Agent Traces tab show?"
- "What is the wow moment in the demo?"

**Understanding the methodology:**
- "How does TRACE calculate AI carbon emissions?"
- "Where do the energy-per-token coefficients come from?"
- "What is SCI-for-AI?"
- "Why doesn't TRACE use carbon offsets?"
- "How does TRACE calculate water consumption?"
- "What is the difference between a confirmed number and an estimate in TRACE?"

**Handling tough questions:**
- "How accurate are the carbon estimates?"
- "What is the confidence level of the methodology?"
- "Is the data real or synthetic?"
- "How would TRACE work with a real client's data?"
- "What would be needed to make TRACE production-ready?"

**Understanding the technology:**
- "What is Cloud Carbon Footprint and how does TRACE use it?"
- "What data does TRACE need from a client?"
- "What tools does TRACE connect to?"
- "What is a token and why does it matter for carbon measurement?"

---

## Key facts at a glance

| Fact | Detail |
|---|---|
| App name | TRACE (Token-level Realtime AI Carbon Estimation) |
| App type | Hackathon MVP / proof-of-concept |
| Built with | Python, Streamlit, pandas, plotly |
| Data used | 100% synthetic (no real client data) |
| Client persona in demo | Northstar Bank — Digital Banking Modernization |
| Number of pages | 4 (Connect, Observe, Optimize, Prove) |
| What it measures | AI inference: cost, carbon, energy, water · Cloud infrastructure: cost, carbon, energy, water |
| Key methodology | SCI-for-AI / ISO 21031 (location-based, no carbon offsets) |
| Key demo result | Applying one recommendation cuts AI carbon by ~49% and AI cost by ~52% |
| CCF relationship | Fork of CCF codebase as a starting point; TRACE MVP does not run CCF code |

---

## Key takeaways

- TRACE makes AI carbon and cost visible side by side — something no existing tool does today
- The methodology is open, sourced from published standards and benchmarks, and honest about its confidence levels
- The demo is fast, visual, and ends with a live "both numbers drop" moment
- This wiki is designed so any teammate can explain the app accurately, even without a technical background
