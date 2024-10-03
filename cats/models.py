from django.db import models
from django.contrib.auth.models import User

class Breed(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Kitten(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    color = models.CharField(max_length=50)
    age_months = models.PositiveIntegerField()
    description = models.TextField()
    rating = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.breed.name} - {self.color}"
