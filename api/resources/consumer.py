from flask_restplus import Resource, reqparse
from models.store import StoreModel
from models.food import FoodModel
from db import db
from datetime import date
from geopy.distance import geodesic 


class Consumer(Resource):
    def get(self, lat, lng, unit):        

        stores = {}

        for s, f in db.session.query(StoreModel, FoodModel).filter(StoreModel.id == FoodModel.store_id, FoodModel.expiration >= date.today()).all():
            if s.id in stores:
                stores[s.id]['items available'] += 1
            else:
                if (unit == 'km'):
                    distance = geodesic((lat, lng), (s.lat,s.lng)).km

                elif (unit == 'miles'):
                    distance = geodesic((lat, lng), (s.lat,s.lng)).miles

                elif (unit == 'meters'):
                    distance = geodesic((lat, lng), (s.lat,s.lng)).meters


                stores[s.id] = {
                    'name'            : s.name, 
                    'phone'           : s.phone,
                    'street'          : s.street,
                    'city'            : s.city,
                    'state'           : s.state,
                    'zipcode'         : s.zipcode,
                    'zipcode'         : s.zipcode,
                    'latitude'        : s.lat, 
                    'longiture'       : s.lng,
                    'open at'         : f'{str(s.open_at.hour).zfill(2)}:{str(s.open_at.minute).zfill(2)}',
                    'close at'        : f'{str(s.close_at.hour).zfill(2)}:{str(s.close_at.minute).zfill(2)}',
                    'items available' : 1,
                    'distance'        : f'{distance}',
                }

        return {'stores' : stores}, 201
        

