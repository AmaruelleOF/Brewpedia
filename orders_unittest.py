import unittest
from orders import *


class OrdersModuleTest(unittest.TestCase):
    # Проверка имени
    def test_valid_name(self):
        self.assertTrue(check_name("valid_username"))

    def test_invalid_name(self):
        self.assertFalse(check_name("invalid username"))

    # Проверка телефона
    def test_valid_phone(self):
        self.assertTrue(check_phone("123-456-7890"))

    def test_invalid_phone(self):
        self.assertFalse(check_phone("invalid phone"))

    # Проверка даты
    def test_past_date(self):
        past_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        self.assertFalse(check_date(past_date))

    def test_future_date(self):
        future_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        self.assertTrue(check_date(future_date))

    def test_today_date(self):
        today_date = datetime.now().strftime("%Y-%m-%d")
        self.assertTrue(check_date(today_date))


if __name__ == '__main__':
    unittest.main()
