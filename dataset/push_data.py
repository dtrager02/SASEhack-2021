import sqlite3
from sqlite3.dbapi2 import Cursor

sheet = ""

db = sqlite3.connect("server/model.db")
cursor = db.cursor()
cursor.execute("DELETE FROM data")
db.commit()
