from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_static_digest import FlaskStaticDigest
from redis import Redis

from config.settings import REDIS_URL


debug_toolbar = DebugToolbarExtension()
db = SQLAlchemy()
redis = Redis.from_url(REDIS_URL)
flask_static_digest = FlaskStaticDigest()
