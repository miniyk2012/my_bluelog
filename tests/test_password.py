import logging
import unittest

from my_bluelog import Admin
from tests import base


class BlogTestCase(base.BaseTestCase):
    def setUp(self):
        super(BlogTestCase, self).setUp()

    def test_password(self):
        user = Admin(name='Grey Li', username='grey', about='I am test', blog_title='Testlog', blog_sub_title='a test')
        user.set_password('123')
        hash1 = user.password_hash
        self.assertTrue(user.validate_password('123'))
        self.assertFalse(user.validate_password('126'))

        user.set_password('123')
        self.assertFalse(user.validate_password('126'))

        # 因为随机盐的存在, 即使密码相同, 密码散列值也不同
        hash2 = user.password_hash
        self.assertNotEqual(hash1, hash2)
