from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter() # Membuat router DRF
router.register(r'product', ProductViewSet) # Menyambungkan StudentsViewSet ke URL /product/

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.homepage, name='homepage'),
    path('cart/', views.cart_index, name='cart_index'),
    path('cart/add/', views.cart_add, name="cart_add"),
    path('cart/clear-cart/', views.clear_cart, name='clear_cart'),
    path('product/', views.products_index, name='product_index'),
    path('product/<int:product_id>/', views.get_product_details, name='get_product_details'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('product/search', views.product_search, name='product_search'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.dashboard_logout, name='logout'),
    
    path('api/', include(router.urls)), # Ini akan menambahkan semua URL yang dibutuhkan untuk API
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)