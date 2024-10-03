from rest_framework import viewsets
from .models import Kitten, Breed
from .serializers import KittenSerializer, BreedSerializer

class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class KittenViewSet(viewsets.ModelViewSet):
    queryset = Kitten.objects.all()  # Убедитесь, что этот атрибут присутствует
    serializer_class = KittenSerializer

