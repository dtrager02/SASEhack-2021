from flask import Blueprint, render_template, request, redirect
from flask.app import Flask
from hate_detect.shared.db import get_db
from hate_detect.site.scraper import scrape


site = Blueprint("site", __name__, template_folder="template",
                 static_folder="static",static_url_path="/site/static")

@site.route("/")
def index():
    return str(get_db().cursor().execute("SELECT text, isHate FROM data ORDER BY date DESC LIMIT 5000").fetchall())
