from db import db

class FoodModel(db.Model):
    __tablename__ = 'foods'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    quantity = db.Column(db.Integer)
    calories = db.Column(db.Integer)
    expiration = db.Column(db.DateTime)
    photo = db.Column(db.String)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    def __init__(self, name, quantity, calories, expiration, store_id):
        self.name = name
        self.quantity = quantity
        self.calories = calories
        self.expiration = expiration
        self.store_id = store_id

    def json(self):
        
        return {
            'id'         : self.id, 
            'name'       : self.name, 
            'quantity'   : self.quantity,
            'calories'   : self.calories, 
            'expiration' : self.expiration.__str__(),
            'store'      : self.store_id
        }

    @classmethod
    def find_by_id(cls, _id):
        return FoodModel.query.filter_by(id = _id).first()

    @classmethod
    def find_by_store_id(cls, _id, store_id):
        return FoodModel.query.filter_by(id = _id, store_id = store_id).first()


    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()        



