.PHONY: help

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
	@echo "  test        run all tests with py.test"

update: guard-PYENV_VIRTUALENV_INIT
	pip install -Ur requirements.txt

clean: guard-PYENV_VIRTUALENV_INIT
	python manage.py clean

lint: guard-PYENV_VIRTUALENV_INIT
	flake8 --exclude=env . > violations.flake8.txt

test: guard-PYENV_VIRTUALENV_INIT
	py.test tests -m "not integration"

integration: guard-PYENV_VIRTUALENV_INIT
	py.test tests -m "integration"

all: guard-PYENV_VIRTUALENV_INIT test integration

server: guard-PYENV_VIRTUALENV_INIT
	python manage.py server