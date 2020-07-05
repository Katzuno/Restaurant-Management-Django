from typing import Any, Sequence

from django.contrib.auth import get_user_model
from factory import DjangoModelFactory, Faker, post_generation

from restaurant_management_django.nutritionals.models import NutritionalInformation


class NutritionalFactory(DjangoModelFactory):
    name = Faker("word")
    unit = Faker("word")

    class Meta:
        model = NutritionalInformation
        django_get_or_create = ["name"]
