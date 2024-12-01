from rest_framework import viewsets, permissions

from . import serializers
from . import models


class PropertyViewSet(viewsets.ModelViewSet):
    """ViewSet for the Property class"""

    queryset = models.Property.objects.all()
    serializer_class = serializers.PropertySerializer
    permission_classes = [permissions.IsAuthenticated]
