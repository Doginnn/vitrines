from rest_framework import serializers
from vitrines.vitrines.models import Evento, Item


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        exclude = ['evento']
