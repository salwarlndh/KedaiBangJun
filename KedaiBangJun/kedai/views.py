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

def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def products_index(request):
    product = Product.objects.all()
    return render(request, 'Products/index.html', {'product':product})

def contact(request):
    return render(request, 'homepage/contact.html')

@login_required
def cart_index(request):
    cart_items = CartItem.objects.filter(cart__user=request.user)
    return render(request, 'Carts/index.html', {'cart_items': cart_items})

@login_required
def cart_add(request, product_id, name, price):
    if request.method == 'POST':
        product_id = int(request.POST.get('product_id'))  # ID produk yang ingin ditambahkan ke keranjang
        quantity = int(request.POST.get('quantity', 1))  # Kuantitas produk, default 1 jika tidak disediakan
        product = Product.objects.get(id=product_id)  # Ambil produk berdasarkan ID
        
        # Cek apakah cart sudah ada untuk user ini
        cart, created = Cart.objects.get_or_create(user=request.user)
        
        # Cek apakah produk sudah ada di cart
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        
        if not created:  # Jika item sudah ada di cart, update kuantitasnya
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        
        cart_item.save()
        return redirect('cart_index')

@login_required
def cart_delete(request, item_id):
    try:
        cart_item = CartItem.objects.get(id=item_id)  # Cari item berdasarkan ID
        cart_item.delete()  # Hapus item dari keranjang
    except CartItem.DoesNotExist:
        pass
    return redirect('view_cart')

@login_required
def cart_update(request, item_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity'))  # Ambil kuantitas yang baru
        cart_item = CartItem.objects.get(id=item_id)  # Ambil item berdasarkan ID
        cart_item.quantity = quantity  # Update kuantitas item
        cart_item.save()
        return redirect('cart_index')  # Redirect ke halaman keranjang


@login_required
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
