__author__ = 'radu.sover'


from contextlib import closing

from sqlalchemy import create_engine
from flaskr import app

def connect_db():
    return create_engine(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with open('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
