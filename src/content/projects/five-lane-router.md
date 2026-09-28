---
title: Five-lane request router
summary: A published ModernBERT classifier that routes requests among five task paths, with its training data, evaluation and tutorial.
order: 10
featured: true
tags: [text-classification, modernbert, edge, evals, jetson]
links:
  - { label: Model on Hugging Face, url: 'https://huggingface.co/ericmey/five-lane-router-modernbert-large' }
  - { label: Dataset, url: 'https://huggingface.co/datasets/ericmey/five-lane-router' }
  - { label: Tutorial, url: 'https://huggingface.co/blog/ericmey/train-your-own-request-router' }
evidence:
  - { claim: 'Model card, results and limits', url: 'https://huggingface.co/ericmey/five-lane-router-modernbert-large' }
  - { claim: '2,334 hand-labelled training rows, with the labelling rules', url: 'https://huggingface.co/datasets/ericmey/five-lane-router' }
  - { claim: 'Public eval, raw predictions and rerun instructions', url: 'https://huggingface.co/blog/ericmey/train-your-own-request-router' }
---

A personal AI assistant was routing every request through a 9B generative model just to select a processing path: `chat`, `image`, `search`, `audio` or `video`. I fine-tuned ModernBERT-large for that classification task and integrated it as a TensorRT FP16 engine on an NVIDIA Jetson Orin Nano. At the model-card release, the 9B model still served live traffic.

**Public, rerunnable evaluation:** on a frozen 60-row authored challenge, the pinned router scored **58 / 60** against **46 / 60** for a predeclared TF-IDF baseline. The [tutorial](https://huggingface.co/blog/ericmey/train-your-own-request-router) includes the scoring steps and raw results. It is a teaching and regression set, authored with knowledge of the label rules, not an independent blind holdout or live-traffic sample.

**Separate sealed comparison:** the [model card](https://huggingface.co/ericmey/five-lane-router-modernbert-large) also reports 60 held-out cases, run three times for each router: 180 / 180 correct calls for ModernBERT and 175 / 180 for the 9B router. Client-side p50 / p95 latency was 42 / 45.6 ms versus 771 / 1,269 ms on different hardware. That comparison is one authored test set, not a production soak or a general model-speed benchmark.

**What I'd point a reviewer at:** the failure that shaped the data. An earlier candidate failed its sealed test by sending a chat request that *mentioned* drawing to `image`. The fix was 253 contrast rows written for that failure shape, without seeing the failing prompts, followed by a fresh sealed test.
