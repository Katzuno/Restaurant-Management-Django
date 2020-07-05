import pytest
from django.http.response import Http404
from django.shortcuts import render
from django.test import RequestFactory
from django.urls import reverse, resolve

from restaurant_management_django.nutritionals.tests.factories import NutritionalFactory
from restaurant_management_django.nutritionals.views import (
    nutritional_information_create_view,
    nutritional_information_list_view,
    nutritional_information_detail_view,
    nutritional_information_update_view,
    nutritional_information_delete_view
)

from restaurant_management_django.users.tests.factories import UserFactory

pytestmark = pytest.mark.django_db


class TestNutritionalListView:
    """
    TODO:
        extracting view initialization code as class-scoped fixture
        would be great if only pytest-django supported non-function-scoped
        fixture db access -- this is a work-in-progress for now:
        https://github.com/pytest-dev/pytest-django/pull/258
    """

    def test_nutritional_list_view(self, rf: RequestFactory):
        nutritional_object = NutritionalFactory()
        url = reverse("nutritionals:list")
        request = rf.get(url)
        request.user = UserFactory()
        resp = nutritional_information_list_view(request)
        assert resp.status_code == 200
        assert nutritional_object.name in resp.rendered_content
