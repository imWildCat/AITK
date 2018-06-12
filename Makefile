.PHONY: help

help:
	@grep '^[^#[:space:]].*:' Makefile

readme:
	pandoc -s README.rst -t markdown_phpextra -o README.md

style-check:
	flake8 aitk/

package-build:
	rm -rf aitk.egg-info
	rm -rf dist
	python setup.py bdist_wheel --universal

release:
	twine upload dist/*