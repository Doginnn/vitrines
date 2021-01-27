from rest_framework import serializers
from vitrines.vitrines.models import Vitrine, Hotel


class VitrineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vitrine
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
