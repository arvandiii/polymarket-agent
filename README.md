# Polymarket Agent

This project is a Python-based agent for interacting with the Polymarket prediction market. It is a script-based application that demonstrates a workflow for gathering data and executing trades using mock data.

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

### Running the application

To run the main application script, use the following command:

```bash
make run
```

This will execute the `main.py` script, which demonstrates the application's workflow with mock data. The output will be printed to the console.

### Running tests

To run the test suite, use the following command:

```bash
make test
```

## Project Structure

```
.
├── main.py             # Main application entry point
├── polymarket_agent/   # Main application code
├── tests/              # Test suite
├── Makefile            # Automation commands
├── pyproject.toml      # Project metadata and dependencies
└── requirements.lock   # Pinned dependencies
```