test:
	poetry run pytest tests

test-coverage:
	poetry run pytest --cov=google_books_api --cov-report=term-missing

documentation:
	poetry run sphinx-apidoc -o docs/source google_books_api
	poetry run sphinx-build -b html docs/source docs/build/html

lint-black:
	poetry run black --check google_books_api tests

black:
	poetry run black google_books_api tests

check-type:
	poetry run mypy google_books_api tests

minor:
	poetry version minor

patch:
	poetry version patch

major:
	poetry version major