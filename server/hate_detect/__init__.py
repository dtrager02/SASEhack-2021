from flask import Flask
from flask_cors import CORS
from hate_detect.api.view import api
from hate_detect.site.view import site

app = Flask(__name__)

app.register_blueprint(api, url_prefix="/api")
app.register_blueprint(site)

CORS(app)

cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})
