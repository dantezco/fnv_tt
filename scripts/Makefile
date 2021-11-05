APP_DIR=.
TYPE=special

# Default Option
default: help

# Options are "skills" or "special"
markovgen:
	pipenv run python markovgen.py $(TYPE)

# Install project packages from Pipfile
install:
	pipenv install --dev

# Open pipenv shell
shell:
	pipenv shell

# Run pylint
lint:
	set -e; pipenv run pylint $(APP_DIR)
 
# Format code with black
format:
	pipenv run black $(APP_DIR)


# Display this help
help:
	@echo
	@echo '  Usage:'
	@echo ''
	@echo '              make <target> [flags...]'
	@echo ''
	@echo '  Targets:'
	@echo ''
	@awk '/^#/{ comment = substr($$0,3) } comment && /^[a-zA-Z][a-zA-Z0-9_-]+ ?:/{ print "   ", $$1, comment }' ./Makefile | column -t -s ':' | sort
	@echo ''
	@echo '  Flags:'
	@echo ''
	@awk '/^#/{ comment = substr($$0,3) } comment && /^[a-zA-Z][a-zA-Z0-9_-]+ ?\?=/{ print "   ", $$1, $$2, comment }' ./Makefile | column -t -s '?=' | sort
	@echo ''
