import django_filters

from restaurant_management_django.products.models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['name', 'status']
