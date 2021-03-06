from flask import Flask
from flask_restplus import Resource, Api, Namespace, fields
from flask_cors import CORS 
from flask_jwt import JWT
from db import db

from resources.store import StoreAPI
from resources.store import Store
from resources.store import StoreList

from security import authenticate, identity
from resources.user import User
from resources.user import UserList


app = Flask(__name__)
app.config.from_object('config')

CORS(app)
api = Api(app, version='1.0', title='Harvest App API',  description='Restful API for Haverst Application')

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all() 

jwt = JWT(app, authenticate, identity)

api.add_resource(StoreAPI, '/store')
api.add_resource(Store, '/store/<string:_id>')
api.add_resource(StoreList, '/stores')    

api.add_resource(User, '/register')
api.add_resource(User, '/user/<string:store>/<string:email>')
api.add_resource(UserList, '/users/<string:store>')



if __name__ == '__main__':
    app.run(debug=True)    