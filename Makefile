init:
	pip install -r requirements.txt --use-mirrors

.PHONY: tests docs
tests:
	python -m unittest discover tests/

docs:
	cd docs ; make html
