install:
	pip install update
	pip install -r requirement.txt
lint:
	pylint --disable=R,C *.py devopslib
test:
	python -m pytest -vv --cov=devopslib test_*.py
format:
	black *.py
all: install lint test format
