__author__ = 'radu.sover'
"""
This should not be a transactioned repo, but for the learning purposes...
"""

from sqlalchemy import select, bindparam
from flaskr.repository.db_meta import statistics

POST_ADDED_KEY = 'added'
POST_REMOVED_KEY = 'removed'

def increment_post(database):
    stm = statistics.update().where(statistics.c.name == POST_ADDED_KEY).\
    values(count=statistics.c.count+1)
    database.execute(stm)

def increment_delete(database):
    stm = statistics.update().where(statistics.c.name == POST_REMOVED_KEY).\
    values(count=statistics.c.count+1)
    database.execute(stm)
