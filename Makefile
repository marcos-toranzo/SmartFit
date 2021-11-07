test:
	pytest

check:
	python -m compileall ./src/

install:
	pip install -r requirements.txt