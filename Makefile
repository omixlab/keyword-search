build_pypi_package:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	python setup.py sdist bdist_wheel

twine_upload: build_pypi_package
	@python setup.py sdist bdist_wheel
	@twine upload \
		--repository-url https://upload.pypi.org/legacy/ \
		dist/*-py3-none-any.whl \
		--verbose