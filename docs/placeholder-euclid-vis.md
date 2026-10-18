### 1. Introduction

The Nancy Grace Roman Space Telescope (hereafter Roman) is a NASA flagship observatory designed to address fundamental questions in cosmology, exoplanet demographics, and astrophysics through wide-field, high-resolution observations of the near-infrared sky. With a 2.4-meter primary mirror and a Wide Field Instrument (WFI) providing a field of view approximately 100 times larger than that of the Hubble Space Telescope, Roman combines space-based angular resolution with unprecedented survey efficiency. Over its nominal five-year primary mission, Roman will execute a diverse observing program spanning thousands of square degrees, monitoring millions of variable sources and producing an extensive archive of imaging, spectroscopy, and time-domain measurements. A defining feature of the mission is its open-data policy: all science observations will be publicly available without a proprietary period, enabling immediate access by the global astronomical community.

Roman's observing program includes three Core Community Surveys (CCS), designed to fulfill the mission's primary science objectives, and General Astrophysics Surveys (GAS), which expand its scientific reach. The CCS programs account for approximately 75% of the available science observing time. The High-Latitude Wide-Area Survey (HLWAS) will obtain imaging and slitless spectroscopy across multiple depth tiers covering more than 12% of the sky, providing measurements of weak gravitational lensing, galaxy clustering, and large-scale structure to constrain dark energy and dark matter. The High-Latitude Time-Domain Survey (HLTDS) will repeatedly observe deep extragalactic fields, primarily on a five-day cadence over two years, enabling precision measurements of Type Ia supernovae and the discovery of a broad population of astrophysical transients. The Galactic Bulge Time-Domain Survey (GBTDS) will monitor dense stellar fields toward the Galactic bulge, with cadences of approximately 12 minutes, to characterize exoplanet populations through gravitational microlensing and enable stellar variability studies. Complementing these programs, the community-defined Galactic Plane Survey (GPS) will combine wide-field imaging, time-domain observations, and spectroscopy to investigate Galactic structure, stellar populations, and star formation. Together with competitively selected GAS programs, these surveys will produce an exceptionally diverse collection of observations with substantially different spatial coverage, depth, cadence, and scientific requirements.

To maximize the scientific return of these observations, Roman employs a data dissemination strategy that distinguishes between prompt data products and formal Data Releases (DRs). Prompt products are generated through routine processing and made publicly available as observations are acquired, providing rapid access to calibrated images, visit-level mosaics, and selected catalogs. However, because prompt products are generated using the best-available calibration reference files and pipeline versions at the time of processing, their calibration and scientific quality may vary throughout the mission. Formal DRs address this limitation through coordinated reprocessing of defined survey datasets using a consistent pipeline version and calibration reference-file context. DRs provide uniformly processed, science-ready products, including higher-level mosaics, photometric catalogs, and survey-specific measurements. While DR Level 3 and Level 4 products are versioned and preserved, reprocessed Level 2 images generally replace their previous versions in the archive. This approach preserves the immediacy of Roman's open-data philosophy while providing the uniformity and reproducibility required for precision measurements and large statistical studies.

The scale and diversity of Roman's surveys introduce significant challenges for defining, producing, and validating these releases. Survey observations may span multiple years, overlap spatially, or require cumulative processing, while individual programs impose different requirements on photometric and astrometric accuracy, image combination, source detection, spectroscopy, and time-domain measurements. A coordinated framework is therefore necessary to determine the contents and timing of each DR, establish the appropriate calibration and processing configuration, and assess the scientific quality of the resulting products. In this paper, we describe Roman's Data Release philosophy and the framework developed to coordinate reprocessing, release generation, and scientific validation. We outline the organizational responsibilities and operational workflow, discuss the principles governing release definitions and scheduling, and present the validation strategy designed to characterize the quality, limitations, and scientific readiness of Roman's publicly available data products.

### 2. The instrument

