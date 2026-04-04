Scan the wiki for gaps and fill them in. No input file needed.

Usage: /distill [topic]

If a topic is given, focus on that area. Otherwise, do a full wiki health pass.

## Steps

1. Run `python agent/lint.py` to get a structural overview:
   - Broken `[[links]]` → pages referenced but not yet written
   - `[UNVERIFIED]` claims in stable pages
   - Orphan pages

2. Read the relevant wiki pages to understand what's missing.

3. **Fill in the gaps**:
   - For each broken link that points to a real concept: create the page using `schemas/concept.md` or `schemas/topic.md`. Write real content — not placeholders.
   - For each `[UNVERIFIED]` claim: check the raw source files. Either confirm and remove the tag, or mark as "disputed" with a note.
   - For orphan pages: link them from an appropriate existing page or from `wiki/index.md`.

4. Update `wiki/index.md` with any new pages.

5. Run `python agent/lint.py` again to confirm issues are resolved.

6. Commit and push:
   ```bash
   git add wiki/
   git commit -m "distill: <brief description of what was filled in>"
   git push
   ```

## Notes

- Only commit to wiki/. Do not commit output/ files.
- If a concept requires more source material to write properly, create a minimal stub (status: draft) and note what's needed.
- Prefer depth on fewer pages over shallow coverage of many.
