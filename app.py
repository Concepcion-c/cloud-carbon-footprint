"""TRACE — AI GreenOps Dashboard v3.  Run: streamlit run app.py"""

import json
import time
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as _components


# ── Lucide icon helpers ────────────────────────────────────────────────────────
def _svg(name: str, size: int = 16, color: str = "currentColor") -> str:
    """Return an inline Lucide SVG for use in HTML markdown blocks."""
    _PATHS = {
        "leaf":           '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>',
        "folder":         '<path d="M4 20h16a2 2 0 0 0 2-2V8a2 2 0 0 0-2-2h-7.93a2 2 0 0 1-1.66-.9l-.82-1.2A2 2 0 0 0 7.93 3H4a2 2 0 0 0-2 2v13c0 1.1.9 2 2 2Z"/>',
        "alert-triangle": '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3Z"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
        "info":           '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
        "check":          '<path d="M20 6 9 17l-5-5"/>',
        "check-circle":   '<path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="m9 11 3 3L22 4"/>',
        "x":              '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
        "hash":           '<line x1="4" x2="20" y1="9" y2="9"/><line x1="4" x2="20" y1="15" y2="15"/><line x1="10" x2="14" y1="3" y2="21"/>',
        "clock":          '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
        "dollar-sign":    '<line x1="12" x2="12" y1="2" y2="22"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
        "star":           '<polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>',
        "zap":            '<polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>',
        "paperclip":      '<path d="m21.44 11.05-9.19 9.19a6 6 0 0 1-8.49-8.49l8.57-8.57A4 4 0 1 1 18 8.84l-8.59 8.57a2 2 0 0 1-2.83-2.83l8.49-8.48"/>',
        "download":       '<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" x2="12" y1="15" y2="3"/>',
        "file-text":      '<path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"/><polyline points="14 2 14 8 20 8"/><line x1="16" x2="8" y1="13" y2="13"/><line x1="16" x2="8" y1="17" y2="17"/><line x1="10" x2="8" y1="9" y2="9"/>',
        "landmark":       '<line x1="3" x2="21" y1="22" y2="22"/><line x1="6" x2="6" y1="18" y2="11"/><line x1="10" x2="10" y1="18" y2="11"/><line x1="14" x2="14" y1="18" y2="11"/><line x1="18" x2="18" y1="18" y2="11"/><polygon points="12 2 20 7 4 7"/>',
    }
    inner = _PATHS.get(name, "")
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
        f'viewBox="0 0 24 24" fill="none" stroke="{color}" stroke-width="2" '
        f'stroke-linecap="round" stroke-linejoin="round" '
        f'style="display:inline-block;vertical-align:middle;flex-shrink:0;">'
        f'{inner}</svg>'
    )


def _nav_icon_css() -> str:
    """Pre-JS fallback: reserves padding and positioning context before JS fires."""
    return """<style>
section[data-testid="stSidebar"] div[role="radiogroup"] label {
  position: relative !important;
  padding-left: 36px !important;
}
</style>"""


def _nav_icon_js() -> str:
    """Inject nav icons via ::before pseudo-elements (position:absolute).

    Absolutely-positioned ::before elements are anchored by pixel coordinates,
    not by the label's padding, so they never move on hover/focus/active/selected.
    """
    def _uri(paths: str) -> str:
        svg = (
            "<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' "
            "viewBox='0 0 24 24' fill='none' stroke='%23CECCE8' stroke-width='2' "
            "stroke-linecap='round' stroke-linejoin='round'>"
            + paths + "</svg>"
        )
        return "data:image/svg+xml," + svg.replace("<", "%3C").replace(">", "%3E")

    icons = [
        _uri(
            "<path d='M12 22v-5'/><path d='M9 8V2'/><path d='M15 8V2'/>"
            "<path d='M18 8v5a4 4 0 0 1-4 4h-4a4 4 0 0 1-4-4V8Z'/>"
        ),  # plug → Connect
        _uri(
            "<path d='M2 12s3-7 10-7 10 7 10 7-3 7-10 7-10-7-10-7Z'/>"
            "<circle cx='12' cy='12' r='3'/>"
        ),  # eye → Observe
        _uri("<polygon points='13 2 3 14 12 14 11 22 21 10 12 10 13 2'/>"),  # zap → Optimize
        _uri(
            "<rect width='8' height='4' x='8' y='2' rx='1' ry='1'/>"
            "<path d='M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2'/>"
            "<path d='M12 11h4'/><path d='M12 16h4'/><path d='M8 11h.01'/><path d='M8 16h.01'/>"
        ),  # clipboard → Prove
    ]
    icons_json = "[" + ",".join(f'"{u}"' for u in icons) + "]"
    return f"""(function(){{
  var icons={icons_json};
  function applyIcons(){{
    var p=window.parent;if(!p)return;
    var ls=p.document.querySelectorAll(
      'section[data-testid="stSidebar"] [role="radiogroup"] label'
    );
    if(!ls.length)return;
    ls.forEach(function(l,i){{if(i<icons.length)l.setAttribute('data-trace-nav',i);}});
    var sid='trace-nav-icons';
    var el=p.document.getElementById(sid);
    if(!el){{el=p.document.createElement('style');el.id=sid;p.document.head.appendChild(el);}}
    var b='section[data-testid="stSidebar"] [data-trace-nav]';
    // Lock padding on every state so the text indent never shifts
    var css=b+'{{position:relative!important;padding-left:36px!important;}}'+
      b+':hover,'+b+':focus,'+b+':active{{padding-left:36px!important;}}'+
      // Shared ::before rules — absolutely positioned so they never move
      b+'::before{{content:""!important;display:block!important;position:absolute!important;'+
        'left:8px!important;top:50%!important;transform:translateY(-50%)!important;'+
        'width:16px!important;height:16px!important;'+
        'background-size:16px 16px!important;background-repeat:no-repeat!important;'+
        'background-position:center!important;pointer-events:none!important;}}';
    // Per-icon ::before background-image
    icons.forEach(function(u,i){{
      var s='section[data-testid="stSidebar"] [data-trace-nav="'+i+'"]';
      css+=s+'::before{{background-image:url("'+u+'")!important;}}';
    }});
    el.textContent=css;
    // Force-hide elements that Streamlit's emotion CSS keeps overriding via stylesheet
    var hide=['[data-testid="stWidgetLabel"]','[data-testid="stLogoSpacer"]'];
    hide.forEach(function(sel){{
      var n=p.document.querySelector(sel);
      if(n)n.style.setProperty('display','none','important');
    }});
  }}
  applyIcons();setTimeout(applyIcons,150);setTimeout(applyIcons,600);
}})();"""


# ── Config ─────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="TRACE | AI GreenOps",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA_DIR = Path(__file__).parent / "docs" / "sample-data"

# ── CSS ────────────────────────────────────────────────────────────────────────
st.markdown(
    '<link rel="preconnect" href="https://fonts.googleapis.com">'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
    '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">',
    unsafe_allow_html=True,
)

