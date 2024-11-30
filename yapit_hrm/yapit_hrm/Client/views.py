from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class SampleModelListView(generic.ListView):
    model = models.SampleModel
    form_class = forms.SampleModelForm


class SampleModelCreateView(generic.CreateView):
    model = models.SampleModel
    form_class = forms.SampleModelForm


class SampleModelDetailView(generic.DetailView):
    model = models.SampleModel
    form_class = forms.SampleModelForm


class SampleModelUpdateView(generic.UpdateView):
    model = models.SampleModel
    form_class = forms.SampleModelForm
    pk_url_kwarg = "pk"


class SampleModelDeleteView(generic.DeleteView):
    model = models.SampleModel
    success_url = reverse_lazy("SampleModel_SampleModel_list")
