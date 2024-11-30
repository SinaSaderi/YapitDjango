from django.db import models
from django.urls import reverse


class Property(models.Model):
    type = models.CharField(max_length=255)
    address = models.CharField(max_length=255)



    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("Property_Property_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Property_Property_update", args=(self.pk,))

