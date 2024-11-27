from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.homepage, name='homepage'),
    path('product/', views.products_index, name='product_index'),
    path('contact/', views.contact, name='contact'),
    path('sign-in/', views.SignIn, name='sign-in'),
    path('sign-out/', views.SignOut, name='sign-out'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)