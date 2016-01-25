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
	@echo "  test        run unit tests"
	@echo "  integration run integration tests"
	@echo "  all         refresh and run all tests and generate coverage reports"

update: guard-PYENV_VIRTUALENV_INIT
	pip install -U  pip --use-mirrors
	pip install -Ur requirements.txt --use-mirrors

update-all: guard-PYENV_VIRTUALENV_INIT update
	pip install -Ur requirements-test.txt --use-mirrors

clean: guard-PYENV_VIRTUALENV_INIT
	python manage.py clean

lint: guard-PYENV_VIRTUALENV_INIT clean
	flake8 --exclude=env . > violations.flake8.txt

test: guard-PYENV_VIRTUALENV_INIT lint
	python manage.py test

integration: guard-PYENV_VIRTUALENV_INIT clean lint
	py.test tests -m "integration"

coverage: guard-PYENV_VIRTUALENV_INIT clean lint
	coverage run --source=tenki manage.py test
	coverage html
	coverage report

ci: clean lint integration coverage
	codecov

all: clean update-all lint integration coverage

server: guard-PYENV_VIRTUALENV_INIT
	python manage.py server