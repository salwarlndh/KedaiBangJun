<<<<<<< HEAD
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

=======
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .models.Cart import Cart, CartItem
from django.shortcuts import render
from .models import Product
from .decorators import group_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from django.db.models import Q
from django.contrib.auth import logout
>>>>>>> 2a401f08d1ccd0b3f9d3f6c7c39e2b073dbd6d60

def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def products_index(request):
    product = Product.objects.all()
    return render(request, 'Products/index.html', {'product':product})

def contact(request):
    return render(request, 'homepage/contact.html')

<<<<<<< HEAD
def cart(request):
    return {'cart' : Cart(request)}


=======
# @login_required
>>>>>>> 2a401f08d1ccd0b3f9d3f6c7c39e2b073dbd6d60
def cart_index(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    return render(request, "Carts/index.html", {"cart_products":cart_products})

<<<<<<< HEAD
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
=======
# @login_required
def cart_add(request, product_id, name, price):
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))  # ID produk yang ingin ditambahkan ke keranjang
        quantity = int(request.POST.get('quantity', 1))  # Kuantitas produk, default 1 jika tidak disediakan
        product = Product.objects.get(id=product_id)  # Ambil produk berdasarkan ID
>>>>>>> 2a401f08d1ccd0b3f9d3f6c7c39e2b073dbd6d60
        
def cart_delete(request):
    pass
def cart_update(request):
    pass
def clear_cart(request):
    # Menghapus cart dari session
    if 'cart' in request.session:
        del request.session['cart']  # Menghapus data keranjang dari session
    return JsonResponse({'message': 'Cart cleared successfully'})

<<<<<<< HEAD
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
=======
# @login_required
def cart_delete(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id)  # Cari item berdasarkan ID
        cart_item.delete()  # Hapus item dari keranjang
    except CartItem.DoesNotExist:
        pass
    return redirect('view_cart')

# @login_required
def cart_update(request, item_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))  # Ambil kuantitas yang baru
        cart_item = CartItem.objects.get(id=item_id)  # Ambil item berdasarkan ID
        cart_item.quantity = quantity  # Update kuantitas item
        cart_item.save()
        return redirect('cart_index')  # Redirect ke halaman keranjang


@login_required
>>>>>>> 2a401f08d1ccd0b3f9d3f6c7c39e2b073dbd6d60
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
