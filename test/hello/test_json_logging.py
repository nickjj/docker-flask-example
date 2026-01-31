import json
import logging
import uuid

from hello.app import create_app


def test_json_logs_enabled(monkeypatch, caplog):
    monkeypatch.setenv("SECRET_KEY", "test")

    app = create_app(
        settings_override={
            "TESTING": True,
            "JSON_LOGS": True,
            "SQLALCHEMY_DATABASE_URI": "sqlite://",
        }
    )

    with app.test_client() as client:
        with caplog.at_level(logging.INFO, logger="hello.request"):
            response = client.get("/healthz")

    assert response.status_code == 200

    messages = [record.message for record in caplog.records]
    assert messages

    payload = json.loads(messages[0])
    assert payload["method"] == "GET"
    assert payload["path"] == "/healthz"
    assert payload["status_code"] == 200
    uuid.UUID(payload["request_id"])
