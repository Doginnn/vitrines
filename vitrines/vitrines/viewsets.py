from rest_framework import viewsets
from . import models
from . import serializers


class HoteisViewSet(viewsets.ModelViewSet):
    queryset = models.Hotel.objects.all()
    serializers_class = serializers.HoteisSerializer
