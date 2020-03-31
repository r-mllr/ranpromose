MODULE := ranpromose
BLUE=\033[0;34m 
PLAIN=\033[0m 

run:
	@python -m $(MODULE)

test:
	@pytest

lint:
	@echo -e "${BLUE}Running Pylint against source and test files...${PLAIN}"
	@pylint --rcfile=setup.cfg **/*.py
	@echo -e "${BLUE}Running Flake8 against source and test files...${PLAIN}"
	@flake8
	@echo -e "${BLUE}Running Bandit against source files...${PLAIN}"
	@bandit -r --ini setup.cfg

clean:
	rm -rf .pytest_cache .coverage .coverage.xml

.PHONY: clean test
