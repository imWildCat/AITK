.PHONY: help

help:
	@grep '^[^#[:space:]].*:' Makefile

readme:
	pandoc -s README.rst -t markdown_phpextra -o README.md

style-check:
	flake8 --config .flake8 aitk/

package-build:
	rm -rf aitk.egg-info
	rm -rf dist
	python setup.py bdist_wheel --universal

release:
	twine upload dist/*

doc-en:
	cd docs/source && sphinx-apidoc -f -o . ../../aitk
	cd docs && PYTHONPATH=.. make html
delete-pyc:
	find . -name \*.pyc -delete