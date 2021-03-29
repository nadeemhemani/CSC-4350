import datetime
import werkzeug
import os
import uuid

from flask import request, send_from_directory
from flask_restplus import Resource, reqparse
from models.food import FoodModel
from werkzeug.utils import secure_filename
from config import UPLOAD_FOLDER


class FoodAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', type=str, required = True, help="Field name cannot be empty")
        parser.add_argument('quantity', type=int, required = True, help="Field name cannot be empty")
        parser.add_argument('calories', type=int, required = True, help="Field name cannot be empty")
        parser.add_argument('expiration', type=str, required = True, help="Field name cannot be empty")
        parser.add_argument('store', type=int, required = True, help="Field name cannot be empty")

        payload = parser.parse_args()

        expiration = datetime.datetime.strptime(payload['expiration'], '%m/%d/%Y')

        food = FoodModel(payload['name'], payload['quantity'], payload['calories'], expiration, payload['store'])
        food.save()
            
        return {
                'status'  : 'ok',
                'message' : 'Store created without issues',
                'record'  : food.json()                   
                }, 201        

class Food(Resource):
    def get(self, _id, store):
        food = FoodModel.find_by_store_id(_id, store)

        if food:
            return food.json()
        else:
            return {
                'status'  : 'error',
                'message' : f'Food {_id} not found in store {store}'
            }, 404

    def delete(self, _id, store):
        food = FoodModel.find_by_store_id(_id, store)

        if food:
            food.delete()

            return {
                'status': 'ok',
                'message' : f'Food {_id} deleted for store {store}'
            }
        else:
            return {
                'status'  : 'error',
                'message' : f'Food {_id} not found in store {store}'
            }, 404

    def put(self, _id, store):
        parser = reqparse.RequestParser()

        parser.add_argument('name', type=str, required = False, help="Field name cannot be empty")
        parser.add_argument('quantity', type=int, required = False, help="Field name cannot be empty")
        parser.add_argument('calories', type=int, required = False, help="Field name cannot be empty")
        parser.add_argument('expiration', type=str, required = False, help="Field name cannot be empty")

        food = FoodModel.find_by_store_id(_id, store)

        if (food):
            payload = parser.parse_args()

            if payload.get('name') is not None: food.name = payload['name']
            if payload.get('quantity') is not None: food.quantity = payload['quantity']
            if payload.get('calories') is not None: food.calories = payload['calories']
            if payload.get('expiration') is not None: food.expiration = datetime.datetime.strptime(payload['expiration'], '%m/%d/%Y')

            food.save()

            return {
                'status': 'ok',
                'message' : f'Food {_id} changed for store {store}'
            }
        else:
            return {
                'status'  : 'error',
                'message' : f'Food {_id} not found in store {store}'
            }, 404

class FoodList(Resource):
    def get(self, store):
        return { 'foods' : [food.json() for food in FoodModel.query.filter_by(store_id = store).all()]}

class FoodImageUploader(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('file',type=werkzeug.datastructures.FileStorage, location='files')

        payload = parser.parse_args()
        food_id =   request.form.to_dict().get("food", "")


        if (payload['file'] == ""):
            return {
                'status'  : 'error',
                'message' : 'File parameter cannot be empty'
            }
        elif (food_id == ""):
            return {
                'status'  : 'error',
                'message' : 'Food_Id parameter cannot be empty'
            }

        food = FoodModel.find_by_id(food_id)

        if (food):
            photo = payload['file']       

            if (photo):
                file_extension = os.path.splitext(photo.filename)[1]
                filename = secure_filename(f'{uuid.uuid4()}{file_extension}')
                file_location = os.path.join(UPLOAD_FOLDER,filename)

                photo.save(file_location)

                food.photo = file_location
                food.save()

                return {
                    'status'  : 'ok',
                    'message' : f'File {filename} uploaded'
                }, 201
            else:
                return  {
                    'status' : 'error',
                    'message' : f'Error processing the upload file'
                }, 403
        else:
            return {
                'status'  : 'error',
                'message' : f'Food {food_id} not found'
            }, 404

class FoodImageDownloader(Resource):
    def get(self, food_id):
        food = FoodModel.find_by_id(food_id)

        if food:
            if food.photo:                
                return send_from_directory(UPLOAD_FOLDER, os.path.basename(food.photo), as_attachment=True)
            else:
                return {
                    'status'  : 'error',
                    'message' : f'Food {food_id} does not have a photo'
                }, 404

        else:
            return {
                'status'  : 'error',
                'message' : f'Food {food_id} not found'
            }, 404













