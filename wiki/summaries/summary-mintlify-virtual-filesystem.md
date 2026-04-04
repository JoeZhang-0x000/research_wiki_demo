---
title: Summary — Building a Virtual Filesystem for Mintlify's AI Assistant
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/building-a-virtual-filesystem-for-mintlifys-2026-04-03.md
  - "https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant"
links:
  - "https://x.com/densumesh/status/2039765361533637016"
tags: [ai-agents, retrieval, filesystem, docs]
---

# Summary — Building a Virtual Filesystem for Mintlify's AI Assistant

## Source Metadata

| Field | Value |
|-------|-------|
| Source type | blog |
| Author(s) | Densumesh |
| Year | 2026 |
| Venue | Mintlify blog / X thread |
| Raw file | `raw/building-a-virtual-filesystem-for-mintlifys-2026-04-03.md` |

## Main Idea

Mintlify replaced per-session documentation sandboxes with a virtual filesystem called ChromaFs that projects its indexed docs store into shell-like file operations. The result is a filesystem-style agent interface with roughly 100 ms session startup instead of about 46 seconds for sandbox creation.

## Key Details

- The motivating failure mode is chunk-only retrieval: exact syntax or multi-page answers can be missed when the answer does not appear in a top-k result
- The design goal is to let the agent navigate docs with familiar primitives such as `grep`, `cat`, `ls`, and `find`
- ChromaFs is built on Vercel Labs' `just-bash`, which provides shell parsing and built-in command behavior behind a pluggable filesystem API
- The system stores a gzipped JSON path tree in Chroma, expands it into in-memory file and directory maps, and filters it by user permissions before use
- `readFile` reconstructs full pages by fetching all chunks for a page slug, sorting by `chunk_index`, and joining them into a single document
- Recursive grep is optimized as a two-stage retrieval path: Chroma coarse filtering followed by in-memory grep over a prefetched candidate set
- All write operations return read-only filesystem errors so the assistant can browse but not mutate docs

## Method / Approach

The core move is to preserve the agent's filesystem mental model while changing the substrate underneath it. Instead of provisioning a real repo clone, Mintlify virtualizes filesystem calls over the same Chroma collection already used for search. Startup-sensitive operations stay in memory, while document reads and grep candidates are resolved against the indexed store and cached.

## Results / Evidence

- Reported p90 sandbox session creation time dropped from about 46 seconds to about 100 milliseconds
- The writeup estimates that a naive sandbox-per-conversation approach at 850,000 monthly conversations would exceed $70,000 per year under the cited Daytona pricing model
- The system is described as serving hundreds of thousands of users across 30,000+ conversations per day

## Limitations

- The source focuses on read-only documentation access rather than general code execution, so the abstraction does not replace full sandboxes for mutable workflows
- The grep optimization depends on custom interception logic rather than plain shell semantics end to end
- Cost and performance figures are presented by the system authors and are not independently benchmarked in the source

## Links to Concepts

- [[virtual-filesystem-interface]] — the source is a concrete implementation of the abstraction
- [[markdown-knowledge-base]] — argues that file-like navigation is a strong interface for agents
- [[graph-rag]] — uses indexed retrieval as a coarse filter beneath a filesystem projection

## Links to Topics

- [[markdown-knowledge-bases]]
- [[graph-rag-systems]]

## Quotes Worth Preserving

> Agents are converging on filesystems as their primary interface.
