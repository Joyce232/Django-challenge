build:
	pip install -r requirements.txt
	docker-compose up -d
	cd challenge && \
		python3 manage.py makemigrations && \
		python3 manage.py migrate

run:
	docker-compose up -d
	cd challenge && \
		python3 manage.py runserver

test:
	cd challenge && \
		python3 manage.py test api.tests.model_tests && \
		python3 manage.py test api.tests.serializer_tests
