run:
	docker-compose up

restart:
	docker-compose restart logistics-api

migrate:
	docker-compose exec logistics-api su -c "python manage.py migrate"

test:
	docker-compose exec logistics-api su -c "python manage.py test"

down:
	docker-compose down
