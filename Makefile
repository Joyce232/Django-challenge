up:
	docker build .
	docker-compose up

down:
	docker-compose down

build:
	docker exec jungle pip install -r requirements.txt
	cd challenge && \
		docker exec jungle python3 manage.py migrate

test:
	cd challenge && \
		docker exec jungle python3 manage.py test api.tests.model_tests && \
		docker exec jungle python3 manage.py test api.tests.serializer_tests

run:
	docker exec -it jungle run $(command)

attach:
	docker attach jungle


