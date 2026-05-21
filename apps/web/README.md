# Smart Housing — Frontend (GitHub Pages)

This app is configured to build a static site in `docs/` so it can be served by GitHub Pages.

Quick steps to publish to GitHub Pages (user site: `aitor-alcazar.github.io/smart-housing`):

1. Configure `vite.config.ts` base path (already set to `/smart-housing/`).
2. Build the site:

```bash
cd apps/web
npm install
npm run build
```

3. Commit and push the generated `docs/` folder to the `main` branch. Then enable GitHub Pages for the repository and set source to `main` / `docs` folder.

Notes:
- The project uses Vite + React + Tailwind; keep `postcss.config.js` and `tailwind.config.ts` if you use Tailwind.
- If you prefer automatic deployments, consider using `gh-pages` or a CI workflow to push `docs/` to the repo.
