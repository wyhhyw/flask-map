from flask_sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)


def create_app():
    db.init_app(app)
    db.create_all()
    return app


# 构建我们的数据库
class POI(db.Model):
    __tablename__ = 'pois'

    poiId = db.Column(db.Integer, primary_key=True)
    poiName = db.Column(db.String(120), index=True, unique=True)
    poiLat = db.Column(db.Float)
    poiLng = db.Column(db.Float)

    def __repr__(self):
        return '<POI {}: [{}, {}]>'.format(self.poiName, self.poiLat, self.poiLng)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __repr__(self):
        return '<User: {}>'.format(self.name)