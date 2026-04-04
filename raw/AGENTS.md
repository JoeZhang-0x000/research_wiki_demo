# AGENTS.md — raw/

## Role of This Directory

`raw/` is the **immutable source-of-truth** for all knowledge in this system.

Files here represent primary inputs: papers, notes, transcripts, web captures, and other unstructured materials.

---

## Rules

### Strictly Enforced

1. **Never edit an existing file in `raw/`.** Once a file is added, it is frozen.
2. **Never delete files from `raw/`.** Even if the content is superseded.
3. **Never reformat or clean up files in `raw/`.** Downstream processing handles normalization.

### Allowed

- Adding new files (any format: `.md`, `.txt`, `.pdf`, `.html`)
- Adding sidecar metadata files (e.g., `paper_xyz.meta.md`) that annotate an existing file without modifying it
- Creating subdirectories for organization (e.g., `raw/hpc/`, `raw/agents/`)

---

## Sidecar Metadata Format

If you need to annotate a raw file (e.g., add tags, mark ingestion status), create a sidecar file:

```
raw/
  paper_flashattention2.txt
  paper_flashattention2.meta.md    ← sidecar
```

Sidecar frontmatter schema:
```yaml
---
sidecar_for: paper_flashattention2.txt
ingested: true
ingested_at: 2024-01-15
tags: [attention, cuda, memory-efficiency]
compiled_to: [wiki/concepts/flash-attention.md]
---
```

---

## File Naming Convention

Use lowercase, hyphen-separated names. Include a type prefix when helpful:

| Prefix     | Example                              |
|------------|--------------------------------------|
| `paper_`   | `paper_megatron-lm-2021.txt`         |
| `note_`    | `note_nvlink-bandwidth-thoughts.md`  |
| `web_`     | `web_anthropic-agents-post.md`       |
| `talk_`    | `talk_sc24-moe-routing.txt`          |

---

## Ingestion Status

Files in `raw/` can be in three states (tracked via sidecar or `agent/ingest.py`):

- **new**: not yet processed
- **ingested**: scanned and logged by `ingest.py`
- **compiled**: wiki pages have been created from this file
