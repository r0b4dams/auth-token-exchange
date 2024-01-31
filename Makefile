.PHONY: setup dev add save clean fusionauth

install: clean
	test -f requirements.txt || touch requirements.txt
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

dev: .venv
	@.venv/bin/python3 src

preview: .venv
	@export MODE=production && .venv/bin/python3 src

add: .venv
	@.venv/bin/pip install $(pkg)
	@$(MAKE) save

save: .venv
	@.venv/bin/pip freeze > requirements.txt

clean:
	@rm -rf .venv
	@find . -type f -name "*.pyc" -delete

fusionauth-up:
	@docker compose --env-file compose.env up

fusionauth-down:
	@docker compose down -v