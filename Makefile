init:
	pip install -r requirements.txt --use-mirrors

.PHONY: tests
tests:
	nosetests tests
