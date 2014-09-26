.PHONY: pypi

pypi:
	pip install wheel twine
	python setup.py register
	python setup.py sdist bdist_wheel
	twine upload dist/*
