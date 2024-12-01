from django.contrib import admin
from django import forms

from . import models


class ClientAdminForm(forms.ModelForm):

    class Meta:
        model = models.Client
        fields = "__all__"


class ClientAdmin(admin.ModelAdmin):
    form = ClientAdminForm
    list_display = ["full_name", "group", "mobile", "email", "address"]
    readonly_fields = []


admin.site.register(models.Client, ClientAdmin)
