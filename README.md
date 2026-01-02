# Polymarket Agent

This project is a Python-based agent for interacting with the Polymarket prediction market. It uses a FastAPI backend and seems to leverage Langchain for AI-powered features.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.9+
*   `make`

### Installation

1.  **Create a virtual environment:**

    ```bash
    python3 -m venv venv
    ```

2.  **Install dependencies:**

    This command will install all the necessary dependencies from `requirements.lock` into the virtual environment.

    ```bash
    make install
    ```

## Usage

### Running the development server

To start the FastAPI development server, run the following command:

```bash
make start-dev
```

This will start the server on `http://127.0.0.1:8000`. You can view the API documentation at `http://127.0.0.1:8000/docs`.

### Running tests

To run the test suite, use the following command:

```bash
make test
```

## Project Structure

```
.
├── polymarket_agent/   # Main application code
├── tests/              # Test suite
├── Makefile            # Automation commands
├── pyproject.toml      # Project metadata and dependencies
└── requirements.lock   # Pinned dependencies
```
