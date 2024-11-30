from django.contrib import admin
from django import forms

from . import models


class PropertyAdminForm(forms.ModelForm):

    class Meta:
        model = models.Property
        fields = "__all__"


class PropertyAdmin(admin.ModelAdmin):
    form = PropertyAdminForm
    list_display = ["type", "address"]
    readonly_fields = []


admin.site.register(models.Property, PropertyAdmin)