Roman's primary science instrument, the Wide Field Instrument (WFI), provides wide-field imaging and slitless spectroscopy over approximately 0.5–2.3 μm. The WFI focal plane comprises 18 Teledyne H4RG-10 HgCdTe sensor chip assemblies (SCAs), each containing 4096 × 4096 pixels with a 10 μm pixel pitch. The detectors are arranged in a roughly rectangular 6 × 3 configuration, with small gaps and offsets between adjacent arrays. Together, they provide approximately 300 million pixels, a plate scale of 0.11 arcsec pixel⁻¹, and an active field of view of 0.281 deg². The instrument includes eight imaging filters and two slitless spectroscopic elements, a prism and a grism. Detailed descriptions of the WFI optical design and detector characteristics are provided by Mosby et al. (2020) and in the <a href="https://roman-docs.stsci.edu/roman-instruments/the-wide-field-instrument">WFI Instrument Handbook</a>.

Each H4RG-10 detector is read out through 32 parallel science outputs, each spanning 128 columns, together with an additional reference output. A four-pixel-wide border of non-photosensitive reference pixels surrounds the array, leaving a 4088 × 4088-pixel active science region. These physical reference pixels, together with the virtual reference pixels sampled by the 33rd amplifier, enable corrections for time-dependent electronic offsets and correlated read noise. The detectors employ non-destructive sampling, in which accumulated charge is measured repeatedly throughout an exposure. To limit telemetry volume, individual reads are combined according to predefined multi-accumulation (MA) tables into a sequence of resultants, which may contain different numbers of reads and need not be uniformly spaced in time. The resulting signal ramps enable estimation of the incident count rate while facilitating identification of cosmic-ray events and other transient detector effects. Further details of detector operation and calibration are presented by Mosby et al. (2020), with the operational readout schemes documented in the <a href="https://roman-docs.stsci.edu/roman-instruments/the-wide-field-instrument/observing-with-the-wfi/wfi-multiaccum-ma-tables">WFI MultiAccum Tables</a>.

Roman science data are delivered primarily in the Advanced Scientific Data Format (ASDF), which combines binary numerical arrays with hierarchical, schema-validated metadata. Unlike traditional FITS files, ASDF supports structured representations of calibration information, coordinate transformations, and processing provenance. Each detector exposure is stored separately. Level 1 (L1) products contain uncalibrated three-dimensional ramps with dimensions (N resultants, 4096, 4096), together with the reference-output data and associated metadata. The exposure-level calibration pipeline, romancal, applies detector corrections and fits the signal ramps to produce Level 2 (L2) calibrated count-rate images with dimensions 4088 × 4088 pixels. These files contain the calibrated science array, uncertainty and data-quality information, and metadata describing the processing configuration and calibration reference files used. The data models and processing algorithms are described in the <a href="https://roman-docs.stsci.edu/data-handbook/wfi-data-levels-and-products">Roman Data Handbook</a> and <a href="https://roman-docs.stsci.edu/data-handbook/roman-wfi-data-pipelines/exposure-level-pipeline">Exposure Level Pipeline documentation</a>.

Higher-level products combine information from multiple exposures and detectors. Level 3 (L3) products include resampled images and mosaics, while Level 4 (L4) products contain derived measurements such as source catalogs, segmentation maps, spectra, and time-domain products. Although ASDF is the principal format for image products, tabular catalogs are also delivered in formats such as Apache Parquet. These products are generated through survey-dependent processing workflows, reflecting the distinct requirements of wide-area imaging, slitless spectroscopy, and time-domain observations. The association files used to group individual observations, together with the metadata identifying pipeline versions and calibration reference files, are therefore essential components of Roman's Data Release infrastructure. Their consistency and traceability provide the foundation for the coordinated reprocessing and scientific validation described in the following sections.

3. Survey Design and Strategy

