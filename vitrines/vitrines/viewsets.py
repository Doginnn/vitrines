from rest_framework import viewsets
from vitrines.vitrines.models import Title, Hotel
from vitrines.vitrines.serializers import TitleSerializer, HotelSerializer


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
