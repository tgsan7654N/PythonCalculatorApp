.PHONY: setup clean check-environment force-rebuild-python run test

setup: check-environment
	@echo "Setting up the virtual environment..."
	@if [ ! -d ".env" ]; then \
		echo "Virtual environment not found. Creating a new one..."; \
		python3 -m venv .env; \
	fi
	. .env/bin/activate && pip install --upgrade pip
	. .env/bin/activate && pip install -r requirements.txt
	. .env/bin/activate && pip install -e .
	@echo "Setup complete!"

check-environment:
	@echo "Checking environment..."
	@if ! command -v python3 >/dev/null 2>&1; then \
		echo "Python3 is not installed. Please install Python3 first."; \
		exit 1; \
	fi
	@if ! python3 -c "import ssl; print(ssl.OPENSSL_VERSION)" >/dev/null 2>&1; then \
		echo "Python3 OpenSSL linkage is broken. Considering a rebuild."; \
		make force-rebuild-python; \
	fi
	@if ! python3 -c "import pip" >/dev/null 2>&1; then \
		echo "pip is not installed or functional. Installing pip..."; \
		curl -O https://bootstrap.pypa.io/get-pip.py; \
		python3 get-pip.py --no-cache-dir --force-reinstall; \
		rm -f get-pip.py; \
	fi
	@echo "Environment check complete."

force-rebuild-python:
	@echo "Rebuilding Python with proper OpenSSL linkage..."
	@if pyenv versions --bare | grep -q "3.11.8"; then \
		echo "Python 3.11.8 is already installed. Rebuilding..."; \
		pyenv uninstall -f 3.11.8; \
	fi
	rm -rf ~/.pyenv/cache
	CFLAGS="-I$(shell brew --prefix openssl)/include" \
	LDFLAGS="-L$(shell brew --prefix openssl)/lib" \
	pyenv install 3.11.8
	@echo "Python 3.11.8 successfully rebuilt."

# Clean up the environment
clean:
	@echo "Cleaning up the environment..."
	rm -rf .env
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*~" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	@echo "Environment cleaned."

run:
	@echo "Running the application..."
	. .env/bin/activate && calculator-app

test:
	@echo "Running tests..."
	. .env/bin/activate && pytest