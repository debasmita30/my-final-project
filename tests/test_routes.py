# tests/test_routes.py
import unittest
from myapp import app
from tests.factories import ProductFactory

class TestProductRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()
        self.product = ProductFactory()
        self.product.save()

    def test_read_product_route(self):
        response = self.client.get(f'/products/{self.product.id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['id'], self.product.id)

    def test_update_product_route(self):
        update_data = {"name": "Updated Product", "price": 1500}
        response = self.client.put(f'/products/{self.product.id}', json=update_data)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], "Updated Product")
        self.assertEqual(data['price'], 1500)

    def test_delete_product_route(self):
        response = self.client.delete(f'/products/{self.product.id}')
        self.assertEqual(response.status_code, 204)

    def test_list_all_products_route(self):
        response = self.client.get('/products')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIsInstance(data, list)

    def test_list_by_name_route(self):
        response = self.client.get(f'/products?name={self.product.name}')
        self.assertEqual(response.status_code, 200)

    def test_list_by_category_route(self):
        response = self.client.get(f'/products?category={self.product.category}')
        self.assertEqual(response.status_code, 200)

    def test_list_by_availability_route(self):
        response = self.client.get(f'/products?availability={self.product.availability}')
        self.assertEqual(response.status_code, 200)
