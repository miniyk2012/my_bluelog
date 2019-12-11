from tests.base import BaseTestCase
from bluelog.settings import basedir


class SettingsTestCase(BaseTestCase):

    def test_basedir(self):
        self.assertEqual(basedir, '/Users/thomas_young/Documents/projects/my_bluelog')