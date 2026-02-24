# InterIA UI — Design System v2.5

This folder provides the **InterIA UI design system** (v2.5):
CSS tokens, base styles, and reusable components for InterIA repositories.

It is meant to be used in:

- GitHub Pages
- small HTML demos
- documentation portals
- local previews (e.g. `python -m http.server`)

---

## 📁 Structure

```text
ui/
 ├── css/
 │    ├── interia.tokens.css      # design tokens (colors, spacing, fonts…)
 │    ├── interia.base.css        # base layout, typography
 │    └── interia.components.css  # reusable components (cards, alerts, gallery, lab layout…)
 └── html/
      ├── layout_base.html        # base page layout demo
      ├── component_cards.html    # cards grid demo
      ├── component_gallery.html  # proof / results gallery demo
      ├── component_mathlab.html  # math-lab layout
      └── component_multiagent.html # multi-agent cluster layout
```

You can copy/paste these files into any InterIA-aligned project and adjust paths as needed.

---

## 🔧 How to use in an HTML page

Minimal example:

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>InterIA UI Demo</title>
  <link rel="stylesheet" href="ui/css/interia.components.css">
</head>
<body>
  <div class="ia-page">
    <h1 class="ia-title">InterIA UI v2.5</h1>
    <p class="ia-subtitle">Reusable components for all InterIA repositories.</p>

    <!-- Insert components here -->
    <!-- For example: -->
    <!-- #include "ui/html/component_cards.html" -->
  </div>
</body>
</html>
```

In practice:

- place `ui/` at the root of your repository (or under `docs/` or `pages/`),
- update the `<link rel="stylesheet" href="...">` path accordingly,
- include the snippets from `ui/html/*.html` where you want to show UI components.

---

## 🧩 Components overview

### 1. Layout & base

Defined in `interia.base.css` and `interia.components.css`:

- `.ia-page` — centered page layout
- `.ia-title`, `.ia-subtitle` — page headings
- `.ia-section`, `.ia-section-title` — section blocks

See `html/layout_base.html` for a full example.

---

### 2. Cards

Defined in `interia.components.css`:

- `.ia-card-grid` — responsive grid for cards
- `.ia-card` — base card component
- `.ia-card-title`, `.ia-card-subtitle`
- `.ia-card-footer`
- `.ia-pill` — small status pill

See `html/component_cards.html`.

---

### 3. Alerts / Callouts

Classes:

- `.ia-alert` + `.ia-alert-info|warning|success`
- `.ia-alert-icon`, `.ia-alert-content`

See `html/layout_base.html` for an example.

---

### 4. Proof / Results Gallery

Grid-style gallery for proofs, results, figures:

- `.ia-gallery-grid`
- `.ia-gallery-item`

See `html/component_gallery.html`.

---

### 5. Math Lab layout

Two-column layout for a math lab overview:

- `.ia-lab-layout` (responsive)
- combines cards, alerts, lists

See `html/component_mathlab.html`.

---

### 6. Multi-agent cluster

For visualizing multi-agent setups:

- `.ia-multiagent-cluster`
- `.ia-agent-chip`
- `.ia-agent-chip-name`, `.ia-agent-chip-role`

See `html/component_multiagent.html`.

---

## 🌗 Dark / Light mode

The current UI is **neutral** and works in both modes with defaults.
If you want to adapt colors dynamically, you can extend `interia.tokens.css` using:

```css
@media (prefers-color-scheme: dark) {
  :root {
    --ia-primary-dark: #0d47a1;
    --ia-primary: #1e88e5;
    --ia-gray-900: #eceff1;
    --ia-gray-100: #1a237e;
    /* etc. */
  }
}
```

---

## 🤝 Contributing

- Keep components **small, composable, and documented**.
- Use tokens from `interia.tokens.css` (no hard-coded colors if possible).
- Prefer semantic HTML and accessible structures.

See the main `CONTRIBUTING.md` in `interia-style` for global rules.
