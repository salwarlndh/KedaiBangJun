from django.db import models
from kedai.models.products import Product

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_price(self):
        return self.quantity * self.product.price

    def _str_(self):
        return f"{self.product.name} - {self.quantity}"