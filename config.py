# config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    TESTING = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'psql2019'

    # Database management
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # AMap map API:
    AMAP_APP_NAME='SmartTip-Demo'
    AMAP_ACCESS_KEY='c84e1b4830a1fa4007b2de453663b62a'