Roman's four community-defined surveys employ distinct observing strategies tailored to their primary scientific objectives. These strategies determine not only the spatial and temporal characteristics of the resulting datasets, but also how observations are grouped, processed, and combined into higher-level science products. The surveys differ substantially in their footprints, depth, cadence, filters, and dithering patterns, motivating survey-specific approaches to Data Release generation and validation. This section summarizes the overall observing strategies of the High-Latitude Wide-Area Survey (HLWAS), High-Latitude Time-Domain Survey (HLTDS), Galactic Bulge Time-Domain Survey (GBTDS), and Galactic Plane Survey (GPS). The specific observations and processing configurations included in individual Data Releases are described separately.

The survey implementations were developed through a community-led process and are documented in the Roman Observations Time Allocation Committee (ROTAC) report and the Roman Community-defined Surveys documentation. We summarize the principal design features relevant to data processing and validation, rather than reproducing the detailed observing specifications available in those references.

3.1 High-Latitude Wide-Area Survey (HLWAS)

The High-Latitude Wide-Area Survey (HLWAS) is designed to provide wide-field near-infrared imaging and slitless spectroscopy for studies of weak gravitational lensing, galaxy clustering, and the large-scale distribution of matter. Its observing strategy balances survey area against depth through four complementary tiers: Wide, Medium, Deep, and Ultra-Deep. The Wide tier covers approximately 2,200 deg² in a single filter, while the Medium tier covers approximately 2,300 deg² with multiband imaging and grism spectroscopy. The Deep tier consists of two fields totaling approximately 19 deg², with additional Ultra-Deep imaging covering approximately 5 deg² within those fields. Together, the tiers provide progressively deeper observations over smaller areas, supporting both the principal cosmological measurements and the calibration of photometric redshifts and galaxy shapes.

Unlike the time-domain surveys, HLWAS is not designed around a uniform temporal cadence. Observations will be distributed throughout the five-year primary mission, with the Deep tier scheduled relatively early. The observing strategy employs mosaics and dither patterns designed to provide contiguous spatial coverage, mitigate detector gaps and bad pixels, improve point-spread-function sampling, and support accurate astrometric and photometric measurements. Multiple exposures and survey passes are combined to generate mosaics and source catalogs at the depths required by each tier.

The filter selection and exposure depth vary by tier. The Wide tier uses F158, while the Medium tier employs F106, F129, and F158 together with grism spectroscopy. The Deep tier includes F087, F106, F129, F146, F158, F184, and F213, as well as grism observations. The Ultra-Deep component obtains additional imaging in F106, F129, and F158. Exposure times, numbers of dithers, and survey-pass configurations are optimized for the different depth and area requirements and are documented in the HLWAS observing specifications.

For Data Release processing, the distinction between tiers is particularly important. Because the tiers have different depths, filters, and spatial footprints, they may require separate association definitions, mosaicking strategies, and validation criteria. Uniformity within a given tier is therefore a central consideration when defining HLWAS Data Release products.

3.2 High-Latitude Time-Domain Survey (HLTDS)

The High-Latitude Time-Domain Survey (HLTDS) is designed to discover and characterize supernovae and other astrophysical transients over a broad range of redshifts. The survey targets northern and southern extragalactic fields, including regions near COSMOS and XMM-LSS, and combines repeated near-infrared imaging with slitless spectroscopy. Its observing program is divided into Pilot, Core, and Extended components, with Wide and Deep regions providing different combinations of area, depth, and temporal coverage. The Deep regions provide the sensitivity required to characterize faint, high-redshift transients, while the Wide regions increase the statistical sample and survey volume.

The Core component is designed to revisit each field approximately every five days over two years, with a nominal cadence tolerance of ±1 day and additional scheduling flexibility when necessary. The Pilot component provides earlier observations that can establish reference imaging and exercise the observing and processing strategy, while the Extended component lengthens the temporal baseline. The combination of these components enables measurements of transient light curves over a range of timescales and supports the construction of increasingly deep reference images as additional observations become available.

