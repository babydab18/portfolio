# Ranvir Chennupalli Portfolio — Ready to Publish

This folder is cleaned up for GitHub Pages. The files no longer have `(1)` in their names, the headshot is wired into the homepage, the two supplied wind-chamber images are on the Wind Chamber project page, the AIAA paper is linked from the Archimedes Propeller project page, and the GitHub icon points to this repository:

https://github.com/babydab18/portfolio

## Folder structure

- `index.html` — homepage
- `projects.html` — project grid
- `project-*.html` — individual project pages
- `resume.html` — resume page
- `style.css` — styling
- `images/` — headshot and project images
- `docs/` — AIAA paper
- `resume.pdf` — ADD THIS FILE before publishing if you want the Resume button to work

## Publish to the existing GitHub repository

Open PowerShell or Git Bash inside this folder and run:

```bash
git init
git add .
git commit -m "Publish aerospace portfolio"
git branch -M main
git remote add origin https://github.com/babydab18/portfolio.git
git push -u origin main
```

If the repository already has files/history and the push is rejected, clone the repository first, copy these files into the cloned folder, then commit and push:

```bash
git clone https://github.com/babydab18/portfolio.git
cd portfolio
# copy the contents of this folder here
git add .
git commit -m "Update portfolio site"
git push origin main
```

Then in GitHub go to **Settings → Pages → Build and deployment → Deploy from a branch**, choose **main** and **/(root)**, then Save.

Your Pages URL will usually be:

`https://babydab18.github.io/portfolio/`

## Add the portfolio to your resume

In the contact/header line of your resume, add a short link such as:

`Portfolio: babydab18.github.io/portfolio`

For a DOCX resume, select that text, press **Ctrl+K**, and hyperlink it to:

`https://babydab18.github.io/portfolio/`

Export the resume to PDF afterward and confirm the link is clickable.

## Still needed

1. Add your actual `resume.pdf` to this folder.
2. Replace the LinkedIn `#` placeholders with your real LinkedIn URL.
3. Add more project images to the remaining project pages whenever you have them.
