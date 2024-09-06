from django.db import models

class Game (models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000)

class offer(models.Model):
    code = models.CharField(max_length=10)
    desccription = models.CharField(max_length=1000)
    discount = models.FloatField()