from django.urls import path

from restaurant_management_django.nutritionals.views import (
    nutritional_information_create_view,
    nutritional_information_list_view,
    nutritional_information_detail_view,
    nutritional_information_update_view,
    nutritional_information_delete_view
)

app_name = "nutritionals"

urlpatterns = [
    path("", view=nutritional_information_list_view, name="list"),
    path("list/", view=nutritional_information_list_view, name="list"),
    path("details/<int:pk>", view=nutritional_information_detail_view, name="detail"),
    path("create/", view=nutritional_information_create_view, name="create"),
    path("update/<int:pk>", view=nutritional_information_update_view, name="update"),
    path("delete/<int:pk>", view=nutritional_information_delete_view, name="delete"),
]
