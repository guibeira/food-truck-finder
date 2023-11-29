USER_ID=$(shell id -u)
GROUP_ID=$(shell id -g)

build:
	docker compose build

run:
	docker compose up

migrate: 
	docker compose run --rm -e LC_ALL=C.UTF-8 -e LANG=C.UTF-8 --user="$(USER_ID):$(GROUP_ID)" web python manage.py migrate

create-migrations: 
	docker compose run --rm -e LC_ALL=C.UTF-8 -e LANG=C.UTF-8 --user="$(USER_ID):$(GROUP_ID)" web python manage.py makemigrations

create_user: 
	docker compose run --rm -e LC_ALL=C.UTF-8 -e LANG=C.UTF-8 --user="$(USER_ID):$(GROUP_ID)" web bash -c "python manage.py createsuperuser"

bash: 
	docker compose run --rm -e LC_ALL=C.UTF-8 -e LANG=C.UTF-8 --user="$(USER_ID):$(GROUP_ID)" web bash
