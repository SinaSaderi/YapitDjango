from django import forms
from . import models


class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ["full_name", "group", "mobile", "email", "address"]
