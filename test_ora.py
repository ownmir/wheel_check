import unittest
from utilities.oratrunc import oracle_trunc, oracle_addition, ModeError
import datetime


class TestTruncAddition(unittest.TestCase):

    def setUp(self):
        """There is form tuple with now and 13 date in future"""
        self.now = datetime.datetime.now()
        self.dates = tuple(self.now + datetime.timedelta(i) for i in (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))

    def test_monday(self):
        """oracle_trunc must return monday"""
        for oracle_date in self.dates:
            with self.subTest(oracle_date=oracle_date):
                self.assertEqual(oracle_trunc(oracle_date, 'DAY').isoweekday(), 1)

    def test_sunday(self):
        """oracle_addition must return sunday"""
        for oracle_date in self.dates:
            with self.subTest(oracle_date=oracle_date):
                self.assertEqual(oracle_addition(oracle_date, 'DAY').isoweekday(), 7)

    def test_exception(self):
        with self.assertRaises(ModeError):
            oracle_trunc(self.now, 'not')
        with self.assertRaises(ModeError):
            oracle_addition(self.now, 'no2')



if __name__ == '__main__':
    unittest.main()
