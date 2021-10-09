from flask import Blueprint

api = Blueprint("api", __name__)

@api.route("/hate/model/add", methods=["POST"])
def add_data_to_model():
    return "hello model add"

@api.route("hate/model/detect", methods=["GET", "POST"])
def detect_text():
    return "hello model detect"
