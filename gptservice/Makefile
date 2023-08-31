VENV_NAME = .venv

.PHONY: create-venv activate-venv install-deps deactivate-venv setup deactivate  run-server-debug run-server

create-venv:
	python3 -m venv $(VENV_NAME)

activate-venv:
	source $(VENV_NAME)/bin/activate

install-deps:
	pip install -r requirements.txt

deactivate-venv:
	deactivate

setup: create-venv activate-venv install-deps

deactivate: deactivate-venv

run-server-debug:
	flask --app main run --debug

run-server:
	python3 main.py