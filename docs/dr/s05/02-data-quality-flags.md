# 5.2 Data Quality Flags, instabilities not flagged

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
