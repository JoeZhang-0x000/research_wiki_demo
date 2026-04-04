Answer a question using only wiki-backed evidence. Answer inline — no files written.

Usage: /query <question>

## Hard Rules

- Run `python skills/evidence.py "<question>" --json` first.
- Use only the returned evidence bundle as factual support.
- Do not answer from model priors or external knowledge.
- Every substantive claim must cite one or more evidence ids like `[S1]`.
- If the bundle says `coverage: not-covered`, say the wiki does not cover the question well enough and stop.
- If you make an inference, label it `Inference:` and still cite the supporting evidence ids.

## Steps

1. Run `python skills/evidence.py "<question>" --json` and inspect the evidence bundle.

2. Read the cited wiki pages in bundle order.
   - Prioritize `summary` pages as primary evidence.
   - Use `concept` and `topic` pages for structure only when they remain traceable to a summary/raw/url in the same bundle.

3. Answer directly in the conversation with this structure:
   - `Answer` — grounded answer only
   - `Evidence` — short citation map from `[S#]` to page and URL/raw provenance
   - `Gaps` — uncovered parts of the question, relevant `[UNVERIFIED]` claims, or thin areas

4. Citation requirements:
   - Every paragraph or bullet in `Answer` ends with citation ids.
   - If a point cannot be tied to bundle evidence, omit it.
   - Prefer citing the most specific `summary` evidence available.

5. After answering, note any gaps:
   - Broken `[[links]]` pointing to non-existent pages
   - `[UNVERIFIED]` claims relevant to the question
   - Topics or summaries that are too thin to support the asked question

6. Ask the user: "Should I fill in any of these gaps?"
   If yes → create/update wiki pages, run `python skills/lint.py`, commit.
   If no → done.
