from django.db import models
from django.urls import reverse


class Client(models.Model):
    full_name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    mobile = models.IntegerField()
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)



    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("SampleModel_SampleModel_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("SampleModel_SampleModel_update", args=(self.pk,))

