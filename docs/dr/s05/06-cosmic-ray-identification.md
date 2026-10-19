# 5.6 Cosmic-Ray Identification

````{admonition} Example text from Euclid: NISP cosmic rays
:class: note

*Reproduced from Euclid Collaboration: Polenta et al. (2025), "Euclid Quick Data Release (Q1). NIR processing and data products", [arXiv:2503.15304](https://doi.org/10.48550/arXiv.2503.15304), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

**3.1.7.1. Single-frame photometric mode.**

The first step in the identification of CRs in the NISP photometric data is performed by the module NIR_CrRejectionSingleFrame. This module utilises the LAcosmic2 algorithm (van Dokkum 2001) to locate CRs in single photometric exposures using Laplacian edge detection. The algorithm has several input parameters that strongly depend on the instrument and conditions of the observations. A balance has to be found between identifying a large fraction of the CRs without masking real (point) sources. This is especially important for NISP, which strongly undersamples the PSF (Euclid Collaboration: Jahnke et al. 2025). For each of the three NISP filters, the optimal set of input parameters were found based on simulated images, for which the ground truth is known. In this tuning, the priority was to avoid masking real objects, since CRs not identified in this module can be picked up by the multi-frame CR-rejection module (see below). The efficiency of this module is higher for the redder filter HE compared to the bluest filter YE, since undersampling is stronger in the bluer passband.

Pixels identified by LAcosmic as CRs are masked by adding the flags COSMIC (bit 16) and INVALID (bit 0) to the DQ layer. We also mask all eight neighbouring pixels to account for interpixel capacitance (IPC) that spreads charge from a pixel to its neighbors, which then also need to be masked in the case of a CR. For details on IPC, we refer to Le Graët et al. (2022) and Euclid Collaboration: Jahnke et al. (2025).

**3.1.7.2. Multi-frame photometric mode.**

This is the second step in identifying and flagging CRs, using information from all available dithers simultaneously and implemented in the NIR_CrRejectionMultiFrame module. This task requires precise astrometric calibration (see Sect. 3.2.7). Each position in the sky, corresponding to a pixel on the array, is observed multiple times with n dithers. In the EWS, the ROS dither pattern results in fractions of pixels observed 1, 2, 3, and 4 times of 1%, 8%, 40%, and 42%, respectively (see Table 2 in Euclid Collaboration: Scaramella et al. 2022). We used pull-clipping for outlier detection (Copin 2022) that is robust on such small samples (n ≥ 3 unflagged data points). More specifically, following a trade-off analysis based on realistic simulations (Euclid Collaboration: Serrano et al. 2024), we rejected pixels with the pull pi ≥ 10, where pi is defined as

```{math}

p_i = \frac{x_i - \bar{x}_i}{\sqrt{\sigma_i^2 + \bar{\sigma}_i^2}} \tag{3}
```

Here, xi and σi are the respective flux and measurement error of dither i, and {math}`\bar{x}_i` and {math}`\bar{\sigma}_i` are the inverse-variance weighted average and the associated sample error without point i. We note that for the monthly visits of Euclid’s self-calibration field (see Sect. 4.2.3 in Euclid Collaboration: Mellier et al. 2025) near the North Ecliptic Pole (NEP) we have coverage of up to n = 76, and that for n < 3 we fall back to the single-frame mode explained above.

To counter false positive CR detections (e.g. stars erroneously identified as CRs) we computed the sum of pixel values in the 3 × 3 pixel region around the candidate CR. The same sum was computed for the other dithers. The CR-detection was rejected if the sums agree to within 3%. All detected CRs were flagged in the DQ layer. For testing purposes (or in the case of a malfunction in specific scenarios) standard sigma-clipping or Grubb’s test can be enabled in NIR PF. This estimates the z-score,

```{math}

z_i = \frac{x_i - \bar{x}}{s} \tag{4}
```

where {math}`\bar{x}` and s are the sample mean and standard deviation, respectively. For small n, this method has the disadvantages that it includes outliers in the sample estimates, and that it does not fully account for individual measurement errors σi. A comparison with the pull-statistic for small sample sizes is given in Copin (2022). Since n ≤ 4 for the EWS, we adopted the pull clipping as default statistic for the NIR PF.
````
