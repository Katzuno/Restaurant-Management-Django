import pytest
from django.http.response import Http404
from django.shortcuts import render
from django.test import RequestFactory
from django.urls import reverse, resolve

from restaurant_management_django.products.tests.factories import ProductFactory
from restaurant_management_django.products.views import (
    product_create_view,
    product_list_view,
    product_detail_view,
    product_update_view,
    product_delete_view
)

from restaurant_management_django.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestProductListView:
    """
    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

    def test_product_list_view(self, rf: RequestFactory):
        nutritional_object = ProductFactory()
        url = reverse("products:list")
        request = rf.get(url)
        request.user = UserFactory()
        resp = product_list_view(request)
        assert resp.status_code == 200
        assert nutritional_object.name in resp.rendered_content
