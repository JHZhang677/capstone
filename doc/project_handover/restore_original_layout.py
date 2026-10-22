#!/usr/bin/env python3
"""Restore preserved code/data to original relative paths without altering the repository.

Input: source_to_repository_manifest.csv and files checked out by Git LFS.
Output: --output directory containing the original project code/data layout.
Run: python3 doc/project_handover/restore_original_layout.py --output /path/to/restored
Dependencies: Python standard library. Existing different files are never overwritten.
Historical absolute paths in notebooks must still be configured before execution.
"""
import argparse
import csv
import hashlib
import shutil
from pathlib import Path


def sha256(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def inside(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root):
        raise ValueError('Unsafe path in manifest: ' + relative)
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    repo = Path(__file__).resolve().parents[2]
    output = args.output.expanduser().resolve()
    if output == repo or repo.is_relative_to(output):
        parser.error('Choose a separate output directory, not the repository or its parent.')
    with Path(__file__).with_name('source_to_repository_manifest.csv').open(newline='') as stream:
        rows = list(csv.DictReader(stream))
    checked = set()
    # Complete preflight before copying, including absence of Git LFS pointer placeholders.
    for row in rows:
        source = inside(repo, row['repository_path'])
        target = inside(output, row['source_relative_path'])
        if source not in checked:
            if not source.is_file() or sha256(source) != row['sha256']:
                raise SystemExit(f'Source missing or checksum mismatch: {source}. Run git lfs pull first.')
            checked.add(source)
        if target.exists() and (not target.is_file() or sha256(target) != row['sha256']):
            raise SystemExit(f'Refusing to replace different existing file: {target}')
    count = 0
    for row in rows:
        source = inside(repo, row['repository_path'])
        target = inside(output, row['source_relative_path'])
        if target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        count += 1
    print(f'Restored {count} files to {output}. Existing matching files were retained.')
    print('Review notebook configuration and historical absolute paths before running analyses.')


if __name__ == '__main__':
    main()
