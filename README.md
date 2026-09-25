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

## Add an article

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

Site-wide name, tagline and links live in `src/site.ts`.
