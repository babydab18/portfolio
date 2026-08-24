# Ranvir Chennupalli Portfolio

Static GitHub Pages portfolio. No build step or dependencies are required.

## Current structure

- `index.html` — homepage
- `resume.html` — resume page (expects `resume.pdf` in the root)
- `projects.html` — top-level project/research index
- `sailor-rover.html` — grouped Sailor Rover research overview
  - `project-windprofiler.html`
  - `project-windchamber.html`
  - `project-rover-controls.html`
- `project-archimedes-propeller.html`
- `project-clearwater-uav.html`
- `project-wildlife-mapper.html`
- `images/` — site images and project media
- `docs/` — linked paper/document files

The Sailor Rover work is intentionally grouped under one top-level tab and one project tile, with sublinks to its three technical workstreams.

## Before publishing

1. Add your latest resume PDF as `resume.pdf` in the root folder.
2. Replace the remaining LinkedIn `href="#"` placeholders with your LinkedIn URL.
3. Open `index.html` locally to check the site.

## Push to GitHub

If this folder is replacing the contents of your existing `babydab18/portfolio` repo, copy these files into your local repo, then run:

```bash
git add .
git commit -m "Group Sailor research and add project media"
git push origin main
```

For a brand-new local clone:

```bash
git init
git add .
git commit -m "Publish aerospace portfolio"
git branch -M main
git remote add origin https://github.com/babydab18/portfolio.git
git push -u origin main
```

Then enable GitHub Pages from **Settings → Pages → Deploy from a branch → main → /(root)**.
