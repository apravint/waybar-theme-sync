"""
waybar-theme-sync package.
Dynamic Palette Synchronization Engine for Waybar & Wofi.
"""

from .sync import (
    DEFAULT_COLORS,
    hex_to_rgba,
    parse_toml_colors,
    generate_waybar_css,
    run_sync,
    main,
)

__version__ = "1.0.0"

__all__ = [
    "DEFAULT_COLORS",
    "hex_to_rgba",
    "parse_toml_colors",
    "generate_waybar_css",
    "run_sync",
    "main",
]
