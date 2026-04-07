# research_wiki

LLM-native knowledge base for AI research — HPC, AI Infra, Agents.

**This repo is for personal use. For a clean reference version, see: https://github.com/JoeZhang-0x000/research_wiki_demo**

---

## How It Works

```
raw/  →  /digest  →  wiki/
                       ↓
                   /query     answer inline
                   /analyze   first-principles report → output/
                   /distill   fill wiki gaps
```

- `raw/` — source materials (Obsidian Clipper, papers, notes)
- `wiki/` — compiled, structured knowledge
- `output/` — ephemeral scratch, gitignored

Ingestion state is structural: a raw file is *compiled* when any `wiki/summaries/` page lists it in `sources:`. No sidecar files.

## Grounded Answers

- Run `python skills/evidence.py "<question>" --json` before `/query` or `/analyze`
- Generated answers must be grounded in `wiki/` only
- Every substantive claim should cite evidence ids such as `[S1]`
- If the wiki lacks coverage, report the gap instead of filling it from model priors

---

## Slash Commands

| Command | What it does |
|---------|-------------|
| `/digest` | Find new raw/ files → compile into wiki → lint → commit → push |
| `/query <question>` | Answer inline from wiki. No files written. |
| `/analyze <topic>` | Five-pass first-principles analysis → `output/analysis-*.md` |
| `/distill [topic]` | Scan wiki for gaps, fill with user approval |
| `/lint` | Run linter, fix issues |
| `/add-skill <name>` | Add a new skill to `skills/` |

---

## Skills

Executable logic lives in `skills/`. Always check before implementing anything.

```bash
python skills/ingest.py          # find undigested raw/ files
python skills/evidence.py "term" # build grounded evidence bundle
python skills/search.py "term"   # search wiki/ (stdout)
python skills/lint.py            # structural health check
python skills/stub.py <type> <name>  # create a blank wiki page
```

---

## Obsidian

Open repo root as a vault. `[[links]]` are Obsidian-compatible.
`links:` frontmatter field stores original URLs from Clipper for clickable references.

---

## Git Conventions

```bash
git commit -m "digest: <titles>"    # after /digest
git commit -m "distill: <topic>"    # after /distill
git commit -m "skill: add <name>"   # after adding a skill
```

`output/` is never committed. Run `python skills/lint.py` before every push.
