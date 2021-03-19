from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    phone = db.Column(db.String(30))
    street = db.Column(db.String(120))
    city = db.Column(db.String(60))
    state = db.Column(db.String(60))
    zipcode = db.Column(db.Integer)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)
    open_at = db.Column(db.DateTime)
    close_at = db.Column(db.DateTime)
                 
    users = db.relationship('UserModel')
    foods = db.relationship('FoodModel')

    def __init__(self, name, phone, street, city, state, zipcode, lat, lng, open_at, close_at):
        self.name = name
        self.phone = phone
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.lat = lat
        self.lng = lng
        self.open_at = open_at
        self.close_at = close_at

    def json(self):
        
        return {
            'id'        : self.id, 
            'name'      : self.name, 
            'street'    : self.street, 
            'city'      : self.city,
            'state'     : self.state, 
            'zipcode'   : self.zipcode, 
            'phone'     : self.phone,
            'latitude'  : self.lat,
            'longitude' : self.lng,
            'open at'   : f'{str(self.open_at.hour).zfill(2)}:{str(self.open_at.minute).zfill(2)}',
            'close at'  : f'{str(self.close_at.hour).zfill(2)}:{str(self.close_at.minute).zfill(2)}',
        }

    @classmethod
    def find_by_id(cls, _id):
        return StoreModel.query.filter_by(id = _id).first()


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()        


        


