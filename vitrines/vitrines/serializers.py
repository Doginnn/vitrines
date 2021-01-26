from rest_framework import serializers
from .models import Hotel


class HoteisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'
