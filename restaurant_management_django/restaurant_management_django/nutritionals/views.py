from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from restaurant_management_django.nutritionals.models import NutritionalInformation


# Create your views here.


class NutritionalInformationCreateView(LoginRequiredMixin, CreateView):
    model = NutritionalInformation
    fields = ['name', 'unit']
    success_url = reverse_lazy('nutritionals:list')


nutritional_information_create_view = NutritionalInformationCreateView.as_view()


class NutritionalInformationListView(LoginRequiredMixin, ListView):
    model = NutritionalInformation


nutritional_information_list_view = NutritionalInformationListView.as_view()


class NutritionalInformationDetailView(LoginRequiredMixin, DetailView):
    model = NutritionalInformation


nutritional_information_detail_view = NutritionalInformationDetailView.as_view()


class NutritionalInformationUpdateView(LoginRequiredMixin, UpdateView):
    model = NutritionalInformation
    fields = ["name", "unit"]
    success_url = reverse_lazy('nutritionals:list')

    def form_valid(self, form):
        messages.add_message(
            self.request, messages.INFO, _("Infos successfully updated")
        )
        return super().form_valid(form)


nutritional_information_update_view = NutritionalInformationUpdateView.as_view()


class NutritionalInformationDeleteView(LoginRequiredMixin, DeleteView):
    model = NutritionalInformation
    success_url = reverse_lazy('nutritionals:list')


nutritional_information_delete_view = NutritionalInformationDeleteView.as_view()
