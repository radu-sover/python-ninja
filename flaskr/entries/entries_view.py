__author__ = 'radu.sover'

from flask import request, session, g, redirect, url_for
from flask import abort, render_template, flash

from flaskr import app
from flaskr.repository import entries_repo


@app.route('/')
def show_entries():
    entries = entries_repo.all_entries(g.db)
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)

    entries_repo.add_entry(g.db, request.form['title'], request.form['text'])

    flash('New entry added successfully')
    return redirect(url_for('show_entries'))
