from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.homepage, name='homepage'),
    path('product/', views.products_index, name='product_index'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart_index, name='cart_index'),
    path('cart_add/', views.cart_add, name="cart_add"),
    path('cart_delete/', views.cart_delete, name='cart_delete'),
    path('cart_update/', views.cart_update, name='cart_update'),
    
    path('dashboard/', views.Dashboard, name='dashboard'),

    path('sign-in/', views.SignIn, name='sign-in'),
    path('sign-up/', views.SignUp, name='sign-up'),
    path('sign-out/', views.SignOut, name='sign-out'),
]