HLTDS observations employ repeated mosaics and dithering to maintain coverage of the survey fields while mitigating detector gaps and improving image sampling. The survey uses multiple near-infrared filters to obtain transient colors and photometric evolution, together with prism and grism observations for spectroscopic characterization. Filter selection, exposure times, and the balance between imaging and spectroscopy vary among the survey components and depth tiers. The complete observing specifications are provided in the HLTDS documentation.

The repeated observations and evolving depth of HLTDS introduce distinctive Data Release requirements. Unlike a survey designed to produce a single uniform-depth map, HLTDS naturally produces cumulative datasets in which the number of contributing epochs, temporal coverage, and limiting depth vary across the footprint. Data Release processing must therefore preserve the temporal information required for transient science while enabling consistent reprocessing of the accumulated observations. Validation must address both the quality of the combined images and catalogs and the consistency of measurements across observing epochs.

3.3 Galactic Bulge Time-Domain Survey (GBTDS)

The Galactic Bulge Time-Domain Survey (GBTDS) is designed primarily to characterize exoplanet populations through gravitational microlensing, while also enabling a broad range of studies of stellar variability, Galactic structure, and compact objects. The survey monitors six WFI fields covering approximately 1.7 deg² toward the Galactic bulge. Five fields form a contiguous region selected to balance stellar density, extinction, and microlensing sensitivity, while a sixth field targets the Galactic Center. The same fields are observed throughout the mission to establish long temporal baselines for photometric and astrometric measurements.

GBTDS observations are organized into ten approximately 72-day Galactic bulge visibility seasons distributed across the five-year mission. Six seasons employ high-cadence monitoring, concentrated near the beginning and end of the mission, while four intervening seasons use lower-cadence observations. During high-cadence seasons, the six fields are observed in a repeating sequence approximately every 12.1 minutes. During low-cadence seasons, shorter monitoring sequences are repeated approximately every five days. This strategy provides both the dense sampling required to detect short-duration planetary microlensing signals and the long temporal baseline needed to characterize stellar variability, proper motions, and long-duration microlensing events.

The six-field observing pattern is maintained across seasons, with mosaic orientations adjusted by approximately 180 degrees between the spring and autumn visibility windows. Small offsets between repeated mosaics provide both integer-pixel and subpixel dithering, mitigating detector defects and improving sampling without significantly interrupting the required cadence. Additional dither patterns are employed for the multiband photometric and spectroscopic snapshot observations.

The primary monitoring filter is F146, with individual exposures of approximately 66 seconds. F087 and F213 observations provide additional color information at lower cadence. Each season also includes three multiband photometric snapshots using F062, F106, F129, F158, and F184, together with three grism spectroscopic snapshots. The snapshots employ longer exposures and additional dithers to characterize stellar populations and support calibration of the primary time-series measurements. Detailed exposure times, MultiAccum patterns, and observing sequences are provided in the GBTDS observing specifications.

GBTDS presents a distinct processing challenge because of its exceptionally large number of repeated observations in crowded stellar fields. Its higher-level science products include time-series photometry, astrometric measurements, and microlensing event catalogs that depend on consistent calibration across entire observing seasons. Consequently, Data Release planning must coordinate the reprocessing of calibrated exposures with the downstream generation of season-level and cumulative science products. Validation must assess not only image and catalog quality, but also photometric stability, astrometric consistency, completeness, and the reliability of time-domain measurements.

3.4 Galactic Plane Survey (GPS)

The Galactic Plane Survey (GPS) extends Roman's observing program to the dense and highly extincted regions of the Milky Way. The survey combines three complementary components: a wide-field imaging survey, a time-domain program, and a set of deep imaging and spectroscopic fields. The wide-field component covers nearly 700 deg² of the Galactic plane, with additional extensions toward the Galactic bulge, Carina, and Serpens South. The time-domain component monitors six selected regions totaling approximately 19 deg², while the deep-field component provides additional imaging and spectroscopy in 15 WFI pointings. Together, these observations enable investigations of Galactic structure, stellar populations, star formation, and variability across a broad range of Galactic environments.

