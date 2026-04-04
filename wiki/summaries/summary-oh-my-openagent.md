---
title: "Summary — code-yeongyu/oh-my-openagent (omo): Agent Harness Plugin"
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/code-yeongyu-oh-my-openagent-omo-the-best-agent-harness-2026-04-04.md
  - "https://github.com/code-yeongyu/oh-my-openagent"
links:
  - "https://github.com/code-yeongyu/oh-my-openagent"
tags: []
---

# Summary — code-yeongyu/oh-my-openagent (omo): Agent Harness Plugin

## Source Metadata

| Field        | Value                                                                       |
|--------------|-----------------------------------------------------------------------------|
| Source type  | web / github / open source plugin                                          |
| Author(s)    | code-yeongyu (yeon gyu kim)                                                 |
| Year         | 2025–2026                                                                   |
| Venue        | GitHub (open source plugin for OpenCode)                                   |
| Raw file     | `raw/code-yeongyu-oh-my-openagent-omo-the-best-agent-harness-2026-04-04.md` |

## Main Idea

Oh My OpenCode (OmO / oh-my-openagent) is an OpenCode plugin that orchestrates multiple specialized discipline agents (Sisyphus as main orchestrator, Hephaestus as deep worker, Prometheus as planner, Oracle/Librarian/Explore as specialists) to function as a complete AI dev team, featuring a hash-anchored edit tool (Hashline), LSP/AST-Grep integration, built-in MCPs, skill-embedded MCPs, and the `ultrawork` command for aggressive parallel task completion.

## Key Details

**Discipline Agents**:

| Agent | Default Model | Role |
|-------|--------------|------|
| **Sisyphus** | claude-opus-4-6 / kimi-k2.5 / glm-5 | Main orchestrator; drives tasks to completion with aggressive parallel execution |
| **Hephaestus** | gpt-5.4 | Autonomous deep worker; explores, researches, executes end-to-end |
| **Prometheus** | claude-opus-4-6 / kimi-k2.5 / glm-5 | Strategic planner; interview mode before execution |
| **Oracle** | — | Architecture and debugging |
| **Librarian** | — | Docs and code search |
| **Explore** | — | Fast codebase grep |

**Hashline Edit Tool** (inspired by oh-my-pi):
- Every line read comes back tagged with a content hash
- Agent edits by referencing those hash tags
- Stale-line errors eliminated—edit rejected if file changed since last read
- Result: Grok Code Fast 1 success rate improved from 6.7% to 68.3% just from the edit tool change

**Ultrawork** (`ultrawork` / `ulw`):
- Single command; activates all agents
- Doesn't stop until task is 100% complete
- Includes Ralph Loop (self-referential continuation) and Todo Enforcer (idle agent yanked back)

**Tool Stack**:
- LSP: `lsp_rename`, `lsp_goto_definition`, `lsp_find_references`, `lsp_diagnostics`
- AST-Grep: Pattern-aware code search/rewrite across 25 languages
- Tmux: Full interactive terminal, REPLs, debuggers, TUIs
- Built-in MCPs: Exa (web search), Context7 (official docs), Grep.app (GitHub search)

**Skill-Embedded MCPs**:
- Skills carry their own MCP servers; spin up on-demand, scoped to task, gone when done
- Context window stays clean

**Model Routing**:
- Agent picks a **category** (visual-engineering, deep, quick, ultrabrain) not a model
- Category maps automatically to the right model per configuration
- `ultrabrain` routes to GPT-5.4 xhigh by default

**Context Injection**:
- Auto-injects AGENTS.md, README.md, conditional rules
- `/init-deep` generates hierarchical AGENTS.md throughout project

**Claude Code Compatibility**:
- Full compatibility with hooks, commands, skills, agents, MCPs, plugins

## Method / Approach

OmO is a plugin for OpenCode (not a standalone harness) that layers on sophisticated orchestration. The key innovation is the Hashline edit tool, which solves the "harness problem" (most agent failures are in the edit tool, not the model). The self-referential Ralph Loop keeps agents working until 100% done rather than stopping at a reasonable-looking stopping point.

## Results / Evidence

- Grok Code Fast 1: 6.7% → 68.3% success rate (Hashline edit tool only)
- Claims Kimi K2.5 + GPT-5.4 beats vanilla Claude Code with zero config
- $24K token spend by maintainer distilled into the plugin's design

## Limitations

- OpenCode plugin dependency—cannot be used standalone
- Heavily opinionated defaults; less flexible for different workflows
- Some features (Prometheus planner interview mode) add latency to task start

## Links to Concepts

- [[agent-harness]] — oh-my-openagent is a plugin harness for OpenCode
- [[hashline-edit-tool]] — hash-anchored content-addressed edits solving stale-line problem
- [[discipline-agents]] — multiple specialized agents with distinct roles
- [[ultrawork]] — aggressive parallel task completion mode
- [[skill-embedded-mcps]] — MCP servers bundled with skills

## Links to Topics

- [[ai-agents]]
- [[coding-agents]]

## Quotes Worth Preserving

> The harness problem is real. Most agent failures aren't the model. It's the edit tool.

> "None of these tools give the model a stable, verifiable identifier for the lines it wants to change... They all rely on the model reproducing content it already saw." — Can Bölük, The Harness Problem
