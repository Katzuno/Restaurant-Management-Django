from typing import Any, Sequence

from django.contrib.auth import get_user_model
from factory import DjangoModelFactory, Faker, post_generation

from restaurant_management_django.products.models import Product


class ProductFactory(DjangoModelFactory):
    name = Faker("name")
    description = Faker("text")
    # Add constraints
    nutritional_values = {
        "Weight (g)": "125.0"
    }
    status = "ACTIVE"

    class Meta:
        model = Product
        django_get_or_create = ["name"]
