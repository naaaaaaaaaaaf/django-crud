from django.db import models

# Create your models here.
# Create your models here.
class Bmi(models.Model):
    name = models.CharField(max_length=100)
    bmi = models.FloatField()