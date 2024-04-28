
RG := r0b4dams
NAME := authexchange
VERSION := $(shell cd src && python3 -c "import $(NAME); print($(NAME).__version__)")
IMAGE := $(ORG)/$(NAME):$(VERSION)

VENV := .venv
PY := $(VENV)/bin/python3
PIP := $(PY) -m pip
COMPOSE_ENV := --env-file compose.env

DEV_FUSIONAUTH_CLIENT_ID := 6e4e9805-9690-476f-a7d8-2552992c41e1
DEV_FUSIONAUTH_CLIENT_SECRET := ZyYv1MrS4XjCZKMu0YShVXsGbXoHw57pkXNBcSukY48

.PHONY: all version venv install install-dev uninstall dev wsgi clean
all:
	@echo "$(NAME) $(VERSION)"
	@$(MAKE) venv

version:
	@echo $(VERSION)

venv: clean
	@python3 -m venv $(VENV)
	@$(PIP) install --upgrade pip

install: venv
	@$(PIP) install -e '.[dev]'

uninstall:
	@$(PIP) uninstall $(NAME) -y

dev: .venv
	@ \
	FUSIONAUTH_CLIENT_ID=$(DEV_FUSIONAUTH_CLIENT_ID) \
	FUSIONAUTH_CLIENT_SECRET=$(DEV_FUSIONAUTH_CLIENT_SECRET) \
	authexchange run --dev

wsgi: .venv
	@ \
	FUSIONAUTH_CLIENT_ID=$(DEV_FUSIONAUTH_CLIENT_ID) \
	FUSIONAUTH_CLIENT_SECRET=$(DEV_FUSIONAUTH_CLIENT_SECRET) \
	authexchange run --prod

clean:
	@find . \
	\( -name .venv \
	-o -name dist \
	-o -name __pycache__ \
	-o -name "*.mypy_cache" \
	-o -name "*.pytest_cache" \
	-o -name "*.egg-info" \
	\) -exec rm -rf {} +

.PHONY: test lint format typecheck build release
test: .venv
	@$(PY) -m pytest tests

lint: .venv
	@$(PY) -m pylint src --ignore-paths src/pyrob/__template__

format: .venv
	@$(PY) -m black src

typecheck: .venv
	@$(PY) -m mypy --install-types --non-interactive src
	@$(PY) -m mypy src

build: venv
	@$(PIP) install --upgrade build
	@$(PY) -m build

release:
	@chmod +x scripts/release
	@scripts/release

docker-build: build
	@docker build \
	--build-arg NAME=$(NAME) \
	--build-arg VERSION=$(VERSION) \
	-t $(IMAGE) .

docker-push: docker-build
	@docker push $(IMAGE)

docker-run:
	docker run -p 9000:9000 $(IMAGE)

docker-up:
	@IMAGE=$(IMAGE) docker compose $(COMPOSE_ENV) up

docker-down:
	@docker compose $(COMPOSE_ENV) down

docker-reset:
	@docker compose $(COMPOSE_ENV) down -v
