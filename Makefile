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
	rm -f tests/_form.html
	rm -f tests/create.html
	rm -f tests/update.html
	rm -f tests/delete.html
	rm -f tests/detail.html
	rm -f tests/list.html
	rm -f tests/templates/tests/_form.html
	rm -f tests/templates/tests/create.html
	rm -f tests/templates/tests/update.html
	rm -f tests/templates/tests/delete.html
	rm -f tests/templates/tests/detail.html
	rm -f tests/templates/tests/list.html
	rm -f tests/forms.py
	rm -f tests/tests.py
	rm -f tests/urls.py
	mv -f tests/urls.py.bak tests/urls.py
	rm -f tests/views.py

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
