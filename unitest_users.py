import unittest
from users import *


class MyModuleTests(unittest.TestCase):

    def test_name_valid(self):
        self.assertTrue(name("john_doe123"))

    def test_name_invalid(self):
        self.assertFalse(name("john_doe!@#"))

    def test_name_empty(self):
        self.assertFalse(name(""))

    def test_name_whitespace(self):
        self.assertFalse(name("john doe"))

    def test_date_past(self):
        past_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        self.assertTrue(date(past_date))

    def test_date_future(self):
        future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        self.assertFalse(date(future_date))

    def test_date_invalid_format(self):
        invalid_date = "2023/06/06"
        with self.assertRaises(ValueError):
            date(invalid_date)


if __name__ == '__main__':
    unittest.main()
