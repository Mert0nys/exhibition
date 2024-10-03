from rest_framework import serializers
from .models import Kitten, Breed

class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'

class KittenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitten
        fields = '__all__'
