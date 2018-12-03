"""Tests for the separation module"""
import unittest
from separation.separation import separate

class SeparateTest(unittest.TestCase):
    """Test the separate function"""

    def test_divisible_number(self):
        """divisible_number_test"""
        input_data = 123712378
        self.assertEqual(separate(input_data), '123,712,378')

    def test_non_divisible_number(self):
        """non_divisible_number_test"""
        input_data = 9328479
        self.assertEqual(separate(input_data), '9,328,479')

    def test_step(self):
        """step_test"""
        input_data = 'Hola mundo'
        self.assertEqual(separate(input_data), 'H,ola, mu,ndo')

    def test_separator(self):
        """separator_test"""
        input_data = 1234567
        self.assertEqual(separate(input_data, 5), '12,34567')

    def test_string(self):
        """string_test"""
        input_data = 1234567
        self.assertEqual(separate(input_data, separator=':'), '1:234:567')


if __name__ == '__main__':
    unittest.main()