GPS is allocated up to 700 hours and is intended to be completed primarily within the first two years of Roman's primary mission. The wide-field component does not employ a uniform short-timescale cadence, but its observations are distributed to provide multiple epochs and support proper-motion measurements. The time-domain component uses field-dependent cadences ranging from approximately 11 minutes to weeks, tailored to the variability timescales and scientific objectives of each region. High-cadence observations target selected star-forming complexes and Galactic Center fields, while lower-cadence observations extend the temporal baseline for longer-period variability.

The wide-field observations employ contiguous mosaics with dithering designed to maintain coverage across detector gaps and improve spatial sampling. The time-domain fields use a combination of adjacent pointings and repeated mosaic patterns, with the exact configuration depending on the field size and cadence. Fast-cadence observations are generally executed as sequences of adjacent pointings, while lower-cadence observations use larger mosaics that preserve the intended field coverage despite changes in telescope orientation. These strategies are described in the GPS implementation documentation.

Most of the wide-field area is observed in four filters: F129, F158, F184, and F213. The time-domain observations primarily use F213, with F184 employed for selected fields and additional filters providing complementary color information. The deep-field component includes all seven broad-band imaging filters, excluding the wide F146 filter, together with prism and grism spectroscopy. Exposure times and dithering strategies vary by component; for example, the time-domain observations generally use approximately 60-second exposures, while the deep-field observations employ longer integrations to reach fainter sources and provide more complete spectral-energy-distribution information.

The combination of wide-area coverage, crowded fields, variable extinction, and heterogeneous observing strategies creates several challenges for GPS Data Releases. Unlike the extragalactic surveys, the GPS footprint contains many spatially separated regions with substantially different source densities and backgrounds. Processing and validation must therefore accommodate variations in crowding, source detection completeness, astrometric precision, and photometric performance. The separation of survey components and fields also provides flexibility in defining Data Release contents, while maintaining a common calibration and processing framework across the survey.

#### 3.5	This data release: scope epochs and data volume	RTB	This section will need customization for each data release. Likely a figure or two showing the specific footprints, if these are not covering the full survey footprint. 

#### 3.6	Relation to previous data releases	RTB	History of data releases, highlighting major calibration channges, data product changes. Also highlighting that the data releases are cumulative.

#### 3.7	Overview of Data Products	RDOCs	This is a high-level overview of the types of products, largely drawn from RDOCs. Highlight any significant changes in products relative to prior data releases 

### 4. Observations

#### 4.1	Observations summary	RTB	Summary tables of the observations -- fields, filters & timing

#### 4.2	Coverage gaps	RTB	Summary of any occasional missing tiles or filters, etc.; Perhaps include a plot of area covered in each filter as a function of exposure time, as a summary of the affects of gaps?

#### 4.3	Coordinated Observations from Other facilities	?	Highlight any coordinated observations from external facilities

### 5. Calibration/Pixel-Level Correction

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

#### 5.1	Summary of WFI Calibration Status for this data release	RTB	Describe basic calibration summarize current estimated uncertainties; for each data release this can be mostly a snapshot of RDOCs, but there is probably work to make it coherent as a static long-term record of the state of calibration that can be understood even if the rest of RDOCs is evolving.

#### 5.2	Darks,  Data Quality Flags, instabilities not flagged	RDOCs	Characterized as part of calibration plan; draw from RDOCs, highlighting any specifics for this data release.

#### 5.4	Gain and gain stability	RDOCs	ditto

#### 5.3	1/f bias correction	RDOCs	ditto

#### 5.4	Flat field	RDOCs	ditto

#### 5.5	Nonlinearities	RDOCs	ditto

#### 5.6	Photometry	RDOCs	Focus on L2; refer to later section for L3?

#### 5.6.1	Zeropoints and Zeropoint stability	RDOCs	ditto

