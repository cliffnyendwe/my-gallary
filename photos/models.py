from django.db import models

# Create your models here.

class location(models,Model):
    location = models.CharField(max_length=40)

    def __str__(self):
        return self.location