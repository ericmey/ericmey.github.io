---
title: Five-lane request router
summary: A ModernBERT-large classifier that decides what kind of answer a request needs (chat, image, search, audio or video) before any larger model runs, on a Jetson Orin Nano.
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
---

A personal AI assistant was routing every request through a 9B generative model just to decide *what kind* of answer to produce. This project replaces that step with a fine-tuned ModernBERT-large classifier running as a TensorRT FP16 engine on an NVIDIA Jetson Orin Nano.

**What was measured, quoted from the model card:** both routers were run on the same 60 held-out cases, three times each. The cases were sealed before training, leak-checked, and used once. The classifier routed **180 / 180** correctly against **175 / 180** for the 9B router, at **42 / 45.6 ms** p50 / p95 client-side latency against 771 / 1,269 ms.

**What that does not show,** also from the card: it is one sealed set of 60 authored cases, not a production soak. The two routers ran on different hardware, so the latency compares routing calls in one setup, not model speed. And at release the 9B was still routing production.

**What I'd point a reviewer at:** the failure that shaped the data. An earlier candidate failed its sealed test by sending a chat request that *mentioned* drawing to `image`. The fix was 253 contrast rows written for that failure shape, without seeing the failing prompts, followed by a fresh sealed test.
