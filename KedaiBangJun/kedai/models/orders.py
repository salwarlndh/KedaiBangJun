from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from kedai.models.products import Product
from kedai.models.customers import Customer

class Order(models.Model):
    STATUS_CHOICES = [
        ('Waiting', 'Waiting'),
        ('Served', 'Served'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'