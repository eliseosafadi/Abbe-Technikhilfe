# Apple Design System — Dark Mode

## Table of Contents
- [Triple Defense for Cards](#triple-defense-for-cards)
- [Elevation Table](#elevation-table)
- [Color Shifts](#color-shifts)
- [Shadow Adjustments](#shadow-adjustments)
- [Frosted Glass in Dark Mode](#frosted-glass-in-dark-mode)
- [Theme Toggle Implementation](#theme-toggle-implementation)
- [Smooth Transition CSS](#smooth-transition-css)
- [Light Mode Anti-Washed-Out Tips](#light-mode-anti-washed-out-tips)
- [Testing Checklist](#testing-checklist)

---

## Triple Defense for Cards

In dark mode, cards can become invisible against dark backgrounds. Every card MUST use all three defenses simultaneously:

1. **Background step** — Card background is one elevation level above its parent.
2. **Border** — Always `border: 1px solid var(--apple-card-border)`.
3. **Shadow** — At minimum `var(--apple-shadow-sm)` to create edge definition.

```css
/* CORRECT — dark-safe card */
.card {
  background: var(--apple-elevated);       /* #2C2C2E in dark */
  border: 1px solid var(--apple-card-border); /* rgba(255,255,255,0.08) in dark */
  box-shadow: var(--apple-shadow-sm);      /* heavier in dark */
  border-radius: 18px;
  padding: 32px;
  transition: background-color 0.4s ease, color 0.3s ease, border-color 0.4s ease, box-shadow 0.4s ease;
}

/* WRONG — invisible in dark mode */
.card-broken {
  background: var(--apple-bg);  /* same as page bg = invisible */
  border: none;                 /* no edge definition */
  box-shadow: none;             /* nothing to see */
}
```

### Decision Matrix

| Parent BG         | Card BG              | Border Required | Shadow Required |
|--------------------|----------------------|-----------------|-----------------|
| `--apple-bg`       | `--apple-surface`    | Yes             | Yes             |
| `--apple-bg`       | `--apple-elevated`   | Yes             | Yes             |
| `--apple-surface`  | `--apple-elevated`   | Yes             | Yes             |
| `--apple-elevated` | custom lighter step  | Yes             | Yes             |

---

## Elevation Table

| Level    | Light Value   | Dark Value    | Usage                   |
|----------|---------------|---------------|-------------------------|
| Base     | `#FFFFFF`     | `#000000`     | Page background         |
| Level 1  | `#F5F5F7`     | `#1C1C1E`     | Section, surface        |
| Level 2  | `#FBFBFD`     | `#2C2C2E`     | Cards, elevated panels  |
| Level 3  | `#FFFFFF`     | `#3A3A3C`     | Popovers, overlays      |
| Level 4  | `#FFFFFF`     | `#48484A`     | Nested elevated content |

In dark mode, each elevation step adds visible lightness. In light mode, the steps are subtle. This is why borders and shadows are essential — they provide edge definition independent of the background-step contrast.

---

## Color Shifts

| Token           | Light              | Dark                 | Notes                          |
|-----------------|---------------------|----------------------|--------------------------------|
| bg              | `#FFFFFF`           | `#000000`            | Inverted                       |
| surface         | `#F5F5F7`           | `#1C1C1E`            | Dark gray, not pure black      |
| elevated        | `#FBFBFD`           | `#2C2C2E`            | Step above surface             |
| text-primary    | `#1D1D1F`           | `#F5F5F7`            | Near-white, not pure white     |
| text-secondary  | `#86868B`           | `#A1A1A6`            | Slightly lighter in dark       |
| accent          | `#0071E3`           | `#2997FF`            | Brighter for dark contrast     |
| card-border     | `rgba(0,0,0,0.06)`  | `rgba(255,255,255,0.08)` | Inverted alpha borders    |

Key principle: Dark mode is NOT simply "invert everything." Colors shift in specific ways:
- Text lightens but stays off-white to reduce eye strain.
- Accents become brighter to maintain contrast ratios.
- Borders switch from dark-on-light to light-on-dark with low opacity.

---

## Shadow Adjustments

Shadows are heavier in dark mode because they need higher contrast against dark surfaces.

```css
:root {
  --apple-shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
  --apple-shadow-md: 0 4px 12px rgba(0,0,0,0.08);
  --apple-shadow-lg: 0 8px 30px rgba(0,0,0,0.12);
  --apple-shadow-xl: 0 20px 60px rgba(0,0,0,0.15);
}

@media (prefers-color-scheme: dark) {
  :root {
    --apple-shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
    --apple-shadow-md: 0 4px 12px rgba(0,0,0,0.4);
    --apple-shadow-lg: 0 8px 30px rgba(0,0,0,0.5);
    --apple-shadow-xl: 0 20px 60px rgba(0,0,0,0.6);
  }
}

[data-theme="dark"] {
  --apple-shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
  --apple-shadow-md: 0 4px 12px rgba(0,0,0,0.4);
  --apple-shadow-lg: 0 8px 30px rgba(0,0,0,0.5);
  --apple-shadow-xl: 0 20px 60px rgba(0,0,0,0.6);
}
```

---

## Frosted Glass in Dark Mode

```css
.glass-nav {
  background: rgba(255,255,255,0.72);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  border-bottom: 1px solid var(--apple-card-border);
  transition: background-color 0.4s ease, color 0.3s ease, border-color 0.4s ease, box-shadow 0.4s ease;
}

[data-theme="dark"] .glass-nav {
  background: rgba(0,0,0,0.72);
}

/* Frosted card panel */
.glass-panel {
  background: rgba(255,255,255,0.5);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  border: 1px solid var(--apple-card-border);
  border-radius: 18px;
}

[data-theme="dark"] .glass-panel {
  background: rgba(28,28,30,0.65);
}
```

---

## Theme Toggle Implementation

### JavaScript

```javascript
function initThemeToggle() {
  const STORAGE_KEY = 'apple-theme';
  const toggle = document.querySelector('[data-theme-toggle]');

  // Determine initial theme
  function getPreferred() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) return stored;
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem(STORAGE_KEY, theme);
    if (toggle) toggle.setAttribute('aria-checked', theme === 'dark');
  }

  // Listen for OS-level changes (only when no stored preference)
  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
    if (!localStorage.getItem(STORAGE_KEY)) {
      applyTheme(e.matches ? 'dark' : 'light');
    }
  });

  // Toggle handler
  if (toggle) {
    toggle.addEventListener('click', () => {
      const current = document.documentElement.getAttribute('data-theme');
      applyTheme(current === 'dark' ? 'light' : 'dark');
    });
  }

  // Apply on load
  applyTheme(getPreferred());
}

document.addEventListener('DOMContentLoaded', initThemeToggle);
```

### Toggle Button HTML

```html
<button
  data-theme-toggle
  role="switch"
  aria-checked="false"
  aria-label="Toggle dark mode"
  class="theme-toggle"
>
  <span class="theme-toggle__icon theme-toggle__icon--light">
    <!-- sun SVG -->
  </span>
  <span class="theme-toggle__icon theme-toggle__icon--dark">
    <!-- moon SVG -->
  </span>
</button>
```

```css
.theme-toggle {
  position: relative;
  width: 44px;
  height: 44px;
  background: none;
  border: none;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--apple-text-secondary);
  transition: color 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.theme-toggle__icon--dark { display: none; }

[data-theme="dark"] .theme-toggle__icon--light { display: none; }
[data-theme="dark"] .theme-toggle__icon--dark  { display: block; }
```

---

## Smooth Transition CSS

Apply to all elements that change with the theme:

```css
body,
.card, .nav, .section, .btn, .input,
.footer, .modal, .badge, .pricing-card,
.testimonial, .feature-card, .product-card,
.search__input, .toggle__track {
  transition: background-color 0.4s ease, color 0.3s ease, border-color 0.4s ease, box-shadow 0.4s ease;
}
```

Avoid applying to ALL elements (`*`) as it causes layout thrashing. Target specific themed components.

---

## Light Mode Anti-Washed-Out Tips

Light mode can look flat if surfaces lack definition.

1. **Use `#F5F5F7` sections** — Alternate between `#FFFFFF` and `#F5F5F7` to create visual rhythm.
2. **Keep card borders** — `rgba(0,0,0,0.06)` is subtle but prevents cards from blending into white.
3. **Shadow hierarchy** — Cards on white need at least `shadow-sm`. Elevated items get `shadow-md`.
4. **Text contrast** — Ensure body text is `#1D1D1F`, not a gray that fails WCAG AA.
5. **Accent as anchor** — Use `#0071E3` sparingly to create focal points.
6. **Image borders** — Light images on white backgrounds need a 1px border: `border: 1px solid rgba(0,0,0,0.06)`.

```css
/* Anti-flat card in light mode */
.card--defined {
  background: var(--apple-elevated);
  border: 1px solid var(--apple-card-border);
  box-shadow: var(--apple-shadow-sm);
}

/* Image with edge definition */
.img--defined {
  border: 1px solid var(--apple-card-border);
  border-radius: 18px;
}
```

---

## Testing Checklist

### Visual Checks

- [ ] Cards are visible on both `--apple-bg` and `--apple-surface` backgrounds in dark mode.
- [ ] Every card has all three defenses: background step, border, shadow.
- [ ] Text passes WCAG AA contrast (4.5:1 body, 3:1 large text) in both modes.
- [ ] Accent color is `#0071E3` in light and `#2997FF` in dark.
- [ ] Frosted glass nav is legible in both modes.
- [ ] Images with transparency do not clash with dark backgrounds.
- [ ] SVG icons use `currentColor` and adapt to theme.
- [ ] Focus rings are visible in both modes.

### Transition Checks

- [ ] Theme toggle switches smoothly (no flash of unstyled content).
- [ ] Transition uses `background-color 0.4s ease, color 0.3s ease, border-color 0.4s ease, box-shadow 0.4s ease`.
- [ ] No elements flash or jump during transition.
- [ ] Scroll position is preserved during toggle.

### Preference Checks

- [ ] System dark mode preference is respected on first visit.
- [ ] User's manual toggle overrides system preference.
- [ ] Preference persists across page loads (localStorage).
- [ ] `@media (prefers-color-scheme: dark)` and `[data-theme="dark"]` produce identical results.
- [ ] `prefers-reduced-motion` is respected for theme transition animations.

### Accessibility Checks

- [ ] Theme toggle has `role="switch"` and `aria-checked`.
- [ ] Theme toggle has a descriptive `aria-label`.
- [ ] Color is not the sole indicator of state (pair with icons/text).
- [ ] High contrast mode does not break layouts.
