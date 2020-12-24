import os


SECRET_KEY = os.getenv("SECRET_KEY", None)

SERVER_NAME = os.getenv("SERVER_NAME",
                        "localhost:{0}".format(os.getenv("DOCKER_WEB_PORT",
                                                         "8000")))
# SQLAlchemy.
pg_user = os.getenv("POSTGRES_USER", "hello")
pg_pass = os.getenv("POSTGRES_PASSWORD", "password")
pg_host = os.getenv("POSTGRES_HOST", "postgres")
pg_port = os.getenv("POSTGRES_PORT", "5432")
pg_db = os.getenv("POSTGRES_DB", pg_user)
db = "postgresql://{0}:{1}@{2}:{3}/{4}".format(pg_user, pg_pass,
                                               pg_host, pg_port, pg_db)
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", db)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Celery.
broker_url = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")
CELERY_CONFIG = {
  "broker_url": broker_url,
  "result_backend": broker_url,
  "include": []
}
