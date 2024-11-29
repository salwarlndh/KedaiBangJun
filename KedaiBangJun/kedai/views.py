from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .cart import Cart
from django.shortcuts import render
from .models import Product
from .decorators import group_required
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth import logout
from rest_framework import viewsets
from .serializers import ProductSerializer

def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def products_index(request):
    product = Product.objects.all()
    return render(request, 'Products/index.html', {'product':product})

def contact(request):
    return render(request, 'homepage/contact.html')

def cart(request):
    return {'cart' : Cart(request)}

def cart_index(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    return render(request, "Carts/index.html", {"cart_products":cart_products})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        cart_quantity = cart.__len__()
        # response = JsonResponse({'Product Name: ': product.name})
        response =  JsonResponse({'qty': cart_quantity})
        return response

def clear_cart(request):
    # Menghapus cart dari session
    if 'cart' in request.session:
        del request.session['cart']  # Menghapus data keranjang dari session
    return JsonResponse({'message': 'Cart cleared successfully'})

def get_product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        return JsonResponse({
            'id': product.id,
            'name': product.name,
            'price': str(product.price),  # Mengembalikan harga sebagai string
            'description': product.description,
        })
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)


# @kasir_required()
def Dashboard(request):
    user = request.user
    if user.groups.filter(name='Kasir').exists():
        return render(request, 'dashboard/kasir.html')
    return HttpResponseForbidden("You do not have permission to access this page.")

@login_required
@group_required('Kasir')
def dashboard_kasir(request):
    return render(request, 'dashboard/index.html')

@login_required
@group_required('Admin')
def dashboard_admin(request):
    return render(request, 'dashboard/index.html')

def dashboard_logout(request):
    logout(request)
    return redirect('homepage')  

def product_search(request):
    query = request.GET.get('q')
    product = Product.objects.all()
    if query:
        product = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(price__icontains=query) |
            Q(picture__icontains=query) 
        )
    else:
        product = Product.objects.all()
    return render(request, 'Products/index.html', {'product': product, 'query': query})

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint yang memungkinkan operasi CRUD untuk model Students.
    """
    queryset = Product.objects.all() # Mengambil semua data mahasiswa dari database
    serializer_class = ProductSerializer # Menggunakan serializer yang sudah kita buat