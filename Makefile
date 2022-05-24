build:
	docker exec jungle pip install -r requirements.txt
	docker exec jungle python3 manage.py makemigrations && \
	docker exec jungle python3 manage.py migrate

run:
	docker exec jungle python3 manage.py runserver

test:
	docker exec jungle python3 manage.py test api.tests.model_tests && \
	docker exec jungle python3 manage.py test api.tests.serializer_tests
