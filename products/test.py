"""
    Tests for the products module, the functions that only wrap pandas operations are not tested because I trust pandas
"""
import unittest
import pandas

from products.products import get_most_expensive, get_cheaper, get_most_discounted, count_by_regex

class ProductsTest(unittest.TestCase):
    """Test the products module functions"""

    def setUp(self):
        """Read the mock products"""
        self.data = pandas.read_csv('products/products_mock.csv')

    def test_most_discounted(self):
        self.assertEqual(3, get_most_discounted(self.data).iloc[0][0])
        self.assertEqual(5, get_most_discounted(self.data).iloc[-1][0])

    def test_count_by_regex(self):
        self.assertEqual(3, count_by_regex(self.data, r"\bred"))
