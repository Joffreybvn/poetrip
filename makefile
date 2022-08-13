
bump:
	bumpversion minor

publish:
	poetry build
	poetry publish

