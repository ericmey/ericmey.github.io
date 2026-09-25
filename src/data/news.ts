// Dated milestones for the News list. Articles are added automatically from the
// writing collection; list here only milestones that are not articles, and link
// each to something a reader can check.
export interface NewsItem { date: string; text: string; url?: string }

export const NEWS: NewsItem[] = [
  {
    date: '2026-09-25',
    text: 'Musubi gains a CPU-only quickstart, proven in CI: two agents share memory, and scopes hold.',
    url: 'https://github.com/ericmey/musubi/pull/825',
  },
  {
    date: '2026-09-24',
    text: 'Published the five-lane router model and its 2,334-row dataset on Hugging Face.',
    url: 'https://huggingface.co/ericmey/five-lane-router-modernbert-large',
  },
];
