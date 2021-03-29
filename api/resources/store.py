import datetime
import requests 
import geocoder

from flask_restplus import Resource, reqparse
from models.store import StoreModel
#from ...import config

from config import MAPQUEST_API_KEY

class StoreAPI(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('name', type=str, required = True, help="Field name cannot be empty")
        parser.add_argument('phone', type=str, required = True, help="Field phone cannot be empty")
        parser.add_argument('street', type=str, required = True, help="Field street cannot be empty")
        parser.add_argument('city', type=str, required = True, help="Field city cannot be empty")
        parser.add_argument('state', type=str, required = True, help="Field state cannot be empty")
        parser.add_argument('zipcode', type=int, required = True, help="Field zipcode cannot be empty")
        parser.add_argument('open', type=str, required = True, help="Field open cannot be empty")
        parser.add_argument('close', type=str, required = True, help="Field close cannot be empty")

        payload = parser.parse_args()

        open_at = datetime.datetime.strptime(payload['open'], '%H:%M:%S')
        close_at = datetime.datetime.strptime(payload['close'], '%H:%M:%S')

        lat, lng = GeoMapping.get_coordinates(payload['street'], payload['city'], payload['state'], payload['zipcode'])

        store = StoreModel(payload['name'], payload['phone'], payload['street'], payload['city'], payload['state'], payload['zipcode'], lat, lng, open_at, close_at)
        store.save()
            
        return {
                'status'  : 'ok',
                'message' : 'Store created without issues',
                'record'  : store.json()                   
                }, 201        

class Store(Resource):
    def get(self, _id):
        store = StoreModel.find_by_id(_id)

        if store:
            return store.json()
        else:
            return {
                'status' : 'error',
                'message' : f'Store {_id} not found'
            }, 404

    def delete(self, _id):
        store = StoreModel.find_by_id(_id)

        if store:
            store.delete()

            return {
                'status': 'ok',
                'message' : f'Store {_id} deleted'
            }
        else:
            return {
                'status' : 'error',
                'message' : f'Store {_id} not found'
            }, 404

    def put(self, _id):
        parser = reqparse.RequestParser()

        parser.add_argument('name', type=str, required = False, help="Field name cannot be empty")
        parser.add_argument('phone', type=str, required = False, help="Field phone cannot be empty")
        parser.add_argument('street', type=str, required = False, help="Field street cannot be empty")
        parser.add_argument('city', type=str, required = False, help="Field city cannot be empty")
        parser.add_argument('state', type=str, required = False, help="Field state cannot be empty")
        parser.add_argument('zipcode', type=int, required = False, help="Field zipcode cannot be empty")
        parser.add_argument('open', type=str, required = False, help="Field open cannot be empty")
        parser.add_argument('close', type=str, required = False, help="Field close cannot be empty")

        store = StoreModel.find_by_id(_id)

        if store:
            payload = parser.parse_args()

            if payload.get('name') is not None: store.name = payload['name']
            if payload.get('phone') is not None: store.phone = payload['phone']
            if payload.get('street') is not None: store.street = payload['street']
            if payload.get('city') is not None: store.city = payload['city']
            if payload.get('state') is not None: store.state = payload['state']
            if payload.get('zipcode') is not None: store.zipcode = payload['zipcode']
            if payload.get('open') is not None: store.open = datetime.datetime.strptime(payload['open'], '%H:%M:%S')
            if payload.get('close') is not None: store.close = datetime.datetime.strptime(payload['close'], '%H:%M:%S')
            
            if ((payload.get('street') is not None) and (payload.get('city') is not None) and (payload.get('state') is not None) and (payload.get('zipcode') is not None)):
                lat, lng = GeoMapping.get_coordinates(payload['street'], payload['city'], payload['state'], payload['zipcode'])

                store.lat = lat
                store.lng = lng
            
            store.save()

            return {
                'status': 'ok',
                'message' : f'Store {_id} changed'
            }
        else:
            return {
                'status' : 'error',
                'message' : f'Store {_id} not found'
            }, 404

class StoreList(Resource):
    def get(self):
        return { 'stores' : [store.json() for store in StoreModel.query.all()]}








class GeoMapping():
    @staticmethod
    def get_coordinates(street, city, state, zipcode):

        g = geocoder.mapquest(f'{street}, {city}, {state}, {zipcode}', key=MAPQUEST_API_KEY)

        if g.ok:
            lat = g.json.get('lat', 0)
            lng = g.json.get('lng', 0)

            return (lat, lng)
        
        return (0, 0)
            
        
        
