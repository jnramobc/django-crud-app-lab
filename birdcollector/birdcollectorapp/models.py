from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Bird model
class Bird(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    
# Define the Sighting model, referencing the Bird model
class Sighting(models.Model):
    bird = models.ForeignKey('Bird', on_delete=models.CASCADE)  # Use a string reference to avoid issues
    location = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f'{self.bird.name} sighted at {self.location} on {self.date}'

# Feeding model (one-to-many relation: Bird to Feedings)
class Feeding(models.Model):
    MEAL_CHOICES = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
    )
    date = models.DateField()
    meal = models.CharField(max_length=1, choices=MEAL_CHOICES, default='B')
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Sighting(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=255)
    bird = models.ForeignKey(Bird, on_delete=models.CASCADE)

    def __str__(self):
        return f"Sighting of {self.bird.name} on {self.date}"
