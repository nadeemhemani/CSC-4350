from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String)
    email = db.Column(db.String)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))

    def __init__(self, password, email, store):
        self.password = password
        self.email = email
        self.store_id = store

    def json(self):
        return { 'id'    : self.id,
                 'email' : self.email,
                 'store' : self.store_id
               }        

    @classmethod
    def find_by_email_store(cls, email, store):
        return UserModel.query.filter_by(email = email, store_id = store).first()
    
    @classmethod
    def find_by_email(cls, email):
        return UserModel.query.filter_by(email = email).first()

    @classmethod
    def find_by_id(cls, _id):
        return UserModel.query.filter_by(id = _id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()    






