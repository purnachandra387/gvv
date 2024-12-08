from django.db import models
from django.contrib.auth.models import User
from garden.models import Garden, Plant

class Task(models.Model):
    TASK_TYPES = [
        ('watering', 'Watering'),
        ('fertilizing', 'Fertilizing'),
        ('pruning', 'Pruning'),
        ('other', 'Other'),
    ]
    garden = models.ForeignKey(Garden, on_delete=models.CASCADE)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    task_type = models.CharField(max_length=50, choices=TASK_TYPES)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.task_type.capitalize()} for {self.plant.name} on {self.due_date}'
