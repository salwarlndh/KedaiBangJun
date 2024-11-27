from django.shortcuts import render
from .decorators import kasir_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages

def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def products_index(request):
    return render(request, 'Products/index.html')

def contact(request):
    return render(request, 'homepage/contact.html')

# Cart
def cart_index(request):
    return render(request, 'Carts/index.html')

def cart_add(request):
    return render(request, "Carts/add_cart.html")

def cart_delete(request):
    return render(request, "Cart/delete_cart.html")

def cart_update(request):
    return render(request, "Cart/update_cart.html")
def product(request):
    return render(request, 'homepage/product.html')

def contact(request):
    return render(request, 'homepage/contact.html')

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
