#!/bin/bash
python manage.py dbshell < m.sql
python manage.py makemigrations site_app
python manage.py makemigrations
python manage.py migrate
python manage.py migrate site_app