__author__ = 'radu.sover'
import os
import unittest
import tempfile

import flaskr
from flaskr.repository import storage

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        storage.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])
        pass

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username = username,
            password = password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_empty_db(self):
        rv = self.app.get('/')
        assert 'Unbelievable. No entries here so far' in str(rv.data)

    def test_login_logout(self):
        rv = self.login('admin', 'default')
        assert 'You are logged in' in str(rv.data)
        rv = self.logout()
        assert 'You are logged out' in str(rv.data)
        rv = self.login('adminx', 'default')
        assert 'Invalid username' in str(rv.data)
        rv = self.login('admin', 'defaultx')
        assert 'Invalid password' in str(rv.data)

    def test_messages(self):
        self.login('admin', 'default')
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)

        rv = str(rv.data)
        assert 'No entries here so far' not in rv
        assert '&lt;Hello&gt;' in rv
        assert '<strong>HTML</strong> allowed here' in rv

if __name__ == '__main__':
    unittest.main()
