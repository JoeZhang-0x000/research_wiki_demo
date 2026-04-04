First-principles analysis. Reasons from irreducible constraints to necessary conclusions.

Usage: /analyze <topic>

---

## What "first principles" means here

First principles are constraints you cannot argue with:
physical laws, information-theoretic limits, logical necessity.

Everything else is a response — either *forced* (no alternative given the constraint)
or *chosen* (one of many valid responses). The analysis distinguishes these.

Numbers are not conclusions. The question is always:
*why must this be, given what cannot be otherwise?*

---

## Step 0: Gather

Run: `python skills/evidence.py "<topic>" --json`

Use the returned evidence bundle as the sole factual basis for the analysis.

If the bundle reports `coverage: not-covered`, stop and tell the user the wiki does not support a grounded analysis of this topic yet.

Read the pages in the bundle, prioritizing `summary` pages. Use `concept` and `topic` pages only when they remain traceable to summary/raw/url provenance inside the same bundle.

Build a citation map from the bundle's `citation_id`s (`[S1]`, `[S2]`, ...).
For each evidence item, keep:
- page path
- snippets
- `sources:`
- resolved URLs

## Hard Rules

- Do not use model priors or outside knowledge.
- Every substantive claim must cite one or more evidence ids like `[S1]`.
- If a statement is a synthesis rather than a direct source claim, prefix it with `Inference:` and still cite the supporting evidence ids.
- If a point cannot be supported from the bundle, omit it.

---

## Pass 1 — The irreducible constraint

What physical or mathematical law makes this problem hard in a way no engineering escapes?
State the fundamental tension: the two things you cannot simultaneously have, and why.

*One paragraph. No hedging. No solution names. End with citations.*

---

## Pass 2 — Forced vs. chosen

For each major design decision:
- **Forced** — any valid solution must do this because the constraint leaves no room
- **Chosen** — this did X; Y was also possible; the difference is the assumption that X's case dominates

`[forced/chosen] <decision> — <one-sentence reason> [S#]`

---

## Pass 3 — What moved

Every choice that solves Pass 1's constraint moves cost somewhere else.

`Solved <X> by moving cost to <Y>` — one line each, with citation ids.
Then: what new assumption is now load-bearing? One line each.

---

## Pass 4 — Adversarial

Strongest case that the approach is right for narrower reasons than claimed,
or that Pass 1's framing is wrong.

Three questions only:
1. Is Pass 1's constraint actually the binding one, or is there a prior?
2. Does the dominant-case assumption in Pass 2 hold in practice?
3. What is the real ceiling — the structural reason improvement terminates?

*Three answers, three sentences max each. Every answer ends with citations.*

---

## Pass 5 — Synthesis

What is actually true, in plain reasoning chains.
Resolve contradictions between passes explicitly.
Prose, not bullets. Every sentence answers "why must this be?" not "what did we observe?"

End with one sentence:
**The one thing that, if it changed, would make this approach obsolete:** (the condition, not a technology name)

Every paragraph ends with citations.

---

## Output format

Write to: `output/analysis-<topic-slug>-<YYYY-MM-DD>.md`

```markdown
---
title: Analysis — <topic>
date: YYYY-MM-DD
sources: [list of wiki pages read]
---

## TL;DR
<2-3 sentences. What is essentially true after all five passes. Written last.>

---

## Pass 1 — The irreducible constraint
...

## Pass 2 — Forced vs. chosen
...

## Pass 3 — What moved
...

## Pass 4 — Adversarial
...

## Pass 5 — Synthesis
...

---

## References
<!-- Use the evidence bundle's citation ids. Include URL when available, otherwise raw/<filename>. -->
- [S1] [[PageName]] — <url or raw/source provenance>
- [S2] [[PageName]] — <url or raw/source provenance>
```

After writing, tell the user:
- The finding in Pass 5 most absent from the wiki's framing
- The Pass 4 challenge hardest to rebut
- Any part of the requested analysis you had to omit because the wiki lacked grounded support

Then ask: "Should I distill any of this into wiki pages?"
Do NOT touch wiki/ until the user says yes.
