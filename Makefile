setup:
	pipenv install

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

run: makemigrations migrate
	python manage.py runserver
