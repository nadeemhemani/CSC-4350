from flask import render_template, make_response
from flask_restplus import Resource

class Signup(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('signup.html'), 200, headers)




        
