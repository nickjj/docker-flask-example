from celery import Celery, Task
import json
import logging
import time
import uuid
from flask import Flask, g, request
from werkzeug.debug import DebuggedApplication
from werkzeug.middleware.proxy_fix import ProxyFix

from hello.extensions import db, debug_toolbar, flask_static_digest
from hello.health.views import health
from hello.page.views import page
from hello.up.views import up


def create_celery_app(app=None):
    """
    Create a new Celery app and tie together the Celery config to the app's
    config. Wrap all tasks in the context of the application.

    :param app: Flask app
    :return: Celery app
    """
    app = app or create_app()

    class FlaskTask(Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery = Celery(app.import_name, task_cls=FlaskTask)
    celery.conf.update(app.config.get("CELERY_CONFIG", {}))
    celery.set_default()
    app.extensions["celery"] = celery

    return celery




def register_request_logging(app):
    if not app.config.get("JSON_LOGS"):
        return

    logger = logging.getLogger("hello.request")

    @app.before_request
    def _set_request_id():
        request_id = request.headers.get("X-Request-Id") or str(uuid.uuid4())
        g.request_id = request_id
        g.request_start = time.perf_counter()

    @app.after_request
    def _log_request(response):
        request_id = getattr(g, "request_id", None) or str(uuid.uuid4())
        payload = {
            "method": request.method,
            "path": request.path,
            "status_code": response.status_code,
            "request_id": request_id,
        }
        logger.info(json.dumps(payload))
        return response


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__, static_folder="../public", static_url_path="")

    app.config.from_object("config.settings")

    if settings_override:
        app.config.update(settings_override)

    middleware(app)
    register_request_logging(app)

    app.register_blueprint(up)
    app.register_blueprint(health)
    app.register_blueprint(page)

    extensions(app)

    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    debug_toolbar.init_app(app)
    db.init_app(app)
    flask_static_digest.init_app(app)

    return None


def middleware(app):
    """
    Register 0 or more middleware (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    # Enable the Flask interactive debugger in the brower for development.
    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    # Set the real IP address into request.remote_addr when behind a proxy.
    app.wsgi_app = ProxyFix(app.wsgi_app)

    return None


celery_app = create_celery_app()
