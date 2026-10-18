# 4. Observations

This section describes the observations included in this data release. It is
one of the release-specific parts of this document: it is rewritten for each
release, while the survey design in [Section 3](s03-survey-design-and-strategy.md)
describes what the surveys are planned to obtain over the whole mission.
[Section 4.1](#observations-summary) summarizes the observations by survey and
by filter: the components and tiers observed, the number of exposures and
epochs, the sky area covered, and the dates. [Section 4.2](#coverage-gaps)
lists where the data fall short of the survey design, such as missing tiles,
filters, or epochs. Together, they define the input to the processing
described in Sections 5 to 13. Because releases are cumulative, the tables
include observations from earlier releases, not only those new to this one.

(observations-summary)=
## 4.1 Observations summary

**Source:** RTB. Summary tables of the observations -- fields, filters & timing

This section summarizes the Wide Field Instrument (WFI) observations included
in this data release. All observations come from Roman's four
community-defined surveys. Each survey is executed as a single observing
program, organized into components or tiers that differ in area, depth,
filters, and cadence. The survey designs are described in
[Section 3](s03-survey-design-and-strategy.md) and, in full, in the
[Roman community-defined surveys documentation](https://roman-docs.stsci.edu/roman-community-defined-surveys).
The tables below report only what was observed and included in this release.
The full planned specifications are not repeated here.

Throughout this section, an **exposure** is one WFI MultiAccum readout,
covering all 18 detectors. The **area** of a tier or component is the sky area
covered by at least one exposure that passed quality checks and was included
in this release. **Dates** are the first and last observation included.

```{admonition} Figure TBD
:class: note
Timeline of the observations in this release: one row per survey and
component, marking the dates of the included visits.
```

| Survey | Program | Survey design | Components or tiers in this release | Exposures | Area (deg²) | Dates observed |
| --- | --- | --- | --- | --- | --- | --- |
| High-Latitude Wide-Area Survey (HLWAS) | 1400 | [HLWAS](https://roman-docs.stsci.edu/roman-community-defined-surveys/high-latitude-wide-area-survey) | TBD | TBD | TBD | TBD |
| High-Latitude Time-Domain Survey (HLTDS) | 1410 | [HLTDS](https://roman-docs.stsci.edu/roman-community-defined-surveys/high-latitude-time-domain-survey) | TBD | TBD | TBD | TBD |
| Galactic Bulge Time-Domain Survey (GBTDS) | 1420 | [GBTDS](https://roman-docs.stsci.edu/roman-community-defined-surveys/galactic-bulge-time-domain-survey) | TBD | TBD | TBD | TBD |
| Galactic Plane Survey (GPS) | 1430 | [GPS](https://roman-docs.stsci.edu/roman-community-defined-surveys/galactic-plane-survey) | TBD | TBD | TBD | TBD |
| **Total** | | | | TBD | TBD | TBD |

### 4.1.1 High-Latitude Wide-Area Survey

The HLWAS is organized into four tiers (Wide, Medium, Deep, and Ultra-Deep)
that trade area for depth. The Wide tier is imaged in a single filter, the
Medium and Deep tiers add grism spectroscopy, and the Ultra-Deep tier lies
within the Deep fields. The survey has no fixed cadence, so the table reports
coverage rather than epochs: the number of passes reached, compared with the
number planned for the tier.
See the [HLWAS design](https://roman-docs.stsci.edu/roman-community-defined-surveys/high-latitude-wide-area-survey)
for tier footprints, exposure times, and depths.

| Tier | Planned imaging filters | Spectroscopy | Exposures | Area (deg²) | Passes completed / planned | Dates observed |
| --- | --- | --- | --- | --- | --- | --- |
| Wide | F158 | — | TBD | TBD | TBD | TBD |
| Medium | F106, F129, F158 | Grism | TBD | TBD | TBD | TBD |
| Deep | F087, F106, F129, F146, F158, F184, F213 | Grism | TBD | TBD | TBD | TBD |
| Ultra-Deep | F106, F129, F158 | — | TBD | TBD | TBD | TBD |

### 4.1.2 High-Latitude Time-Domain Survey

The HLTDS repeatedly images a northern field (ELAIS-N1) and a southern field
(Euclid Deep Field South), each with a Wide and a Deep imaging tier. Prism
spectroscopy is obtained in the southern field only. The survey has a Pilot,
a Core, and an Extended component; the Core component revisits the fields at
an approximately five-day cadence. Because the survey is cumulative, the
table reports epochs, which set both the time sampling and the depth of
co-added images.
See the [HLTDS design](https://roman-docs.stsci.edu/roman-community-defined-surveys/high-latitude-time-domain-survey)
for field centers, cadence requirements, and exposure times.

| Field | Tier | Component | Planned filters or element | Epochs | Exposures | Area (deg²) | Dates observed |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ELAIS-N1 | Wide imaging | TBD | F062, F087, F106, F129, F158 | TBD | TBD | TBD | TBD |
| ELAIS-N1 | Deep imaging | TBD | F087, F106, F129, F158, F184 | TBD | TBD | TBD | TBD |
| EDFS | Wide imaging | TBD | F062, F087, F106, F129, F158 | TBD | TBD | TBD | TBD |
| EDFS | Deep imaging | TBD | F087, F106, F129, F158, F184 | TBD | TBD | TBD | TBD |
| EDFS | Wide spectroscopy | TBD | Prism | TBD | TBD | TBD | TBD |
| EDFS | Deep spectroscopy | TBD | Prism | TBD | TBD | TBD | TBD |

### 4.1.3 Galactic Bulge Time-Domain Survey

The GBTDS monitors six WFI fields toward the Galactic bulge, five contiguous
fields and one at the Galactic Center, over ten observing seasons. In
high-cadence seasons the fields are imaged in F146 every few minutes, with
less frequent F087 and F213 visits for color. Low-cadence seasons sample the
same fields every few days. Each season also includes multiband photometric
snapshots and grism snapshots. The table is organized by season, which is the
natural unit for time-series processing.
See the [GBTDS design](https://roman-docs.stsci.edu/roman-community-defined-surveys/galactic-bulge-time-domain-survey)
for field positions, cadence, and the snapshot sequence.

| Season | Cadence | Dates observed | F146 epochs | F087 / F213 epochs | Photometric snapshots | Grism snapshots | Exposures |
| --- | --- | --- | --- | --- | --- | --- | --- |
| TBD | High / Low | TBD | TBD | TBD | TBD | TBD | TBD |

Within each season, all six fields are observed in sequence, so the numbers of
epochs are per field. Fields with fewer epochs than the others are listed in
[Section 4.2](#coverage-gaps).

### 4.1.4 Galactic Plane Survey

The GPS has three components: a wide-field imaging survey of the inner
Galactic plane, a time-domain program on six selected fields, and deep
imaging and spectroscopy in a set of individual pointings. The wide-field
component uses four filters over most of its area, with an extra filter in
one sub-region. Time-domain cadences differ from field to field.
See the [GPS design](https://roman-docs.stsci.edu/roman-community-defined-surveys/galactic-plane-survey)
for the footprint, sub-regions, field list, and cadences.

| Component | Planned filters or elements | Fields or pointings | Exposures | Area (deg²) | Epochs | Dates observed |
| --- | --- | --- | --- | --- | --- | --- |
| Wide-field | F129, F158, F184, F213 (F106 in Serpens South) | TBD | TBD | TBD | — | TBD |
| Time-domain | Varies by field | TBD | TBD | TBD | TBD | TBD |
| Deep-field and spectroscopic | Broad-band filters except F146; grism and prism | TBD | TBD | TBD | — | TBD |

### 4.1.5 Exposures by filter

This table combines the four surveys to show the total amount of data in each
WFI optical element. It is the starting point for the per-filter calibration
and validation statistics in later sections.

| Element | HLWAS | HLTDS | GBTDS | GPS | Total exposures | Total exposure time (h) |
| --- | --- | --- | --- | --- | --- | --- |
| F062 | — | TBD | TBD | TBD | TBD | TBD |
| F087 | TBD | TBD | TBD | TBD | TBD | TBD |
| F106 | TBD | TBD | TBD | TBD | TBD | TBD |
| F129 | TBD | TBD | TBD | TBD | TBD | TBD |
| F146 | TBD | — | TBD | — | TBD | TBD |
| F158 | TBD | TBD | TBD | TBD | TBD | TBD |
| F184 | TBD | TBD | TBD | TBD | TBD | TBD |
| F213 | TBD | — | TBD | TBD | TBD | TBD |
| Grism | TBD | — | TBD | TBD | TBD | TBD |
| Prism | — | TBD | — | TBD | TBD | TBD |

A dash (—) marks an element that the survey design does not use.

(coverage-gaps)=
## 4.2 Coverage gaps

**Source:** RTB. Summary of any occasional missing tiles or filters, etc.; Perhaps include a plot of area covered in each filter as a function of exposure time, as a summary of the affects of gaps?

