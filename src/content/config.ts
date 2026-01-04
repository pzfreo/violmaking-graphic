import { defineCollection, z } from 'astro:content';

const speakers = defineCollection({
  type: 'data',
  schema: z.object({
    name: z.string(),
    event: z.string(),
    talkTitle: z.string(),
    talkSubtitle: z.string().optional(),
    hasPerformance: z.boolean().default(false),
    timeSlot: z.string(),
    photo: z.string().optional(),
    instruments: z.array(z.object({
      image: z.string(),
      caption: z.string(),
    })).optional(),
  }),
});

export const collections = { speakers };
