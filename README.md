# Python Calculator Application

Welcome to the **Python Calculator Application**! This project provides a simple yet functional calculator app built with PyQt5. The application also includes automated tests and a `Makefile` to streamline setup, testing, and running the application.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
- [Makefile Commands](#makefile-commands)
- [Testing](#testing)
- [Cleaning Up](#cleaning-up)
- [Troubleshooting](#troubleshooting)

---

## Features

- A functional GUI calculator built with PyQt5.
- Automated tests using `pytest`.
- Virtual environment management and dependency installation.
- Easy-to-use `Makefile` for project setup, testing, and running.

---

## Prerequisites

Ensure you have the following installed:

- Python 3.11 or newer (preferably installed via `pyenv`).
- Homebrew (for macOS users) for managing dependencies.
- OpenSSL (via Homebrew) to support secure Python builds.

Install `pyenv` if not already installed:
```bash
brew install pyenv
```

Install OpenSSL:
```bash
brew install openssl
```

---

## Setup

To set up the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd PythonCalculatorApp
   ```

2. Set up the Python environment and install dependencies using the `Makefile`:
   ```bash
   make setup
   ```
   - This will create a virtual environment (`.env`), install project dependencies, and link the application in editable mode.

---

## Usage

Run the calculator application with the following command:
```bash
make run
```

This launches the PyQt5-based calculator GUI.

---

## Makefile Commands

The project includes a `Makefile` with the following commands:

### `make setup`
Sets up the project by:
- Checking if Python and required dependencies are installed.
- Creating a virtual environment if one does not exist.
- Installing required Python packages from `requirements.txt`.

### `make run`
Runs the calculator application. Ensure the virtual environment is activated.

### `make test`
Runs the automated tests using `pytest`:
```bash
make test
```
This ensures all functionalities of the calculator are working as expected.

### `make clean`
Cleans up the project environment by:
- Removing the `.env` virtual environment.
- Deleting compiled Python files (`*.pyc`, `*.pyo`).
- Removing `__pycache__`, `.pytest_cache`, and `*.egg-info` directories.

Run this command:
```bash
make clean
```
Use this to reset the environment before reinitializing it.

### `make check-environment`
Checks whether the required Python and dependencies are installed, and if OpenSSL is correctly linked. Automatically suggests or performs fixes if issues are detected.

---

## Testing

To test the application:
1. Run `make test`:
   ```bash
   make test
   ```
2. The results will indicate whether all tests passed or if there are any failures.

---

## Cleaning Up

To reset the project environment:
```bash
make clean
```
This removes the virtual environment and all cached or temporary files.

---

## Troubleshooting

### Common Issues

1. **`blake2b` or `blake2s` Errors:**
   - Ensure Python is built with OpenSSL correctly linked.
   - Run:
     ```bash
     brew reinstall openssl
     CFLAGS="-I$(brew --prefix openssl)/include" \
     LDFLAGS="-L$(brew --prefix openssl)/lib" \
     pyenv install <python_version>
     ```

2. **Dependency Issues:**
   - If dependencies fail to install, ensure you’re using the latest `pip`:
     ```bash
     python -m pip install --upgrade pip
     ```

3. **Environment Issues:**
   - Clean and reinitialize the environment:
     ```bash
     make clean
     make setup
     ```

---

## Contributions

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## License

This project is licensed under the GPLv3 License.

---

Happy Calculating! 🎉

