setup:
	pipenv install

makemigrations:
	python core/manage.py makemigrations

migrate:
	python core/manage.py migrate

run: makemigrations migrate
	python core/manage.py runserver
