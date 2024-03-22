.PHONY: dev venv lint format typecheck test version clean release

APP_NAME := token_exchange
VERSION := $(shell python3 -c "from src import $(APP_NAME); print($(APP_NAME).__version__)")

VENV := .venv
PY := $(VENV)/bin/python3
PIP := $(PY) -m pip

all: venv
	@echo "$(APP_NAME) $(VERSION)"
	@echo "$(VENV) created. Run the following command to activate:"
	@echo "source $(VENV)/bin/activate" 

venv:
	@python3 -m venv $(VENV)
	@$(PIP) install --upgrade pip build black mypy pylint pytest pytest-mock
	@chmod +x $(VENV)/bin/activate

dev: .venv
	@$(PY) src/token_exchange/main.py

wsgi: .venv
	@export MODE=production && $(PY) src/token_exchange/main.py

lint: .venv
	@$(PY) -m pylint src

format: .venv
	@$(PY) -m black src

typecheck: .venv
	@$(PY) -m mypy src

test: .venv
	@$(PY) -m pytest tests -v

clean:
	@find . \
	\( -name .venv \
	-o -name dist \
	-o -name __pycache__ \
	-o -name "*.mypy_cache" \
	-o -name "*.pytest_cache" \
	-o -name "*.egg-info" \
	\) -exec rm -rf {} +
