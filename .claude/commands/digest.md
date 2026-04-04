Run a full digest cycle: detect new files in raw/, compile them into wiki pages, lint, commit, and push.

Usage: /digest

## Steps

### 1. Detect new files
Run: `python agent/ingest.py --new`

If output says "0 new" → tell the user "Nothing new in raw/ to digest." and stop.

### 2. For each new file listed:

a. **Read the file** at `raw/<filename>` to understand its content.

b. **Mark as ingested**:
   `python agent/ingest.py --mark <filename>`

c. **Create a summary page** in `wiki/summaries/` using `schemas/summary.md`.
   - Fill in ALL sections with real content synthesized from the file.
   - Do not leave placeholder text.
   - Use `[[PageName]]` links for any concepts or topics it relates to.

d. **Create or update concept pages** for any new concepts introduced.
   - Check `wiki/index.md` first — if the concept already exists, update it.
   - If new, create `wiki/concepts/<slug>.md` using `schemas/concept.md`.
   - Fill in all sections. Mark uncertain claims `[UNVERIFIED]`.

e. **Update existing topic pages** if the file adds to a known topic area.
   - Add the paper to the "Landscape" table and "Important References" section.

f. **Record compilation**:
   `python agent/compile.py --mark <filename> wiki/summaries/<summary-slug>.md`

### 3. Update the index
Open `wiki/index.md` and add entries for every new page created.

### 4. Lint
Run: `python agent/lint.py`

Fix any issues before continuing:
- Broken `[[links]]` → create stub pages or fix the link target name
- Orphan pages → add to `wiki/index.md`
- Missing frontmatter → add required fields

### 5. Commit and push
```bash
git add wiki/ output/ raw/
git commit -m "digest: <comma-separated list of source titles>"
git push
```

## Notes
- Process ALL new files in one digest run, not one at a time.
- If a file is a PDF or binary that you cannot read directly, note it and skip — the user will use a skill to convert it first.
- If two new files cover the same concept, write one shared concept page and link both summaries to it.
