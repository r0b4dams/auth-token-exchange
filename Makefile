.PHONY: setup dev add save clean fusionauth-up fusionauth-down

VENV := .venv
PY := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip
ENTRYPOINT := src/main.py
REQ_FILE := requirements.txt


install: clean
	@python3 -m venv $(VENV)
	@test -f $(REQ_FILE) || (touch $(REQ_FILE) && echo "# Install requirements with 'make add pkg=<PKG_NAME>'" > $(REQ_FILE))
	@$(PIP) install -r $(REQ_FILE)

dev: .venv
	@$(PY) $(ENTRYPOINT)

preview: .venv
	@export MODE=production && $(PY) $(ENTRYPOINT)

add: .venv
	@$(PIP) install $(pkg)
	@$(MAKE) save

rm: .venv
	@$(PIP) uninstall $(pkg)
	@$(MAKE) save

save: .venv
	@$(PIP) freeze > $(REQ_FILE)

clean:
	@rm -rf $(VENV)
	@find . -type f -name "*.pyc" -delete

fusionauth-up:
	@docker compose --env-file compose.env up

fusionauth-down:
	@docker compose --env-file compose.env down -v