---
title: Give Your Coding Agent a Maintained Map
summary: A small, reviewable knowledge vault can give a coding agent the right architecture and decisions without asking it to trust stale notes over the code.
date: 2026-09-28
venue: Portfolio
tags: [context engineering, developer tools, coding agents]
---

A coding agent can read a repository, but a fresh session does not know which files explain the system, which decisions are still in force, or which tempting approach already failed. It can reconstruct some of that from code and history. Repeating that work on every task costs time, and the reconstruction can be wrong.

I use a **maintained map**: a small collection of Markdown files that tells the agent where to look and how to check what it finds. This grew out of a lesson I led for engineers on using an Obsidian vault with Claude Code. The useful part is not Obsidian itself. It is the discipline of making context inspectable, versioned, and subordinate to the running system.

## The shape

The entry point should be short. It points to the few documents needed to begin, then routes the agent to more detail only when the task calls for it. A sample structure might look like this:

```text
AGENTS.md                 # short entry point and reading order
knowledge/
  architecture.md         # components and boundaries
  decisions/              # why important choices were made
  workflows/              # build, test, release, recovery
  gotchas/                # failures worth not repeating
sources/                  # immutable imports or raw evidence
```

The folder names matter less than their roles. Keep raw sources separate from your interpretation of them. Record when a claim was last checked, and link it to a file, test, ticket, or other evidence. Put task procedures near the decisions they depend on. Keep the entry point small enough that an agent can load it without drowning in context.

For example, if the task is to add an OAuth callback, the map can point to the existing authentication boundary, the callback tests, and a decision explaining why tokens are stored in one service. The agent still has to inspect the current code. The map narrows the search; it does not answer the task by authority.

## The authority rule

The vault is useful precisely because it can be challenged. A note may describe yesterday's architecture. Code, configuration, tests, and live behavior show what exists now. When they disagree, investigate the difference and update the note. Do not make the code conform to an obsolete page just because the page sounds confident.

That calls for a simple review loop:

1. Find the relevant note and its cited source.
2. Check the current implementation and tests.
3. Make the change and run the appropriate verification.
4. Update the note when the change alters a durable decision or procedure.

Versioning the vault with the project makes this loop easier. A reviewer can see when a document changed, compare it with the code change, and catch an invented or stale claim. Lint can check structure and links; people still have to judge truth.

## What this does and does not show

This approach aims to reduce repeated context loading and corrections. I do **not** have a controlled productivity result for it, and a vault is not a guarantee that an agent will make a good decision. It can fail by collecting stale notes, summarizing evidence incorrectly, or loading so much material that the relevant constraint disappears in the noise.

Start with one real task. Write a short entry point, one architecture page, and one decision or gotcha the agent would otherwise rediscover. Ask an agent to work from those files, then inspect where it still searched, guessed, or contradicted the code. Improve the map from that observation. A useful vault is a maintained part of the engineering system, not a one-time upload of documentation.

The lesson drew on public work such as [AgriciDaniel's Claude–Obsidian example](https://github.com/AgriciDaniel/claude-obsidian). The structure here is one way to apply that pattern in a software repository; the checks and ownership rules are the part I would keep even if the editor or agent changes.
