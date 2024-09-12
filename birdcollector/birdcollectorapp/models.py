from django.db import models
from django.contrib.auth.models import User

class Bird(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # associate with the user

    def __str__(self):
        return self.name
