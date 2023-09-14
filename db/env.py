from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from hello.app import create_app

# There's no access to current_app here so we must create our own app.
app = create_app()
db_uri = app.config["SQLALCHEMY_DATABASE_URI"]
db = app.extensions["sqlalchemy"]

# Provide access to the values within alembic.ini.
config = context.config

# Sets up Python logging.
fileConfig(config.config_file_name)

# Sets up metadata for autogenerate support,
config.set_main_option("sqlalchemy.url", db_uri)
target_metadata = db.metadata

# Configure anything else you deem important, example:
# my_important_option = config.get_main_option("my_important_option")


def run_migrations_offline():
    """
    Run migrations in 'offline' mode.

    This configures the context with just a URL and not an Engine, though an
    Engine is acceptable here as well. By skipping the Engine creation we
    don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """
    Run migrations in 'online' mode.

    In this scenario we need to create an Engine and associate a connection
    with the context.
    """

    # Auto-generated migrations are pretty sketchy but if you use them this
    # will prevent Alembic from creating an empty migration if nothing changed.
    # Source: https://alembic.sqlalchemy.org/en/latest/cookbook.html
    def process_revision_directives(context, revision, directives):
        if config.cmd_opts.autogenerate:
            script = directives[0]
            if script.upgrade_ops.is_empty():
                directives[:] = []

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_revision_directives=process_revision_directives,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
