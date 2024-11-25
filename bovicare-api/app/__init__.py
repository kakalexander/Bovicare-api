from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
CORS(app)

from app import routes

with app.app_context():
    db.create_all()
