from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import Admin
from .models import Customer
from .models import Kasir
from .models import Order
from .models import Product
from .models import Users

class AdminAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'address')
    
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
    
        user, created = Users.objects.get_or_create(username=obj.name, defaults={
            'password' : make_password('default_password'),
            'role': Users.ADMIN
        })

        if not created:
            user.role = Users.ADMIN
            user.save()

admin.site.register(Admin, AdminAdmin)
admin.site.register(Customer)
admin.site.register(Kasir)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Users)
