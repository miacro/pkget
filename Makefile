SHELL=/bin/bash
MAKE=make --no-print-directory

install:
	python setup.py install --user

test:
	python -m unittest discover ./pkget/test

uninstall:
	pip uninstall pkget

.PHONY:
	install uninstall
