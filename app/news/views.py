# app/news/views.py

from . import news
from .. import db
from ..models import News
from flask import current_app as app
from flask import render_template

# render homepage
@news.route('/', methods=['GET', 'POST'])
@news.route('/nieuws', methods=['GET', 'POST'])
@news.route('/nieuws/<int:page>', methods=['GET', 'POST'])
def nieuws(page=1):

	news = News.query.paginate(page, app.config['POSTS_PER_PAGE'], error_out=False)

	return render_template('news/index.html', news=news, title="Overzicht")

# render about page
@news.route('/about')
def about():
	return render_template('news/about.html', title="Over het platform")