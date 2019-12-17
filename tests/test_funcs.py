import datetime
import unittest

from faker import Faker


class FuncTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fake = Faker()

    def test_timestamp(self):
        assert isinstance(self.fake.date_time_this_year(), datetime.datetime)
