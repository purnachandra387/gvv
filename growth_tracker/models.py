from django.db import models
from django.contrib.auth.models import User
from garden.models import Plant



class PlantGrowthLog(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    date = models.DateField()
    observation = models.TextField()
    photo = models.ImageField(upload_to='plant_photos/', blank=True, null=True)

    def __str__(self):
        return f'Log for {self.plant.name} on {self.date}'