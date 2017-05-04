# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')

	#from app import models

	from .home import home as home_blueprint
	app.register_blueprint(home_blueprint)

	# from .admin import admin as admin_blueprint
	# app.register_blueprint(admin_blueprint, url_prefix='/admin')

	return app