# render_stats.py — called by GitHub Actions to refresh github_OtakuCoder2314.svg
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import config.theme_manager as tm
tm.set_theme("cyber_terminal")

from screens import github_screen
from export  import svg_exporter

os.makedirs("outputs", exist_ok=True)
svg = github_screen.render(username="OtakuCoder2314")
svg_exporter.export(svg, "outputs/github_OtakuCoder2314.svg")
print("Refreshed: outputs/github_OtakuCoder2314.svg")
