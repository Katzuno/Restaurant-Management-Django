import pytest

from restaurant_management_django.products.models import Product

pytestmark = pytest.mark.django_db


def create_product(name="test", description="desc", nutritional_values='', status="ACTIVE"):
    return Product.objects.create(name=name, description=description, nutritional_values='', status=status)


def test_product_creation():
    w = create_product()
    assert (isinstance(w, Product)) is True
