# app/home/views.py

from flask import render_template
from . import home
from .. import db
from ..models import News

# render homepage
@home.route('/')
def homepage():
	news = News.query.all()

	return render_template('home/index.html', news=news, title="Overzicht")

# render about page
@home.route('/about')
def about():
	return render_template('home/about.html', title="Over het platform")