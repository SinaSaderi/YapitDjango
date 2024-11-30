from django.contrib import admin
from django import forms

from . import models


class SampleModelAdminForm(forms.ModelForm):

    class Meta:
        model = models.SampleModel
        fields = "__all__"


class SampleModelAdmin(admin.ModelAdmin):
    form = SampleModelAdminForm
    list_display = [
        "created",
        "first_name",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "first_name",
        "last_updated",
    ]


admin.site.register(models.SampleModel, SampleModelAdmin)
