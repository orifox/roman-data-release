# 5.4 Non-Linear Correction

````{admonition} Example text from Euclid: NISP non-linearity
:class: note

*Reproduced from Euclid Collaboration: Polenta et al. (2025), "Euclid Quick Data Release (Q1). NIR processing and data products", [arXiv:2503.15304](https://doi.org/10.48550/arXiv.2503.15304), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

Non-linearity in H2RGs is primarily caused by the behaviour of the photodiode’s junction capacitance. As charge accumulates in a pixel during exposure, the depletion region of the photodiode narrows, leading to an increase in junction capacitance. This change affects the conversion of accumulated charge to voltage, causing deviations from the ideal linear response. Additionally, other components in the signal chain, such as the source follower in the readout integrated circuit and the ADC process, can introduce further non-linearities. These combined effects result in a non-linear relationship between the incident photon flux and the measured signal, with the non-linearity becoming increasingly pronounced as the flux level rises, independent of wavelength (see e.g. Plazas et al. 2017; Barbier et al. 2018).

We calibrated the pixel-level response and non-linearity with custom-designed LEDs (Euclid Collaboration: Hormuth et al. 2025; Euclid Collaboration: Jahnke et al. 2025). Each LED has a narrow emission spectrum and can illuminate the FPA with varying fluxes. For the non-linearity calibration (conducted on the ground and in flight), two key measurements are required: the fitted slope image (Kubik et al. 2016) that represents the non-linear response, and the individual MACC group images that are used to approximate the linear flux, FLinear (e.g. Vacca et al. 2004). For both photometry and spectroscopy readout modes, MACC(4,16,4) and MACC(15,16,11), respectively, five fluence levels were selected to span the dynamic range expected for each mode, accounting for their different exposure times. These measurements were then combined to derive the non-linearity calibration coefficients for each pixel.

The linear flux estimate, FLinear, is derived by modelling the pixel response across various fluence levels using orthonormal polynomials. The first term of this model provides an approximation of the linear flux, as fully described in Euclid Collaboration: Kubik et al. (2026). Orthonormal polynomials were chosen for their practical advantages, including computational efficiency and manageable memory usage, and this approach has been successfully adopted for correcting H2RGs at several facilities. In the long term, more sophisticated models, such as a principal component analysis (PCA), will be evaluated to enhance non-linearity corrections (see also Rauscher et al. 2019). Before the fitting, the ramps are corrected for reference pixels using sliding windows of four pixels. To optimise memory and CPU usage, the ramps, observed multiple times at each fluence level, are averaged for each run. Additionally, frames exceeding 60 000 ADU are rejected to avoid saturation effects.

Following the pre-processing, the non-linearity per pixel is expressed as a fourth-degree polynomial relationship between the estimate of the linearised flux, FLinear, and the measured non-linear flux, FNon-linear, expressed as

```{math}

F_\mathrm{Linear} = \sum_{k=0,4} a_k \, F_\mathrm{Non\text{-}linear}^{k} \tag{1}
```

The degree of the polynomial is constrained by the number of available fitting flux levels. For consistency, we enforced the linear flux to be zero for a zero non-linear flux.

Fitting these polynomials to the thermal vacuum (TV1) calibration data, we measured the non-linearity coefficients and their covariances, which were subsequently used in the NIR PF non-linearity correction for Q1. The validity range is dictated by the dynamic range covered by the LED fluences (1000 ADU to 30 000 ADU), below which non-linearity effects are minimal and above which corrections are applied by linearly extending the polynomial fit rather than using the higher-order coefficients. It should be noted that the values above already include baseline removal. Considering the baseline level shown in Fig. 2, we expect saturation to occur between 40 000 and 50 000 ADU for most of the pixels. For the first data release, DR1, expected in October 2026, additional fluences from PV and calibration observations are expected to enlarge the validity range. The correction step also incorporates gain conversion, and a flagging of pixels where the fit is unreliable. In addition, pixels whose signal exceeds the saturation threshold defined from the ground-test campaign are identified by this PE and flagged using both SATURATION and INVALID bits.
````
