APP_NAME := token_exchange
VERSION := $(shell python3 -c "from src import $(APP_NAME); print($(APP_NAME).__version__)")
VENV := .venv
PY := $(VENV)/bin/python3
PIP := $(PY) -m pip

all: venv
	@echo "$(APP_NAME) $(VERSION)"
	@echo "$(VENV) created. Run the following command to activate:"
	@echo "source $(VENV)/bin/activate" 

.PHONY: venv
venv:
	@python3 -m venv $(VENV)
	@$(MAKE) install
	@chmod +x $(VENV)/bin/activate

.PHONY: install
install:
	@$(PIP) install -r requirements.txt

.PHONY: save
save: .venv
	@$(PIP) freeze > requirements.txt

.PHONY: dev
dev: .venv
	@$(PY) src/token_exchange/main.py

.PHONY: wwgi
wsgi: .venv
	@export MODE=production && $(PY) src/token_exchange/main.py

.PHONY: lint
lint: .venv
	@$(PY) -m pylint src

.PHONY: format
format: .venv
	@$(PY) -m black src

.PHONY: typecheck
typecheck: .venv
	@$(PY) -m mypy src

.PHONY: test
test: .venv
	@$(PY) -m pytest tests -v

.PHONY: clean
clean:
	@find . \
	\( -name .venv \
	-o -name dist \
	-o -name __pycache__ \
	-o -name "*.mypy_cache" \
	-o -name "*.pytest_cache" \
	-o -name "*.egg-info" \
	\) -exec rm -rf {} +
