# G2 Elevate Design Tokens
> Sourced from Figma: **Elevate | Core** (`FiQYsj0JINGS4kXpmqSo3m`)
> Consume this file to reproduce token-accurate output without querying Figma.

---

## Colors

### Brand

| Token | Value | Usage |
|---|---|---|
| `--color-brand-purple` | `#5746b2` | Primary actions, active states, links |
| `--color-brand-orange` | `#ff492c` | Primary Brand CTA, rank-1 badges |
| `--color-brand-purple-hover` | `#4535a0` | Hover state for purple buttons |
| `--color-brand-orange-hover` | `#e03c22` | Hover state for orange buttons |

### Text

| Token | Value | Usage |
|---|---|---|
| `--color-text-primary` | `#1a1a2e` | Headlines, card names, strong values |
| `--color-text-secondary` | `#49495a` | Body copy, taglines, descriptions |
| `--color-text-tertiary` | `#8b8fa8` | Labels, counts, placeholders |
| `--color-text-on-dark` | `#ffffff` | Text on brand/dark backgrounds |

### Surface

| Token | Value | Usage |
|---|---|---|
| `--color-surface-page` | `#f5f4fb` | Page background |
| `--color-surface-card` | `#ffffff` | Card / panel background |
| `--color-surface-subtle` | `#f8f7ff` | Metrics sections, callouts |
| `--color-surface-brand-light` | `#f0eeff` | Active tabs, badge backgrounds, selected states |
| `--color-surface-brand-xlight` | `#fafafe` | Input fields at rest |

### Border

| Token | Value | Usage |
|---|---|---|
| `--color-border-default` | `#e5e3f0` | Card borders, dividers, inputs |
| `--color-border-brand` | `#ddd8f8` | Brand-tinted borders (metrics blocks, badges) |
| `--color-border-brand-mid` | `#c4bbf0` | Hover borders on brand-adjacent elements |
| `--color-border-button-secondary` | `#b0afb6` | Secondary button border (0.5px) |

### Semantic

| Token | Value | Usage |
|---|---|---|
| `--color-leader` | `#ff492c` | G2 Leader badge text/bg accent |
| `--color-leader-bg` | `#fff3f0` | G2 Leader badge background |
| `--color-leader-border` | `#ffd5cc` | G2 Leader badge border |
| `--color-niche-bg` | `#f5f4fb` | Niche Player badge background |
| `--color-stars` | `#fbbf24` | Star rating icons |

---

## Typography

> Figma node: `10124:33060`
> Font family: **Figtree** (Google Fonts)
> Load: `https://fonts.googleapis.com/css2?family=Figtree:wght@400;500;600;700;800;900&display=swap`

### CSS Variables

```css
:root {
  --font-family: 'Figtree', sans-serif;

  /* Sizes */
  --text-xs:   10px;   /* micro labels, counts, uppercase tags */
  --text-sm:   12px;   /* secondary metadata, captions */
  --text-base: 13px;   /* body copy, filter labels, taglines */
  --text-md:   14px;   /* card body, star values, sort selects */
  --text-lg:   16px;   /* card names (mobile), large values */
  --text-xl:   17px;   /* card names */
  --text-2xl:  20px;   /* step headings, section titles */
  --text-3xl:  24px;   /* page headings (compact) */
  --text-4xl:  26px;   /* page headings (default) */

  /* Weights */
  --font-regular:    400;
  --font-medium:     500;
  --font-semibold:   600;
  --font-bold:       700;
  --font-extrabold:  800;
  --font-black:      900;

  /* Line heights */
  --leading-tight:   1.2;
  --leading-snug:    1.4;
  --leading-normal:  1.5;
  --leading-relaxed: 1.6;
  --leading-solid:   1;

  /* Letter spacing */
  --tracking-tight:  -0.01em;
  --tracking-normal:  0;
  --tracking-wide:    0.05em;
  --tracking-wider:   0.06em;
  --tracking-widest:  0.1em;  /* uppercase section labels */
}
```

