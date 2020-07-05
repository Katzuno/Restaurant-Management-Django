import pytest
from django.urls import resolve, reverse

from restaurant_management_django.products.tests.factories import ProductFactory

pytestmark = pytest.mark.django_db


def test_detail():
    product = ProductFactory()
    assert (
        reverse("products:detail", kwargs={"pk": product.id})
        == f"/products/details/{product.id}"
    )
    assert resolve(f"/products/details/{product.id}").view_name == "products:detail"


def test_update():
    product = ProductFactory()
    assert reverse("products:update", kwargs={"pk": product.id}) == f"/products/update/{product.id}"
    assert resolve(f"/products/update/{product.id}").view_name == "products:update"


def test_list():
    assert reverse("products:list") == f"/products/list/"
    assert resolve(f"/products/list/").view_name == "products:list"


def test_create():
    assert reverse("products:create") == f"/products/create/"
    assert resolve(f"/products/create/").view_name == "products:create"


def test_delete():
    product = ProductFactory()
    assert reverse("products:delete", kwargs={"pk": product.id}) == f"/products/delete/{product.id}"
    assert resolve(f"/products/delete/{product.id}").view_name == "products:delete"
