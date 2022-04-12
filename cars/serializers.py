from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        feilds = ['id', 'make', 'model', 'year', 'price']