# Roman Data Release Documentation

This site is the archival record of the data releases of the Nancy Grace Roman
Space Telescope. A data release is a fixed, versioned set of Roman data
products. This site documents how each release was produced: which
observations it includes, how they were calibrated and processed, how the
results were validated, and which pipeline and calibration versions were used.
Instructions for accessing the data are kept in the living Roman documentation
(RDocs), because access methods change over time.

## One set of pages per data release

Each data release has its own copy of the
[Data Release Document](dr/index.md). When a release is made, this site is
tagged with that release's label, and Read the Docs keeps a permanent copy of
the pages exactly as they were at that time. Use the version menu to switch
between releases:

- **A release label** (for example `bp-27a`) shows the documentation for that
  release. It does not change after the release, and it is archived with a DOI.
- **`latest`** shows the documentation in progress for the next release.

Releases are cumulative: each one includes the observations from earlier
releases as well as new ones.

## All data releases

The table below compares every release. The most complete version of this
table is always on `latest`; the copy in each release's pages lists the
releases made up to that point.

```{csv-table}
:file: _data/releases.csv
:header-rows: 1
:class: dr-table
```

```{toctree}
:hidden:
:maxdepth: 3

Data Release Document <dr/index>
Contributor Guide <release-checklist>
```
