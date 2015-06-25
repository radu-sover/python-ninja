__author__ = 'radu.sover'

from flask import Flask

# configuration
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'dev'
USERNAME = 'admin'
PASSWORD = 'default'


# create the flaskr App
app = Flask(__name__)
app.config.from_object(__name__)

import flaskr.handlers.global_h

import flaskr.account.account_view
import flaskr.entries.entries_view
