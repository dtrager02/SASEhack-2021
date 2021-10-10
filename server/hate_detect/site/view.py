from flask import Blueprint, render_template, request, redirect
from flask.app import Flask
from hate_detect.site.scraper import scrape


site = Blueprint("site", __name__, template_folder="template",
                 static_folder="static",static_url_path="/site/static")

@site.route("/")
def index():
    return render_template("index.html")



