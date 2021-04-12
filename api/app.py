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

from resources.food import FoodAPI
from resources.food import Food
from resources.food import FoodList
from resources.food import FoodImageUploader
from resources.food import FoodImageDownloader

from resources.consumer import Consumer

from resources.landing import Landing

app = Flask(__name__)
app.config.from_object('config')

CORS(app)
api = Api(app, version='1.0', title='Harvest App API',  description='Restful API for Haverst Application' , ui=False)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all() 

jwt = JWT(app, authenticate, identity)

api.add_resource(Landing, '/index')

api.add_resource(StoreAPI, '/store')
api.add_resource(Store, '/store/<string:_id>')
api.add_resource(StoreList, '/stores')    

api.add_resource(User, '/register')
api.add_resource(User, '/user/<string:store>/<string:email>')
api.add_resource(UserList, '/users/<string:store>')

api.add_resource(FoodAPI, '/food')
api.add_resource(Food, '/food/<string:_id>/<string:store>')
api.add_resource(FoodList, '/foods/<string:store>')
api.add_resource(FoodImageUploader, '/food/photo/upload')
api.add_resource(FoodImageDownloader, '/food/photo/download/<string:food_id>')

api.add_resource(Consumer, '/consumer/<string:lat>/<string:lng>/<string:unit>')



if __name__ == '__main__':
    app.run(debug=True)    