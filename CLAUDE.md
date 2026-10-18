# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A prototype documentation site for Roman Space Telescope data releases. It is
Sphinx with MyST Markdown and sphinx_rtd_theme (matching the Roman pipeline
docs), built on Read the Docs, and
archived per release through Zenodo (the Sandbox for now). It has no code and
no tests; the "build" is the Sphinx HTML build.

## Commands

```
python3 -m venv .venv
source .venv/bin/activate.csh        # this machine's shell is tcsh; bash/zsh: .venv/bin/activate
pip install -r docs/requirements.txt
sphinx-build -b html docs docs/_build/html      # or: make -C docs html
sphinx-build -W -b html docs docs/_build/html   # treat warnings as errors (release gate)
```

The release checklist requires a clean build with no warnings.

`docs/_static/` holds the Roman logo (copied from the romancal docs) and
`custom.css`. `docs/_templates/layout.html` overrides the theme's sidebar title
block to add the release label; if `sphinx-rtd-theme` is upgraded, compare it
against the theme's own `sidebartitle` block. `index.md` uses one captioned
`toctree` per sidebar group.

## Structure

- `docs/conf.py`: extensions are `myst_parser` and `sphinx_copybutton`. Both
  `.md` and `.rst` are accepted. `release` (shown under the sidebar logo by `_templates/layout.html`) is
  computed in this order: the Read the Docs tag name on tag builds, then
  `git describe --tags`, then the `CITATION.cff` version. Don't hard-code it.
- `docs/index.md`: the root `toctree`. Every new page must be added here or
  marked `orphan: true` in front matter.
- `docs/release-checklist.md`: contributor setup, editing workflow, and the
  release procedure (tag, GitHub Release, then checks on Read the Docs and Zenodo).
- `docs/placeholder-euclid-vis.md`: a template showing the expected structure
  of a data-release document, modeled on the Euclid Q1 VIS paper. Each
  section has a "Roman equivalent: TBD" prompt to be filled in.
- `CITATION.cff`: Zenodo pulls release metadata from here. The title,
  authors, version, and license must match the release.
- `.readthedocs.yaml`: Ubuntu 24.04, Python 3.12, `docs/requirements.txt`.

## Content rules (from the docs themselves)

- MyST directives use exactly three backticks followed by `{directive-name}`
  with no space between them, for example ```` ```{admonition} ````.
- Archival text must not link to living pages (RDocs, Confluence). Copy the
  content in as static text or tables.
- Links to other documentation projects must point to a **tagged** version,
  never `latest`, `stable`, or `main`.
- Release and calibration tags look like `bp-27a`.
- Summaries of external papers are written in our own words, not excerpts.
- Each release pins the calibration and pipeline versions it used in the
  release manifest.

## Workflow

Contributors work on branches and merge to `main` through pull requests.
Merges to `main` rebuild `latest` on Read the Docs, and tags build versioned
docs. Zenodo archives GitHub *Releases*, not bare tags. A real Zenodo
record is permanent, so never use real Zenodo in the prototype.