### Named Text Styles

| Style name | Size | Weight | Line height | Letter spacing | Usage |
|---|---|---|---|---|---|
| `display-page-title` | 26px | 800 | 1.2 | 0 | Page `<h1>` |
| `display-page-title-sm` | 24px | 800 | 1.2 | 0 | Compact page `<h1>` |
| `heading-section` | 20px | 800 | 1.3 | 0 | Step headings, results headers |
| `heading-card-name` | 17px | 800 | 1.2 | 0 | Product card name |
| `heading-card-name-sm` | 16px | 800 | 1.2 | 0 | Card name (smaller variant) |
| `body-default` | 14px | 400–500 | 1.5 | 0 | Standard body copy |
| `body-tagline` | 13px | 400 | 1.4–1.5 | 0 | Card taglines, subtitles |
| `body-description` | 13px | 400 | 1.6 | 0 | Longer card descriptions |
| `label-default` | 13px | 600 | 1.4 | 0 | Filter labels, sort options |
| `label-sm` | 12px | 600 | 1.4 | 0 | Secondary labels, captions |
| `label-caps` | 11px | 700 | 1.2 | 0.08em | Uppercase section headers |
| `label-caps-tight` | 10px | 700 | 1.2 | 0.08–0.1em | Metric labels, badge text |
| `metric-value-lg` | 15px | 800 | 1 | 0 | Metric numbers (table) |
| `metric-value-md` | 14px | 800 | 1 | 0 | Metric numbers (card) |
| `metric-value-sm` | 13px | 700 | 1 | 0 | Compact metric numbers |
| `score-display-lg` | 18px | 800 | 1 | 0 | AI score in large hex/circle |
| `score-display-sm` | 13px | 800 | 1 | 0 | AI score in mini hex/circle |
| `tab-label` | 13px | 600–700 | 1 | 0 | Category tab labels |
| `tab-count` | 10px | 700 | 1 | 0 | Tab count pills |

---

## Buttons

> Figma node: `94:5096`

### Drop-in CSS

```css
/* ── Shared base ── */
.btn {
  font-family: 'Figtree', sans-serif;
  font-weight: 600;
  border-radius: 9999px;        /* pill — all sizes */
  border: none;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  transition: background 0.12s, color 0.12s, border-color 0.12s;
  text-decoration: none;
  white-space: nowrap;
}

/* ── Sizes ── */
.btn-sm {
  height: 32px;
  padding: 0 8px;
  font-size: 14px;
  border-radius: 20px;          /* radius-pill-sm */
}
.btn-md {
  height: 40px;
  padding: 8px 12px;
  font-size: 16px;
  border-radius: 20px;          /* radius-pill-sm */
}
.btn-lg {
  height: 48px;
  padding: 12px 12px;
  font-size: 16px;
  border-radius: 24px;          /* radius-pill-md */
}

/* ── Tiers ── */
.btn-primary {
  background: #5746b2;
  color: #ffffff;
}
.btn-primary:hover { background: #4535a0; }

.btn-primary-brand {
  background: #ff492c;
  color: #ffffff;
}
.btn-primary-brand:hover { background: #e03c22; }

.btn-primary-inverted {
  background: #ffffff;
  color: #5746b2;
}
.btn-primary-inverted:hover { background: #f0eeff; }

.btn-secondary {
  background: #fafafa;
  color: #5746b2;
  border: 0.5px solid #b0afb6;
}
.btn-secondary:hover { background: #f0eeff; border-color: #5746b2; }

.btn-tertiary {
  background: transparent;
  color: #5746b2;
}
.btn-tertiary:hover { background: #f0eeff; }

.btn-text {
  background: transparent;
  color: #49495a;
  padding-left: 0;
  padding-right: 0;
}
.btn-text:hover { color: #5746b2; }

.btn-text-subtle {
  background: transparent;
  color: #8b8fa8;
  padding-left: 0;
  padding-right: 0;
}
.btn-text-subtle:hover { color: #5746b2; }

/* ── States ── */
.btn:disabled,
.btn[aria-disabled="true"] {
  opacity: 0.4;
  cursor: not-allowed;
  pointer-events: none;
}
```

