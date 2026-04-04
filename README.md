# research_wiki

An LLM-native knowledge compilation system for AI research.

Covers: **High-Performance Computing**, **AI Infrastructure**, **AI Agents**

---

## How It Works

Raw research materials (papers, notes, web captures) flow through a pipeline into a structured, evolving markdown knowledge base.

```
raw/  →  ingest  →  compile  →  wiki/
                                  ↓
output/  ←  query  ←  wiki/      distill
  ↓                                ↑
distill  ────────────────────────→ wiki/
```

Each loop:
1. **Collect**: drop source files into `raw/`
2. **Ingest**: scan and log new files
3. **Compile**: create wiki pages from sources (LLM-assisted)
4. **Query**: search wiki, produce output reports
5. **Distill**: extract new knowledge from reports back into wiki
6. **Sync**: commit and push wiki changes to GitHub

---

## Directory Structure

```
raw/          Source materials (local only, not synced to git)
wiki/         Compiled knowledge base (synced)
  concepts/   Atomic concept pages
  topics/     Broad topic overview pages
  summaries/  Per-paper / per-source summary pages
  index.md    Master navigation index
output/       Query reports (synced)
agent/        Pipeline scripts
skills/       Reusable skill scripts
schemas/      Page templates
.claude/commands/  Claude Code slash commands
```

---

## Running the Pipeline

### 1. Ingest new sources

```bash
python agent/ingest.py           # see what's new
python agent/ingest.py --new     # only new files
python agent/ingest.py --mark paper_xyz.md   # mark as ingested
```

### 2. Compile wiki pages

```bash
python agent/compile.py                          # see what needs compiling
python agent/compile.py --stub paper_xyz.md      # create summary stub
# Then fill in the stub (manually or with LLM agent)
python agent/compile.py --mark paper_xyz.md wiki/summaries/summary-xyz.md
```

### 3. Query the wiki

```bash
python agent/query.py "collective communication"
python agent/query.py "memory bandwidth" --type concept
```

Output is written to `output/<query>-report.md`.

### 4. Distill findings

```bash
python agent/distill.py output/collective-communication-report.md
# Review the plan, then act on it (with LLM agent or manually)
```

### 5. Lint

```bash
python agent/lint.py             # check for issues
python agent/lint.py --strict    # exit 1 on any issue (for CI)
```

### 6. Sync to GitHub

```bash
git add wiki/ output/ raw/*.meta.md
git commit -m "distill: <topic>"
git push
```

---

## Claude Code Slash Commands

When working with Claude Code in this repo:

| Command | Description |
|---------|-------------|
| `/query <terms>` | Search wiki and generate report |
| `/ingest <file>` | Ingest a new source file |
| `/distill <report>` | Distill output report into wiki |
| `/lint` | Run linter and fix issues |
| `/add-skill <name>` | Add a new skill to skills/ |

---

## Skills

Reusable scripts live in `skills/`. See `skills/README.md` for the catalog.

To add a skill: `/add-skill <name> <description>` or follow the template in `skills/README.md`.

---

## Typical Workflow

```bash
# 1. Drop source files into raw/
cp ~/Downloads/paper_megatron-2021.pdf raw/
cp ~/notes/llm-serving-thoughts.md raw/

# 2. Run digest (Claude Code slash command)
# /digest
#
# Claude will:
#   - detect new files via `python agent/ingest.py --new`
#   - read each file and write wiki/summaries/ + wiki/concepts/ pages
#   - update wiki/index.md
#   - run lint, fix issues
#   - git add wiki/ raw/ && git commit -m "digest: ..." && git push
```

That's it. One command handles the full loop.

---

## Opening in Obsidian

Open the repo root as an Obsidian vault. All `[[links]]` are Obsidian-compatible.
Use the Graph View to explore concept clusters.

Recommended plugins: Dataview (for dynamic indexes), Obsidian Git (for auto-sync).

---

## Notes

- `raw/` is excluded from git to prevent repo bloat. Keep source files local.
- `raw/*.meta.md` sidecar files ARE tracked — they record ingestion state.
- All wiki pages use YAML frontmatter compatible with Obsidian and Dataview.
- Agent behavior rules are in `AGENTS.md` (root, raw/, wiki/) and `CLAUDE.md`.
