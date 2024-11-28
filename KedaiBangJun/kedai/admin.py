from django.contrib import admin
from django.contrib.auth.hashers import make_password
<<<<<<< HEAD
from .models import Admin
from .models import Customer
from .models import Kasir
from .models import Order
from .models import Product
from .models import Users
# Register your models here.

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
=======
from .models.admin import Admin
from .models.customers import Customer
from .models.kasir import Kasir
from .models.orders import Order
from .models.products import Product
from .models.users import Users

class AdminAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address')

    def save_model(self, request, obj, form, change):
    # Simpan admin terlebih dahulu
        super().save_model(request, obj, form, change)

        # Cek apakah user dengan email admin sudah ada
        user, created = Users.objects.get_or_create(username=obj.name, defaults={ # Pastikan ini model Users kustom
        'password': make_password('default_password'), # Menggunakan hashing password
        'role': Users.ADMIN # Pastikan Anda memiliki field role di model Users
        })

        if not created:
            # Jika user sudah ada, perbarui role (untuk berjaga-jaga)
            user.role = Users.ADMIN
            user.save()

# Daftarkan admin dengan custom AdminAdmin
admin.site.register(Admin, AdminAdmin)
admin.site.register(Kasir)
admin.site.register(Customer)
>>>>>>> 2a401f08d1ccd0b3f9d3f6c7c39e2b073dbd6d60
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Users)
