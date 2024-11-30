from django import forms
from . import models


class SampleModelForm(forms.ModelForm):
    class Meta:
        model = models.SampleModel
        fields = [
            "first_name",
        ]
