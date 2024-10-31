from django.db import models

class Admin(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)
    address = models.TextField()
    
    def __str__(self):
        return self.name