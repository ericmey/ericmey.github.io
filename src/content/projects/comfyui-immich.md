---
title: comfyui-immich
summary: ComfyUI custom nodes that save generated images to a self-hosted Immich library, with prompt and workflow metadata, albums and a connection-status panel.
order: 40
tags: [comfyui, python, immich, image-generation]
links:
  - { label: GitHub, url: 'https://github.com/ericmey/comfyui-immich' }
---

It uploads each render to [Immich](https://immich.app) as it's produced. A local preview is written first, so an Immich outage doesn't lose a render. The API key never becomes a node input, so it never lands in workflow JSON or PNG metadata.

A 2026 security pass found and fixed two issues:
- an import-time network patch that could downgrade other code's HTTPS to plaintext;
- redirects that could carry the API key to another host.

Both are covered by regression tests that fail against the old code. The settings panel is read-only by design, because ComfyUI has no authentication by default.