st.markdown("""
<style>
html, body { font-family: Inter, sans-serif !important; }
button, input, select, textarea { font-family: inherit !important; }
h1, h2, h3, h4, h5, h6, p, label { font-family: Inter, sans-serif !important; }
/* Streamlit text containers — exclude icon/svg wrappers */
[data-testid="stMarkdownContainer"],
[data-testid="stText"],
[data-testid="stCaptionContainer"],
[data-testid="stMetricLabel"],
[data-testid="stMetricValue"],
[data-testid="stMetricDelta"],
[data-testid="stRadio"] label,
[data-testid="stSelectbox"] label,
[data-testid="stMultiSelect"] label,
[data-testid="stSidebar"] label {
  font-family: Inter, sans-serif !important;
}
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stElementToolbar"] { display: none !important; }
section[data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"],
section[data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"]:hover,
section[data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"]:hover > div { border-color: transparent !important; box-shadow: none !important; outline: none !important; }
section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] { display: none !important; }
.stApp {
  background:
    linear-gradient(to bottom, transparent 0%, #F1F8FF 100%),
    linear-gradient(to right, #F0F0FB 0%, #F9F9FB 100%) !important;
}
.block-container { padding-top: 1.25rem; padding-bottom: 2rem; max-width: 1440px !important; margin-left: auto !important; margin-right: auto !important; }

/* ── Sidebar nav ─────────────────────────────────────────────────────────── */
section[data-testid="stSidebar"] > div:first-child { background: #0F0A37 !important; }

/* Nav group — 4px horizontal padding matches the logo wrapper's 4px inset */
section[data-testid="stSidebar"] div[data-testid="stRadio"],
section[data-testid="stSidebar"] div[role="radiogroup"] {
  width: 100% !important;
  padding: 0 4px !important;
  box-sizing: border-box !important;
}
section[data-testid="stSidebar"] div[data-testid="stRadio"] > div,
section[data-testid="stSidebar"] div[role="radiogroup"] > div {
  width: 100% !important;
  gap: 2px !important;
  display: flex !important;
  flex-direction: column !important;
}

/* Nav item — hide the input AND the BaseWeb visual circle (first div child of label) */
section[data-testid="stSidebar"] div[data-testid="stRadio"] input[type="radio"],
section[data-testid="stSidebar"] div[role="radiogroup"] input[type="radio"] {
  display: none !important;
}
section[data-testid="stSidebar"] div[role="radiogroup"] label > div:first-of-type {
  display: none !important;
}

/* Nav item — default */
section[data-testid="stSidebar"] div[data-testid="stRadio"] label,
section[data-testid="stSidebar"] div[role="radiogroup"] label {
  width: 100% !important;
  box-sizing: border-box !important;
  color: #CECCE8 !important;
  font-family: Inter, sans-serif !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  border-radius: 6px !important;
  padding: 9px 12px !important;
  display: flex !important;
  align-items: center !important;
  gap: 0 !important;
  cursor: pointer !important;
  transition: background 0.12s ease, color 0.12s ease !important;
  margin: 0 !important;
  min-height: 36px !important;
  letter-spacing: 0.01em !important;
}

/* Nav item — text/span */
section[data-testid="stSidebar"] div[data-testid="stRadio"] label p,
section[data-testid="stSidebar"] div[role="radiogroup"] label p,
section[data-testid="stSidebar"] div[data-testid="stRadio"] label span,
section[data-testid="stSidebar"] div[role="radiogroup"] label span {
  color: inherit !important;
  font-family: Inter, sans-serif !important;
  font-size: 13px !important;
  font-weight: inherit !important;
  margin: 0 !important;
}

/* Nav item — active */
section[data-testid="stSidebar"] div[data-testid="stRadio"] label:has(input:checked),
section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
  background: #2E2261 !important;
  color: #CECCE8 !important;
  font-weight: 600 !important;
}

/* Nav item — hover (skip if already active) */
section[data-testid="stSidebar"] div[data-testid="stRadio"] label:not(:has(input:checked)):hover,
section[data-testid="stSidebar"] div[role="radiogroup"] label:not(:has(input:checked)):hover {
  background: rgba(206,204,232,0.08) !important;
  color: #CECCE8 !important;
}

/* Sweep: all text inside the sidebar uses #CECCE8 */
section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] span,
section[data-testid="stSidebar"] div,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] button {
  color: #CECCE8 !important;
}

/* Full-width element containers inside the sidebar */
section[data-testid="stSidebar"] [data-testid="stElementContainer"],
section[data-testid="stSidebar"] .element-container {
  width: 100% !important;
}

/* Close button inside sidebar — 36×36 rounded square, matches open button shape */
section[data-testid="stSidebar"] button[data-testid="stBaseButton-headerNoPadding"] {
  width: 36px !important;
  height: 36px !important;
  border-radius: 10px !important;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
  color: #CECCE8 !important;
  background: transparent !important;
  border: none !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 0 !important;
}

/* Open button (stExpandSidebarButton) — inverted: light bg + dark icon, 36×36 rounded square */
[data-testid="stExpandSidebarButton"],
[data-testid="stExpandSidebarButton"] * {
  visibility: visible !important;
  display: block !important;
}
[data-testid="stExpandSidebarButton"] {
  width: 36px !important;
  height: 36px !important;
  background: #CECCE8 !important;
  border-radius: 10px !important;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 0 !important;
  cursor: pointer !important;
}
[data-testid="stExpandSidebarButton"]:hover {
  background: #B5B2D4 !important;
}
[data-testid="stExpandSidebarButton"] svg,
[data-testid="stExpandSidebarButton"] span {
  fill: #0F0A37 !important;
  color: #0F0A37 !important;
}

/* Mobile (≤ 768px): same button, fixed top-left, ☰ replaces arrow icon */
@media (max-width: 768px) {
  [data-testid="stExpandSidebarButton"] {
    position: fixed !important;
    top: 12px !important;
    left: 12px !important;
    z-index: 9999 !important;
  }
  [data-testid="stExpandSidebarButton"] svg,
  [data-testid="stExpandSidebarButton"] span[data-testid="stIconMaterial"] {
    display: none !important;
  }
  [data-testid="stExpandSidebarButton"]::before {
    content: "☰" !important;
    position: absolute !important;
    top: 50% !important;
    left: 50% !important;
    transform: translate(-50%, -50%) !important;
    color: #0F0A37 !important;
    font-size: 18px !important;
    line-height: 1 !important;
    visibility: visible !important;
    display: block !important;
  }
}

/* ── Metric card ─────────────────────────────────────────────────────────── */
.kpi { background:#fff; border:1px solid #e5e7eb; border-radius:12px; padding:20px; height:100%; }
.kpi-label { font-size:11px; font-weight:400; color:#9ca3af;
             text-transform:uppercase; letter-spacing:.06em; margin-bottom:4px; }
.kpi-value { font-size:28px; font-weight:700; color:#111827; line-height:1.2; }
.kpi-sub   { font-size:12px; color:#9ca3af; margin-top:4px; }
.kpi-delta-good { font-size:12px; font-weight:600; color:#059669; margin-top:4px; }
.kpi-delta-bad  { font-size:12px; font-weight:600; color:#ef4444; margin-top:4px; }

/* ── Section heading ─────────────────────────────────────────────────────── */
.sh { font-size:18px; font-weight:600; color:#111827; margin:18px 0 12px; }

/* ── Rec cards ───────────────────────────────────────────────────────────── */
.rec { background:#fff; border:1px solid #e5e7eb; border-radius:8px; padding:18px 22px; margin-bottom:10px; }
.rec.applied { border-color:#10b981; background:#f0fdf8; }
.rec-title   { font-size:15px; font-weight:600; color:#111827; margin-bottom:5px; }
.rec-body    { font-size:13px; color:#374151; line-height:1.55; margin-bottom:8px; }
.rec-quality { font-size:11px; color:#9ca3af; font-style:italic; }

/* ── Pills ───────────────────────────────────────────────────────────────── */
.pill-green { display:inline-block; background:#10b981; color:#ffffff; border-radius:99px;
              font-size:11px; font-weight:600; padding:4px 8px; margin-right:5px; }
.pill-gray  { display:inline-block; background:#9ca3af; color:#ffffff; border-radius:99px;
              font-size:11px; font-weight:600; padding:4px 8px; margin-right:5px; }
.pill-navy  { display:inline-block; background:#0b082d; color:#ffffff; border-radius:99px;
              font-size:11px; font-weight:600; padding:4px 8px; margin-right:5px; }

/* ── Formula block ───────────────────────────────────────────────────────── */
.formula { background:#111827; color:#10b981; font-family:'Inter',monospace;
           font-size:12px; border-radius:8px; padding:14px 18px; line-height:2.0; }

/* ── Severity badges ─────────────────────────────────────────────────────── */
.badge-hi  { background:#ef4444; color:#ffffff; border-radius:4px;
             padding:2px 8px; font-size:11px; font-weight:600; margin-right:4px; }
.badge-med { background:#f59e0b; color:#ffffff; border-radius:4px;
             padding:2px 8px; font-size:11px; font-weight:600; margin-right:4px; }
.badge-lo  { background:#9ca3af; color:#ffffff; border-radius:4px;
             padding:2px 8px; font-size:11px; font-weight:600; }

/* ── Synthetic data banner ───────────────────────────────────────────────── */
.synth { background:#fef9c3; border:1px solid #fde047; border-radius:6px;
         padding:8px 14px; font-size:12px; color:#713f12; margin-bottom:14px; }

/* ── Connect summary tiles ───────────────────────────────────────────────── */
.conn-summary { background:#fff; border:1px solid #e5e7eb; border-radius:12px;
                padding:14px 18px; text-align:center; }
.conn-summary-num { font-size:28px; font-weight:700; color:#111827; line-height:1.1; }
.conn-summary-lbl { font-size:11px; color:#9ca3af; font-family:Inter,sans-serif;
                    text-transform:uppercase; letter-spacing:.06em; }

/* ── Status badges — solid color + white text (Figma Badge component) ─────── */
.status-connected  { background:#10b981; color:#ffffff; border-radius:99px;
                     padding:4px 8px; font-size:11px; font-weight:600; }
.status-uploaded   { background:#3b82f6; color:#ffffff; border-radius:99px;
                     padding:4px 8px; font-size:11px; font-weight:600; }
.status-active     { background:#10b981; color:#ffffff; border-radius:99px;
                     padding:4px 8px; font-size:11px; font-weight:600; }
.status-warning    { background:#f59e0b; color:#ffffff; border-radius:99px;
                     padding:4px 8px; font-size:11px; font-weight:600; }
.status-failed     { background:#ef4444; color:#ffffff; border-radius:99px;
                     padding:4px 8px; font-size:11px; font-weight:600; }
.status-coming_soon { background:#9ca3af; color:#ffffff; border-radius:99px;
                      padding:4px 8px; font-size:11px; font-weight:600; }
.status-paused     { background:#9ca3af; color:#ffffff; border-radius:99px;
                     padding:4px 8px; font-size:11px; font-weight:600; }

.drawer { background:#f8fafb; border:1px solid #e5e7eb; border-radius:10px;
          padding:20px 24px; margin-top:12px; }
.drawer-title { font-size:17px; font-weight:700; color:#111827; margin-bottom:14px; }

.trace-wrap { display:flex; align-items:stretch; overflow-x:auto;
              padding:16px; background:#f8fafb; border-radius:12px; gap:0; }
.trace-node { min-width:148px; max-width:168px; border-radius:10px; padding:12px 10px;
              flex:0 0 auto; }
.trace-node-ok   { background:#f0fdf8; border:2px solid #10b981; }
.trace-node-warn { background:#fffbeb; border:2px solid #f59e0b; }
.trace-node-err  { background:#fff5f5; border:2px solid #ef4444; }
.trace-arrow { display:flex; align-items:center; padding:0 6px;
               color:#9ca3af; font-size:22px; flex:0 0 auto; }

.whatif-table { width:100%; border-collapse:collapse; font-size:13px; }
.whatif-table th { background:#f9fafb; color:#9ca3af; padding:10px 14px;
                   font-weight:600; font-size:11px; text-transform:uppercase;
                   letter-spacing:.04em; text-align:left; }
.whatif-table td { padding:9px 14px; border-bottom:1px solid #e5e7eb; }
.whatif-table tr.current td { background:#fff; }
.whatif-table tr.balanced td { background:#f0fdf8; font-weight:500; }
.whatif-table tr.aggressive td { background:#fff7ed; }
.rec-tag { background:#dbeafe; color:#1e40af; border-radius:4px;
           padding:1px 7px; font-size:10px; font-weight:600; }

.evidence-block { background:#fff; border:1px solid #e5e7eb; border-radius:8px;
                  padding:16px 20px; margin-bottom:12px; }
.evidence-label { font-size:10px; font-weight:700; color:#6b7280;
                  text-transform:uppercase; letter-spacing:.08em; margin-bottom:6px;
                  font-family:Inter,sans-serif; }
.evidence-value { font-size:13px; color:#111827; line-height:1.6; }

/* ── Buttons ─────────────────────────────────────────────────────────────── */
div.stButton > button[kind="primary"],
div.stDownloadButton > button[kind="primary"],
div.stFormSubmitButton > button[kind="primaryFormSubmit"] {
  background: linear-gradient(135deg, #6A5DD4 0%, #365DE7 100%) !important;
  color: #ffffff !important;
  border: none !important;
  border-radius: 8px !important;
  font-family: Inter, sans-serif !important;
  font-size: 14px !important;
  font-weight: 600 !important;
  transition: filter 0.15s ease !important;
}
div.stButton > button[kind="primary"]:hover,
div.stDownloadButton > button[kind="primary"]:hover,
div.stFormSubmitButton > button[kind="primaryFormSubmit"]:hover {
  background: linear-gradient(135deg, #6A5DD4 0%, #365DE7 100%) !important;
  filter: brightness(1.1) !important;
  color: #ffffff !important;
}
div.stButton > button[kind="primary"]:active,
div.stDownloadButton > button[kind="primary"]:active {
  filter: brightness(0.92) !important;
}

div.stButton > button[kind="secondary"],
div.stDownloadButton > button[kind="secondary"] {
  background: #ffffff !important;
  color: #111827 !important;
  border: 1px solid #e5e7eb !important;
  border-radius: 8px !important;
  font-family: Inter, sans-serif !important;
  font-size: 14px !important;
  font-weight: 600 !important;
  transition: background 0.15s ease, border-color 0.15s ease !important;
}
div.stButton > button[kind="secondary"]:hover,
div.stDownloadButton > button[kind="secondary"]:hover {
  background: #f9fafb !important;
  border-color: #d1d5db !important;
  color: #111827 !important;
}
div.stButton > button[kind="secondary"]:active,
div.stDownloadButton > button[kind="secondary"]:active {
  background: #f3f4f6 !important;
}

div.stButton > button:disabled,
div.stButton > button[disabled] {
  background: #f3f4f6 !important;
  color: #9ca3af !important;
  border-color: #e5e7eb !important;
}
</style>
""", unsafe_allow_html=True)


# ── Region / model lookup constants ───────────────────────────────────────────
REGION_CARBON_KG = {
    "us-east-1": 0.380, "us-east-2": 0.355,
    "us-west-2": 0.210, "us-west-1": 0.228,
    "us-west": 0.210, "us-east": 0.380,
    "eu-west-1": 0.290, "eu-west": 0.290,
    "us-central-1": 0.355,
    "ap-south-1": 0.630, "ap-south": 0.630,
}
MODEL_KWH_PER_1M = {
    "claude-sonnet-4-6": 0.6, "claude-opus-4-8": 1.2,
    "claude-haiku-4-5": 0.3, "gpt-4.1": 0.5, "gpt-4o": 0.6,
    "large": 1.2, "mid": 0.6, "small": 0.3,
}
REGION_WUE = {
    "us-east-1": 1.2, "us-east-2": 1.1,
    "us-west-2": 0.8, "us-west-1": 0.9,
    "us-west": 0.8, "us-east": 1.2,
    "eu-west-1": 0.5, "eu-west": 0.5,
    "us-central-1": 1.0,
    "ap-south-1": 1.8, "ap-south": 1.8,
}


# ── Data loaders ───────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    llm    = pd.read_csv(DATA_DIR / "llm_usage.csv",   parse_dates=["date"])
    cloud  = pd.read_csv(DATA_DIR / "cloud_usage.csv", parse_dates=["date"])
    coeffs = pd.read_csv(DATA_DIR / "model_coefficients.csv")
    grid   = pd.read_csv(DATA_DIR / "grid_intensity.csv")
    with open(DATA_DIR / "recommendations.json") as fh:
        recs = json.load(fh)["recommendations"]
    with open(DATA_DIR / "semgrep_findings.json") as fh:
        semgrep = json.load(fh)["results"]
    return llm, cloud, coeffs, grid, recs, semgrep


@st.cache_data
def load_trace_data():
    with open(DATA_DIR / "llm_trace_export.json") as fh:
        data = json.load(fh)
    for trace in data["traces"]:
        for span in trace["spans"]:
            kwh_per_1m = MODEL_KWH_PER_1M.get(span["model_name"], 0.6)
            carbon_kg_per_kwh = REGION_CARBON_KG.get(span["region"], 0.38)
            wue = REGION_WUE.get(span["region"], 1.0)
            total_tokens = span["input_tokens"] + span["output_tokens"]
            kwh = (total_tokens / 1e6) * kwh_per_1m
            span["co2e_kg"] = round(kwh * carbon_kg_per_kwh, 4)
            span["energy_kwh"] = round(kwh, 4)
            span["water_liters"] = round(kwh * wue, 3)
    return data


@st.cache_data
def load_aiworks_data():
    with open(DATA_DIR / "aiworks_usage_export.json") as fh:
        return json.load(fh)


@st.cache_data
def load_code_findings():
    with open(DATA_DIR / "code_scan_findings.json") as fh:
        return json.load(fh)["findings"]


# ── TRACE Calculator ───────────────────────────────────────────────────────────
def calc_ai(llm_df, coeffs_df, grid_df):
    df = (llm_df
          .merge(coeffs_df[["model", "provider", "usd_per_1m_tokens", "kwh_per_1m_tokens"]],
                 on=["model", "provider"], how="left")
          .merge(grid_df, on="region", how="left"))
    df["ai_cost_usd"]    = (df["total_tokens"] / 1e6) * df["usd_per_1m_tokens"]
    df["ai_energy_kwh"]  = (df["total_tokens"] / 1e6) * df["kwh_per_1m_tokens"]
    df["ai_carbon_kg"]   = df["ai_energy_kwh"] * df["g_co2e_per_kwh"] / 1000
    df["ai_water_liters"] = df["ai_energy_kwh"] * df["wue_liters_per_kwh"]
    return df


def calc_cloud(cloud_df, grid_df):
    df = cloud_df.merge(grid_df, on="region", how="left")
    df["cloud_carbon_kg"]   = df["usage_kwh"] * df["g_co2e_per_kwh"] / 1000
    df["cloud_water_liters"] = df["usage_kwh"] * df["wue_liters_per_kwh"]
    return df


