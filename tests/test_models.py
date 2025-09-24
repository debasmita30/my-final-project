# tests/test_models.py
import unittest
from myapp.models import Product  # Adjust import according to your project
from tests.factories import ProductFactory

class TestProductModel(unittest.TestCase):

    def setUp(self):
        # Create a fake product using the factory
        self.product = ProductFactory()

    def test_read_product(self):
        """
        Test reading a product from the database
        """
        # Simulate saving product (if using ORM)
        self.product.save()  

        # Read product by id
        product_from_db = Product.get_by_id(self.product.id)  # adjust method for your ORM

        # Assert the read product matches the saved one
        self.assertIsNotNone(product_from_db)
        self.assertEqual(product_from_db.name, self.product.name)
        self.assertEqual(product_from_db.category, self.product.category)
        self.assertEqual(product_from_db.price, self.product.price)
        self.assertEqual(product_from_db.availability, self.product.availability)

if __name__ == "__main__":
    unittest.main()
