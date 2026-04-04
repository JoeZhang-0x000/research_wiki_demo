# AGENTS.md — research_wiki

This file is read by all AI coding agents (Claude Code, OpenAI Codex, Gemini CLI, etc.)

---

## Mission

Convert raw AI research materials into a structured, evolving markdown knowledge base.
Domains: **High-Performance Computing (HPC)**, **AI Infrastructure**, **AI Agents**.

```
raw/  →  /digest  →  wiki/  →  /query (inline)
                       ↑              ↓ user approves
                    /distill      /analyze → output/
```

---

## Directory Semantics

```
raw/          Source materials. Append-only. Never edit existing files. Fully tracked in git.
wiki/         Compiled knowledge. Evolve via rules. Tracked in git.
  concepts/   Atomic knowledge units
  topics/     Broader topic overviews
  summaries/  Per-source summaries — ingestion state lives here
output/       Ephemeral scratch. Gitignored. Never commit.
skills/       All executable logic. Check here first.
schemas/      Markdown templates. Stable contracts.
.claude/commands/  Slash commands. Wrap skills/.
```

---

## Skills — Check Before Implementing

```bash
ls skills/
python skills/<name>.py --help
```

| Skill | Purpose |
|-------|---------|
| `skills/digest.py` | Full ingestion pipeline: rename new raw files + create summary stubs |
| `skills/evidence.py` | Build grounded evidence bundles from wiki/ + raw/ provenance |
| `skills/backfill_provenance.py` | Repair stale raw refs and missing summary links across wiki/ |
| `skills/ingest.py` | Find raw/ files not yet referenced by wiki/summaries/ |
| `skills/rename.py` | Slugify raw/ filenames based on frontmatter title — updates wiki refs |
| `skills/search.py` | Keyword search across wiki/ — stdout only |
| `skills/lint.py` | Structural checks: broken links, orphans, missing frontmatter |
| `skills/stub.py` | Create a blank wiki page from a schema template |
| `skills/reorganize.py` | Detect + fix Obsidian graph issues (broken links, orphans, duplicates) |

To add a skill: create `skills/<name>.py`, add to `skills/README.md`.

---

## Output vs Wiki — Hard Boundary

| User intent | Destination |
|-------------|-------------|
| User asks to generate / research / report on X | `output/` |
| New raw source ingested | `wiki/` via `/digest` only |
| Filling lint-detected gaps | `wiki/` via `/distill` only |
| Query answer | conversation only |

**`wiki/` is only modified through the pipeline (`/digest`, `/distill`, `/reorganize`).**
**Never write to `wiki/` in response to a user request for generated content.**

## Grounded Generation Policy

- Query, analysis, and any generated prose must be grounded in `wiki/` content only.
- Run `python skills/evidence.py "<question>" --json` before answering or analyzing.
- Every substantive claim must cite one or more evidence ids such as `[S1]`.
- If the wiki does not cover the question well enough, say so explicitly and stop instead of filling gaps from model priors.
- `wiki/summaries/` are the primary evidence layer. `wiki/concepts/` and `wiki/topics/` are synthesis layers and should remain traceable back to summary/raw/url provenance.

---

## Ingestion State

A raw file is **compiled** when any `wiki/summaries/` page lists it in `sources:`.
No sidecar files. No registry. State is implicit in the wiki.

---

## Allowed

- `raw/`: append files only; **rename is allowed during `/digest`** (auto-slugify based on frontmatter title)
- `wiki/`: create/update pages per schemas — **with user approval after any analysis**
- `output/`: write freely, never commit
- `skills/`: add skills, never remove without checking dependents
- Always update `wiki/index.md` when adding a page

## Forbidden

- Deleting wiki pages — use `status: deprecated`
- Inventing facts — use `[UNVERIFIED]`
- Adding sidecar/meta files to `raw/`
- Writing to `wiki/` in response to a user request for a report, analysis, or generated content
- Committing `output/`

---

## Wiki Page Rules

1. Every page conforms to its schema in `schemas/`
2. Required frontmatter: `title`, `type`, `status`, `sources`, `links`
3. Internal links: `[[PageName]]` syntax
4. No orphans — every new page linked from at least one other or `wiki/index.md`
5. `status`: `draft` | `stable` | `deprecated`

---

## Provenance

- `sources:` lists raw files or URLs this page was compiled from
- `links:` lists original web URLs (Obsidian Clipper)
- Uncertain claims: `[UNVERIFIED]` — must be resolved before `status: stable`

---

## Git Conventions

```bash
# After digest
git add wiki/ raw/
git commit -m "digest: <titles>"
git push

# After filling wiki gaps
git add wiki/
git commit -m "distill: <what was filled>"
git push

# After adding a skill
git add skills/ .claude/commands/
git commit -m "skill: add <name>"
git push
```

Run `python skills/lint.py` before every push. Do not push with lint errors.
Do not bundle wiki changes with skill changes.
