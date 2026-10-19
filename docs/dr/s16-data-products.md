# 16. Data Products

## 16.0 Overview

**Source:** RDOCs.

````{admonition} Example text from Euclid: NISP data products
:class: note

*Reproduced from Euclid Collaboration: Polenta et al. (2025), "Euclid Quick Data Release (Q1). NIR processing and data products", [arXiv:2503.15304](https://doi.org/10.48550/arXiv.2503.15304), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

The Euclid Common Data Model is an XML schema (XSD) that defines all Euclid DPs, along with a dictionary of all data types, interfaces, and FITS file formats. A data product is therefore represented as an XML file containing the names of data files and their corresponding metadata, which can be stored in and retrieved from the EAS.

A detailed description of the metadata for all NIR DPs is available in the Data Product Description Document (DPDD, Euclid Collaboration 2025). The DPs produced by NIR PF for Q1 are the DpdNirCalibratedFrame and the corresponding DpdNirCalibratedFrameCatalog.
````

## 16.1 L1 Uncalibrated Exposures

**Source:** RDOCs. Mostly won't change from data release to data release

## 16.2 L2 Exposure Level Data Products

**Source:** RDOCs.

````{admonition} Example text from Euclid: NISP calibrated frames
:class: note

*Reproduced from Euclid Collaboration: Polenta et al. (2025), "Euclid Quick Data Release (Q1). NIR processing and data products", [arXiv:2503.15304](https://doi.org/10.48550/arXiv.2503.15304), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

The DpdNirCalibratedFrame is a fully astrometrically and photometrically calibrated exposure, obtained by applying calibration products and corrections to each individual LE1 photometric image. Image data are stored as FITS files referenced in the DP and are organised into three main sections: DataStorage; BackgroundStorage; and PsfStorage.

DataStorage references the main MEF file that contains the calibrated image data. This file consists of a total of 49 header data units (HDUs). The first HDU or primary header stores the main metadata keywords of the observation sequence that acquired the exposure. For each detector, three HDUs are provided: (i) SCI, containing the scientific image data in electrons; (ii) RMS with the associated root mean square; and (iii) DQ with the data-quality mask for each pixel (Appendix B). The header of each SCI HDU contains the detector WCS and the zero point.

BackgroundStorage references the FITS file of the background image, computed during the background-estimation step (Sect. 3.2.3). Its file structure mirrors that of the scientific image described above. PsfStorage section of the DP refers to two FITS files: the PSF model and the corresponding PSF image (Sect. 3.2.5). Another key metadata tag is QualityParams, which contains a structure to store image-quality parameters and statistics. They are used as input for the DQC pipeline (Sect. 3.3) and are computed by specific tasks in NIR PF.
````

## 16.3 L2 Exposure Level Ancillary products

**Source:** RDOCs. Currently this is the WCS. But in the future might include diffraction spike masks, background model, de-striping model, …

## 16.4 L3 Co-add Data Products

**Source:** RDOCs.

## 16.5 L4 Static Catalogs

**Source:** RDOCs.

````{admonition} Example text from Euclid: NISP source catalogues
:class: note

*Reproduced from Euclid Collaboration: Polenta et al. (2025), "Euclid Quick Data Release (Q1). NIR processing and data products", [arXiv:2503.15304](https://doi.org/10.48550/arXiv.2503.15304), under CC BY 4.0. It describes Euclid, not Roman; section, figure, and equation numbers refer to that paper.*

The DpdNirCalibratedFrameCatalog is the source catalogue extracted from the calibrated exposure, as described in Sect. 3.2.10. Its global metadata structure mirrors that of DpdNirCalibratedFrame. The MEF catalogue produced is referenced under the DataStorage tag of the DP and is structured into 17 HDUs: a primary header followed by a data HDU for each detector. The data HDUs store the source catalogue tables, which include coordinates, size, ellipticity, fluxes, and magnitudes extracted using three different methods by SourceExtractor: APER, AUTO, and PSF, as described in Sect. 3.2.10.
````

## 16.6 L4 Static Catalog Ancillary Products

**Source:** RDOCs. Currently this is segmentation maps and source-injection input/output. This may involve to include other items.

## 16.7 L4 Time-Series Catalogs

**Source:** RDOCs.

## 16.8 Survey-level products

**Source:** RDOCs. To be defined. Could include healpix encoded information on survey depths (computed from the weight maps, but compact and queriable), sky backgrounds. Could include survey footprints.

