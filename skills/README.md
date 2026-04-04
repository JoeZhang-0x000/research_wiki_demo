# Skills

Shared capability library. Check here before implementing anything.

```
python skills/<name>.py --help
```

---

## Built-in Skills

| Script | Description |
|--------|-------------|
| `backfill_provenance.py` | Repair stale raw references and missing summary links across wiki/ |
| `digest.py` | Full ingestion pipeline: rename new raw files + create summary stubs |
| `evidence.py` | Build grounded evidence bundles from wiki/ pages and raw/ provenance |
| `ingest.py` | Find raw/ files not yet referenced by any wiki/summaries/ page |
| `rename.py` | Slugify raw/ filenames based on frontmatter title — updates wiki refs |
| `search.py` | Keyword search across wiki/ — stdout only, no files written |
| `lint.py` | Structural checks: broken links, orphans, missing frontmatter, [UNVERIFIED] in stable pages, raw/ duplicate-name warnings |
| `stub.py` | Create a blank wiki page from a schema template |
| `reorganize.py` | Detect and fix Obsidian graph issues: broken links (fuzzy-matched), orphans, likely duplicates, exact duplicate raw/ sources |

---

## Adding a Skill

1. Create `skills/<name>.py` with a module docstring (purpose / inputs / outputs / deps) and `--help`
2. Add a row to the table above
3. Optionally add `.claude/commands/<name>.md` for a slash command wrapper

Template:
```python
#!/usr/bin/env python3
"""
<name>.py — <one-line description>

Inputs:  ...
Outputs: stdout only (or: writes to <location>)
Deps:    <pip packages, if any>
"""
import argparse

def main():
    parser = argparse.ArgumentParser(description="...")
    args = parser.parse_args()

if __name__ == "__main__":
    main()
```

---

## Planned

- `fetch-arxiv.py` — fetch paper metadata and abstract by arxiv ID or URL
- `fetch-page.py` — fetch and clean a webpage to markdown
- `youtube-transcript.py` — extract transcript from YouTube URL
