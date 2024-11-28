from django.shortcuts import render, get_object_or_404
from .models import Product
from .decorators import group_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, Http404
from .cart import Cart
from .models import Product


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
        
def cart_delete(request):
    pass
def cart_update(request):
    pass
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
        return redirect('dashboard_kasir')
    elif user.groups.filter(name='Admin').exists():
        return redirect('dashboard_admin')
    return HttpResponseForbidden("You do not have permission to access this page.")

@login_required
@group_required('Kasir')
def dashboard_kasir(request):
    return render(request, 'dashboard/index.html')

@login_required
@group_required('Admin')
def dashboard_admin(request):
    return render(request, 'dashboard/index.html')

# def SignIn(request):    
#     if request.user.is_authenticated:
#         return redirect('dashboard')
    
#     context = {
#         'section' : 'sign-in'
#     }
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             redirect_url = 'dashboard' if user.groups.filter(name='Kasir').exists() else 'homepage'
#             return JsonResponse({
#                 'status': 'success',
#                 'message': 'Login successful!',
#                 'redirect_url': redirect_url
#             })
#         else:
#             return JsonResponse({
#                 'status': 'error',
#                 'message': 'invalid username or password',
#                 'errors': {
#                     'login': ['Invalid username or password.']
#                 }
#             })

#     return render(request, 'homepage/sign-in.html', context)
