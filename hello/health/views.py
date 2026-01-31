from flask import Blueprint, jsonify

health = Blueprint("health", __name__)


@health.get("/healthz")
def healthz():
    return jsonify(status="ok")
