# Apple Design System — Animations

## Table of Contents
- [Core Principles](#core-principles)
- [Hover Effects](#hover-effects)
- [Scroll Animations](#scroll-animations)
- [Page Transitions](#page-transitions)
- [Micro-Interactions](#micro-interactions)
- [Loading States](#loading-states)
- [Parallax](#parallax)
- [SwiftUI Animation Presets](#swiftui-animation-presets)

---

## Core Principles

1. **Purposeful motion**: Every animation must serve a function -- guide attention, confirm an action, or reveal content.
2. **Ease curve**: Default to `cubic-bezier(0.25, 0.1, 0.25, 1)` for natural deceleration.
3. **Duration ladder**: 150ms (micro), 300ms (default), 500ms (emphasis), 800ms (page-level).
4. **Respect preferences**: Always wrap motion in `@media (prefers-reduced-motion)` checks.
5. **Theme transitions**: All themed elements use `transition: background-color 0.4s ease, color 0.3s ease, border-color 0.4s ease, box-shadow 0.4s ease`.

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## Hover Effects

### Card Lift

```css
.card-hover {
  background: var(--apple-elevated);
  border: 1px solid var(--apple-card-border);
  border-radius: 18px;
  box-shadow: var(--apple-shadow-sm);
  transition: transform 0.3s cubic-bezier(0.25, 0.1, 0.25, 1),
              box-shadow 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.card-hover:hover {
  transform: translateY(-4px);
  box-shadow: var(--apple-shadow-lg);
}
```

### Scale Effect

```css
.scale-hover {
  transition: transform 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.scale-hover:hover {
  transform: scale(1.02);
}

.scale-hover:active {
  transform: scale(0.98);
}
```

### Image Zoom

```css
.image-zoom {
  overflow: hidden;
  border-radius: 18px;
}

.image-zoom img {
  width: 100%;
  display: block;
  transition: transform 0.6s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.image-zoom:hover img {
  transform: scale(1.05);
}
```

---

## Scroll Animations

### IntersectionObserver Fade-In

```css
.fade-in {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s cubic-bezier(0.25, 0.1, 0.25, 1),
              transform 0.6s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.fade-in--visible {
  opacity: 1;
  transform: translateY(0);
}
```

```javascript
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in--visible');
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.15, rootMargin: '0px 0px -60px 0px' }
);

document.querySelectorAll('.fade-in').forEach((el) => observer.observe(el));
```

### Stagger Animation

```css
.stagger > * {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.5s cubic-bezier(0.25, 0.1, 0.25, 1),
              transform 0.5s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.stagger--visible > *:nth-child(1) { transition-delay: 0ms; }
.stagger--visible > *:nth-child(2) { transition-delay: 100ms; }
.stagger--visible > *:nth-child(3) { transition-delay: 200ms; }
.stagger--visible > *:nth-child(4) { transition-delay: 300ms; }
.stagger--visible > *:nth-child(5) { transition-delay: 400ms; }
.stagger--visible > *:nth-child(6) { transition-delay: 500ms; }

.stagger--visible > * {
  opacity: 1;
  transform: translateY(0);
}
```

```javascript
const staggerObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('stagger--visible');
        staggerObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.1 }
);

document.querySelectorAll('.stagger').forEach((el) => staggerObserver.observe(el));
```

### Counter Animation

```javascript
function animateCounter(el, target, duration = 1500) {
  const start = performance.now();
  const initial = 0;

  function tick(now) {
    const elapsed = now - start;
    const progress = Math.min(elapsed / duration, 1);
    // Ease out: cubic-bezier approximation
    const eased = 1 - Math.pow(1 - progress, 3);
    const current = Math.round(initial + (target - initial) * eased);
    el.textContent = current.toLocaleString();

    if (progress < 1) requestAnimationFrame(tick);
  }

  requestAnimationFrame(tick);
}

// Usage with IntersectionObserver
const counterObserver = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      const target = parseInt(entry.target.dataset.target, 10);
      animateCounter(entry.target, target);
      counterObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.5 });

document.querySelectorAll('[data-counter]').forEach((el) => counterObserver.observe(el));
```

---

## Page Transitions

```css
.page-enter {
  opacity: 0;
  transform: translateY(12px);
}

.page-enter-active {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 0.5s cubic-bezier(0.25, 0.1, 0.25, 1),
              transform 0.5s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.page-exit {
  opacity: 1;
}

.page-exit-active {
  opacity: 0;
  transition: opacity 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}
```

### View Transition API (Modern Browsers)

```javascript
function navigateTo(url) {
  if (!document.startViewTransition) {
    window.location.href = url;
    return;
  }

  document.startViewTransition(async () => {
    const response = await fetch(url);
    const html = await response.text();
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');
    document.querySelector('main').replaceWith(doc.querySelector('main'));
    history.pushState({}, '', url);
  });
}
```

```css
::view-transition-old(root) {
  animation: fade-out 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

::view-transition-new(root) {
  animation: fade-in 0.5s cubic-bezier(0.25, 0.1, 0.25, 1);
}

@keyframes fade-out { to { opacity: 0; } }
@keyframes fade-in { from { opacity: 0; } }
```

---

## Micro-Interactions

### Button Press

```css
.btn-press {
  transition: transform 0.15s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.btn-press:active {
  transform: scale(0.97);
}
```

### Checkmark Draw

```css
@keyframes draw-check {
  from { stroke-dashoffset: 24; }
  to   { stroke-dashoffset: 0; }
}

.checkmark {
  stroke-dasharray: 24;
  stroke-dashoffset: 24;
  animation: draw-check 0.4s cubic-bezier(0.25, 0.1, 0.25, 1) forwards;
  animation-delay: 0.15s;
}
```

### Ripple Feedback

```css
.ripple {
  position: relative;
  overflow: hidden;
}

.ripple::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at var(--x, 50%) var(--y, 50%),
    rgba(0,0,0,0.06) 0%, transparent 60%);
  opacity: 0;
  transition: opacity 0.3s cubic-bezier(0.25, 0.1, 0.25, 1);
}

.ripple:active::after {
  opacity: 1;
}
```

---

## Loading States

### Skeleton Shimmer

```css
.skeleton {
  background: linear-gradient(
    90deg,
    var(--apple-surface) 25%,
    var(--apple-elevated) 50%,
    var(--apple-surface) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 8px;
}

@keyframes shimmer {
  0%   { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}

.skeleton--text {
  height: 17px;
  margin-bottom: 8px;
}

.skeleton--title {
  height: 28px;
  width: 60%;
  margin-bottom: 12px;
}

.skeleton--image {
  height: 200px;
  border-radius: 18px;
}
```

### Spinner

```css
.spinner {
  width: 24px;
  height: 24px;
  border: 3px solid var(--apple-surface);
  border-top-color: var(--apple-accent);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}
```

---

## Parallax

```css
.parallax-section {
  position: relative;
  overflow: hidden;
  min-height: 600px;
}

.parallax-bg {
  position: absolute;
  inset: -20% 0;
  background-size: cover;
  background-position: center;
  will-change: transform;
}
```

```javascript
function initParallax() {
  const elements = document.querySelectorAll('.parallax-bg');

  window.addEventListener('scroll', () => {
    requestAnimationFrame(() => {
      elements.forEach((el) => {
        const rect = el.parentElement.getBoundingClientRect();
        const speed = parseFloat(el.dataset.speed || 0.3);
        const offset = rect.top * speed;
        el.style.transform = `translate3d(0, ${offset}px, 0)`;
      });
    });
  }, { passive: true });
}

initParallax();
```

---

## SwiftUI Animation Presets

```swift
extension Animation {
    /// Default Apple-style ease: matches cubic-bezier(0.25, 0.1, 0.25, 1)
    static let appleEase = Animation.timingCurve(0.25, 0.1, 0.25, 1, duration: 0.3)

    /// Micro interaction (button press)
    static let appleMicro = Animation.timingCurve(0.25, 0.1, 0.25, 1, duration: 0.15)

    /// Emphasis animation (modal, hero)
    static let appleEmphasis = Animation.timingCurve(0.25, 0.1, 0.25, 1, duration: 0.5)

    /// Spring for playful interactions
    static let appleSpring = Animation.spring(response: 0.35, dampingFraction: 0.7)

    /// Page-level transition
    static let applePage = Animation.timingCurve(0.25, 0.1, 0.25, 1, duration: 0.8)
}

// Usage
struct AnimatedCard: View {
    @State private var isVisible = false

    var body: some View {
        CardView()
            .opacity(isVisible ? 1 : 0)
            .offset(y: isVisible ? 0 : 20)
            .animation(.appleEase, value: isVisible)
            .onAppear { isVisible = true }
    }
}
```
