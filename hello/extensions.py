from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_static_digest import FlaskStaticDigest

from config.settings import REDIS_URL


debug_toolbar = DebugToolbarExtension()
db = SQLAlchemy()
flask_static_digest = FlaskStaticDigest()
