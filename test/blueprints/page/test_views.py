from flask import url_for

from lib.test import ViewTestMixin


class TestPage(ViewTestMixin):
    def test_home_page(self):
        """ Home page should respond with a success 200. """
        response = self.client.get(url_for("page.home"))

        assert response.status_code == 200

    def test_up_page(self):
        """ Up page should respond with a success 200. """
        response = self.client.get(url_for("page.up"))

        assert response.status_code == 200
