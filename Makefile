.DEFAULT_GOAL := build
.PHONY: build publish package coverage test lint docs venv
PROJ_SLUG = yaml2sql
CLI_NAME = yaml2sql
PY_VERSION = 3.8
LINTER = pylint


build:
	pip3 install --editable .

run:
	$(CLI_NAME) version
	$(CLI_NAME) --help

submit:
	$(CLI_NAME) submit

freeze:
	pip3 freeze > requirements.txt

lint:
	python3 -m $(LINTER) $(PROJ_SLUG) --fail-under=9.0

test: lint
	python3 -m pytest --cov-report term --cov=$(PROJ_SLUG) tests/

quicktest:
	python3 -m pytest --cov-report term --cov=$(PROJ_SLUG) tests/

coverage: lint
	python3 -m pytest --cov-report html --cov=$(PROJ_SLUG) tests/

docs: test
	cd docs && $(MAKE) html

answers:
	cd docs && $(MAKE) html
	xdg-open docs/build/html/index.html

package: clean docs
	python setup.py sdist

publish: package
	twine upload dist/*

clean:
	rm -rf dist \
	rm -rf docs/build \
	rm -rf *.egg-info
	coverage erase

venv:
	virtualenv --python python$(PY_VERSION) venv

install:
	pip install -r requirements.txt

licenses:
	pip-licenses --with-url --format=rst \
	--ignore-packages $(shell cat .pip-lic-ignore | awk '{$$1=$$1};1')
