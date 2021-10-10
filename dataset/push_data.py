import sqlite3
from sqlite3.dbapi2 import Cursor
import datetime

sheet = "dataset\\out.csv"

db = sqlite3.connect("server/model.db")
cursor = db.cursor()
cursor.execute("DELETE FROM data")
db.commit()

# with open(sheet, "r") as f:
#     f.readline()
#     for line in f:
#         ln = line.split(",")
#         isHate = bool(int(ln[-1]))
#         text = ",".join(ln[:-1])
#         cursor.execute("INSERT INTO data (text, isHate, date) VALUES(?, ?, ?)", (text, isHate, datetime.datetime.now()))
#     db.commit()