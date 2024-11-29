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
    path('cart/clear-cart/', views.clear_cart, name='clear_cart'),
    path('product/', views.products_index, name='product_index'),

    path('checkout/', views.checkout, name='checkout'),
    path('update_order/<int:order_id>/', views.update_order, name='update_order'),
    path('delete_order/', views.delete_order, name='delete_order'),

    path('product/<int:product_id>/', views.get_product_details, name='get_product_details'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.dashboard_logout, name='logout'),

    path('product/search', views.product_search, name='product_search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)