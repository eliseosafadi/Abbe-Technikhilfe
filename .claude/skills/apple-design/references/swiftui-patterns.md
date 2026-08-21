# Apple Design System — SwiftUI Patterns

## Table of Contents
- [AppleDesign Enum](#appledesign-enum)
- [Color Utilities](#color-utilities)
- [View Modifiers](#view-modifiers)
- [Button Styles](#button-styles)
- [Card Components](#card-components)
- [Settings List Patterns](#settings-list-patterns)
- [Navigation](#navigation)
- [Hero Section](#hero-section)
- [Glass and Material Effects](#glass-and-material-effects)
- [Animation Presets](#animation-presets)

---

## AppleDesign Enum

Central namespace for all design tokens.

```swift
import SwiftUI

enum AppleDesign {
    enum Colors {
        static let bg = Color("bg")
        static let surface = Color("surface")
        static let elevated = Color("elevated")
        static let textPrimary = Color("textPrimary")
        static let textSecondary = Color("textSecondary")
        static let accent = Color("accent")

        // Hardcoded fallbacks when asset catalog is unavailable
        static let bgLight = Color(hex: "FFFFFF")
        static let bgDark = Color(hex: "000000")
        static let surfaceLight = Color(hex: "F5F5F7")
        static let surfaceDark = Color(hex: "1C1C1E")
        static let elevatedLight = Color(hex: "FBFBFD")
        static let elevatedDark = Color(hex: "2C2C2E")
        static let textPrimaryLight = Color(hex: "1D1D1F")
        static let textPrimaryDark = Color(hex: "F5F5F7")
        static let textSecondaryLight = Color(hex: "86868B")
        static let textSecondaryDark = Color(hex: "A1A1A6")
        static let accentLight = Color(hex: "0071E3")
        static let accentDark = Color(hex: "2997FF")
    }

    enum Spacing {
        static let xs: CGFloat = 4
        static let sm: CGFloat = 8
        static let md: CGFloat = 16
        static let lg: CGFloat = 24
        static let xl: CGFloat = 32
        static let xxl: CGFloat = 48
        static let xxxl: CGFloat = 64
    }

    enum Radius {
        static let sm: CGFloat = 8
        static let md: CGFloat = 12
        static let lg: CGFloat = 18
        static let xl: CGFloat = 24
    }
}
```

---

## Color Utilities

```swift
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
            traits.userInterfaceStyle == .dark
                ? UIColor(Color(hex: dark))
                : UIColor(Color(hex: light))
        })
    }
}
```

---

## View Modifiers

### Card Modifier

```swift
struct AppleCardModifier: ViewModifier {
    @Environment(\.colorScheme) var colorScheme

    func body(content: Content) -> some View {
        content
            .padding(AppleDesign.Spacing.lg)
            .background(AppleDesign.Colors.elevated)
            .clipShape(RoundedRectangle(cornerRadius: AppleDesign.Radius.lg))
            .overlay(
                RoundedRectangle(cornerRadius: AppleDesign.Radius.lg)
                    .stroke(
                        colorScheme == .dark
                            ? Color.white.opacity(0.08)
                            : Color.black.opacity(0.06),
                        lineWidth: 1
                    )
            )
            .shadow(
                color: colorScheme == .dark
                    ? .black.opacity(0.3)
                    : .black.opacity(0.08),
                radius: 3, y: 1
            )
    }
}

extension View {
    func appleCard() -> some View {
        modifier(AppleCardModifier())
    }
}
```

### Section Modifier

```swift
struct AppleSectionModifier: ViewModifier {
    func body(content: Content) -> some View {
        content
            .padding(.horizontal, AppleDesign.Spacing.lg)
            .padding(.vertical, AppleDesign.Spacing.xxl)
            .frame(maxWidth: .infinity)
    }
}

extension View {
    func appleSection() -> some View {
        modifier(AppleSectionModifier())
    }
}
```

---

## Button Styles

### Primary Pill

```swift
struct ApplePrimaryButtonStyle: ButtonStyle {
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
```

### Secondary Text

```swift
struct AppleSecondaryButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        HStack(spacing: 4) {
            configuration.label
            Image(systemName: "chevron.right")
                .font(.body.weight(.semibold))
                .imageScale(.small)
        }
        .foregroundStyle(Color.accentColor)
        .opacity(configuration.isPressed ? 0.6 : 1.0)
        .animation(.easeOut(duration: 0.15), value: configuration.isPressed)
    }
}
```

### Outline

```swift
struct AppleOutlineButtonStyle: ButtonStyle {
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

### Compact

```swift
struct AppleCompactButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .font(.caption.weight(.medium))
            .padding(.horizontal, 18)
            .padding(.vertical, 8)
            .background(Color.accentColor)
            .foregroundStyle(.white)
            .clipShape(Capsule())
            .scaleEffect(configuration.isPressed ? 0.95 : 1.0)
            .animation(.easeOut(duration: 0.15), value: configuration.isPressed)
    }
}
```

---

## Card Components

### Standard Card with Overlay Border

```swift
struct AppleCard<Content: View>: View {
    @Environment(\.colorScheme) var colorScheme
    let content: () -> Content

    init(@ViewBuilder content: @escaping () -> Content) {
        self.content = content
    }

    var body: some View {
        content()
            .padding(AppleDesign.Spacing.lg)
            .background(AppleDesign.Colors.elevated)
            .clipShape(RoundedRectangle(cornerRadius: AppleDesign.Radius.lg))
            .overlay(
                RoundedRectangle(cornerRadius: AppleDesign.Radius.lg)
                    .stroke(cardBorderColor, lineWidth: 1)
            )
            .shadow(color: shadowColor, radius: 3, y: 1)
    }

    private var cardBorderColor: Color {
        colorScheme == .dark
            ? Color.white.opacity(0.08)
            : Color.black.opacity(0.06)
    }

    private var shadowColor: Color {
        colorScheme == .dark
            ? .black.opacity(0.3)
            : .black.opacity(0.08)
    }
}
```

### Product Card

```swift
struct ProductCard: View {
    @Environment(\.colorScheme) var colorScheme
    let imageName: String
    let title: String
    let price: String

    var body: some View {
        VStack(alignment: .leading, spacing: 0) {
            Image(imageName)
                .resizable()
                .aspectRatio(4/3, contentMode: .fill)
                .clipped()

            VStack(alignment: .leading, spacing: 4) {
                Text(title)
                    .font(.title3.weight(.semibold))
                Text(price)
                    .font(.body)
                    .foregroundStyle(AppleDesign.Colors.textSecondary)
            }
            .padding(AppleDesign.Spacing.lg)
        }
        .background(AppleDesign.Colors.elevated)
        .clipShape(RoundedRectangle(cornerRadius: AppleDesign.Radius.lg))
        .overlay(
            RoundedRectangle(cornerRadius: AppleDesign.Radius.lg)
                .stroke(
                    colorScheme == .dark
                        ? Color.white.opacity(0.08)
                        : Color.black.opacity(0.06),
                    lineWidth: 1
                )
        )
        .shadow(
            color: colorScheme == .dark ? .black.opacity(0.3) : .black.opacity(0.08),
            radius: 3, y: 1
        )
    }
}
```

---

## Settings List Patterns

### SettingsIcon

```swift
struct SettingsIcon: View {
    let systemName: String
    let backgroundColor: Color
    var foregroundColor: Color = .white

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
```

### Inset Grouped Settings List

```swift
struct SettingsView: View {
    var body: some View {
        NavigationStack {
            List {
                Section {
                    NavigationLink {
                        Text("Profile")
                    } label: {
                        Label {
                            VStack(alignment: .leading, spacing: 2) {
                                Text("John Appleseed")
                                    .font(.headline)
                                Text("Apple ID, iCloud+, Media & Purchases")
                                    .font(.caption)
                                    .foregroundStyle(.secondary)
                            }
                        } icon: {
                            Image(systemName: "person.circle.fill")
                                .font(.system(size: 44))
                                .foregroundStyle(.gray)
                        }
                    }
                }

                Section {
                    NavigationLink { Text("Wi-Fi") } label: {
                        Label { Text("Wi-Fi") } icon: {
                            SettingsIcon("wifi", bg: .blue)
                        }
                    }
                    NavigationLink { Text("Bluetooth") } label: {
                        Label { Text("Bluetooth") } icon: {
                            SettingsIcon("antenna.radiowaves.left.and.right", bg: .blue)
                        }
                    }
                    NavigationLink { Text("Cellular") } label: {
                        Label { Text("Cellular") } icon: {
                            SettingsIcon("antenna.radiowaves.left.and.right.circle", bg: .green)
                        }
                    }
                }

                Section {
                    NavigationLink { Text("Notifications") } label: {
                        Label { Text("Notifications") } icon: {
                            SettingsIcon("bell.badge", bg: .red)
                        }
                    }
                    NavigationLink { Text("General") } label: {
                        Label { Text("General") } icon: {
                            SettingsIcon("gear", bg: .gray)
                        }
                    }
                }
            }
            .listStyle(.insetGrouped)
            .navigationTitle("Settings")
        }
    }
}
```

---

## Navigation

```swift
struct AppNavigation: View {
    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: AppleDesign.Spacing.xl) {
                    // Content
                }
                .padding(.horizontal, AppleDesign.Spacing.lg)
            }
            .navigationTitle("Home")
            .navigationBarTitleDisplayMode(.large)
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button(action: {}) {
                        Image(systemName: "person.circle")
                            .imageScale(.large)
                    }
                }
            }
        }
    }
}
```

### Tab-Based Navigation

```swift
struct MainTabView: View {
    var body: some View {
        TabView {
            HomeView()
                .tabItem {
                    Label("Home", systemImage: "house")
                }

            ExploreView()
                .tabItem {
                    Label("Explore", systemImage: "safari")
                }

            SearchView()
                .tabItem {
                    Label("Search", systemImage: "magnifyingglass")
                }

            ProfileView()
                .tabItem {
                    Label("Profile", systemImage: "person")
                }
        }
    }
}
```

---

## Hero Section

```swift
struct HeroSection: View {
    var body: some View {
        VStack(spacing: AppleDesign.Spacing.md) {
            Text("iPhone")
                .font(.system(size: 56, weight: .bold))
                .tracking(-0.5)

            Text("Designed to be loved.")
                .font(.title)
                .foregroundStyle(AppleDesign.Colors.textSecondary)

            HStack(spacing: AppleDesign.Spacing.md) {
                Button("Learn more") {}
                    .buttonStyle(ApplePrimaryButtonStyle())

                Button("Buy") {}
                    .buttonStyle(AppleOutlineButtonStyle())
            }
            .padding(.top, AppleDesign.Spacing.sm)

            Image("hero-product")
                .resizable()
                .aspectRatio(contentMode: .fit)
                .padding(.top, AppleDesign.Spacing.xl)
        }
        .padding(.vertical, AppleDesign.Spacing.xxxl)
        .padding(.horizontal, AppleDesign.Spacing.lg)
        .frame(maxWidth: .infinity)
    }
}
```

---

## Glass and Material Effects

### Frosted Glass Background

```swift
struct GlassBackground: ViewModifier {
    func body(content: Content) -> some View {
        content
            .background(.ultraThinMaterial)
            .clipShape(RoundedRectangle(cornerRadius: AppleDesign.Radius.lg))
    }
}

extension View {
    func glassBackground() -> some View {
        modifier(GlassBackground())
    }
}

// Usage
Text("Overlay content")
    .padding()
    .glassBackground()
```

### Material Navigation Bar

```swift
struct MaterialNavBar<Content: View>: View {
    let title: String
    let content: () -> Content

    var body: some View {
        VStack(spacing: 0) {
            HStack {
                Text(title)
                    .font(.headline)
                Spacer()
            }
            .padding(.horizontal, AppleDesign.Spacing.lg)
            .padding(.vertical, AppleDesign.Spacing.sm)
            .background(.bar)

            content()
        }
    }
}
```

### Blur Card Overlay

```swift
struct BlurCard: View {
    @Environment(\.colorScheme) var colorScheme

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text("Featured")
                .font(.headline)
            Text("Discover new possibilities")
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
        .padding(AppleDesign.Spacing.lg)
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(.ultraThinMaterial)
        .clipShape(RoundedRectangle(cornerRadius: AppleDesign.Radius.lg))
        .overlay(
            RoundedRectangle(cornerRadius: AppleDesign.Radius.lg)
                .stroke(
                    colorScheme == .dark
                        ? Color.white.opacity(0.08)
                        : Color.black.opacity(0.06),
                    lineWidth: 1
                )
        )
    }
}
```

---

## Animation Presets

```swift
extension Animation {
    /// Default Apple-style ease: cubic-bezier(0.25, 0.1, 0.25, 1)
    static let appleEase = Animation.timingCurve(0.25, 0.1, 0.25, 1, duration: 0.3)

    /// Micro interaction (button press, toggle)
    static let appleMicro = Animation.timingCurve(0.25, 0.1, 0.25, 1, duration: 0.15)

    /// Emphasis (modal present, hero reveal)
    static let appleEmphasis = Animation.timingCurve(0.25, 0.1, 0.25, 1, duration: 0.5)

    /// Spring for bouncy interactions
    static let appleSpring = Animation.spring(response: 0.35, dampingFraction: 0.7)

    /// Page-level transition
    static let applePage = Animation.timingCurve(0.25, 0.1, 0.25, 1, duration: 0.8)
}

// Usage examples
struct AnimatedContent: View {
    @State private var isVisible = false

    var body: some View {
        VStack {
            Text("Hello")
                .opacity(isVisible ? 1 : 0)
                .offset(y: isVisible ? 0 : 20)
                .animation(.appleEase, value: isVisible)
        }
        .onAppear {
            isVisible = true
        }
    }
}

struct PressableCard: View {
    @State private var isPressed = false

    var body: some View {
        AppleCard {
            Text("Tap me")
                .font(.headline)
        }
        .scaleEffect(isPressed ? 0.97 : 1.0)
        .animation(.appleSpring, value: isPressed)
        .onTapGesture {}
        .onLongPressGesture(minimumDuration: .infinity, pressing: { pressing in
            isPressed = pressing
        }) {}
    }
}
```
