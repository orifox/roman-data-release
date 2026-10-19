# Roman Data Release: TBD

```{admonition} Draft layout
:class: warning
Values marked **TBD** are placeholders to fill in for each release.
```

**Release label:** TBD (calibration breakpoint, for example `27a`) ·
**Release date:** TBD · **DOI:** TBD

This data release contains TBD deg² of Roman Wide Field Instrument
observations from TBD, taken between TBD and TBD. It includes TBD exposures
and about TBD catalog sources, processed with Romancal TBD and calibration
context TBD. Releases are cumulative: this one includes the observations from
earlier releases as well as new ones. Changes since the previous release are
summarized in [Section 3](s03-survey-design-and-strategy.md).

This page summarizes the release. The full data release document follows
below, one page per section.

## Basic data release information

### Fields

```{admonition} Figure TBD
:class: note
Footprint map of the fields included in this release, by survey and tier.
```

| Survey | Component or tier | Field | Area in this release (deg²) | Filters | Epochs | Dates observed |
| --- | --- | --- | --- | --- | --- | --- |
| HLWAS | TBD | TBD | TBD | TBD | TBD | TBD |
| HLTDS | TBD | TBD | TBD | TBD | TBD | TBD |
| GBTDS | TBD | TBD | TBD | TBD | TBD | TBD |
| GPS | TBD | TBD | TBD | TBD | TBD | TBD |

Coverage gaps, such as missing tiles or filters, are listed in
[Section 4](s04-observations.md).

### Data products released

Products are described in full in [Section 16](s16-data-products.md).

| Level | Product | Included in this release |
| --- | --- | --- |
| L1 | Uncalibrated exposures | TBD |
| L2 | Calibrated exposure-level images | TBD |
| L2 | Exposure-level ancillary products (currently WCS) | TBD |
| L3 | Co-added images and mosaics | TBD |
| L4 | Static source catalogs | TBD |
| L4 | Static catalog ancillary products (segmentation maps, source-injection catalogs) | TBD |
| L4 | Time-series catalogs | TBD |
| — | Survey-level products | TBD |

### Calibration and pipeline versions

| Item | Version |
| --- | --- |
| Romancal pipeline | TBD |
| Calibration reference files (CRDS context, `pmap`) | TBD |
| Science data format | TBD |

Changes since the previous release are summarized in
[Section 15](s15-calibration-and-pipeline-versions.md).

### Data access

Data are served through TBD (images) and TBD (catalogs). Access methods are
expected to change over the life of the mission, so current instructions are
kept in the living Roman documentation; [Section 14](s14-archive-and-data-access.md)
records how access worked at the time of this release.

### How to cite

Cite this release with its DOI (TBD). Citation metadata is in the repository's
`CITATION.cff` file.

## Publications

### Data release overview, data products, and processing

- TBD

### Science results using this release

- TBD

## Data release document

```{toctree}
:maxdepth: 1

s01-introduction
s02-the-instrument
s03-survey-design-and-strategy
s04-observations
s05-calibration-pixel-level-correction
s06-exposure-level-processing
s07-image-rectification-and-co-addition
s08-static-catalog-processing
s09-stacking-and-catalogue-extraction
s10-static-catalog-validation
s11-photometrid-redshift-tuning-and-validation
s12-time-series-catalog-processing
s13-time-series-catalog-validation
s14-archive-and-data-access
s15-calibration-and-pipeline-versions
s16-data-products
zz-euclid-model-notes
```
