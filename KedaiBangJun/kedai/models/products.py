from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from kedai.models.admin import Admin

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    picture = models.ImageField(null=True, blank=True, upload_to="menu_pict/")
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    def __str__(self):
        return self.name