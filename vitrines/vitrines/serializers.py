from rest_framework import serializers
from vitrines.vitrines.models import *


class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('id', 'title', 'subtitle')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name', 'slug', 'state')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('name', 'slug')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
