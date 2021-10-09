from flask import Flask
from hate_detect.api.view import api
from hate_detect.site.view import site

app = Flask(__name__)

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(site)
