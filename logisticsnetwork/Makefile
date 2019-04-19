run:
	docker-compose up

restart:
	docker-compose restart logistics-api

migrate:
	docker-compose exec logistics-api su -c "python manage.py migrate"

test:
	docker-compose exec logistics-api su -c "python manage.py test -v2"

down:
	docker-compose down


# Useful commands during development
loaddata:
	docker-compose exec logistics-api su -c "python manage.py loaddata network.json"

shell:
	docker-compose exec logistics-api su -c "python manage.py shell"

attach:
	docker-compose exec logistics-api /bin/bash

db:
	docker-compose exec db /bin/bash

superuser:
	docker-compose exec logistics-api su -c "python manage.py createsuperuser"
