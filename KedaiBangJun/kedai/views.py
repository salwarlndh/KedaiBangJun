from django.shortcuts import render, redirect
from .decorators import kasir_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Product
from .models.Cart import Cart, CartItem

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


# @kasir_required()
def Dashboard(request):
    context = {
        'section': 'dashboard',
    }
    return render(request, 'dashboard/index.html', context)

def SignIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if not username or not password:
            return JsonResponse({'is_superuser': False, 'error': 'Username and password are required.'}, status=400)

        if user is not None and user.is_superuser and user.is_staff:
            login(request, user)
            return JsonResponse({'is_superuser': True})
        else:
            return JsonResponse({'is_superuser': False, 'error': 'Invalid username or password.'}, status=403)

    context = {
        'section': 'sign-in',
    }
    return render(request, 'homepage/sign-in.html', context)

def SignUp(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        if not name or not username or not email or not phone_number or not address:
            return JsonResponse({'error': 'name, username, email, phone number and address are required.'}, status=400)

        try:
            # Buat pengguna baru
            user = User.objects.create_user(name=name, username=username, email=email, phone_number=phone_number, address=address)
            user.save()
            return JsonResponse({'success': True, 'message': 'User created successfully.'})
        except IntegrityError:
            return JsonResponse({'error': 'Username already exists.'}, status=400)

    context = {
        'section': 'sign-up',
    }
    return render(request, 'homepage/sign-up.html', context)

def SignOut(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "You have been logged out successfully.")
    else:
        messages.info(request, "You were not logged in.")
    return redirect('sign-in')
