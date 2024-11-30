from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class PropertyListView(generic.ListView):
    model = models.Property
    form_class = forms.PropertyForm


class PropertyCreateView(generic.CreateView):
    model = models.Property
    form_class = forms.PropertyForm


class PropertyDetailView(generic.DetailView):
    model = models.Property
    form_class = forms.PropertyForm


class PropertyUpdateView(generic.UpdateView):
    model = models.Property
    form_class = forms.PropertyForm
    pk_url_kwarg = "pk"


class PropertyDeleteView(generic.DeleteView):
    model = models.Property
    success_url = reverse_lazy("Property_Property_list")
