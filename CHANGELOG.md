# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a
Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Changed

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

[Unreleased]: https://github.com/nickjj/docker-flask-example/compare/0.2.0...HEAD
[0.2.0]: https://github.com/nickjj/docker-flask-example/compare/0.1.0...0.2.0
[0.1.0]: https://github.com/nickjj/docker-flask-example/releases/tag/0.1.0
