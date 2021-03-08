import os
from datetime import timedelta 

PROPAGATE_EXCEPTIONS = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = False
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///harvest.db')

MAPQUEST_API_KEY = os.environ.get('MAPQUEST_API_KEY', 'EoZti5KeH2Ce7rmBmnCgJVvIMARHmdpc')

SECRET_KEY = "\dXd(;h9Jn.~sR_m},/Hmh$KyZw>rBmqW-b(HdH<84e[56CF\7Y`vHzTCb,`a8gn>As;FGD])KgN\HK"
JWT_AUTH_URL_RULE='/auth'
JWT_EXPIRATION_DELTA=timedelta(seconds=1800)
JWT_AUTH_USERNAME_KEY = 'email'

UPLOAD_FOLDER='upload/'