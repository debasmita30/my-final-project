# tests/factories.py
import factory
from faker import Faker
from myapp.models import Product  # adjust import according to your project

fake = Faker()

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.LazyAttribute(lambda x: fake.word())
    category = factory.LazyAttribute(lambda x: fake.random_element(["Electronics", "Clothing", "Books"]))
    price = factory.LazyAttribute(lambda x: round(fake.random_number(digits=4), 2))
    availability = factory.LazyAttribute(lambda x: fake.boolean())
