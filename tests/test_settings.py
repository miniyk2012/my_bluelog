from tests.base import BaseTestCase
from bluelog.settings import basedir, DevelopmentConfig


class SettingsTestCase(BaseTestCase):

    def test_basedir(self):
        self.assertEqual(basedir, '/Users/thomas_young/Documents/projects/my_bluelog')
        self.assertEqual(DevelopmentConfig.SQLALCHEMY_DATABASE_URI,
                         'sqlite://///Users/thomas_young/Documents/projects/my_bluelog/data-dev.db')
