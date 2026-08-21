# Apple Design System — Iconography

## Table of Contents
- [SF Symbols](#sf-symbols)
- [Common Symbols Table](#common-symbols-table)
- [SettingsIcon Badge Component](#settingsicon-badge-component)
- [SVG Icons](#svg-icons)
- [Icon Sizing](#icon-sizing)
- [Icon + Text Alignment](#icon--text-alignment)
- [Colored Icon Badges](#colored-icon-badges)

---

## SF Symbols

SF Symbols is Apple's canonical icon library with 5,000+ symbols that automatically align with San Francisco text. Use them on all Apple platforms; for web, replicate the most common ones as inline SVGs.

### Rendering Modes

| Mode           | Description                          | SwiftUI                                |
|----------------|--------------------------------------|----------------------------------------|
| Monochrome     | Single color, adapts to tint         | `.symbolRenderingMode(.monochrome)`    |
| Hierarchical   | Single color with depth layers       | `.symbolRenderingMode(.hierarchical)`  |
| Palette         | Multiple custom colors               | `.symbolRenderingMode(.palette)`       |
| Multicolor     | Apple-defined fixed colors           | `.symbolRenderingMode(.multicolor)`    |

### Symbol Weights

Symbols respect the text weight context. Use `.fontWeight()` or `.imageScale()` to adjust.

```swift
Image(systemName: "gear")
    .font(.title2)
    .fontWeight(.semibold)
    .imageScale(.large)
```

---

## Common Symbols Table

| Purpose             | SF Symbol Name               | Web Fallback       |
|---------------------|------------------------------|---------------------|
| Settings            | `gear`                       | SVG gear            |
| Profile             | `person.circle`              | SVG user circle     |
| Search              | `magnifyingglass`            | SVG magnifier       |
| Close               | `xmark`                      | SVG x               |
| Back / Chevron Left | `chevron.left`               | SVG chevron-left    |
| Forward / Chevron   | `chevron.right`              | SVG chevron-right   |
| Checkmark           | `checkmark`                  | SVG checkmark       |
| External Link       | `arrow.up.right`             | SVG external        |
| Share               | `square.and.arrow.up`        | SVG share           |
| Download            | `arrow.down.circle`          | SVG download        |
| Heart               | `heart`                      | SVG heart           |
| Heart Filled        | `heart.fill`                 | SVG heart-fill      |
| Star                | `star`                       | SVG star            |
| Star Filled         | `star.fill`                  | SVG star-fill       |
| Bell                | `bell`                       | SVG bell            |
| Cart                | `cart`                       | SVG cart            |
| Trash               | `trash`                      | SVG trash           |
| Pencil / Edit       | `pencil`                     | SVG pencil          |
| Plus                | `plus`                       | SVG plus            |
| Minus               | `minus`                      | SVG minus           |
| Info                | `info.circle`                | SVG info            |
| Warning             | `exclamationmark.triangle`   | SVG warning         |
| WiFi                | `wifi`                       | SVG wifi            |
| Battery             | `battery.100`                | SVG battery         |
| Lock                | `lock`                       | SVG lock            |
| Camera              | `camera`                     | SVG camera          |
| Photo               | `photo`                      | SVG photo           |

---

## SettingsIcon Badge Component

A reusable badge icon used in iOS Settings-style lists.

### SwiftUI

```swift
struct SettingsIcon: View {
    let systemName: String
    let backgroundColor: Color
    let foregroundColor: Color

    init(_ systemName: String, bg: Color, fg: Color = .white) {
        self.systemName = systemName
        self.backgroundColor = bg
        self.foregroundColor = fg
    }

    var body: some View {
        Image(systemName: systemName)
            .font(.system(size: 15, weight: .semibold))
            .foregroundStyle(foregroundColor)
            .frame(width: 30, height: 30)
            .background(backgroundColor, in: RoundedRectangle(cornerRadius: 7))
    }
}

// Usage in a List
List {
    Label {
        Text("Wi-Fi")
    } icon: {
        SettingsIcon("wifi", bg: .blue)
    }

    Label {
        Text("Bluetooth")
    } icon: {
        SettingsIcon("antenna.radiowaves.left.and.right", bg: .blue)
    }

    Label {
        Text("Notifications")
    } icon: {
        SettingsIcon("bell.badge", bg: .red)
    }

    Label {
        Text("General")
    } icon: {
        SettingsIcon("gear", bg: .gray)
    }
}
.listStyle(.insetGrouped)
```

### CSS (Web Equivalent)

```css
.settings-icon {
  width: 30px;
  height: 30px;
  border-radius: 7px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.settings-icon svg {
  width: 16px;
  height: 16px;
  fill: #FFFFFF;
}

.settings-icon--blue   { background: #007AFF; }
.settings-icon--red    { background: #FF3B30; }
.settings-icon--green  { background: #34C759; }
.settings-icon--orange { background: #FF9500; }
.settings-icon--gray   { background: #8E8E93; }
.settings-icon--purple { background: #AF52DE; }
```

---

## SVG Icons

### Chevron Right

```html
<svg width="8" height="14" viewBox="0 0 8 14" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 1L7 7L1 13" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

### Checkmark

```html
<svg width="14" height="11" viewBox="0 0 14 11" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 5.5L5 9.5L13 1" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

### External Link (Arrow Up Right)

```html
<svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M4 1H13V10" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M13 1L1 13" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
```

### Close (X Mark)

```html
<svg width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg">
  <path d="M1 1L13 13M13 1L1 13" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>
```

### Search (Magnifying Glass)

```html
<svg width="18" height="18" viewBox="0 0 18 18" fill="none" xmlns="http://www.w3.org/2000/svg">
  <circle cx="7.5" cy="7.5" r="6" stroke="currentColor" stroke-width="2"/>
  <path d="M12 12L16.5 16.5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
</svg>
```

---

## Icon Sizing

| Context         | Size  | SF Symbol Scale | SVG Width/Height |
|-----------------|-------|-----------------|------------------|
| Inline text     | 16px  | `.small`        | 16x16            |
| Body text       | 20px  | `.medium`       | 20x20            |
| Title / heading | 24px  | `.large`        | 24x24            |
| Nav bar         | 22px  | `.medium`       | 22x22            |
| Touch button    | 24px  | `.large`        | 24x24 (in 44px)  |
| Feature icon    | 32px  | —               | 32x32            |
| Hero icon       | 56px  | —               | 56x56            |

### SwiftUI Image Scale

```swift
Image(systemName: "gear")
    .imageScale(.small)   // ~16pt
Image(systemName: "gear")
    .imageScale(.medium)  // ~20pt (default)
Image(systemName: "gear")
    .imageScale(.large)   // ~24pt
```

---

## Icon + Text Alignment

### CSS Inline Alignment

```css
.icon-text {
  display: inline-flex;
  align-items: center;
  gap: 8px;
}

.icon-text svg {
  flex-shrink: 0;
  width: 20px;
  height: 20px;
}
```

### SwiftUI Label

```swift
// Automatic alignment via Label
Label("Settings", systemImage: "gear")
    .font(.body)

// Manual alignment
HStack(spacing: 8) {
    Image(systemName: "checkmark.circle.fill")
        .foregroundStyle(.green)
    Text("Completed")
}
.font(.body)
```

### Baseline Alignment for Larger Icons

```css
.icon-text--baseline {
  display: inline-flex;
  align-items: baseline;
  gap: 8px;
}

.icon-text--baseline svg {
  position: relative;
  top: 0.125em; /* nudge icon to baseline */
}
```

---

## Colored Icon Badges

Round or rounded-rect badges with colored backgrounds and white icons. Common in lists and dashboards.

### CSS

```css
.icon-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  flex-shrink: 0;
}

.icon-badge--sm  { width: 32px; height: 32px; border-radius: 8px; }
.icon-badge--md  { width: 44px; height: 44px; border-radius: 12px; }
.icon-badge--lg  { width: 56px; height: 56px; border-radius: 16px; }

.icon-badge svg {
  fill: #FFFFFF;
}

.icon-badge--blue   { background: #007AFF; }
.icon-badge--green  { background: #34C759; }
.icon-badge--red    { background: #FF3B30; }
.icon-badge--orange { background: #FF9500; }
.icon-badge--purple { background: #AF52DE; }
.icon-badge--teal   { background: #5AC8FA; }
.icon-badge--pink   { background: #FF2D55; }
.icon-badge--indigo { background: #5856D6; }
```

### SwiftUI

```swift
struct IconBadge: View {
    let systemName: String
    let backgroundColor: Color
    var size: CGFloat = 44

    var body: some View {
        Image(systemName: systemName)
            .font(.system(size: size * 0.42, weight: .semibold))
            .foregroundStyle(.white)
            .frame(width: size, height: size)
            .background(backgroundColor, in: RoundedRectangle(cornerRadius: size * 0.27))
    }
}

// Usage
IconBadge(systemName: "bolt.fill", backgroundColor: .orange)
IconBadge(systemName: "lock.fill", backgroundColor: .red, size: 56)
```
