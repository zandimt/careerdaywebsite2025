#!/bin/bash

echo "⏳ Waiting for db to be ready..."
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
  sleep 1
done

echo "📦 Applying migrations..."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

echo "👤 Creating superuser (if not exists)..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')
END

echo "🚀 Starting dev server..."
python manage.py runserver 0.0.0.0:8000
