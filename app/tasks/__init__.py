# app/tasks/__init__.py

from flask import Blueprint

tasks = Blueprint('tasks', __name__)

from . import views
