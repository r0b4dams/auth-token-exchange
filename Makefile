.PHONY: all venv build dev clean

APP_NAME := texserv
VERSION := $(shell python3 -c "from src import $(APP_NAME); print($(APP_NAME).__version__)")
VENV := .venv
PY := $(VENV)/bin/python3
PIP := $(PY) -m pip

all:
	@echo "$(APP_NAME) $(VERSION)"

venv:
	@python3 -m venv $(VENV)
	@$(PIP) install --upgrade pip
	@$(PIP) install --upgrade build black mypy pylint pytest pytest-mock
	@chmod +x $(VENV)/bin/activate

build: clean venv
	@$(PIP) install --upgrade build
	@$(PY) -m build

release:
	@chmod +x scripts/release
	@scripts/release

install-dev: venv uninstall
	@$(PIP) install -e .

uninstall:
	@$(PIP) uninstall $(APP_NAME) -y

clean:
	@scripts/clear_tags
	@find . \
	\( -name .venv \
	-o -name dist \
	-o -name __pycache__ \
	-o -name "*.mypy_cache" \
	-o -name "*.pytest_cache" \
	-o -name "*.egg-info" \
	\) -exec rm -rf {} +

test: .venv
	@$(PY) -m pytest tests -v

lint: .venv
	@$(PY) -m pylint src --ignore-paths src/pyrob/__template__

format: .venv
	@$(PY) -m black src

type: .venv
	@$(PY) -m mypy src
