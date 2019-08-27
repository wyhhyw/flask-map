# config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'psql2019'

    # AMap map API:
    AMAP_APP_NAME='SmartTip-Demo'
    AMAP_ACCESS_KEY='c84e1b4830a1fa4007b2de453663b62a'

    POSTGRES = {
        'user': 'tripuser',
        'pw': SECRET_KEY,
        'db': 'tripdb',
        'host': 'localhost',
        'port': '5432',
    }

    # Database management
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
