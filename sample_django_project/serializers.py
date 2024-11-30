from rest_framework import serializers

from . import models


class SampleModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SampleModel
        fields = [
            "created",
            "first_name",
            "last_updated",
        ]
