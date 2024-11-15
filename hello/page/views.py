import os
from importlib.metadata import version

from flask import Blueprint
from flask import render_template

from config.settings import DEBUG

page = Blueprint("page", __name__, template_folder="templates")


@page.get("/")
def home():
    return render_template(
        "page/home.html",
        flask_ver=version("flask"),
        python_ver=os.environ["PYTHON_VERSION"],
        debug=DEBUG,
    )
