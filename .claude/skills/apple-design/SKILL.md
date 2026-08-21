---
name: apple-design
description: Comprehensive Apple Design System for building stylish, premium UIs with Apple's design language. Covers design tokens, typography, color, layout patterns, components, animations, responsive design, iconography, and dark mode — for both web (HTML/CSS/JS) and SwiftUI. Use this skill whenever the user wants an Apple-style UI, a clean minimal design, a product landing page, a design system, premium pricing cards, app-like web experiences, or mentions wanting something that looks like apple.com, iOS, or macOS. Also trigger when users say things like "make it look premium", "clean modern design", "minimal elegant UI", "sleek interface", or reference Apple's design language — even if they don't explicitly say "Apple style". Trigger for ANY design task where quality and polish matter.
---

# Apple Design System

A complete design system embodying Apple's philosophy: **clarity, deference, and depth**. Every pixel earns its place.

## Reference Map

| Reference File | When to Read | Contents |
|---------------|-------------|---------|
| `references/tokens.md` | **Every project** | Colors, typography, spacing, shadows, radii, CSS vars, SwiftUI extensions |
| `references/layouts.md` | Full pages/screens | Hero patterns, bento grids, split sections, stats ribbons, footers |
| `references/components.md` | UI elements | Buttons, cards, nav, forms, modals, tabs, badges, pricing cards |
| `references/animations.md` | Motion/interaction | Scroll reveals, hover effects, transitions, loading states, parallax |
| `references/responsive.md` | Multi-device | Breakpoints, fluid type, adaptive grids, mobile nav, touch targets |
| `references/iconography.md` | Icons/assets | SF Symbols, SVG patterns, sizing, alignment, colored badges |
| `references/dark-mode.md` | Dark mode | Card visibility, elevation, color shifts, theme toggle, transitions |
| `references/swiftui-patterns.md` | iOS/macOS native | Components, modifiers, button styles, cards, lists, materials |

## Workflow

1. Read `references/tokens.md` — always start here
2. Identify deliverable — page, component, design system, or app screen
3. Read relevant references (1-3 files)
4. Build mobile-first
5. Strip it down — remove 30% of what you added
6. Check dark mode — read `references/dark-mode.md`
7. Add motion last

## Core Principles

**Radical Simplicity** — Remove until removing more would break it.
**Typographic Hierarchy** — Size, weight, and color create hierarchy — not boxes.
**Breathing Room** — When in doubt, add more whitespace.
**Restrained Color** — 2-3 colors max including neutrals.
**Visible Depth** — Cards need triple defense: background step + border + shadow.

## Quick Tokens

| Token | Light | Dark |
|-------|-------|------|
| Background | `#FFFFFF` | `#000000` |
| Surface | `#F5F5F7` | `#1C1C1E` |
| Elevated | `#FBFBFD` | `#2C2C2E` |
| Text primary | `#1D1D1F` | `#F5F5F7` |
| Text secondary | `#86868B` | `#A1A1A6` |
| Accent | `#0071E3` | `#2997FF` |
| Card border | `rgba(0,0,0,0.06)` | `rgba(255,255,255,0.08)` |

## Critical: Card Visibility

Every card MUST have all three:
1. Background color step (bg → surface → elevated)
2. `border: 1px solid var(--apple-card-border)`
3. Appropriate shadow

## Theme Transition

```css
*, *::before, *::after {
  transition: background-color 0.4s ease, color 0.3s ease,
              border-color 0.4s ease, box-shadow 0.4s ease;
}
```

## Anti-Patterns

- Gradients on text
- Cards with no visible boundary in dark mode
- Washed-out light mode (white on near-white)
- Pure white (#FFF) text on dark backgrounds — use #F5F5F7
- Heavy drop shadows (≤ 0.12 light, ≤ 0.30 dark)
- Underlined links
- Rounded corners < 8px
- Centered paragraph text (only headlines)
