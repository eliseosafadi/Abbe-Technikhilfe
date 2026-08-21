# Apple Design System — Layouts

## Table of Contents
- [Page Structure](#page-structure)
- [Hero Patterns](#hero-patterns)
- [Product Showcase](#product-showcase)
- [Feature Grids](#feature-grids)
- [Split Sections](#split-sections)
- [Stats Ribbon](#stats-ribbon)
- [Comparison Table](#comparison-table)
- [CTA Section](#cta-section)
- [Footer](#footer)

---

## Page Structure

```css
.page {
  font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  background: var(--apple-bg);
  color: var(--apple-text-primary);
  -webkit-font-smoothing: antialiased;
}

.section {
  max-width: 980px;
  margin: 0 auto;
  padding: 80px 24px;
}

.section--wide {
  max-width: 1200px;
}

.section--full {
  max-width: 100%;
  padding-left: 0;
  padding-right: 0;
}

.section__eyebrow {
  font-size: 14px;
  font-weight: 600;
  color: var(--apple-accent);
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-bottom: 8px;
}

.section__headline {
  font-size: 48px;
  font-weight: 700;
  line-height: 1.08;
  letter-spacing: -0.012em;
  margin-bottom: 16px;
}

.section__body {
  font-size: 21px;
  line-height: 1.47;
  color: var(--apple-text-secondary);
  max-width: 600px;
}
```

---

## Hero Patterns

### Centered Hero (Light)

```css
.hero-centered {
  text-align: center;
  padding: 120px 24px 80px;
  max-width: 980px;
  margin: 0 auto;
}

.hero-centered__title {
  font-size: 80px;
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: -0.015em;
  color: var(--apple-text-primary);
}

.hero-centered__subtitle {
  font-size: 28px;
  font-weight: 400;
  color: var(--apple-text-secondary);
  margin-top: 16px;
  line-height: 1.14;
}

.hero-centered__cta-group {
  display: flex;
  gap: 16px;
  justify-content: center;
  margin-top: 32px;
}

.hero-centered__image {
  margin-top: 48px;
  width: 100%;
  border-radius: 24px;
  overflow: hidden;
}
```

### Dark Hero (Immersive)

```css
.hero-dark {
  background: #000000;
  color: #F5F5F7;
  text-align: center;
  padding: 120px 24px;
  position: relative;
  overflow: hidden;
}

.hero-dark__title {
  font-size: 80px;
  font-weight: 700;
  line-height: 1.05;
  letter-spacing: -0.015em;
  background: linear-gradient(135deg, #FFFFFF 0%, #A1A1A6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-dark__subtitle {
  font-size: 28px;
  color: #A1A1A6;
  margin-top: 16px;
}

.hero-dark__bg-glow {
  position: absolute;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(41,151,255,0.15) 0%, transparent 70%);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
}
```

### Split Hero (Text + Image)

```css
.hero-split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 48px;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 96px 24px;
}

.hero-split__content {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.hero-split__title {
  font-size: 56px;
  font-weight: 700;
  line-height: 1.07;
  letter-spacing: -0.012em;
}

.hero-split__body {
  font-size: 21px;
  line-height: 1.47;
  color: var(--apple-text-secondary);
}

.hero-split__media {
  border-radius: 24px;
  overflow: hidden;
}

.hero-split__media img {
  width: 100%;
  display: block;
}

@media (max-width: 768px) {
  .hero-split {
    grid-template-columns: 1fr;
    text-align: center;
  }
}
```

---

## Product Showcase

```css
.product-showcase {
  text-align: center;
  padding: 96px 24px;
  background: var(--apple-surface);
}

.product-showcase__image {
  max-width: 720px;
  margin: 48px auto 0;
}

.product-showcase__specs {
  display: flex;
  justify-content: center;
  gap: 48px;
  margin-top: 48px;
}

.product-showcase__spec {
  text-align: center;
}

.product-showcase__spec-value {
  font-size: 48px;
  font-weight: 700;
  color: var(--apple-text-primary);
}

.product-showcase__spec-label {
  font-size: 14px;
  color: var(--apple-text-secondary);
  margin-top: 4px;
}
```

---

## Feature Grids

### 3-Column Grid

```css
.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

.grid-3__card {
  background: var(--apple-elevated);
  border: 1px solid var(--apple-card-border);
  border-radius: 18px;
  padding: 32px;
  box-shadow: var(--apple-shadow-sm);
  transition: var(--apple-theme-transition);
}

@media (max-width: 768px) {
  .grid-3 { grid-template-columns: 1fr; }
}
```

### 2-Column Grid

```css
.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  max-width: 980px;
  margin: 0 auto;
  padding: 0 24px;
}

.grid-2__card {
  background: var(--apple-elevated);
  border: 1px solid var(--apple-card-border);
  border-radius: 18px;
  padding: 40px;
  box-shadow: var(--apple-shadow-sm);
  transition: var(--apple-theme-transition);
}

@media (max-width: 576px) {
  .grid-2 { grid-template-columns: 1fr; }
}
```

### Bento Grid

```css
.bento {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: 280px;
  gap: 16px;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 24px;
}

.bento__item {
  background: var(--apple-elevated);
  border: 1px solid var(--apple-card-border);
  border-radius: 18px;
  padding: 32px;
  box-shadow: var(--apple-shadow-sm);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  transition: var(--apple-theme-transition);
}

.bento__item--wide { grid-column: span 2; }
.bento__item--tall { grid-row: span 2; }
.bento__item--hero { grid-column: span 2; grid-row: span 2; }

@media (max-width: 768px) {
  .bento { grid-template-columns: repeat(2, 1fr); grid-auto-rows: 200px; }
  .bento__item--hero { grid-column: span 2; grid-row: span 1; }
}
```

---

## Split Sections

```css
.split {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 96px 24px;
}

.split--reverse { direction: rtl; }
.split--reverse > * { direction: ltr; }

.split__media img {
  width: 100%;
  border-radius: 18px;
}
```

---

## Stats Ribbon

```css
.stats-ribbon {
  display: flex;
  justify-content: center;
  gap: 64px;
  padding: 64px 24px;
  background: var(--apple-surface);
  border-top: 1px solid var(--apple-card-border);
  border-bottom: 1px solid var(--apple-card-border);
  transition: var(--apple-theme-transition);
}

.stats-ribbon__item { text-align: center; }

.stats-ribbon__value {
  font-size: 56px;
  font-weight: 700;
  letter-spacing: -0.012em;
}

.stats-ribbon__label {
  font-size: 14px;
  color: var(--apple-text-secondary);
  margin-top: 4px;
}

@media (max-width: 576px) {
  .stats-ribbon { flex-direction: column; gap: 32px; }
}
```

---

## Comparison Table

```css
.comparison-table {
  width: 100%;
  border-collapse: collapse;
  max-width: 980px;
  margin: 0 auto;
}

.comparison-table th,
.comparison-table td {
  padding: 16px 24px;
  text-align: left;
  border-bottom: 1px solid var(--apple-card-border);
  font-size: 17px;
}

.comparison-table th {
  font-weight: 600;
  color: var(--apple-text-primary);
}

.comparison-table td {
  color: var(--apple-text-secondary);
}

.comparison-table__highlight {
  background: var(--apple-elevated);
  font-weight: 600;
  color: var(--apple-accent);
}
```

---

## CTA Section

```css
.cta-section {
  text-align: center;
  padding: 96px 24px;
  background: var(--apple-surface);
  transition: var(--apple-theme-transition);
}

.cta-section__title {
  font-size: 48px;
  font-weight: 700;
  letter-spacing: -0.012em;
}

.cta-section__body {
  font-size: 21px;
  color: var(--apple-text-secondary);
  margin-top: 12px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.cta-section__actions {
  display: flex;
  gap: 16px;
  justify-content: center;
  margin-top: 32px;
}
```

---

## Footer

```css
.footer {
  background: var(--apple-surface);
  border-top: 1px solid var(--apple-card-border);
  padding: 32px 24px 24px;
  font-size: 12px;
  color: var(--apple-text-secondary);
  transition: var(--apple-theme-transition);
}

.footer__grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 24px;
  max-width: 980px;
  margin: 0 auto 32px;
}

.footer__col-title {
  font-weight: 600;
  color: var(--apple-text-primary);
  margin-bottom: 12px;
  font-size: 12px;
}

.footer__link {
  display: block;
  color: var(--apple-text-secondary);
  text-decoration: none;
  padding: 4px 0;
}

.footer__link:hover {
  color: var(--apple-text-primary);
}

.footer__bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 980px;
  margin: 0 auto;
  padding-top: 16px;
  border-top: 1px solid var(--apple-card-border);
}

@media (max-width: 768px) {
  .footer__grid { grid-template-columns: repeat(2, 1fr); }
}
```
