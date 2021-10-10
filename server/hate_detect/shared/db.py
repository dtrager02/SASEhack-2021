import sqlite3
from flask import g
from flask import current_app

DATABASE = "./model.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # db.cursor().execute(r"CREATE TABLE data (text TEXT, isHate INTEGER)")
        db.commit()
    return db
