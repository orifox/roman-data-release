# 10.9 Shape parameter color-dependent systematics
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

````{admonition} Example text from Euclid: VIS galaxy counts
:class: note

*Reproduced from Euclid Collaboration: McCracken et al. (2026), "Euclid Quick Data Release (Q1) – II. VIS processing and data products", A&A, 711, A2, [doi:10.1051/0004-6361/202554594](https://doi.org/10.1051/0004-6361/202554594), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

Finally, Fig. 22 shows the galaxy counts for the four different sky patches, computed using the mag_auto magnitudes extracted from the stacked images. Counts are computed in half-magnitude bins normalised to per square degree. Galaxies were selected from the catalogues by imposing a size (≥1.25 times the PSF size) and signal-to-noise (≥10) requirement to mimic the object selection for cosmic shear measurements.

*Fig. 22 of the source paper (not reproduced):* Mean magnitude histogram of galaxy counts per square degree from VIS stacks (a single pointing containing four nominal and two short exposures). The mean is given separately for each of the sky patches of the Q1 release, and each is an average of around 40 stacks. The bin width is 0.5. Galaxies were selected according to a minimum size (≥1.25 times the PSF size) and signal-to-noise (≥10). Each VIS stack covers approximately 0.6208 deg2. The COSMOS galaxy counts are based on estimated IE magnitudes, by fitting SEDs over all the COSMOS bands.

The Dark Cloud region has lower counts because of heavy dust obscuration. In the remaining three Euclid Deep Fields (North, South, and Fornax), the galaxy counts are in excellent agreement, with the turnover magnitudes differing slightly. The turn-off is at fainter magnitudes where the zodiacal sky background is the lowest, or the furthest away from the ecliptic plane. EDF-N is at the north ecliptic pole, and the ecliptic latitude is lower for EDF-S and EDF-F.

The cumulative galaxy counts at IE = 24.5 are around 30 arcmin−2, meeting the general Euclid requirement. Our catalogues can be considered complete here, given that the counts turn over at much fainter magnitudes. We also compare with counts computed using a special version of the COSMOS2020 catalogue (Weaver et al. 2022) where the IE flux of each source has been computed from the best-fitting SED following the methods outlined in Saito et al. (2020). The agreement is excellent, especially given that our area computation does not account for area lost by bright stars or image artefacts.

We note that in the stacked images (whether by VIS PF or by the downstream MER PF), the survey depth varies across the image, with the depth variation dominated by the number of nominal exposures. The bulk of the wide survey consists of pointings with three or four nominal exposures. Analysis of the EDF-N field catalogues shows that the turnover point for the three- and four-image stack depths differs by ∼0.2 mag, and the EDF-N counts in Fig. 22 lies between the three- and four-image stack curves. This same behaviour has been observed in shallower ecliptic latitudes with more zodiacal light than in EDF-N.
````

````{admonition} Example text from Euclid: VIS Q1 image selection
:class: note

*Reproduced from Euclid Collaboration: McCracken et al. (2026), "Euclid Quick Data Release (Q1) – II. VIS processing and data products", A&A, 711, A2, [doi:10.1051/0004-6361/202554594](https://doi.org/10.1051/0004-6361/202554594), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

The Q1 release includes 852 VIS images in four fields: the Euclid Deep Field North (EDF-N), Euclid Deep Field South (EDF-S), Euclid Deep Field Fornax (EDF-F) and single pointing in the Lynds Dark Nebula LDN1641 (“Dark Cloud”, see Euclid Collaboration: Aussel et al. 2026). The Q1 data release contains only data at the depth of the EWS, except for the Dark Cloud, which is deeper.

Applying the data-quality control flags described in Sect. 6 to the Q1 VIS data, we rejected 16 exposures (1.9%). An exposure is discarded if any of the following conditions are met: (i) one of the three criteria (spread_peak, score, or astrometric residual) is met, (ii) all quadrants are masked by the CR_REGION flag, or (iii) the zero-point cannot be computed. Figure 18 shows the distribution of Q1 quality control flags, with the dotted line indicating the threshold above which an image is considered potentially unusable. The effect of this image rejection procedure can be seen in the coverage map in the bottom right-hand panel of in Figure 10 in Euclid Collaboration: Aussel et al. (2026) where shallower depths are a consequence of the rejection of two images affected by guiding errors.
````
