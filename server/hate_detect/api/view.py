from os import truncate
from re import A
import NLP
from flask import Blueprint, request
from hate_detect.shared.db import get_db
from hate_detect.site.scraper import scrape
from hate_detect.api.api_response import APIResponse, AddData, DetectSpeech, ScrapedData

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
    cursor.execute(f"INSERT INTO data (text, isHate) VALUES(\"{text}\" ,true)")
    db.commit()
    
    return APIResponse.success(AddData(True)).make()

@api.route("hate/model/detect", methods=["GET", "POST"])
def detect_text():

    return APIResponse.success(DetectSpeech(True, 1.3)).make()

@api.route('/content/update')
def fourChan():
    texts = [i["message"] for i in scrape()["posts"]]
    predictions = NLP.predict(texts)
    #predictions format:
    #table:[texts array,predictions array)]
    return APIResponse.success(ScrapedData(True,predictions))