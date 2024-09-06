#!/bin/bash

echo "=== Changing dir to /usr/src/app ==="
cd /usr/src/app || (echo "/usr/src/app directory not exist. Stopping script" && exit)
ls -lha /usr/src/app

echo "=== Copy local.py to /usr/src/app/config/ ==="
rm -rfv /usr/src/app/config/*
mkdir -p /usr/src/app/config/
cp -v /opt/django_setup/local.py.example /usr/src/app/config/local.py
ls -lha /usr/src/app/config/

echo "=== Run pip install --upgrade pip ==="
pip install --upgrade pip

echo "=== Run pip install -r requirements.txt ==="
pip install -r requirements.txt

echo "=== Run python manage.py makemigrations ==="
python manage.py makemigrations

echo "=== Run python manage.py migrate ==="
python manage.py migrate

echo "=== Run python manage.py create superuser ==="
python manage.py add_users


echo "=== Run application ==="
python manage.py runserver 0.0.0.0:8000

