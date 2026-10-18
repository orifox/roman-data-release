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

````{admonition} Example text from Euclid: VIS processing function
:class: note

*Reproduced from Euclid Collaboration: McCracken et al. (2026), "Euclid Quick Data Release (Q1) – II. VIS processing and data products", A&A, 711, A2, [doi:10.1051/0004-6361/202554594](https://doi.org/10.1051/0004-6361/202554594), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

The VIS PF is divided into two main functional units: a ‘calibration pipeline’ that computes the master calibration products for each of the instrumental effects and a ‘science pipeline’ that applies each of these corrections to the raw VIS data. Here we describe the calibration and correction of each of these instrumental effects in the order they are applied in the science pipeline. Before launch, VIS PF was developed, tested, and validated by processing highly realistic simulated raw VIS data (Euclid Collaboration: Serrano et al. 2024) created using the best available ground-calibration data.

To understand the functionality required from VIS PF, it is worth briefly describing the reference observing sequence (ROS), described in Euclid Collaboration: Scaramella et al. (2022), Euclid Collaboration: Mellier et al. (2025) and executed at every location in the EWS. Each ROS consists of four dithers in an ‘S’-pattern, where VIS and NISP observe simultaneously. At each dither, VIS takes a 566 s ‘nominal science’ exposure. The first two dithers also contain an additional 95 s VIS ‘short science’ exposure, and calibration exposures fill the remaining two dithers1. With this dither pattern, at least 95% of the pixels are covered by at least three or four nominal exposures. While the EWS comprises a single ROS at each pointing, the EDS fields are visited at least 40 times in a manner similar to the EWS at a range of roll angles. The VIS PF must therefore provide calibrations for both the nominal and short-science exposures.

We should note that the term ‘processing element’ (PE) refers to a sub-element of the VIS PF. Normally, the scope of a given processing element is limited. The term ‘processing function’ refers to the ensemble of PEs that makes up the entire pipeline. In our case, VIS PF refers to the sequence of PEs that comprise the VIS processing pipeline2. We note here that the principal client processing functions for VIS PF are the shear processing function which measures shapes on individual VIS images, and the MER PF, described in Euclid Collaboration: Romelli et al. (2026), which combines data from Euclid instruments with external data. MER PF takes as input from VIS PF the calibrated images described here and an associated PSF model.

In operations, the main VIS PF science pipeline (VIS_ProcessField) is run on every raw science VIS exposure. It applies all the instrumental corrections in the order described below. This pipeline must be robust against bad or incomplete data, and it must also flag data so downstream PFs can apply selection functions if needed. Additionally, given the large number of VIS exposures arriving each day (around 156 during nominal wide-survey acquisitions), data must be processed quickly. This is because downstream PFs also have significant computational requirements, and the ground segment must be able to process all data from a given day’s observations before the next day’s data arrive.

The VIS PF is large and contains many processing elements. In the interests of simplicity, we divide the processing function into three sections. In the first part, described in this section and shown schematically in Fig. 2, pixel-level corrections are carried out on the individual quadrants. In general, each quadrant is treated independently. Next, as described in Sect. 4 and shown schematically in Fig. 7, catalogues are extracted from the processed quadrants and are used to compute the astrometric and photometric solutions. This stage provides the calibrated exposures that are used by SHE and MER processing functions. In the final stage, described in Sect. 5 and shown in Fig. 15, we combine the individual calibrated frames from a ROS to make a stacked image.

Although not strictly part of the VIS PF, for completeness we provide here a high-level summary of the software we developed to assemble the raw data from the VIS camera into MEF files, the VIS ‘Level 1’ or LE1 processor. This software runs at the Science Operations Centre (SOC) and unpacks the compressed raw data transmitted from the spacecraft into a MEF file with 144 extensions. The image metadata is processed from either the raw VIS data or other general housekeeping telemetry, and placed into the FITS headers with specific keywords. The primary header of the MEF contains information specific to the whole image, such as the observation date, image acquisition parameters, instrument temperatures, and spacecraft pointing and attitudes. The header of each extension does not contain much information at this stage, apart from a few quadrant-specific parameters and the data compression ratio for the quadrant. It also contains a preliminary astrometric solution based on the commanded pointing values, RA, Dec, PA, and the FPA geometry (pixel size, dimensions, and layout of the detectors).
````

% Each subsection is its own page in docs/dr/s05/. To change the order,
% move its line in the list below and update the number in its title.
```{toctree}
:maxdepth: 1

s05/calibration-status-summary
s05/data-quality-flags
s05/non-linear-correction
s05/persistence-masking
s05/darks-and-dark-current
s05/cosmic-ray-identification
s05/gain-and-gain-stability
s05/1-f-bias-correction
s05/flat-field
s05/photometry
s05/zeropoints-and-zeropoint-stability
s05/ice
s05/instrument-geometric-distortions-and-stability
s05/psf-characterization-and-stability
s05/astrometry
s05/absolute-astrometry
s05/relative-astrometry
s05/brighter-fatter-effect
s05/intrapixel-capacitance
s05/persistence
s05/astrometric-and-photometric-calibration
```
