# Apple Design System — Components

## Table of Contents
- [Buttons](#buttons)
- [Cards](#cards)
- [Navigation Bar](#navigation-bar)
- [Text Input](#text-input)
- [Search Bar](#search-bar)
- [Toggle Switch](#toggle-switch)
- [Modal](#modal)
- [Segmented Control](#segmented-control)
- [Badges](#badges)
- [Pricing Cards](#pricing-cards)
- [Testimonials](#testimonials)

---

## Buttons

### Primary Pill Button

```css
.btn-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 28px;
  background: var(--apple-accent);
  color: #FFFFFF;
  font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-size: 17px;
  font-weight: 400;
  border: none;
  border-radius: 980px;
  cursor: pointer;
  text-decoration: none;
  transition: background 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.btn-primary:hover {
  background: #0077ED;
}
```

### Secondary Text Button

```css
.btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: none;
  border: none;
  color: var(--apple-accent);
  font-size: 21px;
  font-weight: 400;
  cursor: pointer;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
}

.btn-secondary::after {
  content: '\203A';
  font-size: 24px;
  transition: transform 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.btn-secondary:hover::after {
  transform: translateX(4px);
}
```

### Outline Button

```css
.btn-outline {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 12px 28px;
  background: transparent;
  color: var(--apple-accent);
  font-size: 17px;
  border: 2px solid var(--apple-accent);
  border-radius: 980px;
  cursor: pointer;
  font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  transition: background 0.3s cubic-bezier(0.25, 0.1, 0.25, 1), color 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.btn-outline:hover {
  background: var(--apple-accent);
  color: #FFFFFF;
}
```

### Compact Button

```css
.btn-compact {
  padding: 8px 18px;
  font-size: 12px;
  font-weight: 400;
  border-radius: 980px;
  background: var(--apple-accent);
  color: #FFFFFF;
  border: none;
  cursor: pointer;
}
```

### SwiftUI Buttons

```swift
struct ApplePrimaryButton: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.body)
            .padding(.horizontal, 28)
            .padding(.vertical, 12)
            .background(Color.accentColor)
            .foregroundStyle(.white)
            .clipShape(Capsule())
            .scaleEffect(configuration.isPressed ? 0.97 : 1.0)
            .animation(.easeOut(duration: 0.15), value: configuration.isPressed)
    }
}

struct AppleOutlineButton: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.body)
            .padding(.horizontal, 28)
            .padding(.vertical, 12)
            .foregroundStyle(Color.accentColor)
            .overlay(Capsule().stroke(Color.accentColor, lineWidth: 2))
            .scaleEffect(configuration.isPressed ? 0.97 : 1.0)
            .animation(.easeOut(duration: 0.15), value: configuration.isPressed)
    }
}
```

---

## Cards

### Standard Card

```css
.card {
  background: var(--apple-elevated);
  border: 1px solid var(--apple-card-border);
  border-radius: 18px;
  padding: 32px;
  box-shadow: var(--apple-shadow-sm);
  transition: var(--apple-theme-transition);
}

.card__title {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 8px;
}

.card__body {
  font-size: 17px;
  color: var(--apple-text-secondary);
  line-height: 1.47;
}
```

### Product Card

```css
.product-card {
  background: var(--apple-elevated);
  border: 1px solid var(--apple-card-border);
  border-radius: 18px;
  overflow: hidden;
  box-shadow: var(--apple-shadow-sm);
  transition: transform 0.3s cubic-bezier(0.25, 0.1, 0.25, 1),
              box-shadow 0.3s cubic-bezier(0.25, 0.1, 0.25, 1),
              background-color 0.4s ease, color 0.3s ease,
              border-color 0.4s ease;
}

.product-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--apple-shadow-lg);
}

.product-card__image {
  width: 100%;
  aspect-ratio: 4/3;
  object-fit: cover;
}

.product-card__content {
  padding: 24px;
}

.product-card__name {
  font-size: 21px;
  font-weight: 600;
}

.product-card__price {
  font-size: 17px;
  color: var(--apple-text-secondary);
  margin-top: 4px;
}

.product-card__cta {
  color: var(--apple-accent);
  font-size: 17px;
  margin-top: 12px;
  display: inline-block;
}
```

### Feature Card

```css
.feature-card {
  background: var(--apple-elevated);
  border: 1px solid var(--apple-card-border);
  border-radius: 18px;
  padding: 40px 32px;
  box-shadow: var(--apple-shadow-sm);
  text-align: center;
  transition: var(--apple-theme-transition);
}

.feature-card__icon {
  width: 56px;
  height: 56px;
  margin: 0 auto 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--apple-surface);
  border-radius: 12px;
  font-size: 28px;
}

.feature-card__title {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 8px;
}

.feature-card__body {
  font-size: 17px;
  color: var(--apple-text-secondary);
  line-height: 1.47;
}
```

---

## Navigation Bar

```css
.nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  height: 52px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  background: rgba(255,255,255,0.72);
  backdrop-filter: saturate(180%) blur(20px);
  -webkit-backdrop-filter: saturate(180%) blur(20px);
  border-bottom: 1px solid var(--apple-card-border);
  transition: var(--apple-theme-transition);
}

[data-theme="dark"] .nav {
  background: rgba(0,0,0,0.72);
}

.nav__logo {
  font-size: 21px;
  font-weight: 700;
  color: var(--apple-text-primary);
}

.nav__links {
  display: flex;
  gap: 28px;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav__link {
  font-size: 14px;
  color: var(--apple-text-secondary);
  text-decoration: none;
  transition: color 0.2s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.nav__link:hover {
  color: var(--apple-text-primary);
}
```

---

## Text Input

```css
.input {
  width: 100%;
  padding: 12px 16px;
  font-size: 17px;
  font-family: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'SF Pro Text', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  color: var(--apple-text-primary);
  background: var(--apple-elevated);
  border: 1px solid var(--apple-card-border);
  border-radius: 12px;
  outline: none;
  transition: border-color 0.3s cubic-bezier(0.25, 0.1, 0.25, 1),
              box-shadow 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.input:focus {
  border-color: var(--apple-accent);
  box-shadow: 0 0 0 4px rgba(0,113,227,0.15);
}

.input::placeholder {
  color: var(--apple-text-secondary);
}
```

---

## Search Bar

```css
.search {
  position: relative;
  max-width: 680px;
  margin: 0 auto;
}

.search__icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--apple-text-secondary);
  width: 18px;
  height: 18px;
}

.search__input {
  width: 100%;
  padding: 14px 16px 14px 44px;
  font-size: 17px;
  background: var(--apple-surface);
  border: 1px solid var(--apple-card-border);
  border-radius: 12px;
  color: var(--apple-text-primary);
  outline: none;
  transition: var(--apple-theme-transition);
}

.search__input:focus {
  background: var(--apple-elevated);
  border-color: var(--apple-accent);
  box-shadow: 0 0 0 4px rgba(0,113,227,0.15);
}
```

---

## Toggle Switch

```css
.toggle {
  position: relative;
  width: 51px;
  height: 31px;
}

.toggle__input {
  opacity: 0;
  width: 0;
  height: 0;
}

.toggle__track {
  position: absolute;
  inset: 0;
  background: #E5E5EA;
  border-radius: 31px;
  cursor: pointer;
  transition: background 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.toggle__input:checked + .toggle__track {
  background: #34C759;
}

.toggle__knob {
  position: absolute;
  top: 2px;
  left: 2px;
  width: 27px;
  height: 27px;
  background: #FFFFFF;
  border-radius: 50%;
  box-shadow: 0 1px 3px rgba(0,0,0,0.15);
  transition: transform 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.toggle__input:checked ~ .toggle__knob {
  transform: translateX(20px);
}
```

---

## Modal

```css
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.48);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 2000;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.modal-backdrop--visible {
  opacity: 1;
  pointer-events: auto;
}

.modal {
  background: var(--apple-elevated);
  border: 1px solid var(--apple-card-border);
  border-radius: 18px;
  padding: 32px;
  max-width: 520px;
  width: 90%;
  box-shadow: var(--apple-shadow-xl);
  transform: scale(0.95) translateY(10px);
  transition: transform 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.modal-backdrop--visible .modal {
  transform: scale(1) translateY(0);
}
```

---

## Segmented Control

```css
.segmented {
  display: inline-flex;
  background: var(--apple-surface);
  border: 1px solid var(--apple-card-border);
  border-radius: 8px;
  padding: 2px;
  gap: 2px;
}

.segmented__btn {
  padding: 8px 20px;
  font-size: 14px;
  font-weight: 500;
  border: none;
  background: transparent;
  border-radius: 6px;
  cursor: pointer;
  color: var(--apple-text-secondary);
  transition: all 0.25s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.segmented__btn--active {
  background: var(--apple-elevated);
  color: var(--apple-text-primary);
  box-shadow: var(--apple-shadow-sm);
}
```

---

## Badges

```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: 4px 10px;
  font-size: 12px;
  font-weight: 600;
  border-radius: 980px;
  background: var(--apple-accent);
  color: #FFFFFF;
}

.badge--outline {
  background: transparent;
  color: var(--apple-accent);
  border: 1px solid var(--apple-accent);
}

.badge--surface {
  background: var(--apple-surface);
  color: var(--apple-text-secondary);
}
```

---

## Pricing Cards

```css
.pricing-card {
  background: var(--apple-elevated);
  border: 1px solid var(--apple-card-border);
  border-radius: 18px;
  padding: 40px 32px;
  text-align: center;
  box-shadow: var(--apple-shadow-sm);
  transition: var(--apple-theme-transition);
}

.pricing-card--featured {
  border-color: var(--apple-accent);
  box-shadow: 0 0 0 1px var(--apple-accent), var(--apple-shadow-md);
}

.pricing-card__tier {
  font-size: 14px;
  font-weight: 600;
  color: var(--apple-text-secondary);
  text-transform: uppercase;
  letter-spacing: 0.04em;
}

.pricing-card__price {
  font-size: 56px;
  font-weight: 700;
  margin: 16px 0 8px;
}

.pricing-card__period {
  font-size: 17px;
  color: var(--apple-text-secondary);
}

.pricing-card__features {
  list-style: none;
  padding: 0;
  margin: 24px 0;
  text-align: left;
}

.pricing-card__feature {
  padding: 8px 0;
  font-size: 14px;
  color: var(--apple-text-secondary);
  border-bottom: 1px solid var(--apple-card-border);
}
```

---

## Testimonials

```css
.testimonial {
  background: var(--apple-elevated);
  border: 1px solid var(--apple-card-border);
  border-radius: 18px;
  padding: 32px;
  box-shadow: var(--apple-shadow-sm);
  transition: var(--apple-theme-transition);
}

.testimonial__quote {
  font-size: 21px;
  line-height: 1.47;
  color: var(--apple-text-primary);
  font-style: italic;
}

.testimonial__author {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-top: 20px;
}

.testimonial__avatar {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  object-fit: cover;
}

.testimonial__name {
  font-size: 14px;
  font-weight: 600;
}

.testimonial__role {
  font-size: 12px;
  color: var(--apple-text-secondary);
}
```
