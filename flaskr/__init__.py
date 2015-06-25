__author__ = 'radu.sover'

from flask import Flask

# configuration
DATABASE = 'sqlite:///flaskr.db'
DEBUG = True
SECRET_KEY = 'dev'
USERNAME = 'admin'
PASSWORD = 'default'
APPLICATION_NAME = 'flaskr_01'


# create the flaskr App
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('APPLICATION_NAME')

import flaskr.handlers.global_h

import flaskr.account.account_view
import flaskr.entries.entries_view
