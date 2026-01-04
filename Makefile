# Makefile for polymarket-agent

PY = venv/bin/python
PYM = $(PY) -m

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

install: ## Install Python dependencies from uv.lock
	@echo "Installing dependencies..."
	$(PYM) uv sync --locked

compile-deps: ## Compile dependencies from pyproject.toml into uv.lock
	@echo "Compiling dependencies into uv.lock..."
	$(PYM) uv lock
	
# ====================================================================================
# DEVELOPMENT
# ====================================================================================

run: ## Run the server application script.
	@echo "Running the application..."
	$(PYM) polymarket_agent.server

test: ## Run tests with pytest.
	@echo "Running tests..."
	$(PYM) pytest

format: ## Format code with ruff.
	@echo "Formatting code with ruff..."
	$(PYM) ruff format .

lint: ## Lint code with ruff.
	@echo "Linting code with ruff..."
	$(PYM) ruff check . --fix --exit-zero
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
