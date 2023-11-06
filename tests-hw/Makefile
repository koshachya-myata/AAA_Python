.PHONY: clean lint issue-1 issue-2 issue-3 issue-4 issue-5

#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))


#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Run issue-1
issue-1:
	$(info Running issue 1)
	cd issue-1 && ./issue-1.sh

## Run issue-2
issue-2:
	$(info Running issue 2)
	cd issue-2 && ./issue-2.sh

## Run issue-3
issue-3:
	$(info Running issue 3)
	cd issue-3 && ./issue-3.sh

## Run issue-4
issue-4:
	$(info Running issue 4)
	cd issue-4 && ./issue-4.sh

## Run issue-5
issue-5:
	$(info Running issue 5)
	cd issue-5 && ./issue-5.sh

## Run all issues
make all: issue-1 issue-2 issue-3 issue-4 issue-5

## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -exec rm -r {} \;
	find . -type d -name ".mypy_cache" -exec rm -r {} \;

## Lint using flake8
lint:
	flake8 .



#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')