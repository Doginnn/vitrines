from rest_framework import viewsets
from vitrines.vitrines.models import Hotel, Item
from vitrines.vitrines.serializers import HotelSerializer, ItemSerializer


class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