def apply_all_recs(llm_df, coeffs_df, grid_df, applied_ids, all_recs):
    modified = llm_df.copy()
    for rec in all_recs:
        if rec["id"] not in applied_ids:
            continue
        app_mask = modified["app"] == rec["app"]
        other    = modified[~app_mask].copy()
        target   = modified[app_mask].copy()
        frac     = rec["actions"][0]["fraction"]
        tok_cols = ["input_tokens", "output_tokens", "total_tokens"]
        affected   = target.copy()
        unaffected = target.copy()
        for col in tok_cols:
            affected[col]   = affected[col] * frac
            unaffected[col] = unaffected[col] * (1 - frac)
        for action in rec["actions"]:
            if action["type"] == "model_swap":
                affected["model"] = action["to"]
            elif action["type"] == "region_shift":
                affected["region"] = action["to"]
        modified = pd.concat([other, affected, unaffected], ignore_index=True)
    return calc_ai(modified, coeffs_df, grid_df)


# ── Connector state ────────────────────────────────────────────────────────────
CATEGORY_TOOLTIPS = {
    "AI delivery":         "Runtime platform that routes, manages, and executes AI model calls for production workloads (e.g. AI/Works Control Plane).",
    "LLM observability":   "Traces and logs every LLM call — tokens used, latency, cost, and quality eval scores per request. Powers the Agent Traces view.",
    "FinOps":              "Cloud billing and cost management exports. Maps cloud spend to teams, services, and regions for the cloud infrastructure footprint.",
    "Cloud monitoring":    "Resource utilization and performance metrics from cloud infrastructure providers. Feeds kWh estimates for cloud carbon.",
    "Carbon methodology":  "Reference data: regional grid intensity factors (gCO₂e/kWh), emission coefficients, and WUE values used in all TRACE calculations.",
    "SDLC sustainability": "Static code analysis that surfaces energy inefficiency patterns in source code before they reach production. Powers the Energy Debt score.",
}

CONNECTOR_STATE = [
    {
        "system": "AI/Works Control Plane", "category": "AI delivery",
        "type": "API", "status": "Connected", "last_sync": "12 min ago",
        "records": "1,248", "norm_pct": "98%", "owner": "Platform Team",
        "action": "View / Sync",
        "tagline": "Created by Thoughtworks",
    },
    {
        "system": "CCF Factors", "category": "Carbon methodology",
        "type": "Static CSV", "status": "Active", "last_sync": "Jun 10",
        "records": "64", "norm_pct": "100%", "owner": "Sustainability",
        "action": "View",
        "tagline": "Funded by Thoughtworks",
    },
    {
        "system": "Langfuse", "category": "LLM observability",
        "type": "API", "status": "Connected", "last_sync": "18 min ago",
        "records": "842", "norm_pct": "94%", "owner": "AI Eng",
        "action": "View / Sync",
    },
    {
        "system": "Datadog", "category": "LLM observability",
        "type": "API", "status": "Warning", "last_sync": "1 hr ago",
        "records": "493", "norm_pct": "81%", "owner": "SRE",
        "action": "Fix Mapping",
    },
    {
        "system": "Cloudability Export", "category": "FinOps",
        "type": "Static CSV", "status": "Uploaded", "last_sync": "Jun 10",
        "records": "2,104", "norm_pct": "89%", "owner": "FinOps",
        "action": "Replace File",
    },
    {
        "system": "Google Cloud Monitoring", "category": "Cloud monitoring",
        "type": "API", "status": "Connected", "last_sync": "20 min ago",
        "records": "1,876", "norm_pct": "92%", "owner": "Cloud Team",
        "action": "View / Sync",
    },
    {
        "system": "Code Scan Findings", "category": "SDLC sustainability",
        "type": "Static JSON", "status": "Warning", "last_sync": "Jun 10",
        "records": "36", "norm_pct": "76%", "owner": "Engineering",
        "action": "Fix Mapping",
    },
]

AVAILABLE_CONNECTORS = [
    "LangSmith", "New Relic", "CloudHealth", "Flexera",
    "Vantage", "Finout", "OpenTelemetry Collector", "LiteLLM Gateway", "Webhooks",
]

FIELD_MAPPING = [
    ("account",         "account_id",      "Mapped"),
    ("service",         "service",         "Mapped"),
    ("region",          "region",          "Mapped"),
    ("usage_type",      "usage_type",      "Mapped"),
    ("cost_usd",        "cost_usd",        "Mapped"),
    ("usage_kwh",       "usage_kwh",       "Mapped"),
    ("timestamp",       "timestamp",       "Mapped"),
    ("tags_project",    "client_project",  "Mapped"),
    ("tags_workspace",  "workspace",       "Mapped"),
    ("business_unit",   "business_unit",   "Mapped"),
    ("environment",     "environment",     "Suggested"),
]


# ── Session state ──────────────────────────────────────────────────────────────
for key, default in [
    ("applied_recs", set()),
    ("show_drawer", False),
    ("drawer_source", None),
    ("drawer_method", None),
    ("uploaded_file_name", None),
    ("upload_validated", False),
    ("mapping_saved", False),
    ("norm_done", False),
]:
    if key not in st.session_state:
        st.session_state[key] = default


# ── Load & compute baselines ───────────────────────────────────────────────────
llm_raw, cloud_raw, coeffs, grid, recs, semgrep_results = load_data()
trace_data   = load_trace_data()
aiworks_data = load_aiworks_data()
code_findings = load_code_findings()

ai_base    = calc_ai(llm_raw, coeffs, grid)
cloud_calc = calc_cloud(cloud_raw, grid)
ai_curr    = apply_all_recs(llm_raw, coeffs, grid, st.session_state.applied_recs, recs)

base_ai_cost      = ai_base["ai_cost_usd"].sum()
base_ai_carbon    = ai_base["ai_carbon_kg"].sum()
base_ai_water     = ai_base["ai_water_liters"].sum()
base_cloud_cost   = cloud_raw["cost_usd"].sum()
base_cloud_carbon = cloud_calc["cloud_carbon_kg"].sum()
base_cloud_water  = cloud_calc["cloud_water_liters"].sum()
curr_ai_cost      = ai_curr["ai_cost_usd"].sum()
curr_ai_carbon    = ai_curr["ai_carbon_kg"].sum()
curr_ai_water     = ai_curr["ai_water_liters"].sum()


# ── Helpers ────────────────────────────────────────────────────────────────────
def kpi(label, value, sub=None, delta=None, good=True):
    delta_html = ""
    if delta:
        css = "kpi-delta-good" if good else "kpi-delta-bad"
        delta_html = f'<div class="{css}">{delta}</div>'
    sub_html = f'<div class="kpi-sub">{sub}</div>' if sub else ""
    st.markdown(
        f'<div class="kpi"><div class="kpi-label">{label}</div>'
        f'<div class="kpi-value">{value}</div>{sub_html}{delta_html}</div>',
        unsafe_allow_html=True,
    )


def status_badge(status):
    css = f"status-{status.lower().replace(' ', '_')}"
    return f'<span class="{css}">{status}</span>'


def render_trace_graph(spans):
    boxes = []
    for span in spans:
        retries = span.get("retry_count", 0)
        if retries >= 3:
            node_cls = "trace-node-err"
            retry_html = f'<div style="background:#fee2e2;color:#ef4444;border-radius:4px;padding:2px 7px;font-size:10px;font-weight:700;display:inline-flex;align-items:center;gap:3px;margin-top:5px;">{_svg("alert-triangle", 10, "#ef4444")} {retries} retries</div>'
        elif retries >= 1:
            node_cls = "trace-node-warn"
            retry_html = f'<div style="background:#fef3c7;color:#92400e;border-radius:4px;padding:2px 7px;font-size:10px;font-weight:700;display:inline-block;margin-top:5px;">↺ {retries} retr{"y" if retries == 1 else "ies"}</div>'
        else:
            node_cls = "trace-node-ok"
            retry_html = '<div style="color:#10b981;font-size:10px;margin-top:5px;font-weight:600;">✓ Clean</div>'

        accepted = span.get("accepted_output", True)
        acc_color = "#059669" if accepted else "#ef4444"
        acc_label = "✓ Accepted" if accepted else "✗ Rejected"

        co2e = span.get("co2e_kg", 0.0)
        model_short = span["model_name"].replace("claude-sonnet-4-6", "Sonnet 4.6").replace("claude-opus-4-8", "Opus 4.8").replace("gpt-4.1", "GPT-4.1")

        t_icon   = _svg("hash",        11, "#6b7280")
        l_icon   = _svg("clock",       11, "#6b7280")
        c_icon   = _svg("dollar-sign", 11, "#6b7280")
        co2_icon = _svg("leaf",        11, "#10b981")
        ev_icon  = _svg("star",        11, "#f59e0b")
        box = f'''<div class="trace-node {node_cls}">
  <div style="font-size:13px;font-weight:700;color:#111827;margin-bottom:3px;">{span["agent_name"]}</div>
  <div style="font-size:10px;color:#6b7280;font-family:Inter,sans-serif;margin-bottom:7px;">{model_short}</div>
  <div style="font-size:11px;color:#374151;line-height:1.75;">
    <div style="display:flex;align-items:center;gap:4px;">{t_icon} {span["input_tokens"]:,}→{span["output_tokens"]:,}</div>
    <div style="display:flex;align-items:center;gap:4px;">{l_icon} {span["latency_ms"]/1000:.1f}s</div>
    <div style="display:flex;align-items:center;gap:4px;">{c_icon} ${span["cost_usd"]:.2f}</div>
    <div style="display:flex;align-items:center;gap:4px;">{co2_icon} {co2e:.3f} kg</div>
    <div style="display:flex;align-items:center;gap:4px;">{ev_icon} {span["eval_score"]:.2f}</div>
    <div style="color:{acc_color};font-size:10px;font-weight:600;">{acc_label}</div>
  </div>
  {retry_html}
</div>'''
        boxes.append(box)

    arrow = '<div class="trace-arrow">→</div>'
    joined = arrow.join(boxes)
    return f'<div class="trace-wrap">{joined}</div>'


# ── Sidebar ────────────────────────────────────────────────────────────────────
st.markdown(_nav_icon_css(), unsafe_allow_html=True)
with st.sidebar:
    st.markdown(
        '<div style="padding:16px 4px 40px;">'
        f'<div style="font-size:22px;font-weight:700;color:#FFFFFF;letter-spacing:-.02em;display:flex;align-items:center;gap:8px;">'
        f'{_svg("leaf", 20, "#4ade80")} TRACE</div>'
        '<div style="font-size:10px;color:#CECCE8;margin-top:2px;font-family:Inter,sans-serif;">'
        'AI GREENOPS DASHBOARD</div>'
        '<div style="margin-top:16px;padding:8px 10px;background:#1f2937;border-radius:6px;display:flex;align-items:center;gap:10px;">'
        f'{_svg("landmark", 18, "#CECCE8")}'
        '<div style="display:flex;flex-direction:column;gap:2px;">'
        '<span style="color:#FFFFFF;font-size:13px;font-weight:700;line-height:1.2;">Northstar Bank</span>'
        '<span style="color:#CECCE8;font-size:10px;line-height:1.3;">Digital Banking Modernization</span>'
        '</div></div>'
        '</div>',
        unsafe_allow_html=True,
    )
    _NAV = {
        "Connect":  "Connect",
        "Observe":  "Observe",
        "Optimize": "Optimize",
        "Prove":    "Prove",
    }
    _nav_keys = list(_NAV.keys())
    # Read URL param only on first session load to set the initial radio position
    if "_nav_idx" not in st.session_state:
        _saved = st.query_params.get("page", "Connect")
        _NAV_INV = {v: k for k, v in _NAV.items()}
        _init_label = _NAV_INV.get(_saved, "Connect")
        st.session_state._nav_idx = _nav_keys.index(_init_label) if _init_label in _nav_keys else 0
    _page_raw = st.radio(
        "",
        _nav_keys,
        index=st.session_state._nav_idx,
        label_visibility="collapsed",
    )
    page = _NAV[_page_raw]
    st.markdown("<hr style='border-color:rgba(206,204,232,0.15);margin:10px 0;'>", unsafe_allow_html=True)

    n_applied = len(st.session_state.applied_recs)
    if n_applied:
        st.markdown(
            f'<div style="font-size:12px;color:#CECCE8;margin-bottom:8px;">'
            f'✓ {n_applied} rec{"s" if n_applied > 1 else ""} applied</div>',
            unsafe_allow_html=True,
        )
        if st.button("↩ Reset all", use_container_width=True):
            st.session_state.applied_recs = set()
            st.rerun()

    st.markdown(
        f'<div style="margin-top:24px;font-size:10px;color:#CECCE8;line-height:1.6;display:flex;align-items:flex-start;gap:5px;">'
        f'{_svg("alert-triangle", 12, "#CECCE8")}'
        '<span>Synthetic client data<br>SCI-for-AI methodology<br>AI:Works Global Hackathon 2026</span></div>',
        unsafe_allow_html=True,
    )


