---
title: Musubi runtime and host plugins
summary: An open-source harness and separate plugins that connect Musubi memory to Claude Code, Codex, Grok, Hermes and OpenClaw.
order: 25
featured: true
cover: /diagrams/musubi-ecosystem.svg
tags: [agents, memory, plugins, python, typescript]
links:
  - { label: Shared harness, url: 'https://github.com/sourceblender/musubi-harness' }
  - { label: Sourceblender org, url: 'https://github.com/sourceblender' }
evidence:
  - { claim: 'Harness releases and installation instructions', url: 'https://github.com/sourceblender/musubi-harness/releases' }
  - { claim: 'Claude Code plugin', url: 'https://github.com/sourceblender/musubi-claude' }
  - { claim: 'Codex plugin', url: 'https://github.com/sourceblender/musubi-codex' }
  - { claim: 'Grok plugin', url: 'https://github.com/sourceblender/musubi-grok' }
  - { claim: 'Hermes plugin', url: 'https://github.com/sourceblender/musubi-hermes' }
  - { claim: 'OpenClaw plugin', url: 'https://github.com/sourceblender/musubi-openclaw' }
---

[Musubi](/projects/musubi) is the memory server. The shared harness provides a host-neutral capture and delivery contract, while each plugin adapts that contract to the events and APIs its host actually exposes. That split lets each integration follow its host's installation and release path.

The five linked plugins are separate repositories. Features differ by host: do not assume an install path, automatic capture, or a release in one host applies to another. Start with the repository for the host you use. The harness is [published on PyPI](https://pypi.org/project/musubi-harness/); OpenClaw's package is [on npm](https://www.npmjs.com/package/openclaw-musubi).

The capture contract, evaluation and failure paths matter because agent memory only helps if a missed turn is visible and recoverable. The linked repositories show the implementation and tests.
