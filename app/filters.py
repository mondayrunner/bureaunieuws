# app/filters.py
from datetime import datetime

def timeago(dt, default="Nu geplaatst"):

	#return repr(dt.hour)
	#return repr(datetime.utcnow())

    now = datetime.now()
    diff = now - dt
    
    periods = (
        (diff.days / 365, "jaar", "jaren"),
        (diff.days / 30, "maand", "maanden"),
        (diff.days / 7, "week", "weken"),
        (diff.days, "dag", "dagen"),
        (diff.seconds / 3600, "uur", "uren"),
        (diff.seconds / 60, "minuut", "minuten"),
        (diff.seconds, "seconde", "seconden"),
    )

    for period, singular, plural in periods:
        
        if period:
            return "%d %s" % (period, singular if period == 1 else plural)

    return default



# def string_to_data_time(d):

# 	d = d.replace('/', '-')
# 	if ' ' in d:
# 		_datetime = d.split(' ')
# 		if len(_datetime) == 2:
# 			_d = _string_to_date(_datetime[0])
# 			_t = _string_to_time(_datetime[1])
# 			return _combine_date_time(_d, _t)

# 	return None

# def _combine_date_time(d, t):
# 	if (d is not None) and (t is not None):
# 		return datetime(d.year, d.month, d.day, t.hour, t.minute, t.second)
# 	return None
	
