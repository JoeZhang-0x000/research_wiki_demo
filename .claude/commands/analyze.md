First-principles analysis of a topic using wiki as raw material.
Reasons from irreducible constraints to necessary conclusions.
Output is concise — one claim per line, each claim linked to its source.

Usage: /analyze <topic>

---

## What "first principles" means here

First principles are constraints you cannot argue with:
physical laws, information-theoretic limits, logical necessity.

Everything else is a response to those constraints — either *forced* (no alternative) or *chosen* (one of many valid responses). The analysis distinguishes these.

Numbers are not conclusions. "2x faster" is an observation. The question is always:
*why must this be, given what cannot be otherwise?*

---

## Step 0: Gather sources

Run: `python agent/query.py "<topic>"`
Read every page returned and its linked pages.
For each page read, extract the `sources:` list from its frontmatter.
Build a source map:

```
[[PageName]] → [url1, url2, ...]
```

You will cite these URLs inline throughout the analysis as `([source](url))`.
If a source is a local raw/ file with no URL, cite it as `(raw/filename)`.

---

## Pass 1 — The irreducible constraint

What physical or mathematical law makes this problem hard in a way no engineering escapes?
State the fundamental tension: the two things you cannot simultaneously have, and why.

*One paragraph max. No hedging. No solution names yet.*

---

## Pass 2 — Forced vs. chosen

For each major design decision in the approach:
- **Forced** — any valid solution must do this because the constraint leaves no room
- **Chosen** — this solution did X; Y was also possible; the difference is the assumption that X's dominant case holds

*Bullet list. One line per decision. Cite the wiki page where this decision is described.*

Format per bullet:
`[forced/chosen] <decision> — <one-sentence reason> ([source](url))`

---

## Pass 3 — What moved

Every design choice that solves Pass 1's constraint moves cost somewhere else.
Find where. Not failure modes — *cost displacements*.

Format: `Solved <X> by moving cost to <Y>` — one line each.
Cite the page that describes X. ([source](url))

Then: what new assumption is now load-bearing?
One line per assumption.

---

## Pass 4 — Adversarial

Build the strongest case that the approach is right for narrower reasons than claimed,
or that the framing of Pass 1 is itself wrong.

Three questions only:
1. Is the constraint in Pass 1 actually the binding one, or is there a prior?
2. Does the dominant-case assumption in Pass 2 hold in practice, or only in benchmarks?
3. What is the real ceiling — the structural reason improvement terminates, not a number?

*Three answers, three sentences max each.*

---

## Pass 5 — Synthesis

What is actually true, in plain reasoning chains.
A claim is allowed only if it follows from Pass 1 by logical steps.
Resolve contradictions between passes explicitly.

Format: prose, not bullets. Short paragraphs.
Every sentence answers "why must this be?" not "what did we observe?"
Link each paragraph's grounding claim to its source: ([source](url))

End with one sentence:
**The one thing that, if it changed, would make this approach obsolete:**
State the *condition*, not a technology name.

---

## Final output

Write to: `output/analysis-<topic-slug>-<YYYY-MM-DD>.md`

At the top of the file, include a **Sources** section listing all URLs collected in Step 0.

After writing, tell the user:
- The finding in Pass 5 most absent from the wiki's framing
- The adversarial challenge in Pass 4 you found hardest to rebut
- Ask: "Should I distill any of this into wiki pages?"

Do NOT commit output/ to git.
Do NOT touch wiki/ until the user says yes.
