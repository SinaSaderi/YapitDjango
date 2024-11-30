from rest_framework import serializers

from . import models


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Client
        fields = ["full_name", "group", "mobile", "email", "address"]