### Size Specs

| Size | Height | Padding | Font size | Border radius |
|---|---|---|---|---|
| `sm` | 32px | 0 8px | 14px | 20px (`radius-pill-sm`) |
| `md` | 40px | 8px 12px | 16px | 20px (`radius-pill-sm`) |
| `lg` | 48px | 12px 12px | 16px | 24px (`radius-pill-md`) |

### Tier Specs

| Tier | Background | Text | Border |
|---|---|---|---|
| `primary` | `#5746b2` | `#ffffff` | none |
| `primary-brand` | `#ff492c` | `#ffffff` | none |
| `primary-inverted` | `#ffffff` | `#5746b2` | none |
| `secondary` | `#fafafa` | `#5746b2` | `0.5px solid #b0afb6` |
| `tertiary` | transparent | `#5746b2` | none |
| `text` | transparent | `#49495a` | none |
| `text-subtle` | transparent | `#8b8fa8` | none |

### Usage Rules

- All buttons use **pill** shape at every size — no rounded-rect buttons in Elevate
- `primary-brand` (orange) is for **hero-level CTAs only** — never pair it with `primary` purple in the same button group
- Within a card, use `primary` + `secondary` pairing (both purple family), never `primary-brand` + `secondary`
- `font-weight: 600` across all tiers — not 700
- Loading state: show a spinner inside the button, keep label hidden, disable pointer events

---

## Spacing (inferred from component geometry)

| Token | Value | Usage |
|---|---|---|
| `--space-1` | 4px | Micro gaps (icon to text in labels) |
| `--space-2` | 8px | Compact padding, small gaps |
| `--space-3` | 12px | Card section gap, button padding |
| `--space-4` | 16px | Card internal sections |
| `--space-5` | 20px | Card padding |
| `--space-6` | 24px | Section spacing |
| `--space-8` | 32px | Body padding (compact) |
| `--space-12` | 48px | Body padding (standard) |

---

## Border Radius

| Token | Value | Usage |
|---|---|---|
| `radius-sm` | 4px | Tiny badges, tag corners |
| `radius-md` | 6–7px | Buttons (non-Elevate contexts), small cards |
| `radius-lg` | 8–10px | Logo avatars, dropdown menus, sidebar sections |
| `radius-xl` | 12px | Product cards, main panels |
| `radius-2xl` | 16px | Wizard card |
| `radius-pill-sm` | 20px | Pill buttons (sm/md), count badges |
| `radius-pill-md` | 24px | Pill buttons (lg) |
| `radius-full` | 9999px | All Elevate buttons, score circles |

---

## Shadows

| Token | Value | Usage |
|---|---|---|
| `shadow-card-hover` | `0 4px 20px rgba(87,70,178,0.1)` | Product card hover |
| `shadow-dropdown` | `0 8px 24px rgba(0,0,0,0.1)` | Dropdown menus |
| `shadow-focus-brand` | `0 0 0 4px rgba(87,70,178,0.08)` | Input focus ring |
| `shadow-focus-orange` | `0 0 0 6px rgba(255,73,44,0)` | Mic button pulse |
| `shadow-btn-active` | `0 0 0 4px rgba(87,70,178,0.15)` | Active stepper node |

---

## What to pull next

| Token group | Figma node | Status |
|---|---|---|
| Colors | Already in prototypes | ✅ documented above |
| Typography | `10124:33060` | ✅ documented above |
| Buttons | `94:5096` | ✅ documented above |
| Form inputs / select | TBD | ⬜ not yet extracted |
| Icons | TBD | ⬜ not yet extracted |
| Data visualization (bars, dots) | TBD | ⬜ not yet extracted |
