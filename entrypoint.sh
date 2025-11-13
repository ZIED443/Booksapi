#!/bin/sh
set -e

echo "Running tests..."
pytest apps/ --ds=core.settings.test -v

if [ $? -ne 0 ]; then
    echo " Tests failed! Exiting container."
    exit 1
fi

echo " All tests passed."
echo "Making and applying migrations..."
python manage.py makemigrations users --noinput
python manage.py makemigrations bookstore --noinput
python manage.py makemigrations reservation --noinput
python manage.py migrate users --noinput
python manage.py migrate bookstore --noinput
python manage.py migrate reservation --noinput

if [ "$DJANGO_ENV" = "prod" ]; then
    echo "Collecting static files..."
    python manage.py collectstatic --noinput
    echo "Starting Gunicorn server..."
    gunicorn core.wsgi:application --bind 0.0.0.0:$DJANGO_PORT --workers=${GUNICORN_WORKERS:-4}

else
    echo "Starting Django development server..."
    python manage.py runserver 0.0.0.0:$DJANGO_PORT

fi
