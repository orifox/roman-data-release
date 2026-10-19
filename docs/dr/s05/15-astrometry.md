# 5.15 Astrometry

**Source:** RDOCs. ditto

````{admonition} Example text from Euclid: NISP astrometric calibration
:class: note

*Reproduced from Euclid Collaboration: Polenta et al. (2025), "Euclid Quick Data Release (Q1). NIR processing and data products", [arXiv:2503.15304](https://doi.org/10.48550/arXiv.2503.15304), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

Astrometric calibration accounts for geometric distortions from instrument optics and focal-plane metrology, which define detector positions and orientations. For each pointing and band, this is done by minimising positional differences between sources detected in dithered exposures and those in an external reference catalogue. Currently, Gaia DR3 (Gaia Collaboration 2023) is preferred over the VIS catalogue (Euclid Collaboration: McCracken et al. 2026), since its bright stars – saturated in VIS – remain unsaturated in NISP, providing more reliable reference sources.

Astrometric calibration is performed using SCAMP (Bertin 2006), which operates on catalogues rather than images. This requires both a reference catalogue and source catalogues for the dithered exposures. Source catalogues are provided by SourceExtractor with a configuration optimised for astrometric calibration. The astrometric solution – modelled in NIR PF as a 3rd-order polynomial per detector – is derived by minimising the χ2-sum of positional differences between overlapping detections.

In some cases, particularly when too few stars are available in common with the external catalogue for certain detectors, SCAMP may fail to converge unless its parameters are fine tuned. However, the optimal parameters can vary across fields with different stellar densities. To address this, we implemented an astrometric pre-solution, that is an initial model for geometric distortion along with the relative positions and orientations of the detectors. This pre-solution helps reduce sensitivity to the initial matching radius with the external catalogue. If the radius is too large, it can cause false matches. If it is too small, it may result in no matches, especially near the field edges, where distortion can shift source positions by up to 10″. As a result, the robustness of the distortion-model fitting is significantly improved.

The astrometric pre-solution is created by the distortion-model pipeline in NIR PF, where SCAMP is run on the 76 dithered exposures, per band, of the self-calibration field. SCAMP, following the polynomial PV3 convention (Calabretta & Greisen 2002), applies the distortion polynomial to the world coordinates. Therefore, when transferring the pre-solution to a different dither, adjusting for the different dither’s rotation on the sky is required. This is is done by first converting the pre-solution to the Simple Imaging Polynomial (SIP) convention (Shupe et al. 2005), where the distortion is instead applied to pixel coordinates. It is then translated back to the PV convention using the dither’s centre and rotation, as encoded in the WCS keywords. Currently, these transformations use polynomial fitting functions. An analytic conversion method (see e.g. Shupe et al. 2012) will be used for the next data releases.
````
