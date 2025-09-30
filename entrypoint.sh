#!/bin/bash

# Wait for Postgres
echo "Waiting for Postgres..."
while ! nc -z db 5432; do
  sleep 0.1
done
echo "Postgres started"

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Execute CMD from docker-compose
exec "$@"