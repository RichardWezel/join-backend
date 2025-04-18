from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    color = models.CharField(max_length=7)  # Farbcodes wie #ff4646
    mail = models.EmailField()
    password = models.CharField(max_length=100)
    locked_in = models.BooleanField(default=False)