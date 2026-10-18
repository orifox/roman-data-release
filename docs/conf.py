# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Roman Data Releases'
copyright = '2026, Ori Fox'
author = 'Ori Fox'

# Release label shown in the sidebar and page titles. A Read the Docs build of
# a tag uses the tag name. Other builds (such as "latest") use `git describe`,
# which gives "<tag>-<commits since>-g<hash>" once main moves past a release.
# If git has no tags (shallow clones), fall back to the CITATION.cff version.
import os
import re
import subprocess
from pathlib import Path


def _release_label():
    if os.environ.get("READTHEDOCS_VERSION_TYPE") == "tag":
        return os.environ["READTHEDOCS_VERSION_NAME"]
    try:
        return subprocess.run(
            ["git", "describe", "--tags"],
            cwd=Path(__file__).parent,
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        pass
    cff = Path(__file__).parent.parent / "CITATION.cff"
    match = re.search(r'^version:\s*"?([^"\n]+)"?', cff.read_text(), re.M)
    return match.group(1) if match else ""


release = _release_label()
version = release

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["myst_parser", "sphinx_copybutton"]
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# Same theme and sidebar behavior as the Roman pipeline docs
# (roman-pipeline.readthedocs.io).
html_theme = 'sphinx_rtd_theme'
html_theme_options = {"collapse_navigation": True}
html_logo = "_static/roman-logo.png"
html_title = f"{project} {release}".strip()
html_static_path = ['_static']
html_css_files = ['custom.css']
