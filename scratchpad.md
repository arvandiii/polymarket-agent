# Project Understanding: polymarket-agent

## Purpose
The project `polymarket-agent` appears to be a Python-based agent for interacting with Polymarket. The current implementation is a simple async scheduler running a couple of print tasks.

## Structure
- `polymarket_agent/main.py`: Contains the core logic for the async scheduler and task management.
- `pyproject.toml`: Defines the project metadata and dependencies. It uses `uv` for dependency management.
- `requirements.lock`: Lock file for dependencies, generated from `pyproject.toml`.
- `Makefile`: Contains helper commands for installation, running, testing, and formatting.
- `Dockerfile`: A basic Dockerfile to containerize the application. **It has an issue as it refers to `requirements.txt` which does not exist.**
- `tests/`: Directory for tests (currently empty).
- `.github/workflows/lint-and-format.yml`: A GitHub Actions workflow for linting and formatting.

## Dependencies
- Production: None specified in `pyproject.toml`.
- Development: `ruff`, `pytest`, `uv`.

## Functionality
- The agent can run tasks asynchronously at specified intervals.
- The current tasks are simple print statements.

## Issues/Inconsistencies
- The `Dockerfile` references `requirements.txt`, but the project uses `requirements.lock`. The Docker build will fail.
- The `README.md` is empty.
- The `tests/` directory is empty, so no tests are being run.
- `AGENTS.md` and `GEMINI.md` have identical, seemingly generic instructions.
