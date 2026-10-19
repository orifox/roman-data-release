# 5.9 Brighter-fatter effect

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
