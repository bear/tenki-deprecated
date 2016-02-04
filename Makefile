.PHONY: help clean info

ifeq ($(wildcard .codecov-token),)
  TOKEN = source .codecov-token
else
	TOKEN =
endif

guard-%:
	@ if [ "${${*}}" == "" ]; then \
	  echo "Environment variable $* not set"; \
	fi

help:
	@echo "This project assumes that an active Python virtualenv is present."
	@echo "The following make targets are available:"
	@echo "  update      update python dependencies"
	@echo "  clean       remove unwanted files"
	@echo "  lint        flake8 lint check"
	@echo "  test        run unit tests"
	@echo "  integration run integration tests"
	@echo "  all         refresh and run all tests and generate coverage reports"

update: guard-PYENV_VIRTUALENV_INIT
	pip install -U pip
	pip install -Ur requirements.txt

update-all: guard-PYENV_VIRTUALENV_INIT update
	pip install -Ur requirements-test.txt

clean:
	python manage.py clean

lint: clean
	flake8 --exclude=env . > violations.flake8.txt

# FIXME right now integration tests are run
test: lint
	python manage.py test

integration: lint
	python manage.py integration

coverage: lint
	@coverage run --source=tenki manage.py test
	@coverage html
	@coverage report

info:
	@python --version
	@pip --version
	@virtualenv --version

ci: info clean integration coverage
	@CODECOV_TOKEN=$(CODECOV_TOKEN) && codecov

all: update-all integration coverage

server: guard-PYENV_VIRTUALENV_INIT
	python manage.py server