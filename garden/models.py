from django.db import models
from django.contrib.auth.models import User

class Plant(models.Model):
    name = models.CharField(max_length=100)
    optimal_soil = models.CharField(max_length=100)
    optimal_climate = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Garden(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    layout = models.TextField()  # This can be a JSON field for complex layouts
    plants = models.ManyToManyField(Plant)

    def __str__(self):
        return f'{self.user.username}\'s Garden'
