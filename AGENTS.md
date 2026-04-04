# AGENTS.md — research_wiki

This file is read by all AI coding agents (Claude Code, OpenAI Codex, Gemini CLI, etc.)
operating in this repository. Follow these rules precisely.

---

## Mission

Convert raw AI research materials into a structured, evolving markdown knowledge base.
The knowledge base covers three domains: **High-Performance Computing (HPC)**, **AI Infrastructure**, and **AI Agents**.

The system operates as a closed loop:

```
collect → ingest → compile → query → output → distill → wiki → repeat
```

---

## Directory Semantics

```
raw/          Source materials. Append-only. Never edit existing files.
wiki/         Compiled knowledge pages. Structured. Evolve via rules only.
  concepts/   Atomic knowledge units (one concept per file)
  topics/     Broader topic overviews (aggregate multiple concepts)
  summaries/  Per-source summaries (one per raw file or paper)
output/       Query results and generated reports. Writable/overwritable.
agent/        Pipeline scripts. Edit with care.
skills/       Reusable capability scripts. Extend freely. READ THIS FIRST.
schemas/      Markdown templates. Treat as stable contracts.
.claude/commands/  Claude Code slash commands. Wraps skills/.
```

---

## Skills System — READ BEFORE IMPLEMENTING ANYTHING

**`skills/` is the shared capability library for all agents.**

Before writing any new functionality, run:
```bash
ls skills/
```
and read the docstrings of relevant scripts. Do not reimplement existing skills.

Each skill:
- Is a standalone Python script with a CLI (`--help` supported)
- Has a module-level docstring describing inputs, outputs, and behavior
- Can be called from any agent script or slash command

To add a skill: create `skills/<name>.py`, add an entry to `skills/README.md`.

---

## Allowed Actions

- `raw/`: append new files only. Never modify existing ones.
- `wiki/`: create new pages or update existing ones following schemas in `schemas/`
- `output/`: write or overwrite reports freely
- `agent/`: run scripts, modify pipeline logic carefully
- `skills/`: add new skills, never remove existing ones without checking dependents
- `wiki/index.md`: always update when adding a new wiki page

## Forbidden Actions

- Editing any existing file in `raw/`
- Deleting wiki pages (use `status: deprecated` instead)
- Inventing facts — use `[UNVERIFIED]` for uncertain claims
- Stripping `[[links]]` from wiki pages without replacement
- Using external databases, vector stores, or non-standard dependencies

---

## Wiki Page Rules

1. Every page must conform to its schema (`schemas/concept.md`, `schemas/topic.md`, `schemas/summary.md`)
2. Every page must have YAML frontmatter with at least: `title`, `type`, `status`, `sources`
3. Internal links use `[[PageName]]` syntax
4. No orphan pages — every new page must be linked from at least one other page or `wiki/index.md`
5. `status` values: `draft` | `stable` | `deprecated`

---

## Distillation Policy

When an `output/` report contains reusable knowledge:
1. Identify facts that generalize beyond the specific query
2. Map them to existing concept/topic pages and update, or create new pages
3. Never copy-paste verbatim — synthesize and structure
4. Record provenance in the `sources` frontmatter field

---

## Provenance Rules

- Every wiki page must trace back to at least one file in `raw/` or an external URL
- Cite sources in frontmatter `sources` field as a list
- If a claim has no traceable source, mark it `[UNVERIFIED]`
- Resolve all `[UNVERIFIED]` markers before setting `status: stable`

---

## Pipeline Scripts

Run in order for a full loop iteration:

```bash
python agent/ingest.py          # scan raw/, list new items
python agent/compile.py         # create/update wiki pages from raw/
python agent/query.py "topic"   # search wiki/, write report to output/
python agent/distill.py <file>  # extract knowledge from output/ → wiki/
python agent/lint.py            # check for orphans, broken links, empty sections
```

---

## Git Sync Rules

**After every distill cycle that modifies `wiki/`, you must commit and push.**

`raw/` is excluded from git (see `.gitignore`). It is local-only. Never try to commit files from `raw/` (except `raw/AGENTS.md` and `raw/*.meta.md` which are tracked).

### Commit convention after distillation

```bash
git add wiki/ output/
git add raw/*.meta.md          # sidecar files ARE tracked
git commit -m "distill: <short topic description>"
git push
```

### Commit convention after adding a skill

```bash
git add skills/ .claude/commands/
git commit -m "skill: add <skill-name>"
git push
```

### Commit convention after adding raw source + stub

```bash
git add raw/<file>.meta.md wiki/summaries/<stub>.md wiki/index.md
git commit -m "ingest: add <source title>"
git push
```

Do NOT bundle wiki changes with skills changes in a single commit.
Do NOT push if `python agent/lint.py` reports errors.
