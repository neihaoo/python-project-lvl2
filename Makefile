install:
	poetry install

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

selfcheck:
	poetry check

check: selfcheck test lint

clean:
	rm -rf dist

build: check clean
	poetry build

package-install: build
	python3 -m pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build
