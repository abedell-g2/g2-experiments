# G2 Elevate Design Tokens — Color

**Source:** Figma file `FiQYsj0JINGS4kXpmqSo3m` (Elevate | Core), page "Colors" (node `1:3`)
**Last extracted:** 2026-03-04
**How to use:** Read this file instead of querying Figma for color tokens. All hex values are confirmed against the Figma source.

---

## Drop-in CSS block

Paste this `:root` block into any prototype to use tokens as CSS variables:

```css
:root {
  /* Brand */
  --color-brand:          #ff492c;  /* Rorange — CTA, hot badges, destructive */
  --color-primary:        #5746b2;  /* Purple  — primary interactive, active states, links */
  --color-midnight:       #201f23;  /* Midnight — primary dark text */
  --color-white:          #ffffff;  /* Pure White — card/surface backgrounds */

  /* Text */
  --text-default:         #201f23;  /* Body copy, headings */
  --text-subtle:          #6f6d78;  /* Secondary labels, counts, metadata, placeholders */

  /* Borders */
  --border-light:         #dfdfe2;  /* Card borders, dividers, separators */

  /* Backgrounds (partially confirmed) */
  --bg-page:              #f5f4fb;  /* Page lavender — used in prototypes, TBD from DS */
  --bg-surface:           #ffffff;  /* Card / panel surface */
  --bg-subtle:            #faf9ff;  /* Hover tint, input background */

  /* Semantic aliases */
  --focus-ring:           rgba(87, 70, 178, 0.12);  /* derived from --color-primary */
}
```

---

## Full token reference

| Figma token name | Hex | Scale alias | Use |
|---|---|---|---|
| `brand/core/brand` | `#ff492c` | R100 (Rorange) | CTA buttons, "Most Evaluated" badge, hot dot, destructive |
| `brand/core/primary` | `#5746b2` | P100 (Purple) | Active tabs, links, primary interactive, focus borders |
| `brand/core/midnight` | `#201f23` | N100 (Midnight) | All primary text — headings, labels, body |
| `brand/core/pure-white` | `#ffffff` | N0 | Card backgrounds, page header, input surfaces |
| `text/text-default` | `#201f23` | — | Same as midnight; use for all body text |
| `text/text-nonessential` | `#6f6d78` | — | Counts ("6 products"), metadata, placeholder text |
| `border/border-light` | `#dfdfe2` | — | 1–1.5px borders on cards, dividers, section separators |

---

## What to pull from Figma next

These pages haven't been extracted yet. Pull them when you need them:

| Page | Node | What you'll get |
|---|---|---|
| ~~Typography~~ | ~~10124:33060~~ | ~~Type scale — sizes, weights, line-heights for each level~~ ✓ Done |
| ~~Components › Buttons~~ | ~~94:5096~~ | ~~Button size variants, hover/disabled states, icon rules~~ ✓ Done |
| Components › Cards | TBD | Card radius, padding, shadow specs |
| Components › Forms | TBD | Input height, focus ring, error state colors |
| Spacing | TBD | 4px grid, named spacing tokens |

---

# G2 Elevate Design Tokens — Typography

**Source:** Figma file `FiQYsj0JINGS4kXpmqSo3m` (Elevate | Core), node `10124:33060`
**Last extracted:** 2026-03-04
**How to use:** Read this section instead of querying Figma for typography tokens.

---

## Drop-in CSS block

```css
:root {
  /* Font family — all roles use Figtree */
  --font-body:    'Figtree', sans-serif;
  --font-heading: 'Figtree', sans-serif;
  --font-label:   'Figtree', sans-serif;

  /* Font sizes */
  --text-xs:   0.75rem;    /* 12px — minimum scale size */
  --text-sm:   0.875rem;   /* 14px */
  --text-base: 1rem;       /* 16px */
  --text-lg:   1.3125rem;  /* 21px */
  --text-xl:   1.75rem;    /* 28px */
  --text-2xl:  2.375rem;   /* 38px */
  --text-3xl:  3.1875rem;  /* 51px */
  --text-4xl:  4.1875rem;  /* 67px */

  /* Line heights (paired by scale step) */
  --leading-xs:   1rem;    /* 16px */
  --leading-sm:   1.25rem; /* 20px */
  --leading-base: 1.5rem;  /* 24px */
  --leading-lg:   1.75rem; /* 28px */
  --leading-xl:   2.25rem; /* 36px */
  --leading-2xl:  3rem;    /* 48px */
  --leading-3xl:  4rem;    /* 64px */
  --leading-4xl:  5rem;    /* 80px */

  /* Font weights */
  --font-light:     300;
  --font-regular:   400;
  --font-medium:    500;
  --font-semibold:  600;
  --font-bold:      700;
  --font-extrabold: 800;
  --font-black:     900;

  /* Letter spacing */
  --tracking-base: 0rem;  /* 0px — no tracking defined in DS */
}
```

