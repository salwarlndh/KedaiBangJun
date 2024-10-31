from django.db import models

class Users(models.Model):
    ADMIN = 1
    CUSTOMER = 2
    KASIR = 3
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (CUSTOMER, 'Customer'),
        (KASIR, 'Kasir'),
    )

    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128) # Panjang standar untuk password hash di Django
    role = models.IntegerField(choices=ROLE_CHOICES) # 1 = Admin, 2 = Customer, 3 = Kasir

    def __str__(self):
        return self.username