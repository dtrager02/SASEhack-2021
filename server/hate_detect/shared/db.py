import sqlite3
from flask import g
from flask import current_app

DATABASE = "./model.db"

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.execute(r"CREATE TABLE IF NOT EXIST data (text TEXT, isHate INTEGER)")
        db.commit()
    return db

@current_app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
