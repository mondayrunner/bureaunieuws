# app/home/views.py

from flask import render_template

from . import home

@home.route('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home/index.html', title="Overzicht")

@home.route('/about')
def about():
    """
    Render the about page
    """
    return render_template('home/about.html', title="Over het platform")