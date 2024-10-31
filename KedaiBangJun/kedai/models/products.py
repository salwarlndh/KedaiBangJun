from django.db import models
from kedai.models.admin import Admin

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField()
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name