# Apple Design System — Responsive Design

## Table of Contents
- [Breakpoints](#breakpoints)
- [Fluid Typography](#fluid-typography)
- [Adaptive Grids](#adaptive-grids)
- [Container Widths](#container-widths)
- [Mobile Navigation Collapse](#mobile-navigation-collapse)
- [Touch Targets](#touch-targets)
- [Responsive Images](#responsive-images)
- [Responsive Utilities](#responsive-utilities)

---

## Breakpoints

| Name    | Min Width | Typical Devices                |
|---------|-----------|--------------------------------|
| xs      | 0         | Small phones                   |
| sm      | 576px     | Large phones (landscape)       |
| md      | 768px     | Tablets (portrait)             |
| lg      | 1024px    | Tablets (landscape), laptops   |
| xl      | 1280px    | Desktops                       |
| xxl     | 1440px    | Large desktops, external       |

### CSS Media Queries

```css
/* Mobile first — base styles are for xs */

/* Small */
@media (min-width: 576px)  { /* sm */ }

/* Medium */
@media (min-width: 768px)  { /* md */ }

/* Large */
@media (min-width: 1024px) { /* lg */ }

/* Extra large */
@media (min-width: 1280px) { /* xl */ }

/* 2X large */
@media (min-width: 1440px) { /* xxl */ }
```

### JavaScript Breakpoint Helper

```javascript
const BREAKPOINTS = {
  sm: 576,
  md: 768,
  lg: 1024,
  xl: 1280,
  xxl: 1440,
};

function isAbove(bp) {
  return window.matchMedia(`(min-width: ${BREAKPOINTS[bp]}px)`).matches;
}

function onBreakpoint(bp, callback) {
  const mq = window.matchMedia(`(min-width: ${BREAKPOINTS[bp]}px)`);
  mq.addEventListener('change', callback);
  callback(mq); // initial check
  return () => mq.removeEventListener('change', callback);
}
```

---

## Fluid Typography

Use `clamp()` for smooth scaling between breakpoints.

```css
.fluid-hero {
  font-size: clamp(40px, 5vw + 1rem, 80px);
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: -0.015em;
}

.fluid-display {
  font-size: clamp(32px, 3.5vw + 1rem, 56px);
  font-weight: 700;
  line-height: 1.07;
  letter-spacing: -0.012em;
}

.fluid-headline {
  font-size: clamp(24px, 2.5vw + 0.5rem, 40px);
  font-weight: 600;
  line-height: 1.1;
  letter-spacing: -0.01em;
}

.fluid-title {
  font-size: clamp(21px, 2vw + 0.25rem, 32px);
  font-weight: 600;
  line-height: 1.125;
}

.fluid-body-large {
  font-size: clamp(17px, 1.2vw + 0.25rem, 21px);
  line-height: 1.47;
}

.fluid-body {
  font-size: clamp(15px, 1vw + 0.25rem, 17px);
  line-height: 1.47;
}
```

### Mapping Table

| Style        | Mobile (375px) | Tablet (768px) | Desktop (1280px) |
|-------------|----------------|----------------|-------------------|
| hero        | 40px           | ~56px          | 80px              |
| display     | 32px           | ~42px          | 56px              |
| headline    | 24px           | ~32px          | 40px              |
| title       | 21px           | ~26px          | 32px              |
| body-large  | 17px           | ~19px          | 21px              |
| body        | 15px           | ~16px          | 17px              |

---

## Adaptive Grids

```css
/* Auto-fit grid: cards fill available space */
.auto-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 24px;
}

/* Explicit responsive grid */
.responsive-grid {
  display: grid;
  gap: 24px;
  grid-template-columns: 1fr;
}

@media (min-width: 576px) {
  .responsive-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .responsive-grid { grid-template-columns: repeat(3, 1fr); }
}

@media (min-width: 1280px) {
  .responsive-grid { grid-template-columns: repeat(4, 1fr); }
}

/* Responsive gap scaling */
.scaled-gap {
  gap: 16px;
}

@media (min-width: 768px) {
  .scaled-gap { gap: 24px; }
}

@media (min-width: 1280px) {
  .scaled-gap { gap: 32px; }
}
```

### Bento Grid — Responsive

```css
.bento-responsive {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

@media (min-width: 576px) {
  .bento-responsive { grid-template-columns: repeat(2, 1fr); }
}

@media (min-width: 1024px) {
  .bento-responsive {
    grid-template-columns: repeat(4, 1fr);
    grid-auto-rows: 280px;
  }

  .bento-responsive__wide  { grid-column: span 2; }
  .bento-responsive__tall  { grid-row: span 2; }
  .bento-responsive__hero  { grid-column: span 2; grid-row: span 2; }
}
```

---

## Container Widths

```css
.container {
  width: 100%;
  margin: 0 auto;
  padding: 0 24px;
}

.container--narrow {
  max-width: 980px;
}

.container--wide {
  max-width: 1200px;
}

.container--full {
  max-width: 100%;
  padding: 0;
}

/* Responsive padding */
@media (max-width: 576px) {
  .container {
    padding: 0 16px;
  }
}

@media (min-width: 1440px) {
  .container {
    padding: 0 32px;
  }
}
```

### When to Use Each Container

| Container         | Max Width | Use Case                             |
|-------------------|-----------|--------------------------------------|
| `--narrow`        | 980px     | Text content, feature grids, CTAs    |
| `--wide`          | 1200px    | Product grids, split layouts, bento  |
| `--full`          | 100%      | Heroes, immersive backgrounds        |

---

## Mobile Navigation Collapse

```css
.nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 52px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  background: rgba(255,255,255,0.72);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  border-bottom: 1px solid var(--apple-card-border);
  z-index: 1000;
  transition: var(--apple-theme-transition);
}

.nav__links {
  display: none;
}

.nav__toggle {
  display: flex;
  width: 44px;
  height: 44px;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  cursor: pointer;
}

@media (min-width: 768px) {
  .nav__links {
    display: flex;
    gap: 28px;
  }

  .nav__toggle {
    display: none;
  }
}

/* Mobile drawer */
.nav-drawer {
  position: fixed;
  top: 52px;
  left: 0;
  right: 0;
  bottom: 0;
  background: var(--apple-bg);
  padding: 24px;
  transform: translateY(-100%);
  opacity: 0;
  transition: transform 0.4s cubic-bezier(0.25, 0.1, 0.25, 1),
              opacity 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
  z-index: 999;
}

.nav-drawer--open {
  transform: translateY(0);
  opacity: 1;
}

.nav-drawer__link {
  display: block;
  font-size: 28px;
  font-weight: 600;
  padding: 16px 0;
  color: var(--apple-text-primary);
  text-decoration: none;
  border-bottom: 1px solid var(--apple-card-border);
}
```

```javascript
const toggle = document.querySelector('.nav__toggle');
const drawer = document.querySelector('.nav-drawer');

toggle.addEventListener('click', () => {
  drawer.classList.toggle('nav-drawer--open');
  document.body.style.overflow = drawer.classList.contains('nav-drawer--open') ? 'hidden' : '';
});
```

---

## Touch Targets

Minimum 44x44px for all interactive elements per Apple HIG.

```css
/* Ensure minimum touch target */
.touch-target {
  min-width: 44px;
  min-height: 44px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
}

/* Expand small icons with invisible padding */
.icon-btn {
  position: relative;
  padding: 10px;
}

.icon-btn::before {
  content: '';
  position: absolute;
  inset: -6px; /* expand to 44px if icon is 32px */
}

/* Spacing for lists of tappable items */
.tap-list__item {
  padding: 14px 16px;
  min-height: 44px;
  display: flex;
  align-items: center;
}
```

---

## Responsive Images

```html
<!-- Art direction with <picture> -->
<picture>
  <source media="(min-width: 1024px)" srcset="hero-desktop.webp">
  <source media="(min-width: 576px)" srcset="hero-tablet.webp">
  <img src="hero-mobile.webp" alt="Hero" loading="lazy">
</picture>

<!-- Resolution switching -->
<img
  srcset="photo-400w.webp 400w,
          photo-800w.webp 800w,
          photo-1200w.webp 1200w"
  sizes="(min-width: 1024px) 50vw,
         (min-width: 576px) 80vw,
         100vw"
  src="photo-800w.webp"
  alt="Product photo"
  loading="lazy"
  decoding="async"
>
```

```css
/* Responsive image container */
.responsive-img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 18px;
}

/* Aspect-ratio controlled container */
.aspect-container {
  position: relative;
  overflow: hidden;
  border-radius: 18px;
}

.aspect-container--16x9 { aspect-ratio: 16 / 9; }
.aspect-container--4x3  { aspect-ratio: 4 / 3; }
.aspect-container--1x1  { aspect-ratio: 1 / 1; }

.aspect-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Retina-ready: use 2x images by default */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
  .retina-img {
    image-rendering: -webkit-optimize-contrast;
  }
}
```

---

## Responsive Utilities

```css
/* Show/hide at breakpoints */
.hide-below-sm { display: none; }
@media (min-width: 576px) { .hide-below-sm { display: block; } }

.hide-below-md { display: none; }
@media (min-width: 768px) { .hide-below-md { display: block; } }

.hide-below-lg { display: none; }
@media (min-width: 1024px) { .hide-below-lg { display: block; } }

.hide-above-md { display: block; }
@media (min-width: 768px) { .hide-above-md { display: none; } }

/* Responsive text alignment */
.text-center-mobile {
  text-align: center;
}
@media (min-width: 768px) {
  .text-center-mobile { text-align: left; }
}

/* Responsive spacing */
.section-padding {
  padding: 48px 16px;
}
@media (min-width: 768px) {
  .section-padding { padding: 80px 24px; }
}
@media (min-width: 1280px) {
  .section-padding { padding: 96px 24px; }
}
```