#### 5.6.2	Ice: models, corrections, remaining SED-dependent uncertainties	RTB	Highlight decontaminations that happened over the course of observations included in this data release; plot time-series of ice deposition…

#### 5.7	Instrument geometric distortions and stability	RDOCs	ditto

#### 5.8	PSF characterization and stability	RDOCs	This section would be for L2 PSFs, pointing to a later section for the co-add PSFs.

#### 5.9	Astrometry	RDOCs	ditto

#### 5.9.1	Absolute Astrometry 	RDOCs	This section focuses on L2; need to highlight differences for L3

#### 5.9.2	Relative Astrometry	RDOCs	This section focuses on L2; need to highlight differences for L4

#### 5.10	Brighter-fatter effect	RDOCs	

#### 5.11	Intrapixel Capacitance	RDOCs	

#### 5.12	Persistence   	RDOCs	

#### 5.13. Astrometric and photometric calibration

The second stage, where quadrants are processed together. The paper describes
gain equalisation, a simplified point-spread-function model for monitoring,
a large-scale illumination correction, astrometric calibration against Gaia,
and photometric calibration, including how throughput changes over time were
handled.

**Roman equivalent:** TBD. Reference catalogues used, zero-point strategy,
and the version of any calibration reference files, pinned to a tagged
calibration release (for example, `bp-27a`).


### 6. Exposure Level Processing

#### 6.0	Overview	RDOCs	Basically a snapshot of RDOCs at the time of each release

#### 6.1	Data quality flagging	RDOCs	

#### 6.2	Saturation detection	RDOCs	

#### 6.3	Reference pixel correction	RDOCs	

#### 6.4	Linearity Correction	RDOCs	

#### 6.5	Dark Current subtraction	RDOCs	

#### 6.6	Ramp fitting and jump detection	RDOCs	

#### 6.7	WCS assignment and astrometric registration	RDOCs	

#### 6.8	Flatfielding	RDOCs	

#### 6.9	Photometric zeropoints	RDOCs	

#### 6.10	Uncertainty arrays and error model 	RDOCs	

#### 6.11	Known problems 	RTB	E.g. Highlight implications of exposure-level processing for things that might change during the exposure.

### 7. Image Rectification and Co-Addition

#### 7.0 Overview	RTB	Highlight anything different for this data release

#### 7.1	Sky tesselation	RDOCs	

#### 7.2	Resampling and projection	RDOCs	

#### 7.3	Sky estimation and matching	RDOCs	This could be a long section down the road if/when we include scattered light, zodi and/or thermal in the background estimation.

#### 7.4	Weighting strategy	RDOCs	

#### 7.5	Outlier rejection 	RDOCs	Highlight implications for moving targets or transients

#### 7.6	Uncertainty arrays and error model 	RDOCs	

#### 7.7	Point-spread functions	RTB	Include diagnostics of PSF width and shape

#### 7.8	Known problems	RTB	

### 8. Static Catalog Processing

#### 8.0	Overview	RTB	Highlight changes relative to previous releases

#### 8.1	Treatment of skycell and projection region boundaries	RDOCs

#### 8.2	Local Background estimation	RDOCs	

#### 8.3	Detection algorithm and detection kernels	RDOCs	

#### 8.4	PSF-fit photometry	RDOCs	

#### 8.5	PSF-matching between bands	RDOCs	

#### 8.6	PSF-matched aperture photometry 	RDOCs	

#### 8.7	SED-dependent biases	RDOCs	Brief summary of effects of changing bandpasses (ice and angle-of-incidence.) and pointer to where to go to for advice on how to correct.

#### 8.8	Absolute Photometry	RDOCs	Corrections to apply to standardize the fluxes ("aperture corrections")

#### 8.9	Uncertainties and error model	RDOCs	

#### 8.10	Shape parameters	RDOCs	Mean FWHM, size, ellipticity

