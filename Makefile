-include .env

SERVER_HOST = $(HOST)

ifeq ($(SERVER_HOST),)
	SERVER_HOST = "127.0.0.1"
endif

SERVER_PORT = $(PORT)

ifeq ($(SERVER_PORT),)
	SERVER_PORT = 8000
endif


test:
	pytest

check:
	python -m compileall ./smartfit/

install:
	pip install .

container-test:
	docker run -t -v $(pwd):/app/test marcostoranzo/smartfit

run-server:
	uvicorn smartfit.api.api:app --reload --host $(SERVER_HOST) --port $(SERVER_PORT)

build:
	echo "Nothing to build"
	