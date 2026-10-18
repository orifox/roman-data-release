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


## 5.1 Summary of WFI Calibration Status for this data release

**Source:** RTB. Describe basic calibration summarize current estimated uncertainties; for each data release this can be mostly a snapshot of RDOCs, but there is probably work to make it coherent as a static long-term record of the state of calibration that can be understood even if the rest of RDOCs is evolving.

## 5.2 Data Quality Flags, instabilities not flagged

**Source:** RDOCs. Characterized as part of calibration plan; draw from RDOCs, highlighting any specifics for this data release.

````{admonition} Example text from Euclid: NISP bad-pixel masks
:class: note

*Reproduced from Euclid Collaboration: Polenta et al. (2025), "Euclid Quick Data Release (Q1). NIR processing and data products", [arXiv:2503.15304](https://doi.org/10.48550/arXiv.2503.15304), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

We used ground test data of the H2RGs as the primary resource to identify bad pixels for Q1. These pre-launch evaluations of the pixel performance were taken over three main campaigns: acceptance testing and ranking at the NASA Goddard Space Flight Center’s Detector Characterisation Laboratory (DCL) in 2016; individual component tests in 2019 at the CNRS-IN2P3 Center for Particle Physics in Marseille (CPPM); and fully integrated flight-module tests in space-like conditions (thermal vacuum and thermal balance, or TBTV) at Laboratoire d’Astrophysique de Marseille (LAM) in 2019–2020. The TBTV and final pre-launch payload module (PLM) tests with NISP integrated into the telescope are summarised in Medinaceli et al. (2022).

In addition, baseline calibration measurements were taken during commissioning and incorporated into the bad-pixel maps for NIR PF (see Sect. 3.1.3). Calibration observations obtained during the PV Phase are not reflected in Q1.

Pixels revealed to be permanently inoperable for science, or exhibiting noteworthy performance characteristics that may affect operability, are contained in calibration data products for the NISP Level 2 pipeline. A map has been created for each pixel condition (or ‘flavour’) by detector, assigned a 16-bit unsigned integer 2n, n > 1, and merged into a master bad-pixel mask (BPM) that can be used by NIR PF. The BPM application updates the data quality (DQ) layer accompanying each of the 16 science frames, with no distinction between imaging and spectroscopy modes. For pixels affected by more than one bad flavour condition, the DQ values are obtained by performing a bit-wise sum (logical OR).

The BPM is not restricted to scientifically inoperable pixels. To distinguish unusable from informational flavours, the bit 0 is reserved for the unusable cases. This ‘INVALID’ bit is summed only once, even when a pixel has been flagged with more than one fatal condition, as is often the case. Thus INVALID pixels will always have an odd DQ value. Further details, including bit assignments, can be found in Morris & Kubik (2022) and Euclid Collaboration (2025). Statistics for the non-transient – that is static – pixel masks are summarised in Table 1, and in the following we review the most important flags.

Table 1.NISP detector non-transient DQ flags and dark currents in Q1.
Invalid flags. Pixels in Q1 data are flagged invalid if: (i) they are unresponsive due to disconnection from the readout-integrated circuit; (ii) their quantum efficiency is very low or poorly known; and (iii) if their baseline after bias reset is outside the photometrically calibratable range.

‘Disconnected’ pixels have absent or non-working indium bumps to connect to the photosensitive diodes. They terminate at the capacitor and have no detectable photo-sensitivity. Some positive residual charge is generally present for them in the readout electronics. Measurements were done under specific laboratory conditions at ambient room temperature and thus could not be repeated in the same fashion after launch.

‘Zero-quantum-efficiency’ pixels were identified during detector qualification tests at the DCL. Such pixels are flagged when the measured quantum efficiency (QE) is less than 5% (corresponding to the low-end measurement uncertainty) averaged over wavelengths 920 nm ≤ λ ≤ 1120 nm. Most disconnected pixels have zero QE.

‘Super-QE’ pixels have wavelength-averaged QEs greater than 110%. Such pixels generally surround clusters of disconnected pixels, creating a bright, one-pixel wide halo under illumination as photocurrent flows from the disconnected pixels to the nearest photosensitive neighbours with usable well depths. Figure 3 shows an example. Thus, the measured QEs become artificially high – reaching as much as 200% in some cases – and unrecoverable.

*Fig. 3 of the source paper (not reproduced):* Representative flagged QE ‘flavours’ in Q1, detector 44 in this example. Grey background pixels are in the range of 5–100% QE. Zero and Super QE pixels are INVALID in NIR PF, while Low QE pixels are flagged for monitoring. Super QE pixels often appear as a 1-pixel wide bright halo around groups of disconnected pixels, although the largest group in this example does not exhibit a halo – the QEs of neighbouring pixels are within the nominal range to within the 5% measurement uncertainty. For reference, ‘+’ indicates pixel [x,y] = [1458,1336] in Level 2 2040 × 2040 array coordinates. The labelled QE ranges are wavelength-averaged.

‘Bad baseline’ pixels have baselines that are either too high or too low after bias reset and fall into a range of excessive kTC noise. Because the ground-based baseline data were obtained at a lower temperature than where the NISP FPA operates on orbit by about 6 K, the baselines were remeasured during commissioning (see Sect. 3.1.1) and updated in the BPM. This is the only flavour that has been updated with in-flight data for the Q1 release.

Informational flags. Certain flags have been reserved for monitoring purposes. In Q1, hot and low QE pixels are tracked but are not set to INVALID, pending further evaluation of their operability for science with flight data.

‘Hot’ pixels have been defined differently in the literature by the sensor-chip manufacturers and the intended application. For NISP, the signal of a hot pixel is 3σ above the most probable value of the detector’s measured dark current. Pixels with elevated dark currents are not necessarily INVALID, as long as the unilluminated output signal is stable and below thesaturation limit. Hot pixels were identified from ground-based dark current measurements, then updated and checked for stability in flat-field measurements taken during PV and in the routine phase with the LEDs over a range of fluences.

‘Low-QE’ pixels are flagged when nominal requirements set by NASA during tests at the DCL are not met to within the 5% RMS uncertainty for measurements at 920 nm ≤ λ ≤ 2020 nm,

QE ≥ 74% for λ ∈ [1120, 2020] nm and

QE ≥ [64 + (λ/nm − 920)/20]% for λ ∈ [920, 1120] nm.

The data from such pixels are expected to be calibratable, pending further evaluation with flight data, but will generally exhibit reduced signal-to-noise levels compared to pixels with nominal QE.
````

## 5.3 Non-Linear Correction

````{admonition} Example text from Euclid: NISP non-linearity
:class: note

*Reproduced from Euclid Collaboration: Polenta et al. (2025), "Euclid Quick Data Release (Q1). NIR processing and data products", [arXiv:2503.15304](https://doi.org/10.48550/arXiv.2503.15304), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

Non-linearity in H2RGs is primarily caused by the behaviour of the photodiode’s junction capacitance. As charge accumulates in a pixel during exposure, the depletion region of the photodiode narrows, leading to an increase in junction capacitance. This change affects the conversion of accumulated charge to voltage, causing deviations from the ideal linear response. Additionally, other components in the signal chain, such as the source follower in the readout integrated circuit and the ADC process, can introduce further non-linearities. These combined effects result in a non-linear relationship between the incident photon flux and the measured signal, with the non-linearity becoming increasingly pronounced as the flux level rises, independent of wavelength (see e.g. Plazas et al. 2017; Barbier et al. 2018).

We calibrated the pixel-level response and non-linearity with custom-designed LEDs (Euclid Collaboration: Hormuth et al. 2025; Euclid Collaboration: Jahnke et al. 2025). Each LED has a narrow emission spectrum and can illuminate the FPA with varying fluxes. For the non-linearity calibration (conducted on the ground and in flight), two key measurements are required: the fitted slope image (Kubik et al. 2016) that represents the non-linear response, and the individual MACC group images that are used to approximate the linear flux, FLinear (e.g. Vacca et al. 2004). For both photometry and spectroscopy readout modes, MACC(4,16,4) and MACC(15,16,11), respectively, five fluence levels were selected to span the dynamic range expected for each mode, accounting for their different exposure times. These measurements were then combined to derive the non-linearity calibration coefficients for each pixel.

The linear flux estimate, FLinear, is derived by modelling the pixel response across various fluence levels using orthonormal polynomials. The first term of this model provides an approximation of the linear flux, as fully described in Euclid Collaboration: Kubik et al. (2026). Orthonormal polynomials were chosen for their practical advantages, including computational efficiency and manageable memory usage, and this approach has been successfully adopted for correcting H2RGs at several facilities. In the long term, more sophisticated models, such as a principal component analysis (PCA), will be evaluated to enhance non-linearity corrections (see also Rauscher et al. 2019). Before the fitting, the ramps are corrected for reference pixels using sliding windows of four pixels. To optimise memory and CPU usage, the ramps, observed multiple times at each fluence level, are averaged for each run. Additionally, frames exceeding 60 000 ADU are rejected to avoid saturation effects.

Following the pre-processing, the non-linearity per pixel is expressed as a fourth-degree polynomial relationship between the estimate of the linearised flux, FLinear, and the measured non-linear flux, FNon-linear, expressed as

```{math}
:label: euclid-nisp-eq1

F_\mathrm{Linear} = \sum_{k=0,4} a_k \, F_\mathrm{Non\text{-}linear}^{k}
```

The degree of the polynomial is constrained by the number of available fitting flux levels. For consistency, we enforced the linear flux to be zero for a zero non-linear flux.

Fitting these polynomials to the thermal vacuum (TV1) calibration data, we measured the non-linearity coefficients and their covariances, which were subsequently used in the NIR PF non-linearity correction for Q1. The validity range is dictated by the dynamic range covered by the LED fluences (1000 ADU to 30 000 ADU), below which non-linearity effects are minimal and above which corrections are applied by linearly extending the polynomial fit rather than using the higher-order coefficients. It should be noted that the values above already include baseline removal. Considering the baseline level shown in Fig. 2, we expect saturation to occur between 40 000 and 50 000 ADU for most of the pixels. For the first data release, DR1, expected in October 2026, additional fluences from PV and calibration observations are expected to enlarge the validity range. The correction step also incorporates gain conversion, and a flagging of pixels where the fit is unreliable. In addition, pixels whose signal exceeds the saturation threshold defined from the ground-test campaign are identified by this PE and flagged using both SATURATION and INVALID bits.
````

## 5.4 Persistence Masking

````{admonition} Example text from Euclid: NISP persistence
:class: note

*Reproduced from Euclid Collaboration: Polenta et al. (2025), "Euclid Quick Data Release (Q1). NIR processing and data products", [arXiv:2503.15304](https://doi.org/10.48550/arXiv.2503.15304), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

**3.1.5.1. Persistence model – calibration product from ground characterisation.**

Charge persistence is the effect of electrons being trapped in detector defects, and being released again on time scales of minutes and hours (see e.g. Smith et al. 2008; Leisenring et al. 2016; Tulloch 2018). This leads to ghost images of previous exposures in subsequent exposures, affecting photometric and spectroscopic measurements. NIR PF masks persistence using an effective persistence model calibrated on ground-characterisation data (cf. Euclid Collaboration: Kubik et al. 2026; Kubik et al. 2024) for illuminations below saturation.

During the TV1 characterisation campaign, a standard protocol for persistence calibration was used. It consisted of a set of flat field exposures of 87 s with increasing fluences. Each of the flat exposures was followed by a dark exposure of 430 s.

The signal in the flat fields was estimated by the linear fit to the first 50 frames of the ramp. The subsequent frames were discarded from the fit to avoid non-linearity effects. Dark exposures were used to measure the persistence signal accumulated in exposure times that match those in the ROS (Euclid Collaboration: Jahnke et al. 2025). An example of a resulting persistence image is shown in Fig. 4, where the signal is expressed as a percentage relative to the initial flat field illumination.

*Fig. 4 of the source paper (not reproduced):* Persistence signal accumulated during a dark exposure following an LED flat field illumination. The persistence is expressed as a percentage relative to the original flat field signal.

The first n frames of the dark exposures were discarded to account for persistence decay between consecutive exposures in the reference observing sequence (ROS), with n = 26 for photometric observations during dithering and n = 175 for spectroscopic observations after slewing. The remaining frames were fitted using the on-board signal estimator of Kubik et al. (2016). The photometric readout mode, MACC(4,16,4), was used to estimate persistence in photometric exposures. To estimate persistence in spectroscopic exposures MACC(7,16,1) with 16 frames per group was used, that was the maximum possible, since the dark ramps during TV1 persistence testing were too short to compute persistence in the spectroscopic exposure time. In each case, the obtained slopes were multiplied by the corresponding total exposure time, converted to electrons using the gain per channel map. The dark-current was also subtracted. All coefficients are estimated per pixel, since the persistence amplitudes have high spatial variability (Kubik et al. 2024).

The calibrated effective persistence model yields the persistence charge QP as a function of the previous illumination amplitude S using the expression

```{math}
:label: euclid-nisp-eq2

Q_\mathrm{P}(S) = \left(\alpha + \beta S\right)\left(1 - \mathrm{e}^{-S/\gamma}\right)
```

Separate sets of coefficients α,  β,  and γ are needed to describe persistence in photometric and spectroscopic exposures, due to their different exposure times.

This model is effective in the sense that the persistence decay during one exposure is built in the coefficients of the model, but there is no explicit time dependence of the persistence decay. Other shortcomings of this model are that it does not take into account the superposition of persistence from multiple bright exposures, and it does not account for charge trapping, resulting in a potential lack of signal for bright sources on pixels that have previously seen a low-background exposure.

**3.1.5.2. Persistence masking procedure.**

There are two separate steps to mask persistence, presented schematically in Fig. 5. The first step consists of the estimation of persistence charge contributing to any of the NISP scientific exposures. It is a separate pipeline executed before the proper NIR data reduction, in which for each exposure the persistence charge originating from previous images is estimated and stored as a separate product (persistence estimate image). Taking into account the limitations of the effective model, for each photometric exposure only the persistence charge from one previous spectroscopic image is computed. To account for the persistence decay over one dither, the model computes QP using the calibrated set of parameters in Eq. (2) – this is the prediction of the persistence from a spectroscopic image to the JE-band image – and a rescaling factor is applied to estimate the persistence contribution to the HE- and YE-band images taken next in time. We note that for Q1 processing the persistence contribution originating from photometric exposures is not taken into account because, given the Euclid ROS, that would result in masking most of the bright sources. A more accurate model allowing for a correction procedure is being developed. Likewise, the computation and masking of persistence in spectroscopic exposures is deactivated for Q1.

*Fig. 5 of the source paper (not reproduced):* Persistence masking scheme. In the first step, the persistence estimate is calculated using the persistence model applied to prior exposures (source images) for each target exposure. In the second step, the persistence estimates are thresholded to identify and mask pixels where the persistence charge exceeds 2 e− (indicated in red in the right image). Typically, the percentage of masked pixels does not exceed 2%.

The second step is the persistence masking executed during the NIR scientific pipeline. In this task, for each photometric exposure, the corresponding persistence image is analysed. If the persistence charge amplitude in a pixel exceeds 2 e−, then a PERSIST and INVALID flag is raised in the DQ layer of the science exposure (Appendix B). For some pixels the persistence coefficients could not be calibrated, and consequently the persistence charge could not be estimated. In that case, the PERMODFAIL flag is raised in the DQ layer of the corresponding image.
````

## 5.5 Darks and Dark Current

````{admonition} Example text from Euclid: NISP darks
:class: note

*Reproduced from Euclid Collaboration: Polenta et al. (2025), "Euclid Quick Data Release (Q1). NIR processing and data products", [arXiv:2503.15304](https://doi.org/10.48550/arXiv.2503.15304), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

The master dark frames were updated from ground-based (TBTV) characterisation (Euclid Collaboration: Kubik et al. 2026) with two blocks of measurements taken during PV at 87 s and 548 s integration times, corresponding to the imaging and spectroscopic science modes, respectively. We refer to these as photo- and spectro-darks. The darks are taken after a sufficiently long pause to allow for the decay of previously built-up persistence charge. With the filter wheel in its closed position, the dependence of the measured dark current is thus purely on exposure time. Sets of 500 photo- and 100 spectro-darks were acquired to obtain a sufficient signal-to-noise ratio (S/N). The PE that generates the master dark uses an iterative procedure to reduce the impact of spurious detections from the active space weather near the maximum of the 25th solar cycle.

To estimate the pixel noise performance, the median absolute deviation (MAD) is computed for each pixel on the array of pixel values ai corresponding to multiple exposures (the 0th axis of the datacube of slope images), where the MAD is defined as the median (med) of |a−med(a)|/c. The normalisation constant is c ≈ 0.6745. The MAD is used to set the noise threshold, outside of which values are masked from the array a; that is a> med(a) ± nMAD ×  MAD are masked. However, They are not removed since this is only a noise-performance-selection step needed for the subsequent dark detection. Simulations using ground-based dark currents including readout noise and varied cosmic ray (CR) fluences in the Earth-Sun L2 orbit set the optimum value of nMAD at 3.0.

After masking to the MAD-based threshold, the median of a is taken again, and the result is evaluated for detection of the dark current above the S/N given by the two conditions {math}`|\mathrm{med}(a)| \le \mathrm{RMS}/\sqrt{N_\mathrm{fr}}` and {math}`\mathrm{RMS}/\sqrt{N_\mathrm{fr}} \le 0.3 \times \sqrt{480/N_\mathrm{fr}}`, where RMS is the standard deviation and Nfr is the number of measurements in each pixel meeting its initial threshold; for example, Nfr ≤ 500 in the case of the PV photo-darks. The final median dark currents and their variances comprise the master dark product, along with a DQ flag set for pixels whose dark currents could not be detected to within the two noise conditions. This flag, NODARKDET, is informational and does not necessarily represent an invalid condition. This is because some pixels in H2RGs have such a low dark current that the slopes computed are dominated by the readout noise, and for example, also a floor of weak CR-induced signal not completely compensated by the masking steps – an issue demonstrated with simulations. Strictly speaking, however, such pixels cannot be distinguished from those with sufficiently high noise arising from multiple sources that their dark currents are hidden from detection. Thus, for all flagged pixels the dark current is set to zero and these are excluded from the detector dark-current performance statistics; see Table 1 for the most probable values of the dark current applicable to Q1.
````

## 5.6 Cosmic-Ray Identification

````{admonition} Example text from Euclid: NISP cosmic rays
:class: note

*Reproduced from Euclid Collaboration: Polenta et al. (2025), "Euclid Quick Data Release (Q1). NIR processing and data products", [arXiv:2503.15304](https://doi.org/10.48550/arXiv.2503.15304), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

**3.1.7.1. Single-frame photometric mode.**

The first step in the identification of CRs in the NISP photometric data is performed by the module NIR_CrRejectionSingleFrame. This module utilises the LAcosmic2 algorithm (van Dokkum 2001) to locate CRs in single photometric exposures using Laplacian edge detection. The algorithm has several input parameters that strongly depend on the instrument and conditions of the observations. A balance has to be found between identifying a large fraction of the CRs without masking real (point) sources. This is especially important for NISP, which strongly undersamples the PSF (Euclid Collaboration: Jahnke et al. 2025). For each of the three NISP filters, the optimal set of input parameters were found based on simulated images, for which the ground truth is known. In this tuning, the priority was to avoid masking real objects, since CRs not identified in this module can be picked up by the multi-frame CR-rejection module (see below). The efficiency of this module is higher for the redder filter HE compared to the bluest filter YE, since undersampling is stronger in the bluer passband.

Pixels identified by LAcosmic as CRs are masked by adding the flags COSMIC (bit 16) and INVALID (bit 0) to the DQ layer. We also mask all eight neighbouring pixels to account for interpixel capacitance (IPC) that spreads charge from a pixel to its neighbors, which then also need to be masked in the case of a CR. For details on IPC, we refer to Le Graët et al. (2022) and Euclid Collaboration: Jahnke et al. (2025).

**3.1.7.2. Multi-frame photometric mode.**

This is the second step in identifying and flagging CRs, using information from all available dithers simultaneously and implemented in the NIR_CrRejectionMultiFrame module. This task requires precise astrometric calibration (see Sect. 3.2.7). Each position in the sky, corresponding to a pixel on the array, is observed multiple times with n dithers. In the EWS, the ROS dither pattern results in fractions of pixels observed 1, 2, 3, and 4 times of 1%, 8%, 40%, and 42%, respectively (see Table 2 in Euclid Collaboration: Scaramella et al. 2022). We used pull-clipping for outlier detection (Copin 2022) that is robust on such small samples (n ≥ 3 unflagged data points). More specifically, following a trade-off analysis based on realistic simulations (Euclid Collaboration: Serrano et al. 2024), we rejected pixels with the pull pi ≥ 10, where pi is defined as

```{math}
:label: euclid-nisp-eq3

p_i = \frac{x_i - \bar{x}_i}{\sqrt{\sigma_i^2 + \bar{\sigma}_i^2}}
```

Here, xi and σi are the respective flux and measurement error of dither i, and {math}`\bar{x}_i` and {math}`\bar{\sigma}_i` are the inverse-variance weighted average and the associated sample error without point i. We note that for the monthly visits of Euclid’s self-calibration field (see Sect. 4.2.3 in Euclid Collaboration: Mellier et al. 2025) near the North Ecliptic Pole (NEP) we have coverage of up to n = 76, and that for n < 3 we fall back to the single-frame mode explained above.

To counter false positive CR detections (e.g. stars erroneously identified as CRs) we computed the sum of pixel values in the 3 × 3 pixel region around the candidate CR. The same sum was computed for the other dithers. The CR-detection was rejected if the sums agree to within 3%. All detected CRs were flagged in the DQ layer. For testing purposes (or in the case of a malfunction in specific scenarios) standard sigma-clipping or Grubb’s test can be enabled in NIR PF. This estimates the z-score,

```{math}
:label: euclid-nisp-eq4

z_i = \frac{x_i - \bar{x}}{s}
```

where {math}`\bar{x}` and s are the sample mean and standard deviation, respectively. For small n, this method has the disadvantages that it includes outliers in the sample estimates, and that it does not fully account for individual measurement errors σi. A comparison with the pull-statistic for small sample sizes is given in Copin (2022). Since n ≤ 4 for the EWS, we adopted the pull clipping as default statistic for the NIR PF.
````

## 5.7 Gain and gain stability

**Source:** RDOCs. ditto

## 5.8 1/f bias correction

**Source:** RDOCs. ditto

## 5.9 Flat field

**Source:** RDOCs. ditto

## 5.10 Photometry

**Source:** RDOCs. Focus on L2; refer to later section for L3?

## 5.11.1 Zeropoints and Zeropoint stability

**Source:** RDOCs. ditto

## 5.11.2 Ice: models, corrections, remaining SED-dependent uncertainties

**Source:** RTB. Highlight decontaminations that happened over the course of observations included in this data release; plot time-series of ice deposition…

## 5.12 Instrument geometric distortions and stability

**Source:** RDOCs. ditto

## 5.13 PSF characterization and stability

**Source:** RDOCs. This section would be for L2 PSFs, pointing to a later section for the co-add PSFs.

## 5.14 Astrometry

**Source:** RDOCs. ditto

## 5.14.1 Absolute Astrometry

**Source:** RDOCs. This section focuses on L2; need to highlight differences for L3

## 5.14.2 Relative Astrometry

**Source:** RDOCs. This section focuses on L2; need to highlight differences for L4

## 5.15 Brighter-fatter effect

**Source:** RDOCs.

````{admonition} Example text from Euclid: VIS brighter-fatter effect
:class: note

*Reproduced from Euclid Collaboration: McCracken et al. (2026), "Euclid Quick Data Release (Q1) – II. VIS processing and data products", A&A, 711, A2, [doi:10.1051/0004-6361/202554594](https://doi.org/10.1051/0004-6361/202554594), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

The BFE refers to the redistribution of charge within pixels as charge is accumulated (Downing et al. 2006; Antilogus et al. 2014). This is a consequence of the electric field of the charge; as more charge accumulates, pixel boundaries change. This effect depends nonlinearly on flux, and therefore causes the PSF to become larger for brighter stars. A secondary consequence of the BFE is a slower-than-Poisson increase in variance with flux.

To correct this effect, we compute a kernel to apply to the data. This kernel represents the deflection field of the accumulated charge for one pixel, and is represented by an 11 × 11 matrix. Simulations have shown these dimensions give the correction for the BFE. The BFE kernel is the solution of the Poisson equation with the pixel covariance as the source term. To compute the pixel covariance, a series of pairs of flat-fields at high fluence with the same pointing are subtracted from each other, to remove the non-uniform illumination resulting from the calibration lamp profile. Since the shutter is open during flat-field exposures, the flat-field is immediately followed by a short science exposure to enable the masking of stars and other objects that are present in the flats. Finally, we mask all CRs and any bad pixels. The pixel covariance must be adjusted using a zero correction, which involves modifying the central pixel value of the covariance matrix to ensure that the total sum of all covariance values equals zero. This adjustment is performed before solving the Poisson equation to compute the BFE kernel.

This BFE kernel is used to correct the science image using an iterative flux-conserving approach. First, the image is converted to electrons and flagged pixels are ‘inpainted’ (where their values are replaced by nearby good pixels) to exclude them from the correction. The image is then convolved with the kernel to compute a ‘deflection potential’. At each iteration, the algorithm calculates the required pixel-to-pixel flux transfers from the gradients of this potential. Flux is conserved by ensuring that any charge redistributed from one pixel is added to nearby pixels according to the kernel’s deflection field. This creates a correction image that is then added to the original to redistribute charge based on the BFE kernel. This procedure is repeated until the absolute difference between successive iterations drops below 10−6. The image is the converted back to ADUs and inpainted pixels restored to their original values.

The photometric impact of the BFE correction on stars is shown in Fig. 5. Without BFE correction, the PSF core is broader for brighter stars. Consequently, in an aperture smaller than the scale at which the BFE is important, the flux ratio of identical stars in short and nominal exposures is smaller for brighter stars, as shown on the top panel of Fig. 5 from the ratio of the flux of the brightest pixel. This effect is visible mainly for stars with IE < 19, and is not significant after BFE correction (bottom panel).

*Fig. 5 of the source paper (not reproduced):* Effect of BFE correction on the difference of the surface brightness of the brightest pixel of stars in nominal versus short exposures as a function of VIS magnitude in an aperture of 13 pixels, or 1.″3 diameter.

Figure 6 shows the impact of BFE correction on the PSF model derived with PSFex (Bertin 2011 see also Sect. 4.3) in terms of the Gaussian FWHM (left panel) and size R2 in all quadrants before and after correction. (For a complete definition of the quantities used, see Appendix A). The measured R2 is compared to the reference value {math}`R^2_\mathrm{ref}` for a Gaussian with FWHM = 0.20″.

*Fig. 6 of the source paper (not reproduced):* Effect of BFE correction on the PSF model, as quantified from the FWHM (left panel) and R2/Rref2 (right panel), which is the squared radius relative to that of a Gaussian profile with a FWHM of 0.″2. There is one red marker per quadrant. The black markers and error bars indicate the mean and standard deviation across all quadrants.

While this correction decreases the FWHM, it leaves the PSF size unchanged on average, since this metric provides information on the PSF at scales larger than the BFE correction. However, the correction still reduces the spatial variations on the FPA (the standard deviation across all quadrants is smaller).
````

## 5.16 Intrapixel Capacitance

**Source:** RDOCs.

## 5.17 Persistence

**Source:** RDOCs.

## 5.18 Astrometric and photometric calibration

The second stage, where quadrants are processed together. The paper describes
gain equalisation, a simplified point-spread-function model for monitoring,
a large-scale illumination correction, astrometric calibration against Gaia,
and photometric calibration, including how throughput changes over time were
handled.

**Roman equivalent:** TBD. Reference catalogues used, zero-point strategy,
and the version of any calibration reference files, pinned to a tagged
calibration release (for example, `bp-27a`).
