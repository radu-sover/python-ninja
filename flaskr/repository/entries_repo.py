__author__ = 'radu.sover'

# from sqlalchemy import engine
from sqlalchemy import select
from flaskr.repository import db_meta

def all_entries(database):
    s = select([db_meta.entries.c.title, db_meta.entries.c.text])
    con = database.connect()
    result = con.execute(s)
    entries = [dict(title=row[0], text=row[1]) for row in result]
    result.close()
    return entries


def add_entry(database, title, text):
    con = database.connect()
    ins = db_meta.entries.insert().values(title=title, text=text)
    result = con.execute(ins)
