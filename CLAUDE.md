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
- `docs/index.md`: the site home page. Its hidden root `toctree` has exactly two
  entries, "Data Release Document" (`dr/index`) and "Contributor Guide"
  (`release-checklist`), which is all the sidebar shows at the top level. New
  pages go under one of those two, or are marked `orphan: true`. The master
  table of all releases is generated from `docs/_data/releases.csv` (one row
  per release).
- `docs/release-checklist.md`: contributor setup, editing workflow, and the
  release procedure (tag, GitHub Release, then checks on Read the Docs and Zenodo).
- `docs/dr/`: the data release document, one page per numbered section
  (`sNN-<slug>.md`, H1 = "N. Title", subsections as H2). `dr/index.md` is the
  landing page whose `toctree` lists the sections in order; add new section
  pages there. Subsections from the planning spreadsheet carry a
  `**Source:**` line (RDOCs, RTB, DMS) followed by notes on what to write.
  Section 5 is split further: `s05-calibration-pixel-level-correction.md`
  holds the section intro and a `toctree` of one page per subsection in
  `docs/dr/s05/` (file names prefixed with the subsection number, e.g.
  `05-persistence-masking.md`, `12.1-zeropoints-...md`, so the folder sorts
  in page order; "5.N Title" H1). Order comes from that `toctree`;
  reordering means moving a line, then fixing the title number and the
  file-name prefix (use `git mv`).
  Equations copied from Euclid papers use `\tag{N}` with the paper's number,
  because Sphinx restarts equation numbering on every page.
  `zz-euclid-model-notes.md` holds leftovers from the original Euclid-based
  placeholder and can be deleted when no longer needed.
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
