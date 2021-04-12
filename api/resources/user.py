from flask_restplus import Resource, Api, reqparse
from models.user import UserModel
from flask_jwt import jwt_required, current_identity

class User(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('email', type=str, required=True, help="Field email cannot be empty")        
        parser.add_argument('password', type=str, required=True, help="Field password cannot be empty")
        parser.add_argument('store', type=int, required=True, help="Field store cannot be empty")

        payload = parser.parse_args()

        if UserModel.find_by_email_store(payload['email'], payload['store']):
            return { 
                'status'  : 'error',
                'message' : f'User {payload["email"]} already exits for store {payload["store"]}'
            }, 409
        else:
            user = UserModel(payload['password'], payload['email'], payload['store'] )
            user.save()

            return {
                'status'  : 'ok',
                'message' : 'User created without issues', 
                'record'  : user.json()
            }

    def get(self, store, email):
        user = UserModel.find_by_email_store(email, store)

        if user:
            return user.json()
        else:
            return {
                'status'  : 'error',
                'message' :  f'User {email} not found in store {store}'
            }, 404
                

    def delete(self, store, email):
        user = UserModel.find_by_email_store(email, store)

        if user:
            user.delete()
            
            return {
                'status' : 'ok',
                'message' : f'User {email} deleted from store {store}.'
            }

        else:
            return {
                'status': 'error',
                'message' : f'User {email} not found in store {store}'
            }, 404


    def put(self, store, email):
        parser = reqparse.RequestParser()
        parser.add_argument('password', type=str, required=True, help="Field password cannot be empty")        

        user = UserModel.find_by_email_store(email, store)

        if user:
            payload = parser.parse_args()

            user.password = payload['password']
            user.save()

            return {
                'status'  : 'ok',
                'message' : 'User password changed without issues'
                }, 201            
        else:
            return {
                'status': 'error',
                'message' : f'User {email} not found in store {store}'
            }, 404
                

class UserList(Resource):
    @jwt_required()
    def get(self, store):
         return { 'users' : [user.json() for user in UserModel.query.filter_by(store_id = store).all()]}


class UserProfile(Resource):
    @jwt_required()
    def get(self):
        return current_identity.json()
        
