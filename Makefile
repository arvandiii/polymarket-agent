# Makefile for polymarket-agent

.PHONY: all install start-dev fmt build-docker run-docker run-docker-dev clean help

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
	uv pip sync requirements.txt

# ====================================================================================
# DEVELOPMENT
# ====================================================================================

start-dev: ## Start the FastAPI development server.
	@echo "Starting development server..."
	python scripts/python/setup.py
	fastapi dev scripts/python/server.py

fmt: ## Format code with ruff.
	@echo "Formatting code with ruff..."
	ruff format .

# ====================================================================================
# DOCKER
# ====================================================================================

build-docker: ## Build the project's Docker image.
	@echo "Building docker image..."
	docker build -f Dockerfile --tag polymarket-agents:latest .

run-docker: ## Run the project's Docker container.
	@echo "Running docker image..."
	docker run --rm -it polymarket-agents:latest

run-docker-dev: ## Run the Docker container in development mode (with volume mount).
	@echo "Running docker image in development mode..."
	docker run --rm -it -v $(CURDIR):/home polymarket-agents:latest bash

# ====================================================================================
# CLEANING
# ====================================================================================

clean: ## Clean up generated files and caches.
	@echo "Cleaning up project..."
	@# This is a placeholder for future cleanup commands.
	@# For example:
	@# find . -name '*.pyc' -delete
	@# find . -name '__pycache__' -exec rm -r {} +
