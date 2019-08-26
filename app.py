from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://localhost/tripdb'

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class POI(db.Model):
    poiId = db.Column(db.Integer, primary_key=True)
    poiName = db.Column(db.String(128), index=True, unique=True)
    poiLat = db.Column(db.Float)
    poiLng = db.Column(db.Float)

    def __repr__(self):
        return '<POI {}: [{}, {}]>'.format(self.poiName, self.poiLat, self.poiLng)
