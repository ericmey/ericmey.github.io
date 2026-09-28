// Dated milestones for the News list. Articles are added automatically from the
// writing collection; list here only milestones that are not articles, and link
// each to something a reader can check.
export interface NewsItem { date: string; text: string; url?: string }

export const NEWS: NewsItem[] = [
  {
    date: '2026-09-28',
    text: 'Released Musubi harness 1.7.0, the shared runtime for host integrations.',
    url: 'https://github.com/sourceblender/musubi-harness/releases/tag/v1.7.0',
  },
  {
    date: '2026-09-28',
    text: 'Published the first Musubi Grok plugin release.',
    url: 'https://github.com/sourceblender/musubi-grok/releases/tag/v0.1.0',
  },
  {
    date: '2026-09-24',
    text: 'Published the five-lane router model and its 2,334-row dataset on Hugging Face.',
    url: 'https://huggingface.co/ericmey/five-lane-router-modernbert-large',
  },
];
