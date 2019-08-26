#!/usr/bin/env sh

rm -rf migrations

export FLASK_APP=TripServer.py
export FLASK_DEBUG=1
export APP_CONFIG_FILE=config.py
export DATABASE_URL="postgresql://localhost/tripdb"
export SQLALCHEMY_DATABASE_URI=DATABASE_URL

flask db init
# flask run
