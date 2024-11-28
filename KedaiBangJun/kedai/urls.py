from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.homepage, name='homepage'),
    path('cart/', views.cart_index, name='cart_index'),
    path('cart/add/', views.cart_add, name="cart_add"),
    path('cart/delete/<int:item_id>/', views.cart_delete, name='cart_delete'),
    path('cart/update/<int:item_id>/', views.cart_update, name='cart_update'),
    path('product/', views.products_index, name='product_index'),
    path('product/search', views.product_search, name='product_search'),
    path('contact/', views.contact, name='contact'),
    
    path('dashboard/', views.Dashboard, name='dashboard'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.dashboard_logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)