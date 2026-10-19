# 5.11 Flat field

**Source:** RDOCs. ditto

````{admonition} Example text from Euclid: NISP flat fields
:class: note

*Reproduced from Euclid Collaboration: Polenta et al. (2025), "Euclid Quick Data Release (Q1). NIR processing and data products", [arXiv:2503.15304](https://doi.org/10.48550/arXiv.2503.15304), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

The detectors’ (PRNU) is corrected with flat fields. The ideal PRNU correction would be given by the relative detector response to a uniform illumination from a continuum white-light source. NISP, however, uses LEDs with a near-monochromatic spectral energy distribution (SED) in the near-infrared calibration unit (NI-CU; Euclid Collaboration: Hormuth et al. 2025). NI-CU incorporates five LEDs A to E, ordered by ascending central wavelengths of their spectra (Fig. 8). It illuminates the FPA directly from a small off-axis angle, without passing through a filter (see Section 2.2. of Euclid Collaboration: Hormuth et al. 2025, for more details). The spatial illumination approximately follows a Lambertian cosine profile (Euclid Collaboration: Hormuth et al. 2025).

*Fig. 8 of the source paper (not reproduced):* Comparison of the average QE curves of the 16 NISP detectors, the normalised SEDs of the LEDs, and the YE, JE, and HE passbands (reduced by a factor of 3 in height to avoid cluttering near the top of the plot).

A single LED flat alone thus does not represent an ideal PRNU correction. Therefore, after going through all pre-processing steps listed in Sect. 3.1, we reconstruct filter-dependent flats from the individual LED flats. Denoting the LED flat as FLATLED(x), with x being the pixel position, we compute the filter-dependent flat as

```{math}

\mathrm{FLAT}_\mathrm{Filter}(\mathbf{x}) = \mathrm{FLAT}_\mathrm{LED}(\mathbf{x}) \; P(\mathbf{x}) \tag{5}
```

Here,

```{math}

P(\mathbf{x}) = \frac{\int_{\lambda_1}^{\lambda_2} \mathrm{QE}(\lambda,\mathbf{x}) \; T(\lambda,\mathbf{x}) \; \mathrm{d}\lambda}{\int_{\lambda_3}^{\lambda_4} \mathrm{QE}(\lambda,\mathbf{x}) \; \mathrm{d}\lambda} \tag{6}
```

propagates the LED’s SED across the detector’s QE to reconstruct a broad-band flat from a near-monochromatic light source. T(λ, x) is the filter transmission curve, [λ1, λ2] is the passband of the filter, and [λ3, λ4] is a representative wavelength coverage of the LED spectrum. Notably, due to the LED’ narrow SED, P is independent of the LED spectrum. The mathematical derivation of Eqs. (5) and (6) is given in Appendix A. The data for QE and T(λ) used for the Q1 data processing were measured on the ground (Euclid Collaboration: Schirmer et al. 2022). We note that P is in principle time-dependent over mission-duration due to radiation damage and molecular contamination (Euclid Collaboration: Schirmer et al. 2023), but in the context of the singular Q1 observations this dependence can be neglected.

Of the five LEDs available, only LEDs B to D are used to construct the broad-band flats. Given the mutual wavelength coverages, we use LED B for filter YE, C for JE, and D for HE in Eq. (5). In principle, several LEDs can be combined to reduce uncertainties from the propagator P, but the LED-flat S/N is so high that there is currently no need to do so, mainly because the QE curves are very flat across the passbands, and the S/N in the QE maps themselves is also very high.

Each of the three filter flats is computed from 30 LED flats. In addition to the bad pixels identified by the pre-processing steps, the filter flats require further masking. The first type is vignetting from a baffle near the FPA, which affects the edges of detectors 11, 14, 24, 34, and 44 for LED frames (see Section 2.3. of Euclid Collaboration: Hormuth et al. 2025). Pixels in the vignetting regions are flagged as VIGNET and their values are set to 1.0 in the master flat. The second type of pixels masked are ‘flower’ pixels, which typically present a cross-shaped pattern with a faint core (‘flower centre’) and bright adjacent pixels (‘flower petals’). The same type is found in James Webb Space Telescope (JWST) images, where they are referred to as ‘open’ and ‘adjacent to open’ pixels (Rauscher et al. 2014). Flower pixels are masked as FLOWER and INVALID. We detect these pixels in the flat exposures using a Laplacian kernel. Finally, pixels with values that deviate from the median of the 30 frames by over 50% are flagged as FLATLH, indicating overly low or high values without furtherdiscrimination.

The master flats of the three NISP bands used for the Q1 processing are shown in Fig. 9. The PRNU correction is done by dividing the science frames by the master flat, without prior removal of NI-CU’s Lambertian illumination profile.

*Fig. 9 of the source paper (not reproduced):* Master PRNU flats for Euclid YE, JE, and HE bands used for the processing of Q1 images. The uniform QE is evident from these images.
````
