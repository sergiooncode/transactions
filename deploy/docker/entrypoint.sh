python manage.py migrate
DJANGO_SUPERUSER_PASSWORD=password python manage.py createsuperuser --no-input --username=admin --email=admin@domain.com
python manage.py runserver 0.0.0.0:8000