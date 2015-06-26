__author__ = 'radu.sover'

from flask import request, session, g, redirect, url_for
from flask import abort, render_template, flash

from flaskr import app
import flaskr.common.logging as logging


@app.route('/login', methods=['GET', 'POST'])
def login():
    logging.get_logger(__name__).info(msg='Just an informative log')
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You are logged out')
    return redirect(url_for('show_entries'))
