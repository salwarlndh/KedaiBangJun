from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('about/', views.about, name='about'),
    path('home/', views.homepage, name='homepage'),
    path('product/', views.products_index, name='product_index'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart_index, name='cart_index'),
    path('cart_add/', views.cart_add, name="cart_add"),
    path('cart_delete/', views.cart_delete, name='cart_delete'),
    path('cart_update/', views.cart_update, name='cart_update')
=======
    path('home', views.homepage, name='home'),
    path('about', views.about, name='about'),
    path('product', views.product, name='product'),
    path('contact', views.contact, name='contact'),
>>>>>>> 96dd5c79f8ecbdccb2c99f913cc1b33f07b1def3
]