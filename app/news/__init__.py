# app/news/__init__.py

from flask import Blueprint

news = Blueprint('news', __name__)

from . import views