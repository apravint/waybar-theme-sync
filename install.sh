#!/usr/bin/env bash
# ==============================================================================
# waybar-theme-sync - Quick Installer
# https://github.com/apravint/waybar-theme-sync
# ==============================================================================
set -e

REPO_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

echo "Installing waybar-theme-sync to ~/.local/bin/..."
mkdir -p "$HOME/.local/bin"
cp "$REPO_DIR/waybar_theme_sync/sync.py" "$HOME/.local/bin/waybar-theme-sync"
chmod +x "$HOME/.local/bin/waybar-theme-sync"

echo "✔ Successfully installed waybar-theme-sync!"
echo "Run 'waybar-theme-sync --help' for options."
