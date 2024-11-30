from rest_framework import viewsets, permissions

from . import serializers
from . import models


class SampleModelViewSet(viewsets.ModelViewSet):
    """ViewSet for the SampleModel class"""

    queryset = models.SampleModel.objects.all()
    serializer_class = serializers.SampleModelSerializer
    permission_classes = [permissions.IsAuthenticated]
