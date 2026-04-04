# Skills — Shared Capability Library

This directory contains reusable skill scripts callable by any agent (Claude Code, Codex, etc.) or pipeline script.

**Before implementing any repeated operation, check here first.**

---

## Available Skills

| Script | Description | CLI Example |
|--------|-------------|-------------|
| *(none yet — add your first skill below)* | | |

---

## How to Add a Skill

1. Create `skills/<name>.py` with:
   - A module-level docstring describing: purpose, inputs, outputs, dependencies
   - A `main()` function with argparse (`--help` must work)
   - No side effects when imported (guard with `if __name__ == "__main__"`)

2. Add a row to the table above.

3. Optionally add `.claude/commands/<name>.md` for a Claude Code slash command wrapper.

---

## Skill Template

```python
#!/usr/bin/env python3
"""
<name>.py — <one-line description>

Inputs:  <what it reads>
Outputs: <what it writes / prints>
Deps:    <pip packages required, if any>

Usage:
    python skills/<name>.py <args>
    python skills/<name>.py --help
"""

import argparse

def main():
    parser = argparse.ArgumentParser(description="<description>")
    # add arguments
    args = parser.parse_args()
    # implement

if __name__ == "__main__":
    main()
```

---

## Planned Skills (add as needed)

- `fetch-arxiv.py` — fetch paper metadata and abstract from arxiv by ID or URL
- `parse-pdf.py` — convert a PDF to markdown using a local tool
- `fetch-webpage.py` — fetch and clean a webpage to markdown (via Jina or trafilatura)
- `youtube-transcript.py` — extract transcript from a YouTube video URL
- `watch-raw.py` — watch raw/ for new files and auto-run ingest
