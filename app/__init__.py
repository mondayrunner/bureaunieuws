# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# local imports
from config import app_config

# after existing third-party imports
from flask_migrate import Migrate

# db variable initialization
db = SQLAlchemy()

def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)

	# load config files
	app.config.from_object(app_config[config_name])
	app.config.from_pyfile('config.py')

	# init database
	db.init_app(app)

	# set migration
	migrate = Migrate(app, db)
	
	# import models
	from app import models

	# home blueprint
	from .home import home as home_blueprint
	app.register_blueprint(home_blueprint)

	# from .admin import admin as admin_blueprint
	# app.register_blueprint(admin_blueprint, url_prefix='/admin')

	return app