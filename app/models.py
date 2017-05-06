# app/models.py

from app import db

class News(db.Model):
	id = db.Column(db.Integer, primary_key=True)	
	headline = db.Column(db.Text)
	medium = db.Column(db.String(255))
	external_created_at = db.Column(db.DateTime)
	created_at = db.Column(db.DateTime)

	company_id = db.Column(db.Integer, db.ForeignKey('company.id'))
	company = db.relationship('Company',
		backref=db.backref('news', lazy='dynamic'))

	def __init__(self, headline, medium, company, external_created_at=None, created_at=None):
		self.headline = headline
		self.medium = medium
		if external_created_at is None:
			external_created_at = datetime.utcnow()
		if created_at is None:
			created_at = datetime.utcnow()			
		self.external_created_at = external_created_at
		self.created_at = created_at
		self.company = company

	def __repr__(self):
		return '<News %r>' % self.headline


class Company(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	twitter_handle = db.Column(db.String(255))

	def __init__(self, name, twitter_handle):
		self.name = name
		self.twitter_handle = twitter_handle

	def __repr__(self):
		return '<Company %r>' % self.name