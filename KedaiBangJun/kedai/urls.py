from django.shortcuts import render
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.homepage, name='homepage'),
    path('product/', views.products_index, name='product_index'),
    path('product/search', views.product_search, name='product_search'),
    path('contact/', views.contact, name='contact'),
    
    path('dashboard/', views.Dashboard, name='dashboard'),
    # path('dashboard/admin', views.dashboard_admin, name='dashboard_admin'),
    # path('dashboard/kasir', views.dashboard_kasir, name='dashboard_kasir'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)