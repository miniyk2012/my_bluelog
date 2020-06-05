import unittest
from my_bluelog import create_app
from my_bluelog.extensions import db
from my_bluelog.models import Admin


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        app = create_app('testing')
        self.context = app.test_request_context()
        self.context.push()
        self.client = app.test_client()
        self.runner = app.test_cli_runner()

        db.create_all()
        user = Admin(name='Grey Li', username='grey', about='I am test', blog_title='Testlog', blog_sub_title='a test')
        user.set_password('123')
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        self.context.pop()
