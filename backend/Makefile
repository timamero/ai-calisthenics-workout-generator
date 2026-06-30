.PHONY: help dev lint test

# Default target when you just run 'make'
help:
	@echo "Available commands:"
	@echo "  make dev   - Run the FastAPI development server"
	@echo "  make lint  - Run linting checks (black and flake8)"
	@echo "  make test  - Run tests with pytest"

# Run FastAPI in development mode
dev:
	poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Run code formatting and linting checks
lint:
	poetry run black . && flake8 .

# Run the test suite
test:
	poetry run pytest