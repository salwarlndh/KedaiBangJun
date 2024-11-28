from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from .admin import Admin

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)
    address = models.TextField()
    
    admin_id = models.ForeignKey(Admin, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name
    
@receiver(post_save, sender=Customer)
def create_user_for_Customer(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(
            username=instance.name,
            password=instance.name,
        )
        customer_group, created = Group.objects.get_or_create(name='Customer')
        user.groups.add(customer_group)