test:
	pytest

check:
	python -m compileall ./smartfit/

install:
	pip install -r requirements.txt

container-test:
	docker run -t -v $(pwd):/app/test marcostoranzo/smartfit