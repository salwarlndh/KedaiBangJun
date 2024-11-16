from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Kasir(models.Model):
    id_kasir = models.IntegerField(unique=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(5**5-1) # id_kasir maksimal 5 digit
    ])
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)
    address = models.TextField()
    
    def __str__(self):
        return self.name