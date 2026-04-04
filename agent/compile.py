#!/usr/bin/env python3
"""
compile.py — Compile raw source files into wiki pages.

This script does NOT call an LLM. It performs structural compilation:
- Reads raw/ source files and their sidecars
- Creates stub wiki pages for sources that have no compiled_to entry
- Updates wiki/index.md with new entries

For content-level compilation (extracting concepts, writing definitions),
use an LLM agent (Claude Code / Codex) guided by AGENTS.md and CLAUDE.md.
The LLM agent should call this script to check what needs to be compiled,
then write wiki pages, then run this script with --mark to record completion.

Usage:
    python agent/compile.py                       # list sources needing compilation
    python agent/compile.py --stub <raw-file>     # create a stub wiki summary page
    python agent/compile.py --mark <raw-file> <wiki-page>  # record compiled_to in sidecar
"""

import argparse
import sys
from pathlib import Path
from datetime import date

ROOT = Path(__file__).parent.parent
RAW_DIR = ROOT / "raw"
WIKI_DIR = ROOT / "wiki"
SUMMARIES_DIR = WIKI_DIR / "summaries"
SKIP_FILES = {"AGENTS.md"}
SKIP_SUFFIXES = {".meta.md"}


def find_source_files():
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
    return source_path.with_name(source_path.stem + ".meta.md")


def get_compiled_to(source_path: Path) -> list[str]:
    sidecar = get_sidecar(source_path)
    if not sidecar.exists():
        return []
    in_fm = False
    in_compiled = False
    items = []
    for line in sidecar.read_text().splitlines():
        stripped = line.strip()
        if stripped == "---":
            in_fm = not in_fm
            continue
        if not in_fm:
            continue
        if stripped.startswith("compiled_to:"):
            val = stripped[len("compiled_to:"):].strip()
            if val and val != "[]":
                items.append(val.strip("[]").strip())
            in_compiled = True
            continue
        if in_compiled:
            if stripped.startswith("-"):
                items.append(stripped.lstrip("- ").strip())
            else:
                in_compiled = False
    return [i for i in items if i]


def cmd_list():
    files = find_source_files()
    needs_compile = [f for f in files if not get_compiled_to(f)]
    if not needs_compile:
        print("All source files have been compiled.")
        return
    print(f"Sources needing compilation ({len(needs_compile)}):\n")
    for f in needs_compile:
        print(f"  {f.relative_to(ROOT)}")
    print()
    print("Run: python agent/compile.py --stub <raw-file>  to create a stub summary page.")


def slugify(name: str) -> str:
    """Convert a filename stem to a wiki slug."""
    return name.replace("_", "-").lower()


def cmd_stub(raw_file: str):
    """Create a stub summary page in wiki/summaries/ for a raw file."""
    source = RAW_DIR / raw_file
    if not source.exists():
        print(f"Error: {source} not found", file=sys.stderr)
        sys.exit(1)

    slug = slugify(source.stem)
    # Remove 'paper-' prefix for cleaner summary names
    if slug.startswith("paper-"):
        slug = slug[len("paper-"):]
    out_path = SUMMARIES_DIR / f"summary-{slug}.md"

    if out_path.exists():
        print(f"Page already exists: {out_path.relative_to(ROOT)}")
        print("Edit it directly or use --mark to record it in the sidecar.")
        return

    stub = f"""---
title: Summary — {source.stem}
type: summary
status: draft
created: {date.today().isoformat()}
updated: {date.today().isoformat()}
sources:
  - raw/{source.name}
tags: []
---

# Summary — {source.stem}

## Source Metadata

| Field       | Value            |
|-------------|------------------|
| Source type | [paper/blog/talk/note] |
| Author(s)   | [FILL IN]        |
| Year        | [FILL IN]        |
| Venue       | [FILL IN]        |
| Raw file    | `raw/{source.name}` |

## Main Idea

[FILL IN — 1-3 sentences describing the central claim or contribution]

## Key Details

- [FILL IN]

## Method / Approach

[FILL IN]

## Results / Evidence

[FILL IN]

## Limitations

[FILL IN]

## Links to Concepts

[FILL IN — use [[ConceptName]] links]

## Links to Topics

[FILL IN — use [[TopicName]] links]
"""
    SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)
    out_path.write_text(stub)
    print(f"Created stub: {out_path.relative_to(ROOT)}")
    print(f"Next: fill in the content, then run:")
    print(f"  python agent/compile.py --mark {source.name} wiki/summaries/summary-{slug}.md")


def cmd_mark(raw_file: str, wiki_page: str):
    """Record a compiled_to entry in the sidecar for a source file."""
    source = RAW_DIR / raw_file
    if not source.exists():
        print(f"Error: {source} not found", file=sys.stderr)
        sys.exit(1)

    sidecar = get_sidecar(source)
    if not sidecar.exists():
        # Create minimal sidecar
        content = f"""---
sidecar_for: {source.name}
ingested: true
ingested_at: {date.today().isoformat()}
tags: []
compiled_to:
  - {wiki_page}
---
"""
        sidecar.write_text(content)
        print(f"Created sidecar with compiled_to: {sidecar.relative_to(ROOT)}")
        return

    # Append to existing sidecar's compiled_to field
    text = sidecar.read_text()
    lines = text.splitlines()
    new_lines = []
    in_compiled = False
    inserted = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("compiled_to:"):
            in_compiled = True
            new_lines.append(line)
            continue
        if in_compiled:
            if stripped.startswith("-"):
                new_lines.append(line)
                continue
            else:
                # End of compiled_to list — insert our entry before this line
                if not inserted:
                    new_lines.append(f"  - {wiki_page}")
                    inserted = True
                in_compiled = False
        new_lines.append(line)

    if in_compiled and not inserted:
        new_lines.append(f"  - {wiki_page}")

    sidecar.write_text("\n".join(new_lines) + "\n")
    print(f"Updated sidecar: {sidecar.relative_to(ROOT)}")
    print(f"  compiled_to += {wiki_page}")


def main():
    parser = argparse.ArgumentParser(description="Compile raw sources into wiki pages")
    parser.add_argument("--stub", metavar="FILE", help="Create a stub summary page for FILE in raw/")
    parser.add_argument("--mark", nargs=2, metavar=("RAW_FILE", "WIKI_PAGE"),
                        help="Record compiled_to in sidecar")
    args = parser.parse_args()

    if args.stub:
        cmd_stub(args.stub)
    elif args.mark:
        cmd_mark(args.mark[0], args.mark[1])
    else:
        cmd_list()


if __name__ == "__main__":
    main()
