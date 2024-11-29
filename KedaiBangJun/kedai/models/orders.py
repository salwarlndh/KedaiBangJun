from django.db import models
from django.utils.timezone import now  # Untuk default waktu yang valid


class Order(models.Model):
    STATUS_CHOICES = [
        ('Waiting', 'Waiting'),
        ('Served', 'Served'),
    ]

    customer_name = models.CharField(max_length=100, default='Unknown Customer')  # Default sementara
    product_id = models.IntegerField(default=1)
    product_name = models.CharField(max_length=100, default='default product')
    quantity = models.IntegerField(default=1)  # Tambahkan default
    price = models.FloatField(default=0.0)  # Tambahkan default
    total = models.FloatField(default=0.0, editable=False)  # Non-editable, dihitung otomatis
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Waiting')  # Konsisten dengan pilihan
    created_at = models.DateTimeField(default=now)  # Default waktu sekarang

    def save(self, *args, **kwargs):
        # Hitung total otomatis sebelum menyimpan
        self.total = self.quantity * self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_name} - {self.product_name} ({self.quantity})"
