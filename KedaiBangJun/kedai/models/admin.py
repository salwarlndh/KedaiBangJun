from django.db import models
from django.contrib.auth.models import User, Group
from django.dispatch import receiver
from django.db.models.signals import post_save

class Admin(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=13, unique=True)
    address = models.TextField()
    
    def __str__(self):
        return self.name
    
@receiver(post_save, sender=Admin)
def create_user_for_Admin(sender, instance, created, **kwargs):
    if created:
        user = User.objects.create_user(
            username=instance.name,
            password=instance.name,
        )
        admin_group, created = Group.objects.get_or_create(name='Admin')
        user.groups.add(admin_group)