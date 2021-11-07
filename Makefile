test:
	pytest

check:
	python -m compileall ./smartfit/

install:
	pip install -r requirements.txt