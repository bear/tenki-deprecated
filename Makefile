.PHONY: help install-hook clean info update server
SHELL = /bin/bash

help:
	@echo "This project assumes that an active Python virtualenv is present."
	@echo "The following targets are available:"
	@echo "  update        update python dependencies"
	@echo "  update-all    update python dependencies (including test only)"
	@echo "  install-hook  install git pre-commit hook for python"
	@echo "  clean         remove unwanted files"
	@echo "  lint          flake8 lint check"
	@echo "  test          run unit tests"
	@echo "  integration   run integration tests"
	@echo "  ci            run unit, integration and codecov"
	@echo "  all           refresh and run all tests and generate coverage reports"
	@echo "  server        start the Flask server"

install-hook:
	git-pre-commit-hook install --force --plugins flake8 --plugins json --plugins yaml --flake8_ignore E111,E124,E126,E201,E202,E221,E241,E302,E501,N802,N803

update:
	pip install -U pip
	pip install -Ur requirements.txt

update-all: update
	pip install -Ur requirements-test.txt

clean:
	python manage.py clean

lint: clean
	pycodestyle --config={toxinidir}/setup.cfg 

test: clean
	python manage.py test

integration:
	python manage.py integration

webtest: docker-start
	$(eval DRIVER_IP := $(shell ./wait_for_ip.sh))
	DRIVER_IP=$(DRIVER_IP) python manage.py webtest
	docker-compose stop

coverage:
	@coverage run --source=tenki manage.py test
	@coverage html
	@coverage report

ci: info clean coverage webtest
	CODECOV_TOKEN=`cat .codecov-token` codecov

docker-build:
	docker-compose build
	docker-compose pull
	docker-compose rm -f

docker-start:
	docker-compose up -d

all: update-all integration coverage webtest

info:
	@python --version
	@pip --version
	@virtualenv --version
	@uname -a

server:
	python manage.py server

uwsgi:
	uwsgi --socket 127.0.0.1:5080 --wsgi-file wsgi.py
