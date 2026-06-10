---
name: Executive GreenOps
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#45464d'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#006c49'
  on-secondary: '#ffffff'
  secondary-container: '#6cf8bb'
  on-secondary-container: '#00714d'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#2a1700'
  on-tertiary-container: '#b87500'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffddb8'
  tertiary-fixed-dim: '#ffb95f'
  on-tertiary-fixed: '#2a1700'
  on-tertiary-fixed-variant: '#653e00'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-lg:
    fontFamily: Hanken Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-sm:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-mono:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  kpi-value:
    fontFamily: Hanken Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  sidebar-width: 260px
  container-max: 1440px
  gutter: 24px
  margin-mobile: 16px
  card-padding: 24px
---

## Brand & Style
The design system is engineered for **GlobalHack-TRACE**, an AI GreenOps dashboard tailored for executive oversight and engineering accountability. The brand personality is **authoritative, analytical, and environmentally conscious**. It balances the clinical precision of a developer tool with the high-level clarity required by leadership.

The aesthetic follows a **Corporate Modern** style with **Tonal Layering**. It utilizes a "Split Personality" layout: a deep, technical sidebar representing the power of AI, contrasted against a clean, white-to-light-gray main staging area that prioritizes data legibility. Visual metaphors should evoke "efficiency" and "traceability"—using crisp lines, ample negative space, and high-fidelity data visualizations.

## Colors
The palette is rooted in a **Deep Navy (#0F172A)** primary, used for the sidebar and structural elements to provide an "executive" frame. 

The dashboard canvas uses a light-gray foundation to reduce eye strain during prolonged data analysis. Semantic coloring is strictly reserved for environmental metrics:
- **Emerald Green**: Indicates carbon efficiency, savings, and low-energy compute.
- **Amber**: Signals "Energy Debt" or usage spikes that require attention.
- **Rose Red**: Reserved for critical waste or infrastructure failures.
- **Chart Palette**: Use a professional spectrum of teals, indigos, and grays for neutral data points to ensure the semantic green/red remains impactful.

## Typography
The system employs a multi-font strategy to balance readability with technical depth.
- **Hanken Grotesk** is used for headlines and prominent KPI metrics to provide a sharp, contemporary "startup-meets-enterprise" feel.
- **Inter** handles all body copy and UI controls for maximum legibility.
- **JetBrains Mono** is utilized for small labels, data timestamps, and metadata to reinforce the GreenOps/Technical nature of the platform.

For mobile screens, `display-lg` should scale down to `32px` to maintain hierarchy without overflowing the viewport.

## Layout & Spacing
The layout follows a **Fixed Sidebar + Fluid Canvas** model. 
- **The Sidebar**: 260px width, anchored to the left. It contains the primary navigation and workspace switcher.
- **The Canvas**: A fluid grid using a 12-column system. On desktop, content is contained within a 1440px max-width container, centered on the canvas.
- **Rhythm**: A strict 8px grid governs all spacing. KPIs are grouped in sets of 4 (3 columns each) at the top of the page.
- **Breakpoints**: 
  - *Mobile (<768px)*: Sidebar collapses to a bottom bar or hamburger menu. Margin reduces to 16px. Cards stack vertically.
  - *Tablet (768px - 1024px)*: Sidebar collapses to an icon-only "rail" (72px).

## Elevation & Depth
This design system uses **Tonal Layers** rather than heavy shadows to maintain a clean, executive finish. 
- **Level 0 (Canvas)**: Background color (#F8FAFC).
- **Level 1 (Cards)**: Pure white (#FFFFFF) with a thin 1px border (#E2E8F0). This provides a crisp "Streamlit-plus" look.
- **Level 2 (Dropdowns/Modals)**: White background with a soft, diffused ambient shadow (10% opacity primary color) to indicate temporary overlay.
- **Sidebar Depth**: Uses a slight gradient from the primary color to a darker shade to create a recessed feel, pushing the main content area forward.

## Shapes
The system uses a **Soft (0.25rem)** roundedness approach. This keeps the interface feeling professional and efficient, avoiding the "bubbly" appearance of consumer apps.
- **Standard UI (Buttons, Inputs)**: 4px radius.
- **Containers (Cards, Modals)**: 8px (rounded-lg) for a more distinct structural separation.
- **Status Pills**: Fully rounded (pill) to distinguish them from interactive buttons.

## Components
- **KPI Metrics**: Large headlines for the value, paired with a `label-mono` title and a small percentage trend indicator (Green for down/carbon, Red for up).
- **Data Cards**: White backgrounds, 1px gray borders, and a mandatory 24px internal padding. Title should be `headline-sm`.
- **Buttons**:
  - *Primary*: Deep Navy background, white text.
  - *Secondary*: White background, 1px gray border, Navy text.
  - *Actionable Items*: Use subtle hover states (light gray background) rather than heavy color shifts.
- **Charts**: Use crisp bar and line charts with minimalist axes. Remove grid lines where possible to emphasize the data trend.
- **Input Fields**: Streamlit-inspired but with refined 4px borders. Use `Inter` for input text and a light-gray placeholder.
- **Status Chips**: Low-saturation backgrounds with high-saturation text (e.g., light green background with dark emerald text) to indicate state without overwhelming the hierarchy.