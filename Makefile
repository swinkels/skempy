init:
	pip install -r requirements.txt --use-mirrors

.PHONY: tests docs
tests:
	python -m unittest discover tests/

docs:
	dexy reset ; dexy
	cp output/_README.rst README.rst
	cd docs ; make html

