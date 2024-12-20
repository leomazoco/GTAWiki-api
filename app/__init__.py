from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

from app import config

app = Flask(__name__)
config.read_config(app)
db = SQLAlchemy(app)
api = Api(app)
CORS = CORS(app, supports_credentials=True)

from app import routes
from app.models import *