---

## Full token reference

### Font families

| Figma token | Value | Notes |
|---|---|---|
| `type/font-family/font-body` | Figtree | All body copy |
| `type/font-family/font-heading` | Figtree | All headings |
| `type/font-family/font-label` | Figtree | Labels, badges, UI chrome |

All three roles use the same font — no family switching needed.

### Font sizes + line heights (paired scale)

| Token | rem | px | Line height token | Line height rem | Line height px |
|---|---|---|---|---|---|
| `type/font-size/text-xs` | 0.75rem | 12px | `type/line-height/leading-xs` | 1rem | 16px |
| `type/font-size/text-sm` | 0.875rem | 14px | `type/line-height/leading-sm` | 1.25rem | 20px |
| `type/font-size/text-base` | 1rem | 16px | `type/line-height/leading-base` | 1.5rem | 24px |
| `type/font-size/text-lg` | 1.3125rem | 21px | `type/line-height/leading-lg` | 1.75rem | 28px |
| `type/font-size/text-xl` | 1.75rem | 28px | `type/line-height/leading-xl` | 2.25rem | 36px |
| `type/font-size/text-2xl` | 2.375rem | 38px | `type/line-height/leading-2xl` | 3rem | 48px |
| `type/font-size/text-3xl` | 3.1875rem | 51px | `type/line-height/leading-3xl` | 4rem | 64px |
| `type/font-size/text-4xl` | 4.1875rem | 67px | `type/line-height/leading-4xl` | 5rem | 80px |

### Font weights

| Figma token | Weight name | Numeric | Italic variant available |
|---|---|---|---|
| `type/font-weight/font-light` | Light | 300 | No |
| `type/font-weight/font-regular` | Regular | 400 | Yes (`font-regular-italic`) |
| `type/font-weight/font-medium` | Medium | 500 | Yes (`font-medium-italic`) |
| `type/font-weight/font-semibold` | Semibold | 600 | Yes (`font-semibold-italic`) |
| `type/font-weight/font-bold` | Bold | 700 | Yes (`font-bold-italic`) |
| `type/font-weight/font-extrabold` | Extra Bold | 800 | No |
| `type/font-weight/font-black` | Black | 900 | No |

### Letter spacing

| Figma token | Value | Notes |
|---|---|---|
| `type/letter-spacing/tracking-base` | 0rem (0px) | Only spacing token defined — no tracking used in DS |

---

## Token drift in current prototypes (typography)

Several sub-scale font sizes appear in the prototype files that fall below the DS minimum (`text-xs` = 12px):

| Old value | Replaced with | Notes |
|---|---|---|
| `8px`, `9px`, `10px`, `11px` | `12px` (`--text-xs`) | Applied 2026-03-04 across all 9 files. JS template literals also patched. |

**Remaining off-scale sizes** (between DS steps — not yet addressed):

| Current value | Nearest DS token | Gap | Common usage |
|---|---|---|---|
| `13px` | `--text-sm` (14px) | 1px | Secondary body copy, card descriptions, filter labels |
| `15px` | `--text-base` (16px) | 1px | Metric values, compact names |
| `17px` | `--text-base` (16px) | 1px | Card/product names |

These are small gaps; rounding to the nearest DS step is optional but would improve token alignment.

---

# G2 Elevate Design Tokens — Buttons

**Source:** Figma file `FiQYsj0JINGS4kXpmqSo3m` (Elevate | Core), page "✅ CTA Button" (node `94:5096`)
**Last extracted:** 2026-03-04
**How to use:** Read this section instead of querying Figma for button specs.

---

## Key finding: all buttons are pill-shaped

G2 buttons use `border-radius: 9999px` (full pill). The prototypes used 6–8px radius, which is incorrect.

---

## Size specs

