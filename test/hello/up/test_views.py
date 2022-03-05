from flask import url_for

from lib.test import ViewTestMixin


class TestUp(ViewTestMixin):
    def test_up(self):
        """Up should respond with a success 200."""
        response = self.client.get(url_for("up.index"))

        assert response.status_code == 200

    def test_up_databases(self):
        """Up databases should respond with a success 200."""
        response = self.client.get(url_for("up.databases"))

        assert response.status_code == 200
