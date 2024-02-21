from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db_config import db_settings


app = Flask(__name__)
# app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = (f'postgresql://{db_settings["username"]}:{db_settings["password"]}@'
                                         f'{db_settings["localhost"]}/{db_settings["db_name"]}')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

