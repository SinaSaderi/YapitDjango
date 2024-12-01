from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class ClientListView(generic.ListView):
    model = models.Client
    form_class = forms.ClientForm


class ClientCreateView(generic.CreateView):
    model = models.Client
    form_class = forms.ClientForm


class ClientDetailView(generic.DetailView):
    model = models.Client
    form_class = forms.ClientForm


class ClientUpdateView(generic.UpdateView):
    model = models.Client
    form_class = forms.ClientForm
    pk_url_kwarg = "pk"


class ClientDeleteView(generic.DeleteView):
    model = models.Client
    success_url = reverse_lazy("Client_Client_list")
