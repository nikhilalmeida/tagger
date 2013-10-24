SHELL=/usr/bin/env bash
VIRTUALENV ?= ./venv

.PHONY: setup clobber

${VIRTUALENV}:
	@echo "building ${VIRTUALENV}"
	@python2.7 -m virtualenv ${VIRTUALENV}
	@source ${VIRTUALENV}/bin/activate && \
	    pip install -r requirements.txt
	@touch ${VIRTUALENV}
	@echo "${VIRTUALENV} built"

setup: ${VIRTUALENV}

clobber:
	@echo "deleting ${VIRTUALENV}"
	@rm -rf ${VIRTUALENV}