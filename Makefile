install:
	cd apps/web && npm install
	python -m pip install -r apps/api/requirements.txt

dev:
	@echo "Run in separate terminals:"
	@echo "1) cd apps/api && uvicorn app.main:app --reload --port 8000"
	@echo "2) cd apps/web && npm run dev"
