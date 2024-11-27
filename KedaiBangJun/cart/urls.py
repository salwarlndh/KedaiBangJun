from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_index, name='cart_index'),
    path('cart/add/', views.cart_add, name="cart_add"),
    path('cart/delete/', views.cart_delete, name='cart_delete'),
    path('cart/update/', views.cart_update, name='cart_update'),
    path('cart/clear-cart/', views.clear_cart, name='clear_cart'),
]
