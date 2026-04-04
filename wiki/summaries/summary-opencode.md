---
title: "Summary — anomalyco/opencode: Open Source Coding Agent"
type: summary
status: draft
created: 2026-04-04
updated: 2026-04-04
sources:
  - raw/anomalycoopencode The open source coding agent..md
  - https://github.com/anomalyco/opencode
  - https://opencode.ai/
tags: []
---

# Summary — anomalyco/opencode: Open Source Coding Agent

## Source Metadata

| Field        | Value                                                       |
|--------------|-------------------------------------------------------------|
| Source type  | web / github / open source project                         |
| Author(s)    | AnomalyCo                                                   |
| Year         | 2025                                                        |
| Venue        | GitHub (open source)                                        |
| Raw file     | `raw/anomalycoopencode The open source coding agent..md`   |

## Main Idea

OpenCode is a 100% open-source AI coding agent that is provider-agnostic (works with Claude, OpenAI, Google, or local models), TUI-focused (built by neovim users), and built on a client/server architecture enabling remote control from mobile or other frontends.

## Key Details

- **Installation**: YOLO install script, npm, Homebrew, Scoop, Arch Linux, Nix, mise
- **Desktop app**: BETA—dmg/exe/AppImage available for download
- **Two built-in agents**:
  - `build` — default, full-access for development
  - `plan` — read-only, analysis and code exploration; denies edits, asks permission for bash
- **General subagent**: for complex searches and multi-step tasks; invoked via `@general`
- **Provider-agnostic**: recommended models through OpenCode Zen, but can use Claude, OpenAI, Google, or local models
- **Out-of-the-box LSP support**: Language Server Protocol for code navigation
- **Client/server architecture**: TUI is just one possible frontend; can run headless with remote clients
- **Documentation**: opencode.ai/docs
- **Languages**: 15+ translated READMEs (Chinese, Korean, German, French, Japanese, etc.)
- **Discord community**: available at discord.gg/opencode

## Method / Approach

OpenCode positions itself as a fully open alternative to Claude Code. The client/server architecture decouples the agent runtime (server) from the user interface (client), enabling scenarios like running the agent on a remote machine while controlling it from a mobile app. The TUI is purpose-built for terminal enthusiasts, with deep integration into filesystem and LSP tooling.

## Results / Evidence

No benchmark results are provided; OpenCode is an open-source engineering project rather than a research contribution.

## Limitations

- Desktop app is still in BETA
- Client/server security model for remote operation is [UNVERIFIED] in detail
- Being fully open source means slower feature development compared to well-funded competitors

## Links to Concepts

- [[Agent Harness]] — OpenCode is itself a coding agent harness
- [[Provider-Agnostic Agents]] — key differentiator from Claude Code
- [[LSP Integration]] — out-of-the-box Language Server Protocol support

## Links to Topics

- [[AI Agents]]
- [[Coding Agents]]

## Quotes Worth Preserving

> It's very similar to Claude Code in terms of capability. Here are the key differences: 100% open source; Not coupled to any provider; Out-of-the-box LSP support; A focus on TUI; A client/server architecture.