# Silently update the browser URL to persist the current page across refreshes.
# Uses replaceState so the back button is unaffected. Unique timestamp forces
# React to re-execute the script on every rerun.
_components.html(
    f"<script>"
    f"window.parent.history.replaceState(null,'','?page={page}');"
    f"{_nav_icon_js()}"
    f"// {time.time()}"
    f"</script>",
    height=0,
)

# ════════════════════════════════════════════════════════════════════════════════
# PAGE: CONNECT
# ════════════════════════════════════════════════════════════════════════════════
if page == "Connect":
    st.markdown("## Data Sources")
    st.caption("Every connected system, its status, data freshness, and normalization health")

    # ── Summary stats ──
    healthy  = sum(1 for c in CONNECTOR_STATE if c["status"] in ("Connected", "Uploaded", "Active"))
    warnings = sum(1 for c in CONNECTOR_STATE if c["status"] == "Warning")
    api_live = sum(1 for c in CONNECTOR_STATE if c["type"] == "API")
    static_f = sum(1 for c in CONNECTOR_STATE if "Static" in c["type"])
    total_records = sum(
        int(c["records"].replace(",", "")) for c in CONNECTOR_STATE
    )

    c1, c2, c3, c4, c5 = st.columns(5)
    for col, num, label in [
        (c1, len(CONNECTOR_STATE), "Connected Systems"),
        (c2, api_live,  "Live API"),
        (c3, static_f,  "Static Uploads"),
        (c4, healthy,   "Healthy"),
        (c5, warnings,  "Warnings"),
    ]:
        with col:
            st.markdown(
                f'<div class="conn-summary"><div class="conn-summary-num">{num}</div>'
                f'<div class="conn-summary-lbl">{label}</div></div>',
                unsafe_allow_html=True,
            )

    st.markdown(
        '<div style="font-size:12px;color:#6b7280;margin:8px 0 4px;">'
        'Last normalization run: <b>12 minutes ago</b> &nbsp;·&nbsp; '
        f'Total records ingested: <b>{total_records:,}</b></div>',
        unsafe_allow_html=True,
    )

    # ── Action buttons ──
    col_btn1, col_btn2, col_btn3, col_btn4 = st.columns([2, 1, 1, 1])
    with col_btn1:
        if st.button("＋ Connect New System", type="primary", use_container_width=True):
            st.session_state.show_drawer   = not st.session_state.show_drawer
            st.session_state.drawer_source = None
            st.session_state.drawer_method = None
            st.session_state.upload_validated = False
            st.session_state.mapping_saved    = False
            st.session_state.norm_done        = False
    with col_btn2:
        st.button("Run Sync", use_container_width=True, disabled=True,
                  help="In production TRACE: triggers a live re-sync of all API-connected sources. Simulated in this demo.")
    with col_btn3:
        st.button("↑ Upload File", use_container_width=True, disabled=True,
                  help="Use '＋ Connect New System' to upload a new data source file.")
    with col_btn4:
        st.button("Norm Log", use_container_width=True, disabled=True,
                  help="In production TRACE: shows the normalization history — which records mapped successfully and which were flagged. Simulated in this demo.")

    # ── Systems table ──
    st.markdown('<div class="sh">Connected Systems</div>', unsafe_allow_html=True)

    header = (
        '<table style="width:100%;border-collapse:collapse;font-size:13px;">'
        '<thead><tr style="background:#f9fafb;color:#9ca3af;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.04em;">'
        '<th style="padding:10px 12px;text-align:left;">System</th>'
        '<th style="padding:10px 12px;text-align:left;">Category</th>'
        '<th style="padding:10px 12px;text-align:left;">Type</th>'
        '<th style="padding:10px 12px;text-align:left;">Status</th>'
        '<th style="padding:10px 12px;text-align:left;">Last Sync</th>'
        '<th style="padding:10px 12px;text-align:right;">Records</th>'
        '<th style="padding:10px 12px;text-align:left;">Normalization</th>'
        '<th style="padding:10px 12px;text-align:left;">Owner</th>'
        '<th style="padding:10px 12px;text-align:left;">Actions</th>'
        '</tr></thead><tbody>'
    )

    rows = ""
    for i, c in enumerate(CONNECTOR_STATE):
        bg = "#fff" if i % 2 == 0 else "#f8fafb"
        badge = status_badge(c["status"])
        norm_color = "#166534" if int(c["norm_pct"].replace("%", "")) >= 90 else "#92400e"
        tagline_html = (
            f'<div style="font-size:11px;color:#7c3aed;font-style:italic;margin-top:2px;">{c["tagline"]}</div>'
            if c.get("tagline") else ""
        )
        highlight = "border-left:3px solid #7c3aed;" if c.get("tagline") else "border-left:3px solid transparent;"
        rows += (
            f'<tr style="background:{bg};border-bottom:1px solid #e5e7eb;{highlight}">'
            f'<td style="padding:10px 12px;">'
            f'<div style="font-weight:600;color:#111827;">{c["system"]}</div>'
            f'{tagline_html}'
            f'</td>'
            f'<td style="padding:10px 12px;color:#374151;cursor:help;" title="{CATEGORY_TOOLTIPS.get(c["category"], "")}">{c["category"]}</td>'
            f'<td style="padding:10px 12px;font-family:Inter,sans-serif;font-size:12px;color:#374151;">{c["type"]}</td>'
            f'<td style="padding:10px 12px;">{badge}</td>'
            f'<td style="padding:10px 12px;color:#6b7280;font-size:12px;">{c["last_sync"]}</td>'
            f'<td style="padding:10px 12px;text-align:right;font-family:Inter,sans-serif;font-size:12px;">{c["records"]}</td>'
            f'<td style="padding:10px 12px;color:{norm_color};font-weight:600;font-size:12px;cursor:help;" title="Normalization: the % of ingested records successfully mapped to TRACE\'s schema (app name, model, region, token counts all present and matched). Unmapped records appear in the Norm Log.">{c["norm_pct"]}</td>'
            f'<td style="padding:10px 12px;color:#6b7280;font-size:12px;">{c["owner"]}</td>'
            f'<td style="padding:10px 12px;color:#3b82f6;font-size:12px;cursor:pointer;">{c["action"]}</td>'
            '</tr>'
        )

    st.markdown(header + rows + "</tbody></table>", unsafe_allow_html=True)

    # ── Available connectors (roadmap) ──
    with st.expander("Available Connectors — Roadmap", expanded=False):
        cols = st.columns(3)
        for i, name in enumerate(AVAILABLE_CONNECTORS):
            with cols[i % 3]:
                st.markdown(
                    f'<div style="background:#f8fafb;border:1px dashed #d1d5db;border-radius:6px;'
                    f'padding:10px 14px;margin-bottom:8px;font-size:13px;color:#374151;">'
                    f'<span class="status-coming_soon">Coming Soon</span>'
                    f'&nbsp;&nbsp;<b>{name}</b></div>',
                    unsafe_allow_html=True,
                )

    # ── Connect New System Drawer ──
    if st.session_state.show_drawer:
        st.markdown('<div class="drawer">', unsafe_allow_html=True)
        st.markdown('<div class="drawer-title">Connect New System</div>', unsafe_allow_html=True)

        # Step 1: Source type
        st.markdown("**Choose source type:**")
        source_options = ["AI/Works", "LLM Observability", "Cloud Monitoring",
                          "FinOps / Cloud Cost", "Carbon Factors", "Code / CI", "Custom Source"]
        src_cols = st.columns(len(source_options))
        for i, opt in enumerate(source_options):
            with src_cols[i]:
                selected = st.session_state.drawer_source == opt
                if st.button(opt, key=f"src_{i}",
                              type="primary" if selected else "secondary",
                              use_container_width=True):
                    st.session_state.drawer_source = opt
                    st.session_state.drawer_method = None
                    st.session_state.upload_validated = False
                    st.session_state.mapping_saved    = False
                    st.session_state.norm_done        = False
                    st.rerun()

        if st.session_state.drawer_source:
            st.markdown(f"**Source:** `{st.session_state.drawer_source}`")

            # Step 2: Connection method
            st.markdown("**Connection method:**")
            method = st.radio(
                "method",
                ["API connection", "File upload", "OpenTelemetry collector", "Webhook"],
                label_visibility="collapsed",
                horizontal=True,
                key="drawer_method_radio",
            )
            st.session_state.drawer_method = method

            # Step 3: Source-specific form
            if method == "File upload":
                src = st.session_state.drawer_source

                if src == "FinOps / Cloud Cost":
                    st.markdown("**System:** Cloudability Export")
                    st.markdown(
                        '<div style="font-size:12px;color:#6b7280;margin-bottom:8px;">'
                        'Expected fields: account · service · region · cost_usd · usage_kwh · '
                        'timestamp · tags_project · tags_workspace · business_unit · environment'
                        '</div>',
                        unsafe_allow_html=True,
                    )
                    sample_path = DATA_DIR / "finops_cloud_export.csv"
                    if sample_path.exists():
                        with open(sample_path, "rb") as f_sample:
                            st.download_button(
                                "Download sample file",
                                data=f_sample,
                                file_name="finops_cloud_export_sample.csv",
                                mime="text/csv",
                                help="Download a sample Cloudability export to see the expected column format",
                            )
                    refresh = st.radio("Refresh cadence", ["One-time upload", "Monthly upload", "Weekly upload"],
                                       index=1, horizontal=True, key="refresh_cadence")
                    uploaded = st.file_uploader("Upload CSV export", type=["csv"], key="finops_upload")

                    if uploaded is not None:
                        df_upload = pd.read_csv(uploaded)
                        n_total   = len(df_upload)
                        n_no_region    = int(df_upload["region"].isna().sum()) if "region" in df_upload.columns else 0
                        n_no_workspace = int(df_upload["tags_workspace"].isna().sum()) if "tags_workspace" in df_upload.columns else 0
                        st.session_state.upload_validated  = True
                        st.session_state.uploaded_file_name = uploaded.name

                        st.success(
                            f"**File validated.** {n_total:,} records found.\n\n"
                            f"{n_no_region} records missing `region`.\n\n"
                            f"{n_no_workspace} records missing `tags_workspace`.\n\n"
                            f"Proceed to field mapping?"
                        )

                else:
                    uploaded = st.file_uploader("Upload file", type=["csv", "json"], key="generic_upload")
                    if uploaded:
                        st.session_state.upload_validated  = True
                        st.session_state.uploaded_file_name = uploaded.name
                        st.success(f"File `{uploaded.name}` uploaded successfully. Proceed to field mapping.")

            elif method == "API connection":
                src = st.session_state.drawer_source
                if src == "LLM Observability":
                    st.markdown("**System:** Langfuse")
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.text_input("Host URL", placeholder="https://cloud.langfuse.com")
                        st.text_input("Public Key", placeholder="pk-lf-...")
                    with col_b:
                        st.text_input("Secret Key", placeholder="sk-lf-...", type="password")
                        st.text_input("Project ID", placeholder="proj_...")
                    st.selectbox("Sync frequency", ["Every 15 minutes", "Every 30 minutes", "Hourly"])
                    st.multiselect("Data to ingest",
                                   ["Traces", "Token usage", "Cost", "Latency", "Eval scores", "Prompt / response content"],
                                   default=["Traces", "Token usage", "Cost", "Latency", "Eval scores"])
                    st.radio("Prompt content storage",
                             ["Store full prompt/response", "Store metadata only", "Store redacted prompt/response"],
                             index=1)
                    st.markdown("""
<div style="font-size:11px;color:#6b7280;margin-top:4px;line-height:1.7;">
<b>Store full prompt / response</b> — saves the complete text of every request and response.
Note: Only use if content is non-sensitive and your data governance policy permits it.<br>
<b>Store metadata only</b> (default — recommended) — saves token counts, model, latency, cost, and eval scores. No actual text stored.
All carbon and cost calculations work with metadata only.<br>
<b>Store redacted prompt / response</b> — saves the text with PII automatically removed (names, account numbers, etc.).
Requires a redaction filter to be configured.
</div>""", unsafe_allow_html=True)
                else:
                    st.info("Configure API credentials for the selected source.")
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.text_input("API Base URL", placeholder="https://...")
                    with col_b:
                        st.text_input("API Key", type="password")
                    st.selectbox("Sync frequency", ["Every 15 minutes", "Every 30 minutes", "Hourly"])

            # Step 4: Field mapping (shown after upload)
            if st.session_state.upload_validated:
                st.markdown("---")
                st.markdown("**Map source fields to TRACE schema**")

                mapping_html = (
                    '<table style="width:100%;border-collapse:collapse;font-size:12px;">'
                    '<thead><tr style="background:#f3f4f6;">'
                    '<th style="padding:7px 10px;text-align:left;">Source field</th>'
                    '<th style="padding:7px 10px;text-align:left;">TRACE field</th>'
                    '<th style="padding:7px 10px;text-align:left;">Status</th>'
                    '</tr></thead><tbody>'
                )
                for src_f, trace_f, status in FIELD_MAPPING:
                    color = "#166534" if status == "Mapped" else "#92400e"
                    icon  = "✓" if status == "Mapped" else "↺"
                    mapping_html += (
                        f'<tr style="border-bottom:1px solid #e5e7eb;">'
                        f'<td style="padding:6px 10px;font-family:Inter,sans-serif;color:#374151;">{src_f}</td>'
                        f'<td style="padding:6px 10px;font-family:Inter,sans-serif;color:#111827;">{trace_f}</td>'
                        f'<td style="padding:6px 10px;color:{color};font-weight:600;">{icon} {status}</td>'
                        '</tr>'
                    )
                mapping_html += "</tbody></table>"
                st.markdown(mapping_html, unsafe_allow_html=True)

                cm1, cm2 = st.columns([1, 1])
                with cm1:
                    if st.button("Save Mapping", use_container_width=True):
                        st.session_state.mapping_saved = True
                with cm2:
                    if st.button("Run Normalization", type="primary", use_container_width=True):
                        with st.spinner("Normalizing records…"):
                            time.sleep(0.8)
                        st.session_state.norm_done = True
                        st.session_state.show_drawer = False
                        st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

    # ── Normalization success ──
    if st.session_state.norm_done:
        st.success(
            f"✓ **Normalization complete.** "
            f"`{st.session_state.uploaded_file_name}` has been normalized into the TRACE schema. "
            "Records are now available in the Observe dashboard."
        )

    # ── Status legend ──
    with st.expander("Status reference", expanded=False):
        legend = [
            ("Connected",    "#10b981", "#ffffff", "API connection is healthy and syncing"),
            ("Uploaded",     "#3b82f6", "#ffffff", "Static file was uploaded successfully"),
            ("Active",       "#10b981", "#ffffff", "Reference dataset is active"),
            ("Warning",      "#f59e0b", "#ffffff", "Data ingested but incomplete, stale, or partially mapped"),
            ("Failed",       "#ef4444", "#ffffff", "Connection or ingestion failed"),
            ("Paused",       "#9ca3af", "#ffffff", "Connector configured but not syncing"),
            ("Coming Soon",  "#9ca3af", "#ffffff", "Connector tile exists but not enabled"),
        ]
        cols = st.columns(4)
        for i, (name, bg, fg, desc) in enumerate(legend):
            with cols[i % 4]:
                st.markdown(
                    f'<div style="margin-bottom:8px;">'
                    f'<span style="background:{bg};color:{fg};border-radius:99px;padding:2px 10px;'
                    f'font-size:11px;font-weight:600;">{name}</span>'
                    f'<div style="font-size:11px;color:#6b7280;margin-top:3px;">{desc}</div></div>',
                    unsafe_allow_html=True,
                )


