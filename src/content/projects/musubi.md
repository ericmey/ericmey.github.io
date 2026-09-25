---
title: Musubi
summary: Shared memory for a small fleet of AI agents. It has three planes (episodic, concept, curated) and a lifecycle engine that matures raw captures into a human-reviewable knowledge base.
order: 20
featured: true
tags: [memory, retrieval, qdrant, hybrid-search, agents, python]
links:
  - { label: GitHub, url: 'https://github.com/ericmey/musubi' }
evidence:
  - { claim: 'Architecture decisions (ADRs)', url: 'https://github.com/ericmey/musubi/tree/main/docs/Musubi/13-decisions' }
  - { claim: 'Signed, SBOM-attested release images', url: 'https://github.com/ericmey/musubi/releases' }
---

Musubi is a memory server for the point where one assistant is not enough. It lets several agents, each with its own role, share what they learn through one API.

- **Three planes.** *Episodic* holds raw captures, scored for importance. *Concept* holds themes synthesized nightly from matured episodics. *Curated* holds notes that clear a promotion gate and are written to an Obsidian vault, where a human reviews and edits them. Edits flow back.
- **A lifecycle engine**: maturation, synthesis, promotion, demotion and reflection sweeps. Each one is file-locked, idempotent, and journaled.
- **Hybrid retrieval.** Dense and sparse vectors in Qdrant with a reranker, served by TEI, with fast and deep retrieval paths.
- **Per-namespace auth**: a token grants `r`, `w` or `rw` on namespace patterns, plus a separate `operator` scope ([scope checks](https://github.com/ericmey/musubi/blob/main/src/musubi/auth/scopes.py)).
- **Supply chain.** Every published image is cosign-signed by digest, Trivy-scanned, and ships with a CycloneDX SBOM.

Python 3.12, pydantic v2, strict mypy, FastAPI, Docker Compose, and Ansible for managed hosts.
