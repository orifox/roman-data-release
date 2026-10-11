---
orphan: false
---

# Placeholder: Example Data-Release Documentation

```{admonition} Placeholder page
:class: warning
This page is a **placeholder**. It shows the structure and level of detail
we expect a data-release document to have, using a published paper as the
model. It contains no Roman content yet, and nothing here describes Roman
data or processing. Replace each section as real documentation is written.
```

## Model document

This placeholder follows the structure of a published data-release paper
from a comparable survey mission:

- **Title:** Euclid Quick Data Release (Q1) - II. VIS processing and data products
- **Authors:** Euclid Collaboration (H. J. McCracken et al.)
- **Reference:** Astronomy & Astrophysics, 711, A2 (2026)
- **DOI:** [10.1051/0004-6361/202554594](https://doi.org/10.1051/0004-6361/202554594)
- **ADS bibcode:** 2026A&A...711A...2E
- **Full text:** <https://www.aanda.org/articles/aa/full_html/2026/07/aa54594-25/aa54594-25.html>
- **License:** open access under CC BY 4.0, so reuse is allowed with attribution.

The summaries below are written in our own words from the paper's abstract
and section text. They are orientation notes, not excerpts. Please consult the
paper itself for the actual methods and results.

## How this paper is organized, and what our version needs

Each section lists what the model paper covers, followed by a **Roman
equivalent** prompt for the team to fill in.

### 1. Introduction

The paper opens with the mission and survey context, why the instrument's
requirements drive careful processing, and what the document covers.

**Roman equivalent:** TBD. Survey purpose, which data release this is, and
what this document does and does not cover.

### 2. The instrument

A description of the camera and detectors: the focal-plane layout, readout
structure, and the file format used for delivered images.

**Roman equivalent:** TBD. Detectors, readout, and delivered file structure.
Cite published instrument papers rather than repeating them.

### 3. Pixel-level corrections

The pipeline's first stage, applied to each detector quadrant. The paper
covers these steps, in roughly the order they are applied:

- the overall pipeline design and the reference observing sequence;
- assembly of raw data into image files (Level 1);
- bad-pixel and artefact flagging;
- crosstalk between readout channels;
- bias and dark corrections;
- detector nonlinearity;
- cosmic-ray flagging;
- charge-transfer inefficiency (monitored but not corrected in this release);
- the brighter-fatter effect;
- pixel response non-uniformity (flat-fielding);
- sky-background estimation.

**Roman equivalent:** TBD. One subsection per correction: the algorithm, the
calibration data it uses, the measured accuracy, and what the release applies.

### 4. Astrometric and photometric calibration

The second stage, where quadrants are processed together. The paper describes
gain equalisation, a simplified point-spread-function model for monitoring,
a large-scale illumination correction, astrometric calibration against Gaia,
and photometric calibration, including how throughput changes over time were
handled.

**Roman equivalent:** TBD. Reference catalogues used, zero-point strategy,
and the version of any calibration reference files, pinned to a tagged
calibration release (for example, `bp-27a`).

### 5. Stacking and catalogue extraction

*Based on the section title and abstract only.* The final stage combines
calibrated exposures into stacked images, and extracts catalogues.

**Roman equivalent:** TBD.

### 6. Automated quality control

*Based on the section title and abstract only.* Quality-control metrics are
delivered with each image.

**Roman equivalent:** TBD. Which metrics ship with each product, and how
users should interpret them.

### 7. Validation for this release

*Based on the section title and abstract only.* This is the release-specific
validation: image quality, astrometric accuracy, photometric scatter, and
depth, measured on the release data. In our plan, this is one of the sections
that is expected to change from one data release to the next.

**Roman equivalent:** TBD. Repeatability, external comparisons, sensitivity,
completeness, and uniformity for this release.

### 8. Known caveats

*Based on the section title only.* Limitations users should know about.

**Roman equivalent:** TBD. Anomalies, off-nominal observations, and known
issues for this release.

### 9. Conclusions

*Based on the section title and abstract only.* A summary of performance
against specifications and the outlook for later releases.

**Roman equivalent:** TBD.

### Appendices: data products

The paper includes appendices that define quantities used in the text and
describe each delivered data product in detail.

**Roman equivalent:** TBD. Product descriptions, file formats, flag
definitions, and a table of metrics.

## Notes for the team

- **Static references only.** Where the model paper points to other papers,
  we would cite versioned or archived references. Links to living pages (such
  as RDocs) should be replaced by snapshots in archival text.
- **Cross-document links** to calibration and pipeline documentation should be
  pinned to a tagged version, not `latest`.
- **Release-specific sections** (observations included, sensitivity,
  anomalies, validation) are the ones that will change between releases.
- This page can be deleted once real documentation replaces it.
