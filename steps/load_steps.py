# features/steps/load_steps.py
from behave import given
from tests.factories import ProductFactory
from myapp.models import Product  # adjust import for your ORM

@given('the following products exist')
def step_impl(context):
    """
    Load background products into the database before running scenarios
    """
    for row in context.table:
        product = Product(
            name=row['name'],
            category=row['category'],
            price=float(row['price']),
            availability=row['availability'].lower() == 'true'
        )
        product.save()