| Size | Height | H-padding | V-padding | Radius token | Radius px | Icon size | Font size | Line height |
|---|---|---|---|---|---|---|---|---|
| Lg | 48px | 12px | 12px | `radius-pill-md` | 24px | 20px | text-base (16px) | leading-base (24px) |
| Md | 40px | 12px | 8px | `radius-pill-sm` | 20px | 20px | text-base (16px) | leading-base (24px) |
| Sm | 32px | 8px | — | `radius-pill-sm` | 20px | 16px | text-sm (14px) | leading-sm (20px) |

All sizes add 4px extra horizontal padding inside the label frame (4px left + 4px right), so effective total horizontal space = px + 4px per side.

---

## Tier specs

| Tier | Background | Text color | Border | Token |
|---|---|---|---|---|
| Primary Brand | `#ff492c` (Rorange) | white | none | `--color/background/bg-brand` |
| Primary | `#5746b2` (Purple) | white | none | `--color/background/bg-primary` |
| Primary Inverted | white | `#5746b2` | none | `--color/background/bg-neutral-5` |
| Secondary | `#fafafa` | `#5746b2` | 0.5px `#b0afb6` | `--color/border/border-medium` |
| Tertiary | transparent | `#5746b2` | none | — |
| Text | transparent | `#5746b2` | none | — |
| Text Subtle | transparent | `#6f6d78` | none | — |

> **New color token found:** `--color/border/border-medium: #b0afb6` (lighter than `--border-light: #dfdfe2`)

---

## Typography (all tiers)

| Property | Lg/Md | Sm |
|---|---|---|
| Font family | Figtree | Figtree |
| Font weight | semibold (600) | semibold (600) |
| Font size | text-base (16px) | text-sm (14px) |
| Line height | leading-base (24px) | leading-sm (20px) |
| Letter spacing | 0 | 0 |
| Text transform | Sentence case (CTAs) / Title case (text CTAs) | — |

---

## Usage rules (from Figma docs)

1. Sentence case for CTA buttons; Title case for text-style CTAs
2. Primary CTA is typically right-aligned
3. Button pairs: Primary with Tertiary (not Primary with Secondary)
4. Icons go on the left — except directional arrows (arrow-right goes right)

---

## Drop-in CSS for prototypes

```css
/* Button base */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 4px;
  font-family: 'Figtree', sans-serif;
  font-weight: 600;
  border: none;
  cursor: pointer;
  white-space: nowrap;
  border-radius: 9999px;
}

/* Sizes */
.btn-lg { height: 48px; padding: 12px 16px; font-size: 16px; line-height: 24px; }
.btn-md { height: 40px; padding:  8px 16px; font-size: 16px; line-height: 24px; }
.btn-sm { height: 32px; padding:  0   12px; font-size: 14px; line-height: 20px; }

/* Tiers */
.btn-brand     { background: #ff492c; color: white; }
.btn-primary   { background: #5746b2; color: white; }
.btn-secondary { background: #fafafa; color: #5746b2; border: 0.5px solid #b0afb6; }
.btn-tertiary  { background: transparent; color: #5746b2; }
.btn-text      { background: transparent; color: #5746b2; }
.btn-text-subtle { background: transparent; color: #6f6d78; }

/* Hover states (derived — not yet confirmed from Figma) */
.btn-brand:hover     { background: #e63d22; }
.btn-primary:hover   { background: #4a3a99; }
.btn-secondary:hover { background: #f0eeff; border-color: #5746b2; }
.btn-tertiary:hover  { background: #f0eeff; }
```

---

## Token drift in current prototypes (buttons)

| Property | Prototype value | DS value | Impact |
|---|---|---|---|
| Border-radius | `6px`, `7px`, `8px` | `9999px` (pill) | **High** — significant shape change |
| Button font size | `12px`, `13px` | `16px` (Lg/Md), `14px` (Sm) | **High** — noticeably larger labels |
| Button font weight | `700` (bold) | `600` (semibold) | Low — subtle |
| Secondary border | `1.5px solid #5746b2` | `0.5px solid #b0afb6` | Medium — thinner, lighter border |
| Secondary bg | `white` | `#fafafa` | Negligible |

Applied: 2026-03-04 ✓

---

## Token drift in current prototypes (as of 2026-03-04)

These values appear in the prototype files and should be replaced with the confirmed tokens:

| Old value | Replace with | Token |
|---|---|---|
| `#1a1a2e` | `#201f23` | `--color-midnight` / `--text-default` |
| `#49495a` | `#6f6d78` | `--text-subtle` |
| `#8b8fa8` | `#6f6d78` | `--text-subtle` |
| `#e5e3f0` | `#dfdfe2` | `--border-light` |
