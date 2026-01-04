# Viol Making Symposium

Website for the Viol Making Symposium at West Dean College.

Built with [Astro](https://astro.build) and [Tailwind CSS](https://tailwindcss.com).

## Development

```bash
npm install
npm run dev
```

## Build

```bash
npm run build
```

## Deployment

Deployed automatically to Netlify on push to `main`.

## Adding Content

### Speaker Data
Speaker information is stored in `src/content/speakers/` as YAML files, organized by year.

### Gallery Images
Add instrument photos to `public/images/instruments/` and update `src/pages/gallery.astro`.

### Instagram Feed
To enable the Instagram feed, sign up at [behold.so](https://behold.so), connect the @viol.making account, and add your feed ID to `src/components/InstagramFeed.astro`.
