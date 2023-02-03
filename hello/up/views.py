from flask import Blueprint

from hello.extensions import db
from hello.initializers import redis

up = Blueprint("up", __name__, template_folder="templates", url_prefix="/up")


@up.get("/")
def index():
    return ""


@up.get("/databases")
def databases():
    redis.ping()
    db.engine.execute("SELECT 1")
    return ""
