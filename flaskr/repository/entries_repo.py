__author__ = 'radu.sover'

# from sqlalchemy import engine
from sqlalchemy import select
from flaskr.repository import db_meta

# this will receive a database connection / database engine
# make a class __init__ with db parameter
# class EntriesRepository:
#     def __init__(self, db_engine):
#         self.db_engine = db_engine

def all_entries(database):
    con = database.connect()
    s = select([db_meta.entries.c.title, db_meta.entries.c.text])
    result = con.execute(s)
    entries = [dict(title=row[0], text=row[1]) for row in result]
    result.close()
    return entries


def add_entry(database, title, text):
    con = database.connect()
    ins = db_meta.entries.insert().values(title=title, text=text)
    result = con.execute(ins)
