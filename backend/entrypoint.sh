#!/bin/bash
# flake8: noqa

echo "⏳ Waiting for db to be ready..."
until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER"; do
  sleep 1
done

echo "📦 Applying migrations..."
python manage.py migrate

echo "👤 Creating superuser (if not exists)..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell

echo "🚀 Starting dev server..."
python manage.py runserver 0.0.0.0:8000
