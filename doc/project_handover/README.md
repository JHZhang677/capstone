# Code and dataset handover

This handover preserves the code and data held in the consolidated Haemograph project, including earlier experiments. The report-corrected analysis is the entry point for final results. Historical notebooks remain available to explain development; their saved claims and outputs are not automatically the final project conclusions.

## Where to start

| Folder | Contents |
|---|---|
| [`final_code/report_analysis`](../../final_code/report_analysis) | Corrected report calculations, source notebook snapshots, supporting result tables and final figures |
| [`example_code/analysis_version_history`](../../example_code/analysis_version_history) | All discovered code snapshots, including distinct checkpoint versions and external reference implementations |
| [`data/project_datasets`](../../data/project_datasets) | Source datasets, generated synthetic data, saved results and dataset documentation |
| This folder | File catalogue, version history, schema index, source mapping and restoration instructions |

## Names and versions

Data folders identify the material or analysis purpose. The Armstrong workbook aliases use the source catalogue: `arm_mar19`, `arm_apr18`, `arm_may19`, etc. `arm_aug18_prefix` and `arm_aug18_suffix` identify two different supplied workbooks; they must not be merged on their month alone. The two aspirin workbooks remain separately named. These labels are workbook identifiers, not confirmed donor IDs.

Code filenames combine a descriptive name with the first ten characters of its SHA-256 hash. The hash distinguishes snapshots; it is not a chronological version number. Explicit `v2` or `earlier` labels retain documented version information. Same code with different stored outputs can have different file hashes but the same `source_code_sha256` in the code catalogue.

Identical files are stored once. Every original path still appears in the source mapping and points to that copy. A different file is never removed merely because its name is similar. Native instrument files and some source archive containers are preserved, including their original metadata. The data archive therefore includes more than the final study's analysis cohort.

## Running the code

1. Install Git LFS and run `git lfs pull` after cloning this repository. A ZIP downloaded from the GitHub page may not contain the large-file contents.
2. Read the current analysis README for the final report workflow.
3. To work on an older version, reconstruct the original relative directory layout with:

   ```bash
   python3 doc/project_handover/restore_original_layout.py --output ~/Documents/haemograph_restored
   ```

4. Inspect the notebook's configuration cells before running it. The restoration preserves relative source names; historical absolute paths and old Desktop folder locations still need updating. Imports and literal file references are listed in the code catalogue. These references are extracted from code, not a guaranteed complete dependency graph.
5. Use a separate output directory for experiments. Keep original input files unchanged. No full notebook or model-fitting rerun was performed for this upload preparation.

The restoration script restores only the mapped code/data scope, not the excluded presentations, report documents or literature collection. It verifies source hashes and refuses to overwrite different destination files.

## Exact catalogues

- [Code version catalogue](code_version_catalogue.csv): source path, descriptive repository path, version hashes, code-cell count, imports, referenced filenames and introductory source text.
- [Analysis run order](RUN_ORDER.md): principal inputs, stages and version choices.
- [Readable code guide](CODE_GUIDE.md): grouped versions and their roles.
- [Dataset guide](DATASET_GUIDE.md): materials, roles, naming and important distinctions.
- [Dataset schema index](dataset_schema_index.csv): CSV headers and workbook sheet names as stored; units are not invented.
- [Source mapping](source_to_repository_manifest.csv): original location, repository location, byte size, SHA-256 and duplicate status for every included source file.
- [Excluded files](excluded_files.csv): temporary files, embedded Git metadata and material outside code/data scope.

## Interpretation and attribution

Measured Armstrong blood records have no independently observed clot-time labels. Synthetic reference events are programmed model events. Earlier gel, polymer, collagen, xanthan and other reference materials must not be described as patient blood data.

Upstream software, source README files, licences and dataset briefs are retained in the data collections and are discoverable through the source mapping. Their presence does not make that work a team contribution. Where source documentation does not establish a licence, this handover does not invent one. Publication/source links recorded in the supplied documentation have not all been independently revalidated during packaging.

## Storage

All files under `data/project_datasets` except Markdown documentation use Git LFS. This keeps large datasets and instrument files out of ordinary Git objects. Their upload uses the repository owner's LFS storage/bandwidth allowance. Original notebooks and the small corrected result package use ordinary Git.
