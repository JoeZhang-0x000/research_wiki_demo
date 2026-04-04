Answer a question using the wiki knowledge base. Do not generate output files.

Usage: /query <question>

## How to answer

1. Run `python agent/query.py "$ARGUMENTS"` to find relevant wiki pages.

2. Read the matching pages directly with the Read tool.

3. **Synthesize and answer inline** — respond to the user in the conversation.
   Do not write to output/. Do not generate a report file. Just answer.

4. At the end of your answer, note any gaps you found:
   - Missing concept pages that were referenced but don't exist
   - `[UNVERIFIED]` claims that could be resolved
   - Topics that seem underdeveloped given the question

5. Ask the user: "Should I fill in any of these gaps in the wiki now?"
   If yes → write the missing pages, update wiki/index.md, run lint, commit.
   If no → done.

## What good looks like

User: /query how does flash attention reduce memory usage?
→ You read wiki/concepts/flash-attention.md and related pages.
→ You answer directly: "FlashAttention avoids materializing the N×N matrix by..."
→ You note: "The wiki doesn't yet have a page on [[online-softmax]] which underpins this."
→ You ask if they want you to add it.

## What to avoid

- Do not write to output/ for a query
- Do not say "I've generated a report at output/xxx.md"
- Do not run a query and then ask the user to read the output file themselves
