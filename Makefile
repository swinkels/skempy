init:
	pip install -r requirements.txt --use-mirrors

.PHONY: tests
tests:
	python -m unittest discover tests/
