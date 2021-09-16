import unittest
from models.category import Category
from models.transaction import Transaction
from models.merchant import Merchant

class TestProject(unittest.TestCase):
    def setUp(self):
        self.category = Category("Groceries")
        self.merchant = Merchant("Tesco", self.category)
        self.transaction = Transaction (4.50, '2021-09-14', self.merchant)

    def test_merchant(self):
        self.assertEqual('Tesco', self.merchant.name)