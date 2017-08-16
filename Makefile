SHELL=/bin/bash
MAKE=make --no-print-directory

install:
	python setup.py install --user

uninstall:
	pip uninstall pkget

.PHONY:
	install uninstall
