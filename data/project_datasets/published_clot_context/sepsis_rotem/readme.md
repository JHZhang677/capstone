# Sepsis ROTEM

## Contents

- `Original+ROTEM+Data.zip`: 1,334 whole-blood ROTEM curve images from EXTEM, APTEM, and HEPTEM assays.
- `Rawdata+IgMIVIg.csv`: Clinical variables and ROTEM parameters, including CT, CFT, alpha angle, and MCF, from 26 patients with severe sepsis.
- Individual JPG files: Example ROTEM curves included separately in the source dataset.

## Relevance to This Project

Approximate time-amplitude curves can be extracted from the ROTEM images and used as a secondary validation dataset. Because the curves are raster images rather than numerical signals, digitization introduces pixel and coordinate errors. They should not be the primary data for precise frequency-domain analysis.

## Source

Wand S et al. *IgM-enriched immunoglobulin attenuates systemic endotoxin activity in early severe sepsis: a before-after cohort study*. PLOS ONE, 2016.

- Article DOI: https://doi.org/10.1371/journal.pone.0160907
- Dataset DOI: https://doi.org/10.5061/dryad.6hb49

