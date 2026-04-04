# Claude Code Instructions — research_wiki

This repository is an LLM-native knowledge compilation system for AI research (HPC, AI Infra, Agents).
You are expected to read, write, and maintain a structured markdown knowledge base.

---

## Directory Semantics

| Directory           | Purpose                                              | Mutability       |
| ------------------- | ---------------------------------------------------- | ---------------- |
| `raw/`              | Source materials (papers, notes, links, transcripts) | Append-only      |
| `wiki/`             | Compiled, structured knowledge pages                 | Evolve via rules |
| `output/`           | Ephemeral scratch space — gitignored, not committed  | Write/overwrite  |
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
- Write temporary scratch notes to `output/` (not committed)
- Run any script in `agent/` or `skills/`
- Add new skills to `skills/`
- Update `wiki/index.md` with new links

## Forbidden Actions

- Never edit files already in `raw/` (they are immutable source-of-truth)
- Never delete wiki pages — mark deprecated pages with `status: deprecated` in frontmatter
- Never invent facts. If uncertain, write `[UNVERIFIED]` inline
- Never remove `[[links]]` from wiki pages without replacing them
---

## Editing Strategy

- Prefer append over destructive edit
- When updating a wiki page, preserve all existing `[[links]]` and add new ones
- All wiki pages must use the schema defined in `schemas/`
- Use `[[PageName]]` syntax for internal links (Obsidian-compatible)
- Always update `wiki/index.md` when creating a new wiki page

---

## Core Rule: Never Write to Wiki Without User Approval

After any analysis, query, or report — **always ask the user** before modifying wiki pages.
Do not auto-distill. Do not auto-commit. The user decides what enters the knowledge base.

Specifically:
- `/query` → answer inline → ask "should I fill these gaps in the wiki?"
- `/analyze` → write report to output/ → ask "should I distill any findings into wiki?"
- `/distill` → show what will change → ask before writing

The only exception is `/digest`, which is an explicit user-initiated ingest command
and implies consent to create wiki pages for the new raw files.

---

## Query Policy

When the user asks a question (`/query` or naturally in conversation):
- Read relevant wiki pages and **answer directly in the conversation**
- Do not write to `output/` for a query response
- After answering, surface any gaps (missing pages, `[UNVERIFIED]` claims)
- Ask the user before filling any gaps

## Analysis Policy

When using `/analyze`:
- Run all five passes (Mechanical, Adversarial, Historical, Reductionist, Synthesis)
- Write the full report to `output/analysis-<topic>-<date>.md`
- Tell the user the most surprising findings
- Ask before distilling anything into wiki/

## Distillation Policy

When using `/distill`:
- Run lint to surface gaps
- Show the user what you plan to write/change
- Ask for confirmation before modifying wiki/
- Commit only what the user approved

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
