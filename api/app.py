from flask import Flask, Blueprint
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
from resources.user import UserProfile

from resources.food import FoodAPI
from resources.food import Food
from resources.food import FoodList
from resources.food import FoodImageUploader
from resources.food import FoodImageDownloader

from resources.consumer import Consumer

from resources.landing import Landing
from resources.home import Home
from resources.login import Login
from resources.signup import Signup
from resources.food_management import FoodManagement

app = Flask(__name__)
app.config.from_object('config')

# https://github.com/noirbizarre/flask-restplus/issues/247
@app.route("/")
def get_home():
    return Landing.get(None)


CORS(app)
api = Api(app, version='1.0', title='Harvest App API',  description='Restful API for Haverst Application', doc=False)
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
api.add_resource(UserProfile, '/user/profile')

api.add_resource(FoodAPI, '/food')
api.add_resource(Food, '/food/<string:_id>/<string:store>')
api.add_resource(FoodList, '/foods/<string:store>')
api.add_resource(FoodImageUploader, '/food/photo/upload')
api.add_resource(FoodImageDownloader, '/food/photo/download/<string:food_id>')

api.add_resource(Consumer, '/consumer/<string:lat>/<string:lng>/<string:unit>')


api.add_resource(Home, '/home')
api.add_resource(Login, '/login')
api.add_resource(Signup, '/signup')
api.add_resource(FoodManagement, '/food_management')

# https://github.com/noirbizarre/flask-restplus/issues/712
#api.add_resource(Landing, '/')
#@app.route("/")
#def get_home():
#    return Landing.get(None)


if __name__ == '__main__':
    app.run(debug=True)    