#### 8.11	Source injection and recovery	RDOCs	

#### 8.12	Photometric redshifts	RDOCs	

#### 8.13	Warnings and flags	RDOCs	

#### 8.14	Known artifacts and systematics	RTB	

### 9. Stacking and catalogue extraction

#### 9.0	Overview	RDOCs	This whole section could instead be a subsection of "Static Catalog Validation"…

#### 9.1	Input source models	RDOCs	

#### 9.2	Limitations	RDOCs	Caveats: Inserting in to L3 images so PSF & sampling is only approximate; Not accounting for SED-dependent bandpass variations due to ice or angle of incidence. Not accounting for astrometric effect of filter refraction.

#### 9.3	Injection, recovery and photometry	RDOCs	

#### 9.4	Catalog description	RDOCS	

#### 9.5	Summary statistics	RTB	This is where one might show limiting magnitudes and show validation of the photometric uncertainties based on source injection & recovery.

### 10. Static Catalog Validation

#### 10.0	Overview		

#### 10.1	Photometric repeatability		Across data releases, across epochs and across border regions; demonstrate that the catalog-reported  uncertainties are reliable
  Zeropoints and Zeropoint stability		Save as for LVL2's above
  Flux Conservation 		L2 -> L3
  Noise Propogation		L2 -> L3
  S/N Improvement		L2 -> L3

#### 10.2	Photometry External Comparisons		Compare to HST, JWST or other facilities

#### 10.3	Stellar Locus		
  Depth/Sensitivity		5/sigma and 10/sigma completeness limits, blank-sky aperture measurements
  Source injection and recovery		Same as for LVL2's above

#### 10.4	Color-dependent systematics		

#### 10.5	Astrometric repeatability		Across data releases, across epochs and across border regions

#### 10.6	Astrometry External Comparisons		Compare to HST, JWST or other facilities
  Astrometric consistency		L2 -> L3

#### 10.7	Shape parameter repeatability		Demonstrate catalog-reported uncertainties are reliable, e.g.
  Shape parameter statistics		scatter, vs time, vs position on detector, ellipticity residuals?

#### 10.8	Shape parameter external comparisons		
  PSF Conservation		L2 -> L3

#### 10.9	Shape parameter color-dependent systematics		
  Source Detection & Catalog Validation		Detection efficiency
  Source Detection & Catalog Validation		Contamination rate
  Matching Statistics 		Between filters
  Galaxy Counts		Galaxy counts dN/dmdN/dm and cumulative source density. End-to-end validation of catalog quality and survey depth. End-to-end validation of catalog quality and survey depth. 
  Quality Control		"Check distributions for threshold exceedances:
peak of spread_model distribution
width of spread_model distribution
percentage of pixels impacted by CRs
percentage of pixels flagged as CRs
number of quadrants masked by CR_REGION (>5% pixels flagged)
astrometric residual averaged over FPA
median value of e1 of selected stars
median values of e2 of selected stars
median value of the R^2 of elected stars
overall image quality score"

#### 10.10	Outlier summary		Investigate outliers and provide guidance. E.g. what fraction of the 100 "reddest" objects in the survey are real? Can you filter to improve this? What fraction of the 100 "largest" or "smallest" or "flattest" galaxies at some faint magnitude are real? Can you improve by filtering? Science use cases can guide what to check -- e.g. LRDs, AGNs, emission-line galaxies, LSB galaxies, etc.

### 11. Photometrid Redshift Tuning and Validation

#### 10.0	Overview	RTB	Generic text will largely be on RDOCs already

#### 11.1	Training/tuning data sets and tuning parameters	RTB	This may vary from data release to datea release given that training sets and algorithms are likely to be evolving.

#### 11.2	Photometric redshift validation: peak estimates		Histograms of spec-z vs photo-z in bins of spec-z (much more revealing than z vs. photo-z plot)

#### 11.3	Photometric redshift validation: probability distributions		E.g. Q-Q plots

