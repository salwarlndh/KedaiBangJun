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
    path('cart/delete/', views.cart_delete, name='cart_delete'),
    path('cart/update/', views.cart_update, name='cart_update'),
    path('cart/clear-cart/', views.clear_cart, name='clear_cart'),
    path('product/', views.products_index, name='product_index'),
    path('product/<int:product_id>/', views.get_product_details, name='get_product_details'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('dashboard/admin', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard/kasir', views.dashboard_kasir, name='dashboard_kasir'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)