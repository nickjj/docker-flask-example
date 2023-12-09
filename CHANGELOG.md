# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Changed

- Convert `SECRET_KEY` into a required env var
- Add `required: false` to `depends_on` in `docker-compose.yml` (requires Docker Compose v2.20.2+)
- Refactor `create_celery_app` function to be compatible with Python 3.12+

#### Languages and services

- Update `Python` to `3.12.1`
- Update `Node` to `20.6.1`
- Update `Postgres` to `16.1`
- Update `Redis` to `7.2.3`

#### Back-end dependencies

- Update `Flask-DB` to `0.4.0`
- Update `Flask-DebugToolbar` to `0.14.1`
- Update `Flask-SQLAlchemy` to `3.1.1`
- Update `Flask-Static-Digest` to `0.4.0` (now it optionally supports Brotli compression)
- Update `Flask` to `3.0.0`
- Update `SQLAlchemy` to `2.0.23`
- Update `alembic` to `1.13.0`
- Update `black` to `23.11.0`
- Update `celery` to `5.3.6`
- Update `flake8` to `6.1.0`
- Update `gunicorn` to `21.2.0`
- Update `psycopg` to `3.1.14`
- Update `pytest-cov` to `4.1.0`
- Update `pytest` to `7.4.3`
- Update `redis` to `5.0.1`
- Update `werkzeug` to `3.0.1`

#### Front-end dependencies

- Update `autoprefixer` to `10.4.16`
- Update `esbuild` to `0.19.8`
- Update `postcss` to `8.4.32`
- Update `tailwindcss` to `3.3.6`

## [0.11.0] - 2023-05-13

### Added

- Ability to customize `UID` and `GID` if you're not using `1000:1000` (check the `.env.example` file)
- Output `docker compose logs` in CI for easier debugging
- `isort` to auto-sort Python imports and a new `./run format:imports` command
- `./run quality` to run all lint and format commands in 1 command

### Changed

- Adjust `x-assets` to use a `stop_grace_period` of `0` for faster CTRL+c times in dev
- Reference `PORT` variable in the `docker-compose.yml` web service instead of hard coding `8000`
- Adjust Hadolint to exit > 0 if any style warnings are present
- Rename `esbuild.config.js` to `esbuild.config.mjs` and refactor config for esbuild 0.17+
- In `hello/up/views.py`, update raw SQL `SELECT 1` health check for SQLAlchemy 2.0
- Explicitly set `DEBUG` config option based off the `FLASK_DEBUG` env var so the intent is clear

#### Languages and services

- Update `Python` to `3.11.3`
- Update `Node` to `18.15.0`
- Update `Postgres` to `15.3`
- Update `Redis` to `7.0.11`

#### Back-end dependencies

- Replace `psycopg2` with `psycopg` (3.1.9)
- Update `Flask-SQLAlchemy` to `3.0.3`
- Update `Flask-Static-Digest` to `0.3.0`
- Update `Flask` to `2.3.2`
- Update `SQLAlchemy-Utils` to `0.41.1`
- Update `SQLAlchemy` to `2.0.13`
- Update `alembic` to `1.10.4`
- Update `black` to `23.3.0`
- Update `flake8` to `6.0.0`
- Update `isort` to `5.12.0`
- Update `psycopg2` to `2.9.6`
- Update `pytest-cov` to `4.0.0`
- Update `pytest` to `7.3.1`
- Update `redis` to `4.5.5`
- Update `werkzeug` to `2.3.4`

#### Front-end dependencies

- Update `autoprefixer` to `10.4.14`
- Update `esbuild` to `0.17.19`
- Update `postcss-import` to `15.1.0`
- Update `postcss` to `8.4.23`
- Update `tailwindcss` to `3.3.2`

### Removed

- `set -o nounset` from `run` script since it's incompatible with Bash 3.2 (default on macOS)

### Fixed

- Correctly append `_test` database name to database URI when using query strings
- Ensure Flake8, Black and isort all use 79 as the max line length

## [0.10.0] - 2022-09-08

### Added

- `set -o nounset` to `run` script to exit if there's any undefined variables

### Changed

- Replace `FLASK_ENV` with `FLASK_DEBUG` (`FLASK_ENV` will be deprecated in Flask 2.3)
- Switch Docker Compose `env_file` to `environment` for `postgres` to avoid needless recreates on `.env` changes
- Replace override file with Docker Compose profiles for running specific services
- Update Github Actions to use Ubuntu 22.04
- Enable BuildKit by default in the `.env.example` file

