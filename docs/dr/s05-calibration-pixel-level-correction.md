# 5. Calibration/Pixel-Level Correction

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

Introduction		This section describes the state of calibration at the time of the data release; this section can be identical between releases sharing the same identifier -- e.g. 27a

## 5.1 Summary of WFI Calibration Status for this data release

**Source:** RTB. Describe basic calibration summarize current estimated uncertainties; for each data release this can be mostly a snapshot of RDOCs, but there is probably work to make it coherent as a static long-term record of the state of calibration that can be understood even if the rest of RDOCs is evolving.

## 5.2 Darks, Data Quality Flags, instabilities not flagged

**Source:** RDOCs. Characterized as part of calibration plan; draw from RDOCs, highlighting any specifics for this data release.

## 5.4 Gain and gain stability

**Source:** RDOCs. ditto

## 5.3 1/f bias correction

**Source:** RDOCs. ditto

## 5.4 Flat field

**Source:** RDOCs. ditto

## 5.5 Nonlinearities

**Source:** RDOCs. ditto

## 5.6 Photometry

**Source:** RDOCs. Focus on L2; refer to later section for L3?

## 5.6.1 Zeropoints and Zeropoint stability

**Source:** RDOCs. ditto

## 5.6.2 Ice: models, corrections, remaining SED-dependent uncertainties

**Source:** RTB. Highlight decontaminations that happened over the course of observations included in this data release; plot time-series of ice deposition…

## 5.7 Instrument geometric distortions and stability

**Source:** RDOCs. ditto

## 5.8 PSF characterization and stability

**Source:** RDOCs. This section would be for L2 PSFs, pointing to a later section for the co-add PSFs.

## 5.9 Astrometry

**Source:** RDOCs. ditto

## 5.9.1 Absolute Astrometry

**Source:** RDOCs. This section focuses on L2; need to highlight differences for L3

## 5.9.2 Relative Astrometry

**Source:** RDOCs. This section focuses on L2; need to highlight differences for L4

## 5.10 Brighter-fatter effect

**Source:** RDOCs.

## 5.11 Intrapixel Capacitance

**Source:** RDOCs.

## 5.12 Persistence

**Source:** RDOCs.

## 5.13. Astrometric and photometric calibration

The second stage, where quadrants are processed together. The paper describes
gain equalisation, a simplified point-spread-function model for monitoring,
a large-scale illumination correction, astrometric calibration against Gaia,
and photometric calibration, including how throughput changes over time were
handled.

**Roman equivalent:** TBD. Reference catalogues used, zero-point strategy,
and the version of any calibration reference files, pinned to a tagged
calibration release (for example, `bp-27a`).
