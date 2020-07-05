import pytest

from restaurant_management_django.nutritionals.models import NutritionalInformation

pytestmark = pytest.mark.django_db


def create_nutritional(name="test", unit="tg"):
    return NutritionalInformation.objects.create(name=name, unit=unit)


def test_nutritional_creation():
    w = create_nutritional()
    assert (isinstance(w, NutritionalInformation)) is True
