from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView
from restaurant_management_django.products.models import Product

# Create your views here.
from restaurant_management_django.products.forms import ProductFilter


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'description', 'nutritional_values', 'status']
    success_url = reverse_lazy('products:list')


product_create_view = ProductCreateView.as_view()


class ProductListView(LoginRequiredMixin, FilterView):
    model = Product
    template_name = 'products/product_list.html'
    filterset_class = ProductFilter


product_list_view = ProductListView.as_view()


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


product_detail_view = ProductDetailView.as_view()


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'nutritional_values', 'status']
    success_url = reverse_lazy('products:list')

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


product_update_view = ProductUpdateView.as_view()


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('products:list')


product_delete_view = ProductDeleteView.as_view()