#### Languages and services

- Update `Python` to `3.10.5`
- Update `Node` to `16.15.1`
- Update `PostgreSQL` to `14.5`
- Update `Redis` to `7.0.4`

#### Back-end dependencies

- Update `Flask` to `2.2.2`
- Update `SQLAlchemy-Utils` to `0.38.3`
- Update `SQLAlchemy` to `1.4.40`
- Update `alembic` to `1.8.1`
- Update `black` to `22.6.0`
- Update `celery` to `5.2.7`
- Update `flake8` to `5.0.4`
- Update `jinja` to `2.1.2`
- Update `redis` to `4.3.4`
- Update `werkzeug` to `2.2.2`

#### Front-end dependencies

- Update `autoprefixer` to `10.4.8`
- Update `esbuild` to `0.15.2`
- Update `postcss` to `8.4.16`
- Update `tailwindcss` to `3.1.8`

### Removed

- Docker Compose `env_file` property for `redis` to avoid needless recreates on `.env` changes
- Drop support for Docker Compose v1 (mainly to use profiles in an optimal way, it's worth it!)

## [0.9.0] - 2022-05-15

### Added

- `yarn cache clean` after `yarn install` in `Dockerfile` (Hadolint warning)
- `--no-cache-dir` flag to `pip3 install` command in `bin/pip3-install` (Hadolint warning)
- [esbuild-copy-static-files](https://github.com/nickjj/esbuild-copy-static-files) plugin to drastically improve how static files are copied (check `assets/esbuild.config.js`)

### Changed

- Update Bash shebang to use `#!/usr/bin/env bash` in `pip3-install` and `docker-entrypoint-web`
- Refactor `/up/` endpoint into its own view and add `/up/databases` as a second URL

#### Languages and services

- Update `Python` to `3.10.4`
- Update `Node` to `16.14.2`
- Update `PostgreSQL` to `14.2`
- Update `Redis` to `7.0.0`

#### Back-end dependencies

- Update `Flask` to `2.1.2`
- Update `SQLAlchemy-Utils` to `0.38.2`
- Update `SQLAlchemy` to `1.4.36`
- Update `alembic` to `1.7.7`
- Update `black` to `22.3.0`
- Update `celery` to `5.2.6`
- Update `flask-debugtoolbar` to `0.13.1`
- Update `jinja2` to `3.1.1`
- Update `psycopg2` to `2.9.3`
- Update `pytest` to `7.1.2`
- Update `redis` to `4.3.1`
- Update `werkzeug` to `2.1.1`

#### Front-end dependencies

- Update `autoprefixer` to `10.4.7`
- Update `esbuild` to `0.14.39`
- Update `postcss-import` to `14.1.0`
- Update `postcss` to `8.4.13`
- Update `tailwindcss` to `3.0.24`

### Fixed

- `COPY --chown=node:node ../ ../` has been fixed to be `COPY --chown=node:node . ..`

## [0.8.0] - 2021-12-25

### Added

- Lint Dockerfile with <https://github.com/hadolint/hadolint>
- `/node_modules/.bin` to `$PATH` to easier access Yarn installed binaries
- `yarn:build:js` and `yarn:build:css` run script commands

### Changed

- Update `assets/tailwind.config.js` based on the new TailwindCSS v3 defaults
- Replace all traces of Webpack with esbuild
- Move JS and CSS from `assets/app` to `assets/js` and `assets/css`
- Rename `webpack` Docker build stage to `assets`
- Copy all files into the `assets` build stage to simplify things
- Replace `cp -a` with `cp -r` in Docker entrypoint to make it easier to delete older assets
- Rename `run hadolint` to `run lint:dockerfile`
- Rename `run flake8` to `run lint`
- Rename `run black` to `run format`
- Rename `run pytest` to `run test`
- Rename `run pytest-cov` to `run test:coverage`
- Rename `run bash` to `run shell`

#### Languages and services

- Update `Node` to `16.13.1`
- Update `PostgreSQL` to `14.1` and switch to Debian Bullseye Slim
- Update `Redis` to switch to Debian Bullseye Slim

#### Back-end packages

- Update `SQLAlchemy-Utils` to `0.38.1`
- Update `SQLAlchemy` to `1.4.29`
- Update `alembic` to `1.7.5`
- Update `celery` to `5.2.1`
- Update `flake8` to `4.0.1`
- Update `psycopg2` to `2.9.2`
- Update `py` to `1.11.0`
- Update `redis` to `4.0.2`
- Update `werkzeug` to `2.0.2`

#### Front-end packages

- Update `autoprefixer` to `10.4.0`
- Update `postcss` to `8.4.5`
- Update `tailwindcss` to `3.0.7`

### Removed

- Deleting old assets in the Docker entrypoint (it's best to handle this out of band in a cron job, etc.)

## [0.7.0] - 2021-10-10

### Changed

- Use f string for `db` variable in `config/settings.py`

#### Languages and services

- Update `Python` to `3.10.0` and switch to Debian Bullseye Slim
- Update `PostgreSQL` to `14.0`
- Update `Redis` to `6.2.6`

#### Back-end packages

- Update `Flask-DB` to `0.3.2`
- Update `Flask` to `2.0.2`
- Update `SQLAlchemy-Utils` to `0.37.8`
- Update `SQLAlchemy` to `1.4.25`
- Update `alembic` to `1.7.4`
- Update `celery` to `5.1.2`
- Update `psycopg2` to `2.9.1`
- Update `pytest-cov` to `3.0.0`
- Update `pytest` to `6.2.5`

#### Front-end packages

- Update `@babel/core` to `7.15.8`
- Update `@babel/preset-env` to `7.15.8`
- Update `@babel/register` to `7.15.3`
- Update `autoprefixer` to `10.3.7`
- Update `copy-webpack-plugin` to `9.0.1`
- Update `css-loader` to `6.4.0`
- Update `css-minimizer-webpack-plugin` to `3.1.1`
- Update `mini-css-extract-plugin` to `2.4.2`
- Update `postcss-loader` to `6.1.1`
- Update `postcss` to `8.3.9`
- Update `tailwindcss` to `2.2.16`
- Update `webpack-cli` to `4.9.0`
- Update `webpack` to `5.58.1`

## [0.6.0] - 2021-05-27

### Added

- `hello/initializers.py` now exists to define frequently used imports, variables, etc.

### Changed

- Use the Docker Compose spec in `docker-compose.yml` (removes `version:` property)
- Update Tailwind from `2.1.0` to `2.1.2`
- Update all Webpack related dependencies to their latest versions
- Update Flask from `1.1.2` to `2.0.1`
- Update Celery from `5.0.5` to `5.1.0`
- Update Alembic from `1.5.8` to `1.6.4`
- Update SQLAlchemy from `1.4.11` to `1.4.15`
- Update SQLAlchemy-Utils from `0.37.0` to `0.37.4`
- Update Redis from `6.0.10` to `6.2.3`
- Update pytest from `6.2.2` to `6.2.4`
- Update pytest-cov from `2.11.1` to `2.12.0`
- Use the new Flask 2.0 `.get` decorator

## [0.5.0] - 2021-04-24

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

- `hello/blueprints/` namespace has been removed
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

[Unreleased]: https://github.com/nickjj/docker-flask-example/compare/0.11.0...HEAD
[0.11.0]: https://github.com/nickjj/docker-flask-example/compare/0.10.0...0.11.0
[0.10.0]: https://github.com/nickjj/docker-flask-example/compare/0.9.0...0.10.0
[0.9.0]: https://github.com/nickjj/docker-flask-example/compare/0.8.0...0.9.0
[0.8.0]: https://github.com/nickjj/docker-flask-example/compare/0.7.0...0.8.0
[0.7.0]: https://github.com/nickjj/docker-flask-example/compare/0.6.0...0.7.0
[0.6.0]: https://github.com/nickjj/docker-flask-example/compare/0.5.0...0.6.0
[0.5.0]: https://github.com/nickjj/docker-flask-example/compare/0.4.0...0.5.0
[0.4.0]: https://github.com/nickjj/docker-flask-example/compare/0.3.0...0.4.0
[0.3.0]: https://github.com/nickjj/docker-flask-example/compare/0.2.0...0.3.0
[0.2.0]: https://github.com/nickjj/docker-flask-example/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/nickjj/docker-flask-example/releases/tag/0.1.0
