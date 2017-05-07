# app/api/views.py
from .. import db
from ..models import News, Company

class TwitterScraper():
	"""Twitter scraper"""

	def __init__(self):
		self.data = []

	def scrape():
		return 'scraping'