from rest_framework import viewsets, permissions

from . import serializers
from . import models


class ClientViewSet(viewsets.ModelViewSet):
    """ViewSet for the Client class"""

    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
