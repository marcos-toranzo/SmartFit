test:
	pytest

check:
	python -m compileall ./smartfit/

install:
	pip install .

container-test:
	docker run -t -v $(pwd):/app/test marcostoranzo/smartfit