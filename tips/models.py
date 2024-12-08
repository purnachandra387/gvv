from django.db import models

class GardeningTip(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
