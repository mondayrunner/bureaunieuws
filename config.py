# config.py

class Config(object):
	"""
	Common configurations
	"""

	POSTS_PER_PAGE = 12

class DevelopmentConfig(Config):
	"""
	Development configurations
	"""

	DEBUG = True
	SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
	"""
	Production configurations
	"""

	DEBUG = False

app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig
}