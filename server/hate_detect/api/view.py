from os import truncate
from re import A
from flask import Blueprint, request
from hate_detect.shared.db import get_db
import datetime

from hate_detect.api.api_response import APIResponse, AddData, DetectSpeech

api = Blueprint("api", __name__)

@api.route("/hate/model/add", methods=["POST"])
def add_data_to_model():
    # TODO: Normalize text to ascii
    text = request.args.get("text")
    if not text:
        return APIResponse.error("Missing required paramater \"text\"", 400).make()

    db = get_db()
    # TODO: SQL INJECTION DANGER
    cursor = db.cursor()
    cursor.execute("INSERT INTO data (text, isHate, date) VALUES(?, ?, ?)", (text, True, datetime.datetime.now()))
    db.commit()
    
    return APIResponse.success(AddData(True)).make()

@api.route("hate/model/detect", methods=["GET", "POST"])
def detect_text():
    return APIResponse.success(DetectSpeech(True, 1.3)).make()
