# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added

- `bin/rename-project` script to assist with renaming the project
- Use Black to format Python code

### Changed

- Switch `OptimizeCSSAssetsPlugin` with `CssMinimizerPlugin` for Webpack 5
- Replace deprecated Webpack 5 `file-loader` with `asset/resource`
- Avoid using multi-line imports with commas or parenthesis
- Update SQLAlchemy from `1.3.23` to `1.4.11`
- Update SQLAlchemy-Utils from `0.36.8` to `0.37.0`
- Update Flask-SQLAlchemy from `2.4.4` to `2.5.1`
- Update gunicorn from `20.0.4` to `20.1.0`
- Update Alembic from `1.5.4` to `1.5.8`
- Update flake8 from `3.8.4` to `3.9.1`
- Update TailwindCSS to `2.1.0` and enable the JIT compiler
- Replace `APP_NAME` in `run` script with `POSTGRES_USER` for connecting to psql

### Removed

- Unused `webpack` import in Webpack config
- Remove Webpack's cache since the JIT compiler is pretty speedy as is

### Fixed

- Code styling issues in the Webpack config (single quotes, semi-colons, etc.)
- Set an empty ENTRYPOINT for the worker to avoid race conditions when copying static files
- Fix `run` script error for unbound variable in older versions of Bash on macOS

## [0.4.0] - 2021-03-02

### Added

- `PORT` env variable to be compatible with more hosting providers
- `CELERY_LOG_LEVEL` env variable to configure Celery's log level (defaults to `info`)
- `run cmd` to run any command you want in the web container, ie. `run cmd python3 --version`

### Changed

- Rename `DOCKER_WEB_PORT` to `DOCKER_WEB_PORT_FORWARD`
- Refactor `run` script so all web container commands use the new `cmd` function
- Replace `##` comments with `#` in the `run` script

### Removed

- Ability to customize gunicorn bind host, it's hard coded to `0.0.0.0` now
- `curl` and `libpq-dev` apt dependencies from the webpack image (they're not needed)
- Remove unnecessary `mkdir` for the pip cache dir and chown'ing `/home/python`

### Fixed

- Define `PYTHONPATH="."` env var in the Dockerfile so that `flask db migrate` works
- Update Flask-DB to `0.3.1` which makes sure `alembic.ini.new` gets properly initalized
- Commit `public/.keep` and make sure the `.keep` file is never removed

## [0.3.0] - 2021-02-20

### Added

- `run pip3:outdated` task to show outdated Python dependencies
- `run yarn:outdated` task to show outdated Node dependencies

### Changed

- Update PostgreSQL from `13.1` to `13.2`
- Update Redis from `6.0.9` to `6.0.10`
- Update Python from `3.9.1` to `3.9.2`
- Update Node from `14.15.1` to `14.5.5`
- Update all Python and Node packages to their latest stable releases
- Import `Redis` more efficiently in `hello/extensions.py`
- Disable Flask tip about `python-dotenv` when running any `flask` CLI command
- Refactor `run` script to remove a lot of duplication by introducing helper functions

### Removed

- `terser-webpack-plugin` from `package.json` since it comes with Webpack 5 by default

## [0.2.0] - 2020-12-27

### Changed

- Use `REDIS_URL` to configure connections for Redis directly and Celery
- Add Redis `PING` check to the `/up` health check endpoint

### Removed

- Unnecessary `CELERY_TASK_LIST` comment in `hello/app.py`, this was a left over copy / paste mishap

## [0.1.0] - 2020-12-24

### Added

- Everything!

[Unreleased]: https://github.com/nickjj/docker-flask-example/compare/0.4.0...HEAD
[0.4.0]: https://github.com/nickjj/docker-flask-example/compare/0.3.0...0.4.0
[0.3.0]: https://github.com/nickjj/docker-flask-example/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/nickjj/docker-flask-example/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/nickjj/docker-flask-example/releases/tag/0.1.0
