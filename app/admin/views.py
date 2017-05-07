# app/admin/views.py

from . import admin
from .. import db
from ..models import News, Company
from flask import render_template

# render admin login
@admin.route('/', methods=['GET', 'POST'])
def admin():
	return "admin"

@admin.route('/twitter')
def twitter():
	return "twitter"