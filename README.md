# waybar-theme-sync 🎨

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Waybar](https://img.shields.io/badge/Supports-Waybar%20%7C%20Wofi-teal.svg)](https://github.com/Alexays/Waybar)

> **Dynamic Palette Synchronization Engine for Waybar & Wofi.**  
> Automatically transforms TOML color palettes (Omarchy, Alacritty, or custom) into dynamic CSS variables and live-reloads Waybar without restarts.

---

## ⚡ Features

- **Dynamic Theme Conversion**: Converts TOML color definitions into `@define-color` CSS variables.
- **Instant Hot-Reload**: Automatically signals Waybar via `SIGUSR2` so styles re-render in real-time.
- **Continuous Watcher Mode**: Run with `--watch` to listen for palette changes and re-render instantly.
- **Zero Heavy Dependencies**: Pure Python standard library implementation &mdash; runs out of the box on any Linux system.

---

## 🚀 Installation

### Option 1: Direct Script Install

```bash
git clone https://github.com/apravint/waybar-theme-sync.git
cd waybar-theme-sync
./install.sh
```

### Option 2: Pip Install

```bash
pip install .
```

---

## 📖 Usage

### 1. Basic Conversion & Live Reload
```bash
waybar-theme-sync --input ~/my-palette.toml --output ~/.config/waybar/colors.css --reload
```

### 2. Auto-Watch Mode (Daemon)
Listen for wallpaper/theme changes and keep Waybar in sync continuously:
```bash
waybar-theme-sync --input ~/.local/state/omarchy/current/theme/colors.toml --watch --reload
```

---

## 🎨 Waybar Integration

In your `~/.config/waybar/style.css`, simply import the generated `colors.css`:

```css
@import "colors.css";

window#waybar {
    background: @bg;
    color: @fg;
    border: 1px solid @border;
}

#workspaces button.active {
    color: @accent;
}
```

---

## 📄 License

Licensed under the [MIT License](LICENSE).
