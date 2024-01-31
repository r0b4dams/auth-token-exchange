.PHONY: setup dev add save clean

setup: clean
	test -f requirements.txt || touch requirements.txt
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

dev: .venv
	@.venv/bin/python3 src/main.py

preview: .venv
	@export MODE=production && .venv/bin/python3 src/main.py

add: .venv
	@.venv/bin/pip install $(pkg)
	@$(MAKE) save

save: .venv
	@.venv/bin/pip freeze > requirements.txt

clean:
	@rm -rf .venv
	@find . -type f -name "*.pyc" -delete