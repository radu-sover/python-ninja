__author__ = 'radu.sover'


from sqlalchemy import create_engine
from flaskr.repository.db_meta import metadata


def connect_db(config):
    return create_engine(config['DATABASE'])


def init_db(config):
    engine = create_engine(config['DATABASE'])
    metadata.create_all(engine)
    # with closing(connect_db()) as db:
    #     with open('schema.sql', mode='r') as f:
    #         db.cursor().executescript(f.read())
    #     db.commit()
