up:
	docker-compose up

down:
	docker-compose down

build:
	docker exec jungle pip install -r requirements.txt
	docker exec jungle python3 manage.py makemigrations && \
	docker exec jungle python3 manage.py migrate

test:
	docker exec jungle python3 manage.py test api.tests.model_tests && \
	docker exec jungle python3 manage.py test api.tests.serializer_tests

admin:
	docker exec -it jungle python3 manage.py createsuperuser
run:
	docker exec -it jungle run $(command)

attach:
	docker attach jungle


