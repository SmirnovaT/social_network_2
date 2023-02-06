api_container_name = api

build:
	docker-compose build

run:
	docker-compose up

run_detached:
	docker-compose up -d

kill:
	docker-compose down

container_status:
	docker ps -a

log:
	docker logs $(api_container_name)

inspect:
	docker exec -it $(api_container_name) bash

inspect_root:
	docker exec -u 0 -it $(api_container_name) bash

restart:
	make kill && make build && make run

attach:
	docker attach $(api_container_name)

drop_volumes:
	docker-compose down -v

make_revision:
	docker exec $(api_container_name) alembic revision --autogenerate -m ""