#### 11.4	Photometric redshift validation: clustering		Histograms of photo-z - spec-z for close-separation pairs (validation that photo-z estimates are relaiable fainter than the spectroscopic training sets)

#### 11.5	Outlier summary		Summarize behavior of outliers and give guidance on whether any filtering on other catalog parameters (e.g. crowding) can mitigate their effects. What fraction of the 100 "highest redshift" galaxies are likely to be real?

### 12. Time-Series Catalog Processing

#### 12.0	Overview	RTB	Highlight changes relative to previous releases

#### 12.1	Object Selection	RDOCs	

#### 12.2	PSF selection	RDOCs	

#### 12.3	PSF fitting	RDOCs	

#### 12.4	Aperture photometry	RDOCs	

#### 12.5	SED-dependent biases	RDOCs	Brief summary of effects of changing bandpasses (ice and angle-of-incidence.) and pointer to where to go to for advice on how to correct.

#### 12.6	Absolute Photometry	RDOCs	Corrections to apply to standardize the fluxes ("aperture corrections")

#### 12.7	Uncertainties and error model	RDOCs	

#### 12.8	Flags and warnings	RDOCs	

#### 12.9	Moving targets	RDOCs	E.g. proper motions

### 13. Time-Series Catalog Validation

#### 13.0	Overview	RTB	

#### 13.1	Photometric repeatability		

#### 13.2	Absolute Photometry		

#### 13.3	Photometry External Comparisons		E.g. Compare to RAPID, SNe cosmology time series

#### 13.4	Astrometric repeatability		

#### 13.5	Astrometry external comparisons		Astrometry should be *better* here than in the L4 static catalogs. What should be shown to demonstrate this?

#### 13.6	Astrometry: Proper motions		Compare to Gaia & Rubin, e.g.

### 14. Archive and Data Access

#### 14.0	Overview	RDOCs	One could decide *NOT* to put this in the data release "paper" because access methods could evolve, while the record of the calibration and data-processing is an important archival description of the data themselves.

#### 14.1	Image access	RDOCs	

#### 14.2	Sky viewer	RDOCs	How to overlay footprints, weight maps…

#### 14.3	Cutouts	RDOCs	

#### 14.4	Catalog access	RDOCs	Both via on-site databases and LSDB on AWS. (Currently the source-injection input/output are not in a database, but they ought to be, and access described here as well.)

### 15. Data Products

#### 14.0	Overview	RDOCs	

#### 14.1	L1 Uncalibrated Exposures	RDOCs	Mostly won't change from data release to data release

#### 14.2	L2 Exposure Level Data Products	RDOCs	

#### 14.3	L2 Exposure Level Ancillary products	RDOCs	Currently this is the WCS. But in the future might include diffraction spike masks, background model, de-striping model, …

#### 14.4	L3 Co-add Data Products	RDOCs	

#### 14.5	L4 Static Catalogs	RDOCs	

#### 14.6	L4 Static Catalog Ancillary Products	RDOCs	Currently this is segmentation maps and source-injection input/output. This may involve to include other items.

#### 14.7	L4 Time-Series Catalogs	RDOCs	

#### 14.8	Survey-level products	RDOCs	To be defined. Could include healpix encoded information on survey depths (computed from the weight maps, but compact and queriable), sky backgrounds. Could include survey footprints. 

### 15. Calibration and Pipeline Versions

#### 15.1 Romancal pipeline version	DMS	Version number and summary of changes relative to previous release (extracted and summarized for scientrists from the release notes).

#### 15.2	Calibration Reference Files	RTB	Minimal would just be the "pmap". Maximal (and more useful as an archival record) would be to extract and summarize the descriptions of changes for each of the reference files for this version relative to the last data release. That information is in principle there in the reference files themselves, but it is significant effort to turn this into a readable narrative  (AI could perhaps help?).

#### 15.3Science Data Formatting	DMS	Document any significant changes. 

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
