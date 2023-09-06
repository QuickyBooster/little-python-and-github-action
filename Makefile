install:
	pip install update
	pip install -r requirement.txt
lint:
	pylint --disable=R,C *.py devopslib