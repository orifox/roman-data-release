# 5.12 Photometry

**Source:** RDOCs. Focus on L2; refer to later section for L3?

````{admonition} Example text from Euclid: NISP absolute flux calibration
:class: note

*Reproduced from Euclid Collaboration: Polenta et al. (2025), "Euclid Quick Data Release (Q1). NIR processing and data products", [arXiv:2503.15304](https://doi.org/10.48550/arXiv.2503.15304), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

For Euclid’s cosmology science aims, we have an accuracy goal of 5% on the absolute flux calibration of NISP. This comes easily, since we calibrate against spectrophotometric WDs in HST CALSPEC, which have an estimated accuracy of 1% (Bohlin et al. 2014, 2017, 2020).

For NISP imaging we could use the all-sky faint WDs network (Narayan et al. 2019; Bohlin et al. 2024) in CALSPEC. However, none of them are visible in Euclid’s continuous viewing zones that extend 2.°5 from the ecliptic poles. We therefore established a faint WD, WDJ175318.65+644502.15 (Gaia SourceID 1440758225532172032) in the self-calibration field near the NEP. This was tied to CALSPEC using photometric and spectroscopic HST observations with WFC3/IR and STIS (programme IDs 16702 and 17442, Appleton et al. 2021; Deustua et al. 2023). This star is stable to within 1% over timescales ranging from 100 seconds to several years. With HE = 18.36, it is faint enough for NISP, which saturates at around 16.5 AB mag.

Flux calibration is established by comparing the observed flux Fobs in instrumental units (e− s−1) with the true flux Ftrue in μJy. The true flux integrated over a passband is obtained by convolving the WD’s model spectral flux density Sν with the passbands’ spectral response T(ν),

```{math}

F_\mathrm{true} = \frac{\int \dfrac{T(\nu)\, S_\nu}{\nu} \, \mathrm{d}\nu}{\int \dfrac{T(\nu)}{\nu} \, \mathrm{d}\nu} \tag{12}
```

Here, ν is the frequency, and the spectral response T(ν) for passbands YE, JE, and HE is taken from Euclid Collaboration: Schirmer et al. (2022).

Fobs is measured with SourceExtractor within a fixed aperture of diameter 6 pixels. We use our PSF model (Sect. 3.2.5) to compute the fraction of the flux that falls outside this aperture, and correct Fobs accordingly. Finally, the absolute flux calibration factor, or IS in NIR PF, is defined as

```{math}

\mathrm{IS} = \frac{F_\mathrm{true}\,[\mu\mathrm{Jy}]}{F_\mathrm{obs}\,[\mathrm{e}^{-}\,\mathrm{s}^{-1}]} \tag{13}
```

Flux calibration of the Q1 data is based on the self-calibration observations – that contain the WD – in June 2024 (see Sect. 5.2). Figure 15 presents the individual measurements of the WD in two NISP detectors, together with the corresponding IS. As can be seen, the 3σ uncertainty of the IS is well within the required 5% boundary.
````
