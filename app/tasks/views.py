# app/tasks/views.py

from . import tasks
from .. import db
from ..models import News, Company
from flask import render_template, current_app as app
import tweepy

# render task overview
@tasks.route('/', methods=['GET'])
def index():

	# configure Twitter API
	api = configureTwitter()

	tweets = api.user_timeline(id="fabrique")

	return render_template('tasks/index.html', tweets = tweets, title="Task runner")

def configureTwitter():
	auth = tweepy.OAuthHandler(app.config['TWITTER_CONSUMER_KEY'], app.config['TWITTER_CONSUMER_SECRET'])
	auth.set_access_token(app.config['TWITTER_OAUTH_TOKEN'], app.config['TWITTER_OAUTH_SECRET'])

	return tweepy.API(auth)