---
title: Musubi for OpenClaw
summary: A first-class memory provider for OpenClaw agents, backed by Musubi. Eligible completed turns are committed to a durable outbox, with semantic recall, exact reads and deliberate stores.
order: 30
cover: /diagrams/openclaw-musubi.svg
tags: [typescript, plugin, memory, agents]
links:
  - { label: GitHub, url: 'https://github.com/sourceblender/musubi-openclaw' }
  - { label: npm, url: 'https://www.npmjs.com/package/openclaw-musubi' }
---

The TypeScript plugin takes OpenClaw's memory slot and routes it through [Musubi](/projects/musubi). Eligible completed turns enter a local SQLite outbox before delivery; failed deliveries can be retried. The package is [published on npm](https://www.npmjs.com/package/openclaw-musubi). The repository also carries newer source changes, so check the npm version before assuming the published package matches its main branch. It is one member of the [Musubi plugin family](/projects/musubi-ecosystem).
