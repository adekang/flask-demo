from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint
from flask_restful import Api
from .resources.register import Register, HelloWorld

api_blueprint = Blueprint('api', __name__, url_prefix="/api")
api = Api(api_blueprint)
api.add_resource(Register, '/register')
api.add_resource(HelloWorld, '/hello')

db = SQLAlchemy()