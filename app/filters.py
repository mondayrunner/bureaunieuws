# app/filters.py
import jinja2
import flask
import time
from datetime import datetime

blueprint = flask.Blueprint('filters', __name__)

# using the decorator
@jinja2.contextfilter
@blueprint.app_template_filter()
def timesince(dt, default="just now"):

	#print dt
	"""
	Returns string representing "time since" e.g.
	3 days ago, 5 hours ago etc.
	"""

	#timestamp = datetime.strftime(dt, '%Y-%m-%d %H:%M:%S')
	#dt = datetime.strptime(dt, f)

	pattern = '%d-%m-%Y %H:%M:%S'
	db_time = datetime.strptime(str(dt), pattern)	
	return db_time

	#db_time = datetime.fromtimestamp(epoch)

	now = datetime.utcnow()
	diff = now - db_time
	
	periods = (
		(diff.days / 365, "year", "years"),
		(diff.days / 30, "month", "months"),
		(diff.days / 7, "week", "weeks"),
		(diff.days, "day", "days"),
		(diff.seconds / 3600, "hour", "hours"),
		(diff.seconds / 60, "minute", "minutes"),
		(diff.seconds, "second", "seconds"),
	)

	for period, singular, plural in periods:
		
		if period:
			return "%d %s ago" % (period, singular if period == 1 else plural)

	return default
