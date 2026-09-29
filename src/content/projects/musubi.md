---
title: Musubi
summary: Shared storage and retrieval for agent observations and context, with a path from raw captures to human-reviewed notes.
order: 20
featured: true
tags: [memory, retrieval, qdrant, hybrid-search, agents, python]
links:
  - { label: GitHub, url: 'https://github.com/ericmey/musubi' }
  - { label: Host plugins, url: 'https://github.com/sourceblender/musubi-harness' }
evidence:
  - { claim: 'Architecture decisions (ADRs)', url: 'https://github.com/ericmey/musubi/tree/main/docs/Musubi/13-decisions' }
  - { claim: 'Evaluation workflow and benchmark code', url: 'https://github.com/ericmey/musubi/blob/main/.github/workflows/evals.yml' }
---

Musubi is a memory server for the point where one assistant is not enough. Several agents can capture observations and retrieve relevant context through one API while keeping namespace and access boundaries. The server and [host integrations](/projects/musubi-ecosystem) are public, with separate release paths.

- **Three planes.** *Episodic* holds raw captures, scored for importance. *Concept* holds themes synthesized nightly from matured episodics. *Curated* holds notes that clear a promotion gate and are written to an Obsidian vault, where a human reviews and edits them. Edits flow back.
- **A lifecycle engine**: maturation, synthesis, promotion, demotion and reflection sweeps. Each one is file-locked, idempotent, and journaled.
- **Hybrid retrieval.** Dense and sparse vectors in Qdrant with a reranker, served by TEI, with fast and deep retrieval paths.
- **Per-namespace auth**: a token grants `r`, `w` or `rw` on namespace patterns, plus a separate `operator` scope ([scope checks](https://github.com/ericmey/musubi/blob/main/src/musubi/auth/scopes.py)).
- **Evaluation.** A CI retrieval benchmark checks changes against a recorded baseline and keeps regressions visible for investigation.

Python 3.12, pydantic v2, strict mypy, FastAPI, Docker Compose, and Ansible for managed hosts.
