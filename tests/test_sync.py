import unittest
import tempfile
import os
from waybar_theme_sync.sync import (
    hex_to_rgba,
    parse_toml_colors,
    generate_waybar_css,
    DEFAULT_COLORS,
    run_sync,
)


class TestWaybarThemeSync(unittest.TestCase):
    def test_hex_to_rgba(self):
        self.assertEqual(hex_to_rgba("#ffffff", 1.0), "rgba(255, 255, 255, 1.0)")
        self.assertEqual(hex_to_rgba("#000000", 0.5), "rgba(0, 0, 0, 0.5)")
        self.assertEqual(hex_to_rgba("#1a1b26", 0.8), "rgba(26, 27, 38, 0.8)")

    def test_parse_toml_colors_missing_file(self):
        colors = parse_toml_colors("/non/existent/path.toml")
        self.assertEqual(colors, DEFAULT_COLORS)

    def test_parse_toml_colors_valid_file(self):
        with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".toml") as tmp:
            tmp.write('background = "#0f172a"\n')
            tmp.write('accent = "#38bdf8"\n')
            tmp_path = tmp.name

        try:
            colors = parse_toml_colors(tmp_path)
            self.assertEqual(colors["background"], "#0f172a")
            self.assertEqual(colors["accent"], "#38bdf8")
            self.assertEqual(colors["foreground"], DEFAULT_COLORS["foreground"])
        finally:
            os.remove(tmp_path)

    def test_generate_waybar_css(self):
        colors = {
            "dark_background": "#0f172a",
            "foreground": "#f8fafc",
            "accent": "#38bdf8",
            "muted": "#64748b",
        }
        css = generate_waybar_css(colors, opacity=0.9)
        self.assertIn("@define-color bg rgba(15, 23, 42, 0.9);", css)
        self.assertIn("@define-color fg #f8fafc;", css)
        self.assertIn("@define-color accent #38bdf8;", css)

    def test_run_sync_execution(self):
        with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".toml") as in_tmp:
            in_tmp.write('accent = "#22c55e"\n')
            in_path = in_tmp.name

        with tempfile.NamedTemporaryFile("w+", delete=False, suffix=".css") as out_tmp:
            out_path = out_tmp.name

        try:
            run_sync(in_path, out_path, opacity=0.75, reload=False)
            with open(out_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("@define-color accent #22c55e;", content)
        finally:
            if os.path.exists(in_path):
                os.remove(in_path)
            if os.path.exists(out_path):
                os.remove(out_path)


if __name__ == "__main__":
    unittest.main()
