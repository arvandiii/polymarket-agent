# Makefile for polymarket-agent

VENV_PYTHON = venv/bin/python

.PHONY: all install compile-deps start-dev fmt build-docker run-docker run-docker-dev clean help

all: help

help: ## Show this help message.
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'


# ====================================================================================
# INSTALLATION
# ====================================================================================

install: ## Install Python dependencies from requirements.txt
	@echo "Installing dependencies..."
	$(VENV_PYTHON) -m uv pip sync requirements.lock

compile-deps: ## Compile dependencies from pyproject.toml into requirements.lock
	@echo "Compiling dependencies into requirements.lock..."
	$(VENV_PYTHON) -m uv pip compile pyproject.toml --all-extras -o requirements.lock

# ====================================================================================
# DEVELOPMENT
# ====================================================================================

start-dev: ## Start the FastAPI development server.
	@echo "Starting development server..."
	venv/bin/fastapi dev scripts/server.py

test: ## Run tests with pytest.
	@echo "Running tests..."
	venv/bin/pytest

fmt: ## Format code with ruff.
	@echo "Formatting code with ruff..."
	venv/bin/ruff format .

# ====================================================================================
# DOCKER
# ====================================================================================


# ====================================================================================
# CLEANING
# ====================================================================================

clean: ## Clean up generated files and caches.
	@echo "Cleaning up project..."
	@# This is a placeholder for future cleanup commands.
	@# For example:
	@# find . -name '*.pyc' -delete
	@# find . -name '__pycache__' -exec rm -r {} +
