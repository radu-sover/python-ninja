__author__ = 'radu.sover'


def all_entries(database):
    cur = database.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return entries


def add_entry(database, title, text):
    database.execute('insert into entries (title, text) values (?, ?)', (title, text))
    database.commit()
