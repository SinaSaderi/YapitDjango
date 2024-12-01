from django import forms
from . import models


class PropertyForm(forms.ModelForm):
    class Meta:
        model = models.Property
        fields = ["type", "address"]
