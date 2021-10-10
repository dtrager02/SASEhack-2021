import sqlite3
from flask import g
from flask import current_app
import hate_detect.api.NLP as NLP
DATABASE = "./model.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.cursor().execute(r"CREATE TABLE IF NOT EXISTS data (text TEXT, isHate INTEGER, date DATA)")
        db.commit()
    return db



def get_model(retrain = False):
    model = getattr(g, '_model', None)
    if model is None or retrain:
        MODEL = NLP.train_model(get_db())
        model = g._model = MODEL
        print("trained model")
    return model

def update_added_count():
    db = get_db()
    count = getattr(g,"_count",0)
    g._count += 1
    if(count%10):
        get_model(retrain = True)
    

    
