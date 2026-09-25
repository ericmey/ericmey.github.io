import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

// One Markdown file per project. Adding a finished project = adding one file.
const projects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(), // one sentence, shown on cards
    order: z.number().default(100), // lower = earlier on the page
    featured: z.boolean().default(false),
    status: z.enum(['active', 'maintained', 'archived']).default('active'),
    tags: z.array(z.string()).default([]),
    links: z
      .array(z.object({ label: z.string(), url: z.url() }))
      .default([]),
    // Every public claim on a project page should point at something a reader can check.
    evidence: z
      .array(z.object({ claim: z.string(), url: z.url() }))
      .default([]),
  }),
});

// One Markdown file per article. External articles (HF, LinkedIn) just carry `url`.
const articles = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/articles' }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    date: z.coerce.date(),
    venue: z.string(), // e.g. "Hugging Face", "LinkedIn"
    url: z.url().optional(), // external home of the article, if any
    tags: z.array(z.string()).default([]),
    draft: z.boolean().default(false),
  }),
});

export const collections = { projects, articles };
