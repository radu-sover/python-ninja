__author__ = 'radu.sover'

from flask import request, session, g, redirect, url_for
from flask import abort, render_template, flash

from flaskr import app, mongo
from flaskr.repository import entries_repo
from flaskr.repository import statistics_repo as s_repo

# this will have a dependency on the repo

@app.route('/')
def show_entries():
    entries = entries_repo.all_entries(g.db, mongo)
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)

    with g.db.begin() as connection:
        entries_repo.add_entry(connection, mongo, request.form['title'], request.form['text'])
        s_repo.increment_post(connection)

    flash('New entry added successfully')
    return redirect(url_for('show_entries'))


@app.route('/delete', methods=['POST'])
def remove_entry():
    if not session.get('logged_in'):
        abort(401)

    to_remove = request.form['id']
    mongo_id = request.form['_id']
    with g.db.begin() as connection:
        entries_repo.remove_entry(connection, mongo, to_remove, mongo_id)
        s_repo.increment_delete(connection)

    flash('Entry deleted')
    return redirect(url_for('show_entries'))
