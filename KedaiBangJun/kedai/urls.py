from django.urls import path
from . import views

urlpatterns = [
    path('home', views.homepage, name='home'),
    path('about', views.about, name='about'),
    path('product', views.product, name='product'),
    path('contact', views.contact, name='contact'),
]