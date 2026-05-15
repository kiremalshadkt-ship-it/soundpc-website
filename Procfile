web: python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn soundpc_website.wsgi:application --bind 0.0.0.0:$PORT
