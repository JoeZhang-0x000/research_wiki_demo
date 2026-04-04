#!/usr/bin/env python3
"""
ingest.py — Scan raw/ and report ingestion status of all source files.

Usage:
    python agent/ingest.py                  # list all files and their status
    python agent/ingest.py --new            # list only files not yet ingested
    python agent/ingest.py --mark <file>    # mark a file as ingested (creates sidecar)

Output:
    Prints a status table to stdout.
    Sidecar .meta.md files are written to raw/ when using --mark.
"""

import argparse
import os
import sys
from pathlib import Path
from datetime import date

RAW_DIR = Path(__file__).parent.parent / "raw"
SKIP_FILES = {"AGENTS.md"}
SKIP_SUFFIXES = {".meta.md"}


def find_source_files():
    """Return list of non-sidecar, non-AGENTS source files in raw/."""
    files = []
    for path in sorted(RAW_DIR.rglob("*")):
        if not path.is_file():
            continue
        if path.name in SKIP_FILES:
            continue
        if any(path.name.endswith(s) for s in SKIP_SUFFIXES):
            continue
        files.append(path)
    return files


def get_sidecar(source_path: Path) -> Path:
    """Return the expected sidecar path for a source file."""
    return source_path.with_name(source_path.stem + ".meta.md")


def read_sidecar_field(sidecar_path: Path, field: str) -> str | None:
    """Read a single frontmatter field from a sidecar file. Returns None if missing."""
    if not sidecar_path.exists():
        return None
    in_frontmatter = False
    for line in sidecar_path.read_text().splitlines():
        if line.strip() == "---":
            in_frontmatter = not in_frontmatter
            continue
        if in_frontmatter and line.startswith(field + ":"):
            return line.split(":", 1)[1].strip()
    return None


def get_status(source_path: Path) -> str:
    """Return ingestion status: new | ingested | compiled."""
    sidecar = get_sidecar(source_path)
    if not sidecar.exists():
        return "new"
    compiled = read_sidecar_field(sidecar, "compiled_to")
    if compiled and compiled.strip() not in ("", "[]", "null"):
        return "compiled"
    ingested = read_sidecar_field(sidecar, "ingested")
    if ingested and ingested.lower() == "true":
        return "ingested"
    return "new"


def mark_ingested(source_path: Path):
    """Create or update sidecar to mark file as ingested."""
    sidecar = get_sidecar(source_path)
    if sidecar.exists():
        print(f"  Sidecar already exists: {sidecar.relative_to(RAW_DIR.parent)}")
        return
    content = f"""---
sidecar_for: {source_path.name}
ingested: true
ingested_at: {date.today().isoformat()}
tags: []
compiled_to: []
---
"""
    sidecar.write_text(content)
    print(f"  Created sidecar: {sidecar.relative_to(RAW_DIR.parent)}")


def cmd_list(new_only: bool = False):
    files = find_source_files()
    if not files:
        print("No source files found in raw/")
        return

    col_w = max(len(str(f.relative_to(RAW_DIR.parent))) for f in files) + 2
    header = f"{'File':<{col_w}}  Status"
    print(header)
    print("-" * len(header))

    counts = {"new": 0, "ingested": 0, "compiled": 0}
    for f in files:
        status = get_status(f)
        counts[status] += 1
        if new_only and status != "new":
            continue
        rel = str(f.relative_to(RAW_DIR.parent))
        print(f"{rel:<{col_w}}  {status}")

    print()
    print(f"Total: {len(files)} files — {counts['new']} new, {counts['ingested']} ingested, {counts['compiled']} compiled")


def main():
    parser = argparse.ArgumentParser(description="Ingest scanner for raw/ directory")
    parser.add_argument("--new", action="store_true", help="List only new (unprocessed) files")
    parser.add_argument("--mark", metavar="FILE", help="Mark a file in raw/ as ingested")
    args = parser.parse_args()

    if args.mark:
        target = RAW_DIR / args.mark
        if not target.exists():
            print(f"Error: {target} does not exist", file=sys.stderr)
            sys.exit(1)
        mark_ingested(target)
    else:
        cmd_list(new_only=args.new)


if __name__ == "__main__":
    main()
