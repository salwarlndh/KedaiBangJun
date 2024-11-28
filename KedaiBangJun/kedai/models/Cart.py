from django.db import models
from django.contrib.auth.models import User
from .products import Product

class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Menyimpan cart untuk user tertentu
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_total(self):
        # Menghitung total harga cart
        return sum(item.get_total() for item in self.cartitem_set.all())
    
    def get_item_count(self):
        # Menghitung jumlah total item dalam cart
        return sum(item.quantity for item in self.cartitem_set.all())
    
    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cartitems', on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, related_name='cartitems', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def get_total(self):
        # Menghitung total harga per item (harga * quantity)
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} (x{self.quantity})"
