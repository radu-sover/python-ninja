__author__ = 'radu.sover'

# from sqlalchemy import engine
from sqlalchemy import select, bindparam
from flaskr.repository import db_meta
from ..model.entry import Entry

# this will receive a database connection / database engine
# make a class __init__ with db parameter
# class EntriesRepository:
#     def __init__(self, db_engine):
#         self.db_engine = db_engine

def all_entries(database, mongo):
    con = database.connect()
    s = select([db_meta.entries])
    result = con.execute(s)
    entries = [Entry(
                row[db_meta.entries.c.id],
                row[db_meta.entries.c.title],
                row[db_meta.entries.c.text]) for row in result]

    result.close()

    entries = mongo.db.entries.find()

    return entries


def add_entry(database, mongo, title, text):
    con = database.connect()
    ins = db_meta.entries.insert().values(title=title, text=text)
    result = con.execute(ins)

    entries = mongo.db.entries
    entries.insert(Entry(result.lastrowid, title, text).__dict__)


def remove_entry(database, mongo, id, mongo_id):
    con = database.connect()
    s = db_meta.entries.delete().where(db_meta.entries.c.id == bindparam('id'))
    result = con.execute(s, id=id)
    # en = mongo.db.entries.find(mongo_id)
    # mongo.db.entries.remove(en)
