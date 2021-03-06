__author__ = 'radu.sover'

# import logging
from flask import Flask
# from flask.ext.pymongo import PyMongo
# from flask_debugtoolbar import DebugToolbarExtension
from flaskr.repository import storage


# create the flaskr App
app = Flask(__name__)

app.config.from_object('config')
# mongo = PyMongo(app=app)

# toolbar = DebugToolbarExtension()
# toolbar.init_app(app)

storage.init_db(app.config)

# logging.basicConfig(filename='application.log', level=logging.INFO)
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
# logging.getLogger('sqlalchemy.pool').setLevel(logging.INFO)

import flaskr.handlers.global_h
import flaskr.account.account_view
import flaskr.entries.entries_view
