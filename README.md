# ericmey.github.io

Portfolio site for Eric Mey: projects, writing, and the evidence behind them. Built with [Astro](https://astro.build) and deployed to GitHub Pages by `.github/workflows/deploy.yml`.

## Add a project

Create `src/content/projects/<slug>.md`:

```markdown
---
title: My project
summary: One sentence, shown on the card.
order: 60            # lower appears first
featured: false      # true = shown on the home page
tags: [python, evals]
links:
  - { label: GitHub, url: 'https://github.com/...' }
evidence:            # every public claim should point at something checkable
  - { claim: 'Eval report and raw predictions', url: 'https://...' }
---

Body in Markdown.
```

## Import published articles

Articles Eric has published (LinkedIn, Hugging Face) live as packets on the posted shelf
(`~/Vaults/Eric/Journal/Publications/posted/YYYYMMDD-slug/`). Pull them in, with covers:

```bash
uv run --with pillow --with pyyaml python scripts/import_posted.py
```

This regenerates `src/content/articles/<slug>.md` and `public/covers/<slug>.webp` from the
shelf, so re-running is safe. Commit the result.

## Add an article by hand

Create `src/content/articles/<slug>.md`. For an article published elsewhere, set `url` and leave the body empty. For one hosted here, omit `url` and write the body.

```markdown
---
title: Why evals matter
summary: One or two sentences.
date: 2026-10-01
venue: LinkedIn
url: 'https://...'
---
```

The build validates every front-matter field, so a typo fails the build instead of the site.

## Develop

```bash
npm ci
npm run dev      # http://localhost:4321
npm run build    # static output in dist/
```

Site-wide name, tagline and links live in `src/site.ts`. Dated milestones for the home-page
News list live in `src/data/news.ts` (published articles are added to News automatically).

## Design

Graphite and amber, taken from Eric's profile banner. Tokens are at the top of
`src/styles/global.css`. `--amber` is decorative (rules, glows, buttons), and `--amber-text` is
the AA-contrast variant for any amber text. Fonts are self-hosted via Fontsource:
Fraunces (display), Inter (body), JetBrains Mono (meta), all OFL. The theme toggle persists
in `localStorage` and defaults to the OS preference.
