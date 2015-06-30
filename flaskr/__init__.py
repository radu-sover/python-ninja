__author__ = 'radu.sover'

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


# create the flaskr App
app = Flask(__name__)
app.config.from_object('config')

toolbar = DebugToolbarExtension()

toolbar.init_app(app)

import flaskr.handlers.global_h

import flaskr.account.account_view
import flaskr.entries.entries_view
