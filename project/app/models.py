from django.db import models

# Create your models here.

class Animal(models.Model):
    """
    """

    name = models.CharField(max_length=8, default='lion')
    sound = models.CharField(max_length=8, default='roar')
