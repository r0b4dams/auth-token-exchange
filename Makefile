.PHONY: all venv build dev clean client

ORG := r0b4dams
APP_NAME := authexchange
VERSION := $(shell cd src && python3 -c "import $(APP_NAME); print($(APP_NAME).__version__)")
VENV := .venv
PY := $(VENV)/bin/python3
PIP := $(PY) -m pip
COMPOSE_ENV := --env-file compose.env

all:
	@echo "$(APP_NAME) $(VERSION)"
	@$(MAKE) venv

venv:
	@python3 -m venv $(VENV)
	@$(PIP) install --upgrade pip
	@$(PIP) install --upgrade build black mypy pylint pytest
	@chmod +x $(VENV)/bin/activate

build: clean venv
	@$(PIP) install --upgrade build
	@$(PY) -m build

install: venv uninstall
	@$(PIP) install -e .

uninstall:
	@$(PIP) uninstall $(APP_NAME) -y

clean:
	@find . \
	\( -name .venv \
	-o -name dist \
	-o -name __pycache__ \
	-o -name "*.mypy_cache" \
	-o -name "*.pytest_cache" \
	-o -name "*.egg-info" \
	\) -exec rm -rf {} +

test: .venv
	@$(PY) -m pytest tests

lint: .venv
	@$(PY) -m pylint src --ignore-paths src/pyrob/__template__

format: .venv
	@$(PY) -m black src

typecheck: .venv
	@$(PY) -m mypy --install-types --non-interactive src
	@$(PY) -m mypy src

client:
	@cd client && yarn && yarn dev

docker-up:
	@docker compose $(COMPOSE_ENV) up

docker-down:
	@docker compose $(COMPOSE_ENV) down

docker-reset:
	@docker compose $(COMPOSE_ENV) down -v

docker-build: build
	@docker build \
	--build-arg NAME=$(APP_NAME) \
	--build-arg VERSION=$(VERSION) \
	-t $(ORG)/$(APP_NAME):$(VERSION) .

docker-run:
	@docker run --add-host host.docker.internal:host-gateway $(ORG)/$(APP_NAME):$(VERSION)