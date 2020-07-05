from django.urls import path

from restaurant_management_django.products.views import (
    product_create_view,
    product_list_view,
    product_detail_view,
    product_update_view,
    product_delete_view
)

app_name = "products"

urlpatterns = [
    path("", view=product_list_view, name="list"),
    path("list/", view=product_list_view, name="list"),
    path("details/<int:pk>", view=product_detail_view, name="detail"),
    path("create/", view=product_create_view, name="create"),
    path("update/<int:pk>", view=product_update_view, name="update"),
    path("delete/<int:pk>", view=product_delete_view, name="delete"),
]
