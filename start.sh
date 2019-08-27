#!/usr/bin/env sh

rm -rf migrations

export FLASK_APP=manage.py
export FLASK_DEBUG=1
export APP_CONFIG_FILE=config.py

# !!execute these scripts (!only!) once!
# python manage.py db init
# python manage.py db migrate
# python manage.py db upgrade

# flask db init
flask run
