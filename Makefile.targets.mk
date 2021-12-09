.PHONY: format
format:
	$(call log, reorganizing imports & formatting code)
	isort --virtual-env="$(DIR_VENV)" \
		"$(DIR_TESTS)" \
		|| exit 1
	black \
		"$(DIR_TESTS)" \
		|| exit 1


.PHONY: qa
qa: contributors tests coverage code-typing code-format code-linters
	$(call log, QA checks)


.PHONY: contributors
contributors:
	$(call log, validate contributors)
	$(DIR_REPO)/validate_contributors.sh


.PHONY: tests
tests:
	$(call log, running tests)
	rm -f .coverage
	rm -f coverage.xml
	rm -rf htmlcov
	pytest


.PHONY: coverage
coverage:
	$(call log, calculating coverage)
	coverage html
	coverage xml


.PHONY: code-typing
code-typing:
	$(call log, checking code typing)
	mypy


.PHONY: code-format
code-format:
	$(call log, checking code format)
	isort --virtual-env="$(DIR_VENV)" --check-only \
		"$(DIR_TESTS)" \
		|| exit 1
	black --check \
		"$(DIR_TESTS)" \
		|| exit 1


.PHONY: code-linters
code-linters:
	$(call log, linting)
	flake8


.PHONY: sh
sh:
	$(call log, starting Python shell)
	ipython


.PHONY: venv-dir
venv-dir:
	$(call log, initializing venv directory)
	test -d .venv || mkdir .venv


.PHONY: venv
venv: venv-dir
	$(call log, installing packages)
	pipenv install


.PHONY: venv-dev
venv-dev: venv-dir
	$(call log, installing development packages)
	pipenv install --dev


.PHONY: venv-deploy
venv-deploy: venv-dir
	$(call log, installing packages into system)
	pipenv install --deploy --system


.PHONY: venv-deploy-all
venv-deploy-all: venv-dir
	$(call log, installing all packages into system)
	pipenv install --dev --deploy --system


.PHONY: upgrade-venv
upgrade-venv: venv-dir
	$(call log, upgrading all packages in virtualenv)
	pipenv update --dev
