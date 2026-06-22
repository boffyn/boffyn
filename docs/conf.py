import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.abspath("../"))

project = "boffyn"
copyright = "2026, Richard Terry"
author = "Richard Terry"


def find_version(*paths):
    path = Path(*paths)
    content = path.read_text()
    match = re.search(r"^__version__\s*=\s*['\"]([^'\"]*)['\"]", content, re.M)
    if match:
        return match.group(1)
    raise RuntimeError("Unable to find version string.")


release = find_version("..", "boffyn", "__init__.py")

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_static_path = ["_static"]
html_title = ""
html_theme_options = {
    "light_css_variables": {
        "font-stack": "Barlow, sans-serif;",
        "font-stack--monospace": "Fira Mono, monospace",
        "font-stack--headings": "Barlow, sans-serif;",
    },
}
