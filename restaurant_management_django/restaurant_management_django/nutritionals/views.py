from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from restaurant_management_django.restaurant_management_django.nutritionals.models import NutritionalInformation


# Create your views here.


class NutritionalInformationDetailView(LoginRequiredMixin, DetailView):
    model = NutritionalInformation()
    slug_field = "username"
    slug_url_kwarg = "username"


nutritional_information_detail_view = NutritionalInformationDetailView.as_view()
