# Claude Code Instructions — research_wiki

This repository is an LLM-native knowledge compilation system for AI research (HPC, AI Infra, Agents).
You are expected to read, write, and maintain a structured markdown knowledge base.

---

## Directory Semantics

| Directory           | Purpose                                              | Mutability       |
| ------------------- | ---------------------------------------------------- | ---------------- |
| `raw/`              | Source materials (papers, notes, links, transcripts) | Append-only      |
| `wiki/`             | Compiled, structured knowledge pages                 | Evolve via rules |
| `output/`           | Query results and reports                            | Write/overwrite  |
| `agent/`            | Pipeline scripts (ingest, compile, query, distill)   | Edit carefully   |
| `skills/`           | Reusable skill scripts callable by any agent         | Extend freely    |
| `schemas/`          | Markdown templates for wiki page types               | Stable           |
| `.claude/commands/` | Claude Code slash commands (thin wrappers)           | Extend freely    |

---

## Skills System

**All reusable capabilities live in `skills/`.**

Before implementing any repeated operation from scratch, check `skills/` for an existing skill.
Each skill is a self-contained script with a CLI interface and a header comment describing its purpose.

To discover available skills:
```bash
ls skills/
head -5 skills/<skill-name>.py   # read the docstring
```

When adding a new skill:
1. Create `skills/<skill-name>.py` with a clear module docstring and `--help` support
2. Add a corresponding `.claude/commands/<skill-name>.md` slash command if it's frequently used
3. Document it in `skills/README.md`

---

## Allowed Actions

- Append new files to `raw/` (never edit existing raw files)
- Create or update pages in `wiki/concepts/`, `wiki/topics/`, `wiki/summaries/`
- Write reports to `output/`
- Run any script in `agent/` or `skills/`
- Add new skills to `skills/`
- Update `wiki/index.md` with new links

## Forbidden Actions

- Never edit files already in `raw/` (they are immutable source-of-truth)
- Never delete wiki pages — mark deprecated pages with `status: deprecated` in frontmatter
- Never invent facts. If uncertain, write `[UNVERIFIED]` inline
- Never remove `[[links]]` from wiki pages without replacing them
- Never overwrite `output/` reports without checking if they are referenced by wiki pages

---

## Editing Strategy

- Prefer append over destructive edit
- When updating a wiki page, preserve all existing `[[links]]` and add new ones
- All wiki pages must use the schema defined in `schemas/`
- Use `[[PageName]]` syntax for internal links (Obsidian-compatible)
- Always update `wiki/index.md` when creating a new wiki page

---

## Distillation Policy

When you produce an `output/` report that contains reusable knowledge:
1. Identify claims that belong in `wiki/concepts/` or `wiki/topics/`
2. Either update an existing page or create a new one using the correct schema
3. Add a `Sources` entry pointing back to the output file
4. Do not copy-paste verbatim — synthesize and structure

---

## Provenance Rules

Every wiki page must have a `sources` field in its frontmatter listing the raw files or URLs it was derived from.
Every claim marked `[UNVERIFIED]` must be resolved before a page is considered `status: stable`.

---

## Git Sync Rules

**`raw/` is tracked in git.** All source files and sidecars are committed alongside wiki pages.

**Primary workflow: `/digest`**
When the user says "digest" or runs `/digest`, follow the steps in `.claude/commands/digest.md`:
1. `python agent/ingest.py --new` — find new files
2. Read each file, write wiki pages (summaries + concepts)
3. Update `wiki/index.md`
4. `python agent/lint.py` — fix issues
5. `git add wiki/ raw/ && git commit -m "digest: <titles>" && git push`

**After adding a skill:**
```bash
git add skills/ .claude/commands/
git commit -m "skill: add <name>"
git push
```

Do NOT push if `python agent/lint.py` reports errors.
Do NOT bundle wiki changes with skill changes in one commit.
