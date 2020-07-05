import pytest
from django.urls import resolve, reverse

from restaurant_management_django.nutritionals.tests.factories import NutritionalFactory

pytestmark = pytest.mark.django_db


def test_detail():
    nutritional = NutritionalFactory()
    assert (
        reverse("nutritionals:detail", kwargs={"pk": nutritional.id})
        == f"/nutritionals/details/{nutritional.id}"
    )
    assert resolve(f"/nutritionals/details/{nutritional.id}").view_name == "nutritionals:detail"


def test_update():
    nutritional = NutritionalFactory()
    assert reverse("nutritionals:update", kwargs={"pk": nutritional.id}) == f"/nutritionals/update/{nutritional.id}"
    assert resolve(f"/nutritionals/update/{nutritional.id}").view_name == "nutritionals:update"


def test_list():
    assert reverse("nutritionals:list") == f"/nutritionals/list/"
    assert resolve(f"/nutritionals/list/").view_name == "nutritionals:list"


def test_create():
    assert reverse("nutritionals:create") == f"/nutritionals/create/"
    assert resolve(f"/nutritionals/create/").view_name == "nutritionals:create"


def test_delete():
    nutritional = NutritionalFactory()
    assert reverse("nutritionals:delete", kwargs={"pk": nutritional.id}) == f"/nutritionals/delete/{nutritional.id}"
    assert resolve(f"/nutritionals/delete/{nutritional.id}").view_name == "nutritionals:delete"
