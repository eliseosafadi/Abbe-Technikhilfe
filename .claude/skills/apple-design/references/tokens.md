# Apple Design System — Design Tokens

## Table of Contents
- [Color Tokens](#color-tokens)
- [Typography Scale](#typography-scale)
- [Spacing System](#spacing-system)
- [Border Radius](#border-radius)
- [Shadows](#shadows)
- [Animation Curves](#animation-curves)
- [CSS Custom Properties](#css-custom-properties)
- [Card Visibility Rules](#card-visibility-rules)
- [SwiftUI Extensions](#swiftui-extensions)

---

## Color Tokens

### Light Mode

| Token               | Value                  | Usage                        |
|----------------------|------------------------|------------------------------|
| bg                   | `#FFFFFF`              | Page background              |
| surface              | `#F5F5F7`              | Section backgrounds          |
| elevated             | `#FBFBFD`              | Cards, popovers              |
| text-primary         | `#1D1D1F`              | Headings, body text          |
| text-secondary       | `#86868B`              | Captions, labels             |
| accent               | `#0071E3`              | Links, CTAs, focus rings     |
| card-border          | `rgba(0,0,0,0.06)`    | Card & divider borders       |

### Dark Mode

| Token               | Value                    | Usage                        |
|----------------------|--------------------------|------------------------------|
| bg                   | `#000000`                | Page background              |
| surface              | `#1C1C1E`                | Section backgrounds          |
| elevated             | `#2C2C2E`                | Cards, popovers              |
| text-primary         | `#F5F5F7`                | Headings, body text          |
| text-secondary       | `#A1A1A6`                | Captions, labels             |
| accent               | `#2997FF`                | Links, CTAs, focus rings     |
| card-border          | `rgba(255,255,255,0.08)` | Card & divider borders       |

---

## Typography Scale

### Web (CSS)

```
Font stack: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif
```

| Name          | Size   | Weight | Line Height | Letter Spacing | Use Case           |
|---------------|--------|--------|-------------|----------------|--------------------|
| hero          | 80px   | 700    | 1.05        | -0.015em       | Landing hero       |
| display       | 56px   | 700    | 1.07        | -0.012em       | Page titles        |
| headline      | 40px   | 600    | 1.1         | -0.01em        | Section heads      |
| title-1       | 32px   | 600    | 1.125       | -0.005em       | Sub-sections       |
| title-2       | 28px   | 600    | 1.14        | 0              | Card titles        |
| title-3       | 24px   | 600    | 1.17        | 0              | Widget titles      |
| body-large    | 21px   | 400    | 1.47        | 0.011em        | Intro paragraphs   |
| body          | 17px   | 400    | 1.47        | -0.022em       | Default body       |
| callout       | 14px   | 400    | 1.43        | -0.016em       | Supporting text    |
| caption       | 12px   | 400    | 1.33        | 0              | Labels, metadata   |

### SwiftUI (iOS)

| Style          | SwiftUI Modifier          | Approx Size |
|----------------|---------------------------|-------------|
| Large Title    | `.font(.largeTitle)`      | 34pt        |
| Title          | `.font(.title)`           | 28pt        |
| Title 2        | `.font(.title2)`          | 22pt        |
| Title 3        | `.font(.title3)`          | 20pt        |
| Headline       | `.font(.headline)`        | 17pt bold   |
| Body           | `.font(.body)`            | 17pt        |
| Callout        | `.font(.callout)`         | 16pt        |
| Subheadline    | `.font(.subheadline)`     | 15pt        |
| Footnote       | `.font(.footnote)`        | 13pt        |
| Caption        | `.font(.caption)`         | 12pt        |
| Caption 2      | `.font(.caption2)`        | 11pt        |

---

## Spacing System

8px base grid:

| Token   | Value | Common Usage                    |
|---------|-------|---------------------------------|
| space-1 | 4px   | Inline icon gap                 |
| space-2 | 8px   | Tight element padding           |
| space-3 | 12px  | Compact card padding            |
| space-4 | 16px  | Standard padding, gap           |
| space-5 | 20px  | Section inner spacing           |
| space-6 | 24px  | Card padding                    |
| space-7 | 32px  | Between content blocks          |
| space-8 | 48px  | Section vertical padding        |
| space-9 | 64px  | Major section breaks            |
| space-10| 80px  | Hero vertical padding           |
| space-11| 96px  | Page-level vertical breathing   |
| space-12| 120px | Maximum section separation      |

---

## Border Radius

| Token       | Value | Usage                   |
|-------------|-------|-------------------------|
| radius-sm   | 8px   | Buttons, badges, inputs |
| radius-md   | 12px  | Cards, dropdowns        |
| radius-lg   | 18px  | Modal corners           |
| radius-xl   | 24px  | Hero cards, images      |
| radius-full | 980px | Pill buttons, avatars   |

---

## Shadows

### Light Mode

| Level     | Value                                          |
|-----------|------------------------------------------------|
| shadow-sm | `0 1px 3px rgba(0,0,0,0.08)`                  |
| shadow-md | `0 4px 12px rgba(0,0,0,0.08)`                 |
| shadow-lg | `0 8px 30px rgba(0,0,0,0.12)`                 |
| shadow-xl | `0 20px 60px rgba(0,0,0,0.15)`                |

### Dark Mode

| Level     | Value                                          |
|-----------|------------------------------------------------|
| shadow-sm | `0 1px 3px rgba(0,0,0,0.3)`                   |
| shadow-md | `0 4px 12px rgba(0,0,0,0.4)`                  |
| shadow-lg | `0 8px 30px rgba(0,0,0,0.5)`                  |
| shadow-xl | `0 20px 60px rgba(0,0,0,0.6)`                 |

---

## Animation Curves

| Name        | Value                              | Usage                    |
|-------------|------------------------------------|--------------------------|
| ease-apple  | `cubic-bezier(0.25, 0.1, 0.25, 1)` | Default for all motion  |
| ease-out    | `cubic-bezier(0, 0, 0.58, 1)`     | Enter animations         |
| ease-in     | `cubic-bezier(0.42, 0, 1, 1)`     | Exit animations          |
| spring      | `cubic-bezier(0.34, 1.56, 0.64, 1)` | Playful micro-actions  |

Standard durations: `150ms` (micro), `300ms` (default), `500ms` (emphasis), `800ms` (page-level).

---

## CSS Custom Properties

```css
:root {
  /* Colors — Light */
  --apple-bg: #FFFFFF;
  --apple-surface: #F5F5F7;
  --apple-elevated: #FBFBFD;
  --apple-text-primary: #1D1D1F;
  --apple-text-secondary: #86868B;
  --apple-accent: #0071E3;
  --apple-card-border: rgba(0,0,0,0.06);

  /* Shadows — Light */
  --apple-shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
  --apple-shadow-md: 0 4px 12px rgba(0,0,0,0.08);
  --apple-shadow-lg: 0 8px 30px rgba(0,0,0,0.12);

  /* Typography */
  --apple-font: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;

  /* Spacing */
  --apple-space-1: 4px;
  --apple-space-2: 8px;
  --apple-space-3: 12px;
  --apple-space-4: 16px;
  --apple-space-5: 20px;
  --apple-space-6: 24px;
  --apple-space-7: 32px;
  --apple-space-8: 48px;
  --apple-space-9: 64px;

  /* Radius */
  --apple-radius-sm: 8px;
  --apple-radius-md: 12px;
  --apple-radius-lg: 18px;
  --apple-radius-xl: 24px;
  --apple-radius-full: 980px;

  /* Motion */
  --apple-ease: cubic-bezier(0.25, 0.1, 0.25, 1);
  --apple-duration: 300ms;

  /* Theme transition */
  --apple-theme-transition: background-color 0.4s ease, color 0.3s ease, border-color 0.4s ease, box-shadow 0.4s ease;
}

/* System-level dark preference */
@media (prefers-color-scheme: dark) {
  :root {
    --apple-bg: #000000;
    --apple-surface: #1C1C1E;
    --apple-elevated: #2C2C2E;
    --apple-text-primary: #F5F5F7;
    --apple-text-secondary: #A1A1A6;
    --apple-accent: #2997FF;
    --apple-card-border: rgba(255,255,255,0.08);
    --apple-shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
    --apple-shadow-md: 0 4px 12px rgba(0,0,0,0.4);
    --apple-shadow-lg: 0 8px 30px rgba(0,0,0,0.5);
  }
}

/* Manual toggle override */
[data-theme="dark"] {
  --apple-bg: #000000;
  --apple-surface: #1C1C1E;
  --apple-elevated: #2C2C2E;
  --apple-text-primary: #F5F5F7;
  --apple-text-secondary: #A1A1A6;
  --apple-accent: #2997FF;
  --apple-card-border: rgba(255,255,255,0.08);
  --apple-shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
  --apple-shadow-md: 0 4px 12px rgba(0,0,0,0.4);
  --apple-shadow-lg: 0 8px 30px rgba(0,0,0,0.5);
}

/* Smooth theme transition on all themed elements */
body, .card, .nav, .section, .btn, .input {
  transition: var(--apple-theme-transition);
}
```

---

## Card Visibility Rules

Cards MUST follow these rules to remain visible in both themes:

1. **Background step**: Card background must be one elevation step above its parent (`surface` on `bg`, `elevated` on `surface`).
2. **Border always present**: Every card must include `border: 1px solid var(--apple-card-border)`.
3. **Shadow reinforcement**: Apply at minimum `var(--apple-shadow-sm)` to every card.
4. **Dark mode triple defense**: In dark mode, cards rely on all three (bg step + border + shadow) simultaneously. Removing any one can make the card invisible.
5. **Never use pure white cards on white backgrounds** in light mode, and never use `#000` cards on `#000` backgrounds in dark mode.

```css
/* Correct card pattern */
.card {
  background: var(--apple-elevated);
  border: 1px solid var(--apple-card-border);
  box-shadow: var(--apple-shadow-sm);
  border-radius: var(--apple-radius-md);
  transition: var(--apple-theme-transition);
}
```

---

## SwiftUI Extensions

```swift
import SwiftUI

enum AppleDesign {
    enum Colors {
        static let bg = Color("bg") // Asset catalog adaptive
        static let surface = Color("surface")
        static let elevated = Color("elevated")
        static let textPrimary = Color("textPrimary")
        static let textSecondary = Color("textSecondary")
        static let accent = Color("accent")
    }

    enum Spacing {
        static let xs: CGFloat = 4
        static let sm: CGFloat = 8
        static let md: CGFloat = 16
        static let lg: CGFloat = 24
        static let xl: CGFloat = 32
        static let xxl: CGFloat = 48
    }

    enum Radius {
        static let sm: CGFloat = 8
        static let md: CGFloat = 12
        static let lg: CGFloat = 18
        static let xl: CGFloat = 24
    }
}

extension Color {
    init(hex: String) {
        let hex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&int)
        let r, g, b, a: UInt64
        switch hex.count {
        case 6: (r, g, b, a) = (int >> 16, int >> 8 & 0xFF, int & 0xFF, 255)
        case 8: (r, g, b, a) = (int >> 24, int >> 16 & 0xFF, int >> 8 & 0xFF, int & 0xFF)
        default: (r, g, b, a) = (0, 0, 0, 255)
        }
        self.init(
            .sRGB,
            red: Double(r) / 255,
            green: Double(g) / 255,
            blue: Double(b) / 255,
            opacity: Double(a) / 255
        )
    }

    static func adaptive(light: String, dark: String) -> Color {
        Color(UIColor { traits in
            traits.userInterfaceStyle == .dark ? UIColor(Color(hex: dark)) : UIColor(Color(hex: light))
        })
    }
}
```
