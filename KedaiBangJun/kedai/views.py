from django.shortcuts import render
from .decorators import kasir_required

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

def SignOut(request):
    logout(request)
    return redirect('sign-in') 