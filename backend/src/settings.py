# flake8: noqa

"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 5.2.

For more information, see:
https://docs.djangoproject.com/en/5.2/topics/settings/
"""

import os
from datetime import date, datetime, time
from pathlib import Path

from decouple import Config, RepositoryEnv

env = Config(repository=RepositoryEnv(".env.local"))

# === Paths ===
BASE_DIR = Path(__file__).resolve().parent.parent

# === Security ===
SECRET_KEY = env("SECRET_KEY")
DEBUG = env("DEBUG")
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'svcover.localhost', 'backend']

# === Installed Apps ===
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "constance",
    "constance.backends.database",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "api",
]

# === Middleware ===
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# === Rest Framework ===
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
}

# === URL Config ===
ROOT_URLCONF = "src.urls"

# === Templates ===
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "src.wsgi.application"

# === Database ===
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT", default="5432"),
    }
}

# === Password Validation ===
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# === Internationalization ===
LANGUAGE_CODE = "en-us"
TIME_FORMAT = "H:i"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# === Static Files ===
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# === Media Files ===
MEDIA_URL = "/uploads/"
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads")

# === Default Primary Key Field ===
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# === CORS ===

# TODO: Update this to your frontend URL
CORS_ALLOW_ALL_ORIGINS = True # debugging
# CORS_ALLOWED_ORIGINS = ["http://localhost:3000"]
CORS_ALLOW_CREDENTIALS = True


# === Cover API ===
COVER_API_URL = "http://svcover.localhost:8000/api"

# === Constance Configuration ===
CONSTANCE_BACKEND = "constance.backends.database.DatabaseBackend"

CONSTANCE_ADDITIONAL_FIELDS = {
    "date_field": ["django.forms.DateField", {}],
    "time_field": ["django.forms.TimeField", {}],
    "datetime_field": ["django.forms.DateTimeField", {}],
    "integer_field": ["django.forms.IntegerField", {"min_value": 1}],
}

CONSTANCE_CONFIG = {
    "EVENT_DATE": (
        date(2025, 5, 14),
        "Date of the Cover Career Day",
        "date_field",
    ),
    "EVENT_START_TIME": (
        time(9, 0),
        "Start time of the Cover Career Day",
        "time_field",
    ),
    "EVENT_END_TIME": (
        time(19, 0),
        "End time of the Cover Career Day",
        "time_field",
    ),
    "REGISTRATIONS_OPEN": (
        datetime(2025, 4, 23, 0, 0),
        "Open registrations",
        "datetime_field",
    ),
    "REGISTRATIONS_CLOSED": (
        datetime(2025, 5, 14, 19, 0),
        "Close registrations",
        "datetime_field",
    ),
    "SESSIONS_OPEN": (
        datetime(2025, 4, 30, 0, 0),
        "Open registrations for sessions",
        "datetime_field",
    ),
    "SESSIONS_CLOSED": (
        datetime(2025, 5, 14, 11, 30),
        "Close registrations for sessions",
        "datetime_field",
    ),
    "EVENT_CAPACITY": (150, "Maximum amount of participants", "integer_field"),
}

CONSTANCE_CONFIG_FIELDSETS = {
    "🗓️ Event Info": ("EVENT_DATE", "EVENT_START_TIME", "EVENT_END_TIME"),
    "📅 Registration Windows": ("REGISTRATIONS_OPEN", "REGISTRATIONS_CLOSED"),
    "🧾 Session Selection Windows": ("SESSIONS_OPEN", "SESSIONS_CLOSED"),
    "👥 Capacity": ("EVENT_CAPACITY",),
}

# === Mailing ===
EMAIL_BACKEND = (
    "django.core.mail.backends.filebased.EmailBackend"  # Change to SMTP in production
)
DEFAULT_FROM_EMAIL = "no-reply@yourdomain.com"
EMAIL_FILE_PATH = os.path.join(
    BASE_DIR, "emails"
)  # Change this to a proper directory for production
EMAIL_HOST = env("EMAIL_HOST")
EMAIL_PORT = env("EMAIL_PORT")
EMAIL_HOST_USER = env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
EMAIL_USE_TLS = True
