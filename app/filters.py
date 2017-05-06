# app/filters.py

from datetime import datetime

def timeago(dt, default="Nu geplaatst"):

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
    
