.PHONY: clean-pyc clean-build docs

help:
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "docs - generate Sphinx HTML documentation, including API docs"
	@echo "release - package and upload a release"
	@echo "sdist - package"

clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-tests:
	rm tests/_form.html
	rm tests/create.html
	rm tests/delete.html
	rm tests/detail.html
	rm tests/forms.py
	rm tests/list.html
	rm tests/tests.py
	rm tests/update.html
	rm tests/urls.py
	rm tests/urls.py.bak tests/urls.py
	rm tests/views.py

lint:
	flake8 appgen tests

test:
	python runtests.py tests

coverage:
	coverage run --source appgen runtests.py tests
	coverage report -m
	coverage html
	open htmlcov/index.html

docs:
	rm -f docs/django-app-gen.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ appgen
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	open docs/_build/html/index.html

release: clean
	python setup.py sdist upload
	python setup.py bdist_wheel upload

sdist: clean
	python setup.py sdist
	ls -l dist