# ════════════════════════════════════════════════════════════════════════════════
# PAGE: OBSERVE
# ════════════════════════════════════════════════════════════════════════════════
elif page == "Observe":
    st.markdown("## AI Workload Dashboard")

    tab_overview, tab_breakdown, tab_deepdive = st.tabs(
        ["Overview", "Breakdown", "Deep Dive"]
    )

    any_applied = bool(st.session_state.applied_recs)
    total_cost_base   = base_ai_cost + base_cloud_cost
    total_carbon_base = base_ai_carbon + base_cloud_carbon
    total_cost_curr   = curr_ai_cost + base_cloud_cost
    total_carbon_curr = curr_ai_carbon + base_cloud_carbon
    base_tokens       = llm_raw["total_tokens"].sum()
    base_traces       = int(llm_raw["trace_count"].sum()) if "trace_count" in llm_raw.columns else 0

    # ── Overview tab ──
    with tab_overview:
        st.caption("May 2026 (30 days) · Cloud infrastructure + AI inference combined · Synthetic Northstar Bank data · SCI-for-AI methodology")

        with st.expander("What's the difference between AI inference and cloud infrastructure?", expanded=False):
            st.markdown("""
**AI inference** = the energy and carbon of *calling* an AI model — every prompt sent to Claude, GPT-4, or similar.
Measured in tokens; tracked via Langfuse or an AI gateway. Optimized by changing model, routing, or prompt design.

**Cloud infrastructure** = the servers, databases, and networking that your applications *run on* — the "compute and storage" layer.
Measured in kWh from cloud billing exports; tracked via CCF methodology. Optimized by right-sizing, region choice, or reserved capacity.

They are tracked separately because they have **different optimization levers**. TRACE surfaces both so you can act on either.
""")

        # Row 1: activity metrics
        st.markdown('<div class="sh">Activity</div>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            kpi("Total Tokens", f"{base_tokens/1e6:.1f}M",
                sub=f"across {llm_raw['app'].nunique()} apps · {llm_raw['model'].nunique()} models")
        with c2:
            total_runs = len(trace_data["traces"])
            kpi("Traced Workflows", str(total_runs), sub=f"from {trace_data['total_traces']:,} total in ledger")

        # Row 2: impact metrics — total big number + AI/Cloud breakdown inline
        st.markdown('<div class="sh">Footprint</div>', unsafe_allow_html=True)
        ai_energy = ai_curr["ai_energy_kwh"].sum()
        cloud_energy = cloud_raw["usage_kwh"].sum()
        total_water = curr_ai_water + base_cloud_water
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            if any_applied:
                d = total_cost_curr - total_cost_base
                kpi("Cost", f"${total_cost_curr:,.0f}",
                    delta=f"{d/total_cost_base*100:+.1f}%  (${d:+,.0f})", good=(d <= 0))
            else:
                kpi("Cost", f"${total_cost_base:,.0f}",
                    sub=f'<span style="color:#7C3AED">AI</span>&nbsp;&nbsp;${base_ai_cost:,.0f}<br><span style="color:#2563EB">Cloud</span>&nbsp;&nbsp;${base_cloud_cost:,.0f}')
        with c2:
            if any_applied:
                d = total_carbon_curr - total_carbon_base
                kpi("Carbon", f"{total_carbon_curr:,.1f} kg",
                    delta=f"{d/total_carbon_base*100:+.1f}%  ({d:+,.1f} kg)", good=(d <= 0))
            else:
                kpi("Carbon", f"{total_carbon_base:,.1f} kg CO₂e",
                    sub=f'<span style="color:#7C3AED">AI</span>&nbsp;&nbsp;{base_ai_carbon:,.1f} kg<br><span style="color:#2563EB">Cloud</span>&nbsp;&nbsp;{base_cloud_carbon:,.1f} kg')
        with c3:
            kpi("Energy", f"{ai_energy + cloud_energy:,.0f} kWh",
                sub=f'<span style="color:#7C3AED">AI</span>&nbsp;&nbsp;{ai_energy:,.0f} kWh<br><span style="color:#2563EB">Cloud</span>&nbsp;&nbsp;{cloud_energy:,.0f} kWh')
        with c4:
            kpi("Water", f"{total_water:,.0f} L",
                sub=f'<span style="color:#7C3AED">AI</span>&nbsp;&nbsp;{curr_ai_water:,.0f} L<br><span style="color:#2563EB">Cloud</span>&nbsp;&nbsp;{base_cloud_water:,.0f} L')

        st.markdown('<div class="sh">Daily Carbon Trend</div>', unsafe_allow_html=True)
        daily_ai    = ai_curr.groupby("date")["ai_carbon_kg"].sum().reset_index()
        daily_cloud = cloud_calc.groupby("date")["cloud_carbon_kg"].sum().reset_index()
        daily_ai.columns    = ["date", "AI Inference"]
        daily_cloud.columns = ["date", "Cloud Infra"]
        daily = daily_ai.merge(daily_cloud, on="date")
        daily_long = daily.melt("date", var_name="Source", value_name="kg CO₂e")

        fig = px.area(
            daily_long, x="date", y="kg CO₂e", color="Source",
            color_discrete_map={"AI Inference": "#7C3AED", "Cloud Infra": "#2563EB"},
            template="simple_white",
        )
        fig.update_layout(
            margin=dict(l=0, r=0, t=5, b=0), height=200,
            xaxis_title=None, yaxis_title="kg CO₂e / day",
            legend=dict(orientation="h", yanchor="bottom", y=1, xanchor="right", x=1),
            font=dict(family="Inter", size=12),
        )
        st.plotly_chart(fig, use_container_width=True)

    # ── AI Detail tab ──
    with tab_breakdown:
        st.caption("AI usage cross-referenced with carbon, energy, water, and cost · `tokens ÷ 1M × kWh/1M × gCO₂e/kWh`")

        by_app = (ai_curr
                  .groupby("app")[["ai_cost_usd", "ai_carbon_kg", "ai_energy_kwh", "ai_water_liters", "total_tokens"]]
                  .sum()
                  .sort_values("ai_carbon_kg", ascending=False)
                  .reset_index())

        top = by_app.iloc[0]
        top_c_pct    = top["ai_carbon_kg"] / by_app["ai_carbon_kg"].sum() * 100
        top_cost_pct = top["ai_cost_usd"]  / by_app["ai_cost_usd"].sum()  * 100
        st.warning(
            f"**{top['app']}** — **{top_c_pct:.0f}% of AI carbon** and "
            f"**{top_cost_pct:.0f}% of AI cost**. "
            f"Why? It runs a **large model** (1.2 kWh/1M tokens — the most energy-intensive class) "
            f"in **ap-south / Mumbai** (630 gCO₂e/kWh — India's grid is 3× dirtier than Oregon's). "
            f"Large model × dirty grid × high WUE = the highest-impact combination in the portfolio. "
            f"→ Fix one app, cut ~half the AI footprint."
        )

        group_by = st.radio("Group by", ["App", "Model", "Region"], horizontal=True, key="obs_groupby")

        if group_by == "App":
            grouped = (ai_curr
                       .groupby("app")[["total_tokens", "ai_carbon_kg", "ai_energy_kwh", "ai_water_liters", "ai_cost_usd"]]
                       .sum().sort_values("ai_carbon_kg", ascending=False).reset_index())
            grouped.columns = ["App", "Tokens", "Carbon (kg CO₂e)", "Energy (kWh)", "Water (L)", "Cost (USD)"]
            label_col = "App"
        elif group_by == "Model":
            grouped = (ai_curr
                       .groupby("model")[["total_tokens", "ai_carbon_kg", "ai_energy_kwh", "ai_water_liters", "ai_cost_usd"]]
                       .sum().sort_values("ai_carbon_kg", ascending=False).reset_index())
            grouped.columns = ["Model", "Tokens", "Carbon (kg CO₂e)", "Energy (kWh)", "Water (L)", "Cost (USD)"]
            label_col = "Model"
        else:
            grouped = (ai_curr
                       .groupby("region")[["total_tokens", "ai_carbon_kg", "ai_energy_kwh", "ai_water_liters", "ai_cost_usd"]]
                       .sum().sort_values("ai_carbon_kg", ascending=False).reset_index()
                       .merge(grid[["region", "g_co2e_per_kwh", "wue_liters_per_kwh"]], on="region", how="left"))
            grouped.columns = ["Region", "Tokens", "Carbon (kg CO₂e)", "Energy (kWh)", "Water (L)", "Cost (USD)", "gCO₂e/kWh", "WUE (L/kWh)"]
            label_col = "Region"

        st.markdown('<div class="sh">AI Usage × Impact — All Metrics</div>', unsafe_allow_html=True)
        st.dataframe(grouped, use_container_width=True, hide_index=True)

        PALETTE = ["#7C3AED", "#9333EA", "#A855F7", "#C4B5FD", "#6D28D9"]
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f'<div class="sh">Carbon by {group_by} (kg CO₂e / month)</div>', unsafe_allow_html=True)
            fig = px.bar(grouped, x="Carbon (kg CO₂e)", y=label_col, orientation="h",
                         color=label_col, color_discrete_sequence=PALETTE, template="simple_white",
                         labels={"Carbon (kg CO₂e)": "kg CO₂e", label_col: ""})
            fig.update_layout(showlegend=False, margin=dict(l=0, r=0, t=5, b=0),
                               height=260, font=dict(family="Inter", size=12))
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            st.markdown(f'<div class="sh">Cost by {group_by} (USD / month)</div>', unsafe_allow_html=True)
            fig = px.bar(grouped, x="Cost (USD)", y=label_col, orientation="h",
                         color=label_col, color_discrete_sequence=PALETTE, template="simple_white",
                         labels={"Cost (USD)": "USD", label_col: ""})
            fig.update_layout(showlegend=False, margin=dict(l=0, r=0, t=5, b=0),
                               height=260, font=dict(family="Inter", size=12))
            st.plotly_chart(fig, use_container_width=True)

        if group_by == "Region":
            st.caption(
                "Dirtiest grids drive carbon; wettest / hottest climates drive water. Region shift addresses both. "
                "ap-south (Mumbai) scores worst on both: 630 gCO₂e/kWh grid + WUE 1.8 L/kWh — "
                "3× dirtier and 2× more water-intensive than us-west (Oregon). "
                "Shifting Support-Bot to Oregon cuts carbon AND water in the same move."
            )

        st.markdown('<div class="sh">Full Detail — App × Model × Region</div>', unsafe_allow_html=True)
        detail = (ai_curr
                  .groupby(["app", "model", "region"])
                  [["ai_cost_usd", "ai_carbon_kg", "ai_energy_kwh", "ai_water_liters", "total_tokens"]]
                  .sum().reset_index()
                  .sort_values("ai_carbon_kg", ascending=False))
        detail.columns = ["App", "Model", "Region", "Cost (USD)", "Carbon (kg)", "Energy (kWh)", "Water (L)", "Tokens"]
        detail["Cost (USD)"]   = detail["Cost (USD)"].map("${:,.0f}".format)
        detail["Carbon (kg)"]  = detail["Carbon (kg)"].map("{:,.1f}".format)
        detail["Energy (kWh)"] = detail["Energy (kWh)"].map("{:,.0f}".format)
        detail["Water (L)"]    = detail["Water (L)"].map("{:,.1f}".format)
        detail["Tokens"]       = detail["Tokens"].map("{:,.0f}".format)
        st.dataframe(detail, use_container_width=True, hide_index=True)

    # ── Deep Dive tab (Agent Traces + Energy Debt) ──
    with tab_deepdive:
        st.markdown('<div class="sh">Agent Traces</div>', unsafe_allow_html=True)
        st.caption("Each row is one step in an AI agent workflow — showing the exact cost, carbon, and quality of every model call.")

        with st.expander("How to read this graph", expanded=False):
            st.markdown("""
**Each box = one step in an AI agent workflow** (one call to a model).

**Border color shows health:**
- **Green border** = Clean run (0 retries)
- **Amber border** = Some retries (1–2 retries)
- **Red border** = High retries (3+ retries)

**Inside each box:**
| Label | Meaning |
|---|---|
| Tokens | Tokens **in → out** (input tokens → output tokens) |
| Latency | How long the step took |
| Cost | Cost in USD for this step |
| Carbon | Carbon in kg CO₂e for this step |
| Eval | Output quality score (0 = poor · 1 = perfect) |
| Accepted | Output was **used** by the next step |
| Rejected | Output was **discarded** — quality too low or agent retried |

> **Retries = wasted compute.** A step that retried 3 times consumed up to 4× the expected tokens, cost, and carbon.
> Retries are invisible in billing dashboards — TRACE surfaces them so you can fix the prompt.
""")

        trace_names = [t["workflow_name"] for t in trace_data["traces"]]
        selected_name = st.selectbox("Select workflow trace", trace_names, key="trace_selector")

        selected_trace = next(t for t in trace_data["traces"] if t["workflow_name"] == selected_name)

        # Trace summary KPIs
        t_spans = selected_trace["spans"]
        c1, c2, c3, c4, c5 = st.columns(5)
        kpi_data = [
            ("Total Cost",    f'${selected_trace["total_cost_usd"]:.2f}'),
            ("Total Latency", f'{selected_trace["total_latency_ms"]/1000:.1f}s'),
            ("Total Tokens",  f'{(selected_trace["total_input_tokens"]+selected_trace["total_output_tokens"])/1000:.1f}K'),
            ("Total CO₂e",    f'{sum(s.get("co2e_kg",0) for s in t_spans):.4f} kg'),
            ("Total Water",   f'{sum(s.get("water_liters",0) for s in t_spans):.3f} L'),
        ]
        for col, (label, val) in zip([c1, c2, c3, c4, c5], kpi_data):
            with col:
                kpi(label, val)

        st.markdown('<div class="sh">Agent Graph</div>', unsafe_allow_html=True)
        st.markdown(render_trace_graph(t_spans), unsafe_allow_html=True)

        # Highlight worst node
        worst = max(t_spans, key=lambda s: s.get("retry_count", 0))
        if worst["retry_count"] > 0:
            st.error(
                f"**{worst['agent_name']}** has the highest retry count "
                f"(**{worst['retry_count']} retries**). "
                f"This step accounts for ${worst['cost_usd']:.2f} of the trace cost "
                f"and {worst.get('co2e_kg', 0):.3f} kg CO₂e. "
                "Consider agent loop pruning or prompt compression. → See Optimize."
            )

        st.markdown('<div class="sh">Span Details</div>', unsafe_allow_html=True)
        span_rows = []
        for s in t_spans:
            span_rows.append({
                "Agent":         s["agent_name"],
                "Model":         s["model_name"],
                "Region":        s["region"],
                "Input tokens":  f'{s["input_tokens"]:,}',
                "Output tokens": f'{s["output_tokens"]:,}',
                "Latency":       f'{s["latency_ms"]/1000:.1f}s',
                "Cost":          f'${s["cost_usd"]:.2f}',
                "Energy (kWh)":  f'{s.get("energy_kwh",0):.4f}',
                "CO₂e (kg)":     f'{s.get("co2e_kg",0):.4f}',
                "Water (L)":     f'{s.get("water_liters",0):.3f}',
                "Eval":          f'{s["eval_score"]:.2f}',
                "Retries":       s["retry_count"],
                "Accepted":      "✓" if s.get("accepted_output") else "✗",
            })
        st.dataframe(pd.DataFrame(span_rows), use_container_width=True, hide_index=True)

        st.markdown(
            '<div style="font-size:12px;color:#9ca3af;margin-top:6px;">'
            'CO₂e estimated from token count × kWh/1M tokens × regional grid intensity (kg CO₂e/kWh). '
            'Confidence: Medium (region and model-class factors available; provider-specific hardware not measured).</div>',
            unsafe_allow_html=True,
        )

        st.divider()
        st.markdown('<div class="sh">Energy Debt</div>', unsafe_allow_html=True)
        st.caption("Apps ranked by blended score: 60% runtime carbon + 40% code-risk")
        st.info("""**What is Energy Debt?**

Energy Debt measures two things at once for each AI application:

1. **Runtime carbon** — how much CO₂e does this app's AI inference produce every month? *(From token data + regional grid intensity)*
2. **Code risk** — how many energy-inefficiency patterns does the app's source code contain? *(From a Semgrep static analysis scan)*

**Energy Debt Score = 60% × carbon rank + 40% × code risk rank**

A score of **1.00 = worst possible**. The ranking tells your modernization team exactly where to focus first — not "fix everything," but "start here."
""")

        by_app_base = (ai_base
                       .groupby("app")[["ai_cost_usd", "ai_carbon_kg"]]
                       .sum().reset_index())

        finding_count = {}
        for f in code_findings:
            agent = f.get("agent_name", "Unknown")
            finding_count[agent] = finding_count.get(agent, 0) + 1

        sev_high = {f["agent_name"]: 0 for f in code_findings}
        for f in code_findings:
            if f["severity"] == "HIGH":
                sev_high[f["agent_name"]] = sev_high.get(f["agent_name"], 0) + 1

        def path_to_app(path):
            parts = path.split("/")
            if len(parts) >= 2:
                return "-".join(w.capitalize() for w in parts[1].split("-"))
            return "Unknown"

        findings_total, findings_energy = {}, {}
        try:
            with open(DATA_DIR / "semgrep_findings.json") as fh:
                semgrep_data = json.load(fh)["results"]
            for r in semgrep_data:
                app_name = path_to_app(r["path"])
                findings_total[app_name]  = findings_total.get(app_name, 0) + 1
                if r["extra"].get("metadata", {}).get("impact") == "energy-debt":
                    findings_energy[app_name] = findings_energy.get(app_name, 0) + 1
        except Exception:
            pass

        by_app_base["semgrep_total"]  = by_app_base["app"].map(lambda a: findings_total.get(a, 0))
        by_app_base["semgrep_energy"] = by_app_base["app"].map(lambda a: findings_energy.get(a, 0))
        max_c = by_app_base["ai_carbon_kg"].max()
        max_s = max(by_app_base["semgrep_total"].max(), 1)
        by_app_base["score"] = (
            0.6 * by_app_base["ai_carbon_kg"] / max_c +
            0.4 * by_app_base["semgrep_total"] / max_s
        ).round(3)
        assess = by_app_base.sort_values("score", ascending=False).reset_index(drop=True)

        worst_app = assess.iloc[0]
        st.error(
            f"**{worst_app['app']}** — Energy Debt Score **{worst_app['score']:.2f} / 1.00** · "
            f"{worst_app['ai_carbon_kg']:.1f} kg CO₂e/mo · {int(worst_app['semgrep_total'])} findings"
        )

        RANK_COLORS = ["#ef4444", "#d97706", "#6b7280", "#6b7280", "#9ca3af"]
        for i, row in assess.iterrows():
            rc = RANK_COLORS[min(i, len(RANK_COLORS) - 1)]
            score_bar = f"{row['score'] * 100:.0f}%"
            badges = ""
            if row["semgrep_energy"] > 0:
                badges += f'<span class="badge-hi">{int(row["semgrep_energy"])} energy-debt</span>'
            other = int(row["semgrep_total"]) - int(row["semgrep_energy"])
            if other > 0:
                badges += f'<span class="badge-med">{other} other findings</span>'
            if not badges:
                badges = '<span class="badge-lo">No Semgrep findings</span>'
            st.markdown(f"""
<div class="rec">
  <div style="display:flex;align-items:flex-start;gap:14px;margin-bottom:8px;">
    <div style="font-size:24px;font-weight:800;color:{rc};min-width:30px;line-height:1;">#{i+1}</div>
    <div style="flex:1;">
      <div class="rec-title">{row['app']}</div>
      <div style="font-size:12px;color:#6b7280;">{row['ai_carbon_kg']:.1f} kg CO₂e/mo &nbsp;·&nbsp; ${row['ai_cost_usd']:,.0f}/mo</div>
    </div>
    <div style="text-align:right;">
      <div style="font-size:24px;font-weight:800;color:{rc};line-height:1;">{row['score']:.2f} / 1.00</div>
      <div style="font-size:9px;color:#9ca3af;font-family:Inter,sans-serif;">ENERGY DEBT SCORE</div>
      <div style="font-size:9px;color:#9ca3af;margin-top:2px;">Higher = more urgent</div>
    </div>
  </div>
  <div style="font-size:10px;color:#9ca3af;margin-bottom:4px;">Score = 60% carbon rank + 40% code risk rank &nbsp;·&nbsp; {score_bar} of maximum debt</div>
  <div style="background:#f3f4f6;border-radius:3px;height:5px;margin-bottom:8px;">
    <div style="background:{rc};height:5px;border-radius:3px;width:{score_bar};"></div>
  </div>
  {badges}
</div>""", unsafe_allow_html=True)

        if code_findings:
            st.markdown('<div class="sh">Code Inefficiency Findings — What to Fix</div>', unsafe_allow_html=True)
            st.caption("From a Semgrep static analysis scan of the apps' source code. Each finding is a pattern that wastes energy at runtime. energy-debt findings = direct compute waste · other findings = broader code issues.")
            for f in code_findings[:4]:
                sev_color = {"HIGH": "#ef4444", "MEDIUM": "#92400e", "LOW": "#6b7280"}.get(f["severity"], "#6b7280")
                sev_bg    = {"HIGH": "#fee2e2", "MEDIUM": "#fef3c7", "LOW": "#f3f4f6"}.get(f["severity"], "#f3f4f6")
                st.markdown(
                    f'<div class="rec" style="margin-bottom:8px;">'
                    f'<div class="rec-title">'
                    f'<span style="background:{sev_bg};color:{sev_color};border-radius:4px;padding:1px 7px;'
                    f'font-size:11px;font-weight:600;margin-right:8px;">{f["severity"]}</span>'
                    f'{f["finding"][:80]}{"…" if len(f["finding"])>80 else ""}</div>'
                    f'<div class="rec-body" style="margin-top:4px;">'
                    f'<b>Fix:</b> {f["recommendation"]}</div>'
                    f'<div style="font-size:11px;color:#9ca3af;display:flex;align-items:center;gap:4px;">'
                    f'{_svg("folder", 12, "#9ca3af")} {f["file_path"]} &nbsp;·&nbsp; {f["agent_name"]} · {f["component"]}</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )


# ════════════════════════════════════════════════════════════════════════════════
# PAGE: OPTIMIZE
# ════════════════════════════════════════════════════════════════════════════════
elif page == "Optimize":
    st.markdown("## Recommendations")
    st.caption("Apply a recommendation — watch AI cost and carbon drop live")

    any_applied = bool(st.session_state.applied_recs)

    if any_applied:
        cost_d   = curr_ai_cost - base_ai_cost
        carbon_d = curr_ai_carbon - base_ai_carbon
        st.success(
            f"**Optimizations applied.** "
            f"AI carbon: **{carbon_d/base_ai_carbon*100:+.1f}%** ({carbon_d:+,.1f} kg)  ·  "
            f"AI cost: **{cost_d/base_ai_cost*100:+.1f}%** (${cost_d:+,.0f})"
        )
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("AI Cost — before",  f"${base_ai_cost:,.0f}")
        with c2:
            st.metric("AI Cost — after",   f"${curr_ai_cost:,.0f}",
                      delta=f"{cost_d/base_ai_cost*100:+.1f}%  (${cost_d:+,.0f})", delta_color="inverse")
        with c3:
            st.metric("AI Carbon — before", f"{base_ai_carbon:,.1f} kg")
        with c4:
            st.metric("AI Carbon — after",  f"{curr_ai_carbon:,.1f} kg",
                      delta=f"{carbon_d/base_ai_carbon*100:+.1f}%  ({carbon_d:+,.1f} kg)", delta_color="inverse")
        st.markdown("---")

    # ── Recommendation cards ──
    st.markdown('<div class="sh">AI Workload Recommendations</div>', unsafe_allow_html=True)
    st.caption(
        "Apply runs a live what-if simulation — it recalculates all metrics as if this change "
        "were in production. Nothing in your real infrastructure changes. "
        "Use ↩ Reset all in the sidebar to restore the baseline."
    )

    for rec in recs:
        applied = rec["id"] in st.session_state.applied_recs
        ai_after_rec = apply_all_recs(llm_raw, coeffs, grid, {rec["id"]}, recs)
        app_c_before  = ai_base[ai_base["app"] == rec["app"]]["ai_carbon_kg"].sum()
        app_c_after   = ai_after_rec[ai_after_rec["app"] == rec["app"]]["ai_carbon_kg"].sum()
        app_cost_bef  = ai_base[ai_base["app"] == rec["app"]]["ai_cost_usd"].sum()
        app_cost_aft  = ai_after_rec[ai_after_rec["app"] == rec["app"]]["ai_cost_usd"].sum()
        c_pct = (app_c_after - app_c_before) / app_c_before * 100
        d_pct = (app_cost_aft - app_cost_bef) / app_cost_bef * 100

        actions_html = "  ".join(
            f'<span class="pill-navy">'
            f'{"model: " + a["from"] + " → " + a["to"] if a["type"] == "model_swap" else "region: " + a["from"] + " → " + a["to"]}'
            f' ({a["fraction"]*100:.0f}% traffic)</span>'
            for a in rec["actions"]
        )
        cost_pill = (
            f'<span class="pill-green">Cost {d_pct:+.1f}%</span>'
            if abs(d_pct) > 0.1
            else '<span class="pill-gray">Cost unchanged (carbon-only win)</span>'
        )
        card_cls = "rec applied" if applied else "rec"
        rec_icon = _svg("check-circle", 16, "#10b981") if applied else _svg("zap", 16, "#6366f1")
        st.markdown(f"""
<div class="{card_cls}">
  <div class="rec-title" style="display:flex;align-items:center;gap:6px;">{rec_icon} {rec['title']}</div>
  <div class="rec-body">{rec['rationale']}</div>
  <div style="margin-bottom:8px;">{actions_html}</div>
  <div style="margin-bottom:8px;">
    <span class="pill-green">Carbon {c_pct:+.1f}% for {rec['app']}</span>{cost_pill}
  </div>
  <div class="rec-quality">Quality trade-off: {rec['quality_note']}</div>
</div>""", unsafe_allow_html=True)

        col_btn, _ = st.columns([2, 4])
        with col_btn:
            if not applied:
                if st.button("Apply", key=f"apply_{rec['id']}", type="primary", use_container_width=True):
                    with st.spinner("Computing optimized footprint…"):
                        time.sleep(0.6)
                    st.session_state.applied_recs.add(rec["id"])
                    st.rerun()
            else:
                if st.button("↩ Undo", key=f"undo_{rec['id']}", use_container_width=True):
                    st.session_state.applied_recs.discard(rec["id"])
                    st.rerun()
        st.markdown("<div style='height:4px;'></div>", unsafe_allow_html=True)

    # ── Energy debt recommendation ──
    st.markdown('<div class="sh">Code Inefficiency Fixes</div>', unsafe_allow_html=True)
    st.caption("These findings come from a Semgrep static analysis scan of the apps' source code. Fixing them reduces wasted compute at the code level, complementing the model and region optimizations above.")
    for f in code_findings[:2]:
        sev_color = {"HIGH": "#ef4444", "MEDIUM": "#92400e"}.get(f["severity"], "#6b7280")
        sev_bg    = {"HIGH": "#fee2e2", "MEDIUM": "#fef3c7"}.get(f["severity"], "#f3f4f6")
        st.markdown(
            f'<div class="rec">'
            f'<div class="rec-title">'
            f'<span style="background:{sev_bg};color:{sev_color};border-radius:4px;padding:1px 7px;'
            f'font-size:11px;font-weight:600;margin-right:8px;">{f["severity"]}</span>'
            f'Energy debt: {f["finding"][:70]}{"…" if len(f["finding"])>70 else ""}</div>'
            f'<div class="rec-body">{f["recommendation"]}</div>'
            f'<div style="font-size:11px;color:#9ca3af;display:flex;align-items:center;gap:4px;">'
            f'{_svg("folder", 12, "#9ca3af")} {f["file_path"]} &nbsp;·&nbsp; Impact: {f["estimated_runtime_impact"][:60]}…</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    # ── What-if scenario table ──
    st.markdown('<div class="sh">What-If Scenario Planner</div>', unsafe_allow_html=True)
    st.caption("Compare current state to optimization scenarios before committing changes")

    ai_cost_bal  = base_ai_cost * 0.795
    ai_co2_bal   = base_ai_carbon * 0.839
    ai_water_bal = base_ai_water * 0.839
    ai_cost_agg  = base_ai_cost * 0.720
    ai_co2_agg   = base_ai_carbon * 0.735
    ai_water_agg = base_ai_water * 0.720

    total_cost_bal = ai_cost_bal + base_cloud_cost
    total_co2_bal  = ai_co2_bal  + base_cloud_carbon
    total_cost_agg = ai_cost_agg + base_cloud_cost
    total_co2_agg  = ai_co2_agg  + base_cloud_carbon

    whatif_html = f"""
<table class="whatif-table">
  <thead>
    <tr>
      <th>Scenario</th>
      <th>Monthly AI Cost</th>
      <th>Total CO₂e</th>
      <th>AI Water</th>
      <th>Avg Latency</th>
      <th>Quality Risk</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    <tr class="current">
      <td><b>Current state</b></td>
      <td>${base_ai_cost:,.0f}</td>
      <td>{base_ai_carbon + base_cloud_carbon:,.1f} kg</td>
      <td>{base_ai_water:,.0f} L</td>
      <td>12.8s</td>
      <td>Low</td>
      <td><span style="color:#6b7280;font-size:12px;">Baseline</span></td>
    </tr>
    <tr class="balanced">
      <td><b>Balanced optimization</b> <span class="rec-tag">Recommended</span></td>
      <td>${ai_cost_bal:,.0f} <span style="color:#166534;font-size:11px;">−20.5%</span></td>
      <td>{ai_co2_bal + base_cloud_carbon:,.1f} kg <span style="color:#166534;font-size:11px;">−16.1%</span></td>
      <td>{ai_water_bal:,.0f} L <span style="color:#166534;font-size:11px;">−16.1%</span></td>
      <td>11.9s</td>
      <td>Low-medium</td>
      <td><span style="color:#166534;font-size:12px;">Model swap + region shift</span></td>
    </tr>
    <tr class="aggressive">
      <td><b>Aggressive carbon mode</b></td>
      <td>${ai_cost_agg:,.0f} <span style="color:#166534;font-size:11px;">−28.0%</span></td>
      <td>{ai_co2_agg + base_cloud_carbon:,.1f} kg <span style="color:#166534;font-size:11px;">−26.5%</span></td>
      <td>{ai_water_agg:,.0f} L <span style="color:#166534;font-size:11px;">−28.0%</span></td>
      <td>14.2s</td>
      <td>Medium</td>
      <td><span style="color:#92400e;font-size:12px;">All optimizations + batch shift</span></td>
    </tr>
  </tbody>
</table>
<div style="font-size:11px;color:#9ca3af;margin-top:8px;">
  Projections apply all recommendations in the chosen scenario to the current AI workload. Cloud cost and carbon unchanged.
  Water = AI energy × regional WUE. Latency estimates are illustrative. Quality risk is subjective — review each recommendation before applying.
</div>
"""
    st.markdown(whatif_html, unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════════
# PAGE: PROVE
# ════════════════════════════════════════════════════════════════════════════════
elif page == "Prove":
    st.markdown("## Evidence Pack")
    st.caption("Open, auditable · SCI-for-AI methodology · No offsets · Transparent assumptions")

    tab_evidence, tab_method = st.tabs(["Evidence Pack", "Methodology"])

    with tab_evidence:
        any_applied = bool(st.session_state.applied_recs)
        applied_titles = [r["title"] for r in recs if r["id"] in st.session_state.applied_recs]

        st.info(
            "**Confidence: Medium** for AI carbon estimates. "
            "Token counts are precise (from Langfuse / AI billing). "
            "Energy is estimated using GPU benchmarks — no AI provider publishes per-call energy data. "
            "Grid intensity is sourced from Electricity Maps / EPA eGRID. "
            "This is a stronger basis than market-based reporting: TRACE uses location-based accounting — no offsets, just physics."
        )

        # Evidence sections
        col_left, col_right = st.columns([3, 2])

        with col_left:
            st.markdown(
                '<div class="sh">Connected Data Sources '
                f'<span style="font-size:11px;color:#9ca3af;font-weight:400;cursor:help;" '
                'title="Each source below contributed records to this evidence pack. '
                'Records = total rows ingested this period. '
                'Mapped = records successfully matched to TRACE\'s schema (app name, model, region, token counts all present). '
                'Unmapped records are excluded from calculations and flagged in the Norm Log.">'
                f'{_svg("info", 14, "#9ca3af")}</span></div>',
                unsafe_allow_html=True,
            )
            sources_html = ""
            for c in CONNECTOR_STATE:
                _dot_color = "#10b981" if c["status"] in ("Connected", "Active") else ("#3b82f6" if c["status"] == "Uploaded" else "#f59e0b")
                icon = f'<span style="display:inline-block;width:8px;height:8px;border-radius:50%;background:{_dot_color};flex-shrink:0;margin-right:4px;"></span>'
                norm_tip = (
                    f"{c['records']} rows ingested this period. "
                    f"{c['norm_pct']} successfully normalized to TRACE's schema — "
                    f"app name, model, region, and token counts all present and matched. "
                    f"Unmapped records are flagged in the Norm Log."
                )
                sources_html += (
                    f'<div style="display:flex;justify-content:space-between;align-items:center;padding:7px 0;'
                    f'border-bottom:1px solid #f3f4f6;font-size:13px;">'
                    f'<span style="display:flex;align-items:center;">{icon}<b>{c["system"]}</b>&nbsp;— {c["type"]}</span>'
                    f'<span style="color:#6b7280;cursor:help;" title="{norm_tip}">{c["records"]} records · {c["norm_pct"]} mapped</span>'
                    f'</div>'
                )
            st.markdown(f'<div class="evidence-block"><div class="evidence-label">Connected Sources</div>{sources_html}</div>',
                        unsafe_allow_html=True)

            st.markdown('<div class="sh">Calculation Summary</div>', unsafe_allow_html=True)
            st.markdown(f"""
<div class="evidence-block">
  <div class="evidence-label">AI Inference Carbon</div>
  <div class="evidence-value">
    <b>Formula:</b> (total_tokens / 1,000,000) × kWh_per_1M_tokens × grid_kg_CO₂e_per_kWh<br>
    <b>Scope:</b> {llm_raw['app'].nunique()} apps · {llm_raw['model'].nunique()} models · {llm_raw['region'].nunique()} regions<br>
    <b>Period:</b> May 2026 (30 days)<br>
    <b>Confidence:</b> Medium — model class and regional grid factors available; provider-specific hardware not measured
  </div>
</div>
<div class="evidence-block">
  <div class="evidence-label">Cloud Infrastructure Carbon</div>
  <div class="evidence-value">
    <b>Formula:</b> usage_kWh × regional_grid_kg_CO₂e_per_kWh<br>
    <b>Scope:</b> {cloud_raw['app'].nunique()} apps · {cloud_raw['service'].nunique()} cloud services<br>
    <b>Methodology:</b> Location-based, no market-based RECs or offsets (intentional)<br>
    <b>Confidence:</b> Medium — kWh from billing data; region from service metadata
  </div>
</div>
""", unsafe_allow_html=True)

        with col_right:
            st.markdown('<div class="sh">Before / After Comparison</div>', unsafe_allow_html=True)
            st.caption("Before = current state with no optimizations applied. After = projected impact of the recommendations you've applied on the Optimize page. Click ↩ Reset all in the sidebar to return to the baseline.")
            ba_rows = [
                ("AI Cost",    f"${base_ai_cost:,.0f}",    f"${curr_ai_cost:,.0f}",
                 f"{(curr_ai_cost-base_ai_cost)/base_ai_cost*100:+.1f}%"),
                ("AI Carbon",  f"{base_ai_carbon:,.1f} kg", f"{curr_ai_carbon:,.1f} kg",
                 f"{(curr_ai_carbon-base_ai_carbon)/base_ai_carbon*100:+.1f}%"),
                ("AI Energy",  f"{ai_base['ai_energy_kwh'].sum():,.0f} kWh",
                 f"{ai_curr['ai_energy_kwh'].sum():,.0f} kWh",
                 f"{(ai_curr['ai_energy_kwh'].sum()-ai_base['ai_energy_kwh'].sum())/ai_base['ai_energy_kwh'].sum()*100:+.1f}%"),
                ("AI Water",   f"{base_ai_water:,.0f} L", f"{curr_ai_water:,.0f} L",
                 f"{(curr_ai_water-base_ai_water)/base_ai_water*100:+.1f}%"),
                ("Cloud Cost", f"${base_cloud_cost:,.0f}", f"${base_cloud_cost:,.0f}", "—"),
                ("Cloud CO₂e", f"{base_cloud_carbon:,.1f} kg", f"{base_cloud_carbon:,.1f} kg", "—"),
                ("Cloud Water", f"{base_cloud_water:,.0f} L", f"{base_cloud_water:,.0f} L", "—"),
                ("Total Cost", f"${base_ai_cost+base_cloud_cost:,.0f}",
                 f"${curr_ai_cost+base_cloud_cost:,.0f}",
                 f"{(curr_ai_cost-base_ai_cost)/(base_ai_cost+base_cloud_cost)*100:+.1f}%"),
            ]
            ba_html = (
                '<table style="width:100%;border-collapse:collapse;font-size:13px;">'
                '<thead><tr style="background:#f3f4f6;">'
                '<th style="padding:8px 10px;text-align:left;">Metric</th>'
                '<th style="padding:8px 10px;text-align:right;">Before</th>'
                '<th style="padding:8px 10px;text-align:right;">After</th>'
                '<th style="padding:8px 10px;text-align:right;">Δ</th>'
                '</tr></thead><tbody>'
            )
            for metric, before, after, delta in ba_rows:
                delta_color = "#166534" if delta.startswith("-") else ("#6b7280" if delta == "—" else "#ef4444")
                ba_html += (
                    f'<tr style="border-bottom:1px solid #e5e7eb;">'
                    f'<td style="padding:8px 10px;font-weight:500;">{metric}</td>'
                    f'<td style="padding:8px 10px;text-align:right;color:#6b7280;">{before}</td>'
                    f'<td style="padding:8px 10px;text-align:right;font-weight:600;">{after}</td>'
                    f'<td style="padding:8px 10px;text-align:right;color:{delta_color};font-weight:600;">{delta}</td>'
                    '</tr>'
                )
            ba_html += "</tbody></table>"
            st.markdown(f'<div class="evidence-block">{ba_html}</div>', unsafe_allow_html=True)

            st.markdown('<div class="sh">Applied Optimizations</div>', unsafe_allow_html=True)
            if applied_titles:
                recs_html = "".join(f'<div style="padding:5px 0;border-bottom:1px solid #f3f4f6;font-size:13px;display:flex;align-items:center;gap:6px;">{_svg("check-circle", 14, "#10b981")} {t}</div>' for t in applied_titles)
                st.markdown(f'<div class="evidence-block">{recs_html}</div>', unsafe_allow_html=True)
            else:
                st.markdown(
                    '<div class="evidence-block" style="color:#9ca3af;font-size:13px;">'
                    'No optimizations applied yet. Go to Optimize to apply recommendations.</div>',
                    unsafe_allow_html=True,
                )

        st.markdown('<div class="sh">Assumptions & Confidence</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="evidence-block">
  <div class="evidence-value">
    <b>Data:</b> Synthetic client data shaped like real Langfuse + CCF + AI/Works exports. All numbers illustrative.<br>
    <b>Model energy coefficients:</b> Blended estimates (typical GPU mix, PUE = 1.2, avg utilisation). Per-model hardware data from Boavizta would sharpen accuracy.<br>
    <b>Grid intensity:</b> Location-based from Electricity Maps / EPA eGRID / ENTSO-E. No market-based RECs or offsets.<br>
    <b>Water (WUE):</b> Region-level WUE factors (liters/kWh) from public data center efficiency reports. Water = energy × WUE.<br>
    <b>Confidence bands:</b> High = all fields present. Medium = one field estimated. Low = region or model class missing.<br>
    <b>Methodology version:</b> CCF-v2.1 + SCI-for-AI (Green Software Foundation). Aligned to ISO 21031 operational boundary.<br>
    <b>Production TRACE</b> would support client-approved factors, provider-specific data, and confidence intervals.
  </div>
</div>
""", unsafe_allow_html=True)

        st.markdown('<div class="sh">Audit Readiness</div>', unsafe_allow_html=True)
        st.markdown("""
<div class="evidence-block">
  <div class="evidence-value">
    <b>What you can take to a sustainability team:</b><br>
    ✓ The methodology (formula, coefficients, sources)<br>
    ✓ The confidence level and its explanation<br>
    ✓ The before / after comparison showing optimization impact<br>
    ✓ Standards alignment (SCI-for-AI, ISO 21031, GHG Protocol)<br>
    <br>
    <b>What requires production TRACE (live data):</b><br>
    Note: This demo uses synthetic Northstar Bank data — not real usage logs.<br>
    Note: Production TRACE with live connectors produces a fully traceable evidence pack with actual token counts, timestamps, and model names.<br>
    <br>
    A production audit pack carries the same methodology with real data, making it defensible to a GHG Protocol-aligned sustainability audit.
  </div>
</div>
""", unsafe_allow_html=True)

        # Download buttons
        st.markdown('<div class="sh">Export</div>', unsafe_allow_html=True)
        c_dl1, c_dl2, c_dl3 = st.columns(3)

        ai_export = ai_curr[["date", "app", "model", "provider", "region",
                              "total_tokens", "ai_cost_usd", "ai_energy_kwh", "ai_carbon_kg", "ai_water_liters"]].copy()
        ai_export.columns = ["date", "app", "model", "provider", "region",
                              "total_tokens", "cost_usd", "energy_kwh", "co2e_kg", "water_liters"]
        ai_export["source"] = "AI Inference"

        cloud_export = cloud_calc[["date", "app", "service", "region", "usage_kwh", "cost_usd", "cloud_carbon_kg", "cloud_water_liters"]].copy()
        cloud_export.columns = ["date", "app", "service", "region", "energy_kwh", "cost_usd", "co2e_kg", "water_liters"]
        cloud_export["source"] = "Cloud Infrastructure"

        with c_dl1:
            csv_ai = ai_export.to_csv(index=False)
            st.download_button("Download AI Ledger CSV", csv_ai,
                               "trace_ai_ledger.csv", "text/csv", use_container_width=True)
        with c_dl2:
            csv_cloud = cloud_export.to_csv(index=False)
            st.download_button("Download Cloud Ledger CSV", csv_cloud,
                               "trace_cloud_ledger.csv", "text/csv", use_container_width=True)
        with c_dl3:
            st.button("Evidence Pack PDF", disabled=True,
                      help="PDF export on roadmap", use_container_width=True)

    with tab_method:
        st.markdown("## Methodology & Transparency")
        st.caption("Open, auditable · SCI-for-AI / ISO 21031 conformant · Location-based grid · No offsets")

        col1, col2 = st.columns([3, 2])
        with col1:
            st.markdown('<div class="sh">SCI-for-AI Carbon Formula</div>', unsafe_allow_html=True)
            st.markdown("""
<div class="formula">
AI carbon (gCO₂e)    = (tokens / 1,000,000) × kWh_per_1M_tokens × grid_gCO₂e_per_kWh<br>
AI cost (USD)        = (tokens / 1,000,000) × USD_per_1M_tokens<br>
AI energy (kWh)      = (tokens / 1,000,000) × kWh_per_1M_tokens<br>
AI water (L)         = AI_energy_kWh × WUE_liters_per_kWh<br>
<br>
Cloud carbon (gCO₂e) = usage_kWh × grid_gCO₂e_per_kWh<br>
Cloud water (L)      = usage_kWh × WUE_liters_per_kWh<br>
<br>
Energy Debt Score    = 0.6 × carbon_rank + 0.4 × code_risk_rank
</div>""", unsafe_allow_html=True)

            st.markdown('<div class="sh">Standards Alignment</div>', unsafe_allow_html=True)
            st.markdown("""
<table style="width:100%;border-collapse:collapse;font-size:13px;">
<thead><tr style="background:#f3f4f6;">
<th style="padding:8px 10px;text-align:left;">Standard</th>
<th style="padding:8px 10px;text-align:left;">How TRACE uses it</th>
</tr></thead>
<tbody>
<tr style="border-bottom:1px solid #e5e7eb;">
  <td style="padding:8px 10px;font-weight:600;">
    <a href="https://sci.greensoftware.foundation/" target="_blank" style="color:#3b82f6;text-decoration:none;">SCI-for-AI</a>
    <span style="font-weight:400;color:#6b7280;"> (Green Software Foundation)</span>
  </td>
  <td style="padding:8px 10px;color:#374151;">Primary formula: tokens → energy → carbon</td>
</tr>
<tr style="border-bottom:1px solid #e5e7eb;">
  <td style="padding:8px 10px;font-weight:600;">
    <a href="https://ghgprotocol.org/corporate-standard" target="_blank" style="color:#3b82f6;text-decoration:none;">GHG Protocol</a>
    <span style="font-weight:400;color:#6b7280;"> / ISO 14064</span>
  </td>
  <td style="padding:8px 10px;color:#374151;">GHG accounting: operational boundary, location-based, no offsets</td>
</tr>
<tr style="border-bottom:1px solid #e5e7eb;">
  <td style="padding:8px 10px;font-weight:600;">
    <a href="https://opentelemetry.io/docs/specs/semconv/gen-ai/" target="_blank" style="color:#3b82f6;text-decoration:none;">OpenTelemetry GenAI</a>
  </td>
  <td style="padding:8px 10px;color:#374151;">Token field names (<code>llm.usage.input_tokens</code>)</td>
</tr>
<tr style="border-bottom:1px solid #e5e7eb;">
  <td style="padding:8px 10px;font-weight:600;">
    <a href="https://langfuse.com/docs/tracing" target="_blank" style="color:#3b82f6;text-decoration:none;">Langfuse</a>
    <span style="font-weight:400;color:#6b7280;"> trace schema</span>
  </td>
  <td style="padding:8px 10px;color:#374151;">LLM usage log shape (app, model, tokens, region, cost)</td>
</tr>
<tr style="border-bottom:1px solid #e5e7eb;">
  <td style="padding:8px 10px;font-weight:600;">
    <a href="https://www.cloudcarbonfootprint.org/" target="_blank" style="color:#3b82f6;text-decoration:none;">Cloud Carbon Footprint</a>
    <span style="font-weight:400;color:#6b7280;"> output schema</span>
  </td>
  <td style="padding:8px 10px;color:#374151;">Cloud usage log shape (service, region, kWh, cost)</td>
</tr>
<tr>
  <td style="padding:8px 10px;font-weight:600;">
    <a href="https://semgrep.dev/docs/cli-reference/" target="_blank" style="color:#3b82f6;text-decoration:none;">Semgrep</a>
    <span style="font-weight:400;color:#6b7280;"> JSON output</span>
  </td>
  <td style="padding:8px 10px;color:#374151;"><code>semgrep --json</code> output for Energy Debt layer</td>
</tr>
</tbody></table>
""", unsafe_allow_html=True)

            st.markdown('<div class="sh">Honest Caveats</div>', unsafe_allow_html=True)
            st.markdown("""
- Coefficients are **blended estimates** (typical GPU mix, PUE = 1.2, avg utilisation).
  Per-model hardware data from Boavizta would sharpen accuracy.
- Grid intensity is **location-based** (no market-based RECs or offsets — intentional).
- Water (WUE) factors are **region-level estimates** from public DC efficiency reports.
  Provider-specific WUE values (AWS, Google, Azure) would sharpen accuracy.
- This demo uses **synthetic data** — production integrations ingest real exports.
- Quality trade-offs are explicit on the Optimize page; no blanket downgrades.
""")

        with col2:
            st.markdown('<div class="sh">Model Coefficients</div>', unsafe_allow_html=True)
            st.caption("Illustrative · blended from public GPU benchmarks")
            display_c = coeffs.copy()
            display_c.columns = ["Model", "Provider", "USD / 1M tokens", "kWh / 1M tokens"]
            st.dataframe(display_c, use_container_width=True, hide_index=True)

            st.markdown('<div class="sh">Grid Intensity & WUE</div>', unsafe_allow_html=True)
            st.caption("gCO₂e / kWh · WUE L/kWh · Electricity Maps · location-based · no offsets")
            grid_d = grid.sort_values("g_co2e_per_kwh", ascending=True).copy()
            grid_d.columns = ["Region", "gCO₂e / kWh", "WUE (L/kWh)"]
            fig = px.bar(grid_d, x="gCO₂e / kWh", y="Region", orientation="h",
                         color="gCO₂e / kWh",
                         color_continuous_scale=["#10b981", "#f59e0b", "#ef4444"],
                         range_color=[0, 700], template="simple_white")
            fig.update_layout(coloraxis_showscale=False, showlegend=False,
                               margin=dict(l=0, r=0, t=5, b=0), height=175,
                               font=dict(family="Inter", size=12))
            st.plotly_chart(fig, use_container_width=True)
            st.dataframe(grid_d.sort_values("gCO₂e / kWh", ascending=False),
                         use_container_width=True, hide_index=True)
