__author__ = 'radu.sover'

from flask import request, session, g, redirect, url_for
from flask import abort, render_template, flash

from flaskr import app, mongo
from flaskr.repository import entries_repo

# this will have a dependency on the repo

@app.route('/')
def show_entries():
    entries = entries_repo.all_entries(g.db, mongo)
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)

    entries_repo.add_entry(g.db, mongo, request.form['title'], request.form['text'])

    flash('New entry added successfully')
    return redirect(url_for('show_entries'))

@app.route('/delete', methods=['POST'])
def remove_entry():
    if not session.get('logged_in'):
        abort(401)

    to_remove = request.form['id']
    mongo_id = request.form['_id']
    entries_repo.remove_entry(g.db, mongo, to_remove, mongo_id)

    flash('Entry deleted')
    return redirect(url_for('show_entries'))
