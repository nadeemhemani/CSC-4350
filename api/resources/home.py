from flask import render_template, make_response,redirect
from flask.helpers import url_for
from flask_restplus import Resource
from flask_jwt import jwt_required

class Home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('home.html'), 200, headers)




        
