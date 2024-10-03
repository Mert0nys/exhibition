from django.test import TestCase
import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Kitten, Breed

@pytest.mark.django_db
def test_create_kitten():
    client = APIClient()
    user = User.objects.create_user(username='testuser', password='testpass')
    client.force_authenticate(user=user)

    breed = Breed.objects.create(name="Persian")
    
    response = client.post('/api/kittens/', {
        'breed': breed.id,
        'color': 'White',
        'age_months': 2,
        'description': 'Cute kitten'
    })
    
    assert response.status_code == status.HTTP_201_CREATED

