# 5.4 Persistence Masking

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

Q_\mathrm{P}(S) = \left(\alpha + \beta S\right)\left(1 - \mathrm{e}^{-S/\gamma}\right) \tag{2}
```

Separate sets of coefficients α,  β,  and γ are needed to describe persistence in photometric and spectroscopic exposures, due to their different exposure times.

This model is effective in the sense that the persistence decay during one exposure is built in the coefficients of the model, but there is no explicit time dependence of the persistence decay. Other shortcomings of this model are that it does not take into account the superposition of persistence from multiple bright exposures, and it does not account for charge trapping, resulting in a potential lack of signal for bright sources on pixels that have previously seen a low-background exposure.

**3.1.5.2. Persistence masking procedure.**

There are two separate steps to mask persistence, presented schematically in Fig. 5. The first step consists of the estimation of persistence charge contributing to any of the NISP scientific exposures. It is a separate pipeline executed before the proper NIR data reduction, in which for each exposure the persistence charge originating from previous images is estimated and stored as a separate product (persistence estimate image). Taking into account the limitations of the effective model, for each photometric exposure only the persistence charge from one previous spectroscopic image is computed. To account for the persistence decay over one dither, the model computes QP using the calibrated set of parameters in Eq. (2) – this is the prediction of the persistence from a spectroscopic image to the JE-band image – and a rescaling factor is applied to estimate the persistence contribution to the HE- and YE-band images taken next in time. We note that for Q1 processing the persistence contribution originating from photometric exposures is not taken into account because, given the Euclid ROS, that would result in masking most of the bright sources. A more accurate model allowing for a correction procedure is being developed. Likewise, the computation and masking of persistence in spectroscopic exposures is deactivated for Q1.

*Fig. 5 of the source paper (not reproduced):* Persistence masking scheme. In the first step, the persistence estimate is calculated using the persistence model applied to prior exposures (source images) for each target exposure. In the second step, the persistence estimates are thresholded to identify and mask pixels where the persistence charge exceeds 2 e− (indicated in red in the right image). Typically, the percentage of masked pixels does not exceed 2%.

The second step is the persistence masking executed during the NIR scientific pipeline. In this task, for each photometric exposure, the corresponding persistence image is analysed. If the persistence charge amplitude in a pixel exceeds 2 e−, then a PERSIST and INVALID flag is raised in the DQ layer of the science exposure (Appendix B). For some pixels the persistence coefficients could not be calibrated, and consequently the persistence charge could not be estimated. In that case, the PERMODFAIL flag is raised in the DQ layer of the corresponding image.
````
