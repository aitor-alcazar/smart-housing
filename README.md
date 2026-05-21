# Smart Housing

Smart Housing is an AI-assisted property viability analysis MVP with a **static GitHub Pages frontend** and a **FastAPI backend**.

## Architecture

```txt
apps/web   -> Vite + React + TypeScript static site (GitHub Pages)
apps/api   -> FastAPI + SQLite + deterministic scoring + mock/OSS AI provider abstraction
```

## Stack
- Frontend: Vite, React, TypeScript, Tailwind, React Hook Form, Zod, Recharts
- Backend: FastAPI, SQLModel, SQLite, httpx, Pillow
- AI providers: Mock (implemented), Ollama/Llama.cpp (documented extension points)

## Folder structure
See prompt-aligned structure under `apps/web` and `apps/api` plus `.github/workflows/deploy-pages.yml`.

## Local installation
```bash
make install
```

## Run locally
```bash
make dev
# then run commands shown by Makefile in two terminals
```
- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- Swagger: http://localhost:8000/docs

## Docker
```bash
docker-compose up --build
```

## GitHub Pages deployment
1. Create GitHub repo `smart-housing`.
2. Push to `main`.
3. In GitHub Settings → Pages, select **GitHub Actions**.
4. Add repository variable `VITE_API_BASE_URL` to your deployed API URL.
5. Workflow builds from `apps/web/dist` and deploys static assets.

## Backend deployment options
Deploy `apps/api` to VPS, Render, Railway, Fly.io, or any Docker host.

## Env vars
See `.env.example`.

## Ollama/Llama setup
```bash
ollama serve
ollama pull llama3.1:8b
```
Alternatives: `llama3.2:3b`, `mistral:7b`, `qwen2.5:7b`.

## API docs & examples
- `GET /health`
- `POST /api/properties/scrape` `{ "url": "https://..." }`
- `POST /api/evaluations` `{ "property_id": "...", "use_ai": true }`

## Scraping limitations / compliance
No CAPTCHA bypass, no auth bypass, no private APIs, only public pages, timeouts/limits required.

## Legal, AI, and financial notice
- Informational MVP only.
- Not legal/tax/banking/valuation advice.
- AI output can be wrong; verify with professionals.

## Screenshot
Run locally and capture `/`, `/preferences`, `/evaluate`, `/evaluations/:id`.

## Roadmap
- Better portal-specific scrapers (Idealista/Fotocasa/Pisos)
- Comparable prices and neighborhood insights
- Transport/noise/sunlight scoring
- Mortgage simulator and renovation by room
- PDF export and multi-user accounts
- Browser extension and map-based search
- Vision model integration and RAG over user docs
