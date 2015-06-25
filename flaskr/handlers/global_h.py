__author__ = 'radu.sover'

from flask import g

from flaskr import app
from flaskr.repository.storage import connect_db


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db')
    if db is not None:
        db.dispose()
