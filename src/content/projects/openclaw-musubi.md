---
title: openclaw-musubi
summary: A first-class memory provider for OpenClaw agents, backed by Musubi. Every completed turn is committed to a durable outbox, with semantic recall, exact reads and deliberate stores.
order: 30
tags: [typescript, plugin, memory, agents]
links:
  - { label: GitHub, url: 'https://github.com/ericmey/openclaw-musubi' }
  - { label: npm, url: 'https://www.npmjs.com/package/openclaw-musubi' }
---

The TypeScript plugin that takes OpenClaw's exclusive memory slot and routes it through [Musubi](/projects/musubi). Each completed turn is written to a local SQLite outbox before the agent's turn hook returns. Failed deliveries are retried, and ones that stay blocked are held for an operator instead of being silently dropped. It lives in its own repository, following Musubi's [ADR 0022](https://github.com/ericmey/musubi/blob/main/docs/Musubi/13-decisions/0022-extension-ecosystem-naming.md): non-Python integrations live in sibling `<system>-musubi` repositories on their host ecosystem's release cycle.
