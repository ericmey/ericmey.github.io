---
title: openclaw-musubi
summary: A first-class memory provider for OpenClaw agents, backed by Musubi. Every completed turn is committed to a durable outbox, with semantic recall, exact reads and deliberate stores.
order: 30
tags: [typescript, plugin, memory, agents]
links:
  - { label: GitHub, url: 'https://github.com/ericmey/openclaw-musubi' }
  - { label: npm, url: 'https://www.npmjs.com/package/openclaw-musubi' }
---

The TypeScript plugin that takes OpenClaw's exclusive memory slot and routes it through [Musubi](/projects/musubi). Each completed turn is written to a local SQLite outbox before the agent's turn hook returns, so a Musubi outage delays memory instead of losing it. It lives in its own repository, following Musubi's rule that non-Python integrations ship in their host ecosystem's own package format and release cycle.
