from flask import url_for

from lib.test import ViewTestMixin


class TestHealthz(ViewTestMixin):
    def test_healthz(self):
        response = self.client.get(url_for("health.healthz"))

        assert response.status_code == 200
        assert response.get_json() == {"status": "ok"}
