import unittest
import re

from myform import is_valid_phone_number


class TestCheckPhoneNumber(unittest.TestCase):
    def test_invalid_phone_numbers(self):
        list_phone_uncor = ["12345",
            "1234567890123456",
            "12345abcde",
            "1-800",
            "+",
            "() 123 456-7890",
            "123-45-6789",
            "800.1234.5678",
            "123.4567.890",
            "1 800 123",
            "800.123.4567x",
            "1-800-123-4567-",
            "1--800-123-4567",
            "(123) 456 7890 ext. 123"]
        for phone_number in list_phone_uncor:
            print(f"Testing invalid phone number: {phone_number}")
            self.assertFalse(is_valid_phone_number(phone_number), f"Expected {phone_number} to be valid")

    def test_valid_phone_numbers(self):
        list_phone_cor = [
            "1234567890",
            "+1 (800) 123-4567",
            "(123) 456-7890",
            "123 456 7890",
            "123-456-7890",
            "800-123-4567"]
        for phone_number in list_phone_cor:
            print(f"Testing invalid phone number: {phone_number}")
            self.assertTrue(is_valid_phone_number(phone_number), f"Expected {phone_number} to be invalid")


if __name__ == '__main__':
    unittest.main()
