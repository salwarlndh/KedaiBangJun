from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.homepage, name='homepage'),
    path('product/', views.products_index, name='product_index'),
    path('contact/', views.contact, name='contact'),
<<<<<<< HEAD
=======
    path('cart/', views.cart_index, name='cart_index'),
    path('cart_add/', views.cart_add, name="cart_add"),
    path('cart_delete/', views.cart_delete, name='cart_delete'),
    path('cart_update/', views.cart_update, name='cart_update'),
    
    path('dashboard/', views.Dashboard, name='dashboard'),

>>>>>>> 84aefad21697880841e288e286b38c769be06e87
    path('sign-in/', views.SignIn, name='sign-in'),
    path('sign-up/', views.SignUp, name='sign-up'),
    path('sign-out/', views.SignOut, name='sign-out'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)