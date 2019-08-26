from TripServer import db
# from sqlalchemy.dialects.postgresql import JSON

class POI(db.Model):
    __tablename__ = 'pois'

    poiId = db.Column(db.Integer, primary_key=True)
    poiName = db.Column(db.String(120), index=True, unique=True)
    poiLat = db.Column(db.Float)
    poiLng = db.Column(db.Float)

    def __repr__(self):
        return '<POI {}: [{}, {}]>'.format(self.poiName, self.poiLat, self.poiLng)