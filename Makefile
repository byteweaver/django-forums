VIRTUALENV_FOLDER=env
PIP_BIN=$(VIRTUALENV_FOLDER)/bin/pip
PYTHON_BIN=$(VIRTUALENV_FOLDER)/bin/python


all: environment

environment:
	test -d "$(VIRTUALENV_FOLDER)" || virtualenv --no-site-packages $(VIRTUALENV_FOLDER)

reqirements: environment
	$(PIP_BIN) install -r requirements.txt

test: reqirements
	$(PYTHON_BIN) forums/tests/runtests.py
