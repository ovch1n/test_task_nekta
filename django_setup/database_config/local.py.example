import os
from datetime import datetime

DEBUG = True

ADMINS = (('ovch1n', 'oB4uH132@gmail.com'), ('ovch1n', 'oB4uH@yandex.ru'),)

ALLOWED_HOSTS = [os.environ.get("DJANGO_ALLOWED_HOSTS")]

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("POSTGRES_ENGINE"),
        "NAME": os.environ.get("POSTGRES_DB"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
