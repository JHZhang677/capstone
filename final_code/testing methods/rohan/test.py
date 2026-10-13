#!/usr/bin/env python3
"""Organize files in a folder into subfolders by file type."""

import shutil
import sys
from pathlib import Path

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff", ".ico", ".heic"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm", ".m4v", ".mpg", ".mpeg"},
    "Audio": {".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a", ".wma", ".opus"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".md", ".tex"},
    "Spreadsheets": {".xls", ".xlsx", ".csv", ".ods", ".tsv"},
    "Presentations": {".ppt", ".pptx", ".odp", ".key"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz", ".bz2", ".xz"},
    "Code": {".py", ".js", ".ts", ".java", ".c", ".cpp", ".h", ".cs", ".go", ".rs",
             ".rb", ".php", ".html", ".css", ".json", ".xml", ".yml", ".yaml", ".sh"},
    "Executables": {".exe", ".msi", ".apk", ".deb", ".dmg", ".app", ".bat"},
    "Fonts": {".ttf", ".otf", ".woff", ".woff2"},
}


def category_for(ext):
    ext = ext.lower()
    for name, exts in CATEGORIES.items():
        if ext in exts:
            return name
    return "Others"


def organize(folder):
    folder = Path(folder).expanduser().resolve()
    if not folder.is_dir():
        print(f"Not a folder: {folder}")
        return

    script = Path(__file__).resolve()
    moved = 0

    for item in list(folder.iterdir()):
        if item.is_dir() or item == script:
            continue
        cat = category_for(item.suffix) if item.suffix else "NoExtension"
        dest_dir = folder / cat
        dest_dir.mkdir(exist_ok=True)

        dest = dest_dir / item.name
        n = 1
        while dest.exists():
            dest = dest_dir / f"{item.stem}_{n}{item.suffix}"
            n += 1

        shutil.move(str(item), str(dest))
        print(f"{item.name} -> {cat}/")
        moved += 1

    print(f"\nDone. {moved} file(s) organized.")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    organize(target)