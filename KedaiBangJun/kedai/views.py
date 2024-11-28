from django.shortcuts import render
from .models import Product
from .decorators import group_required
# from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import render
# from django.db import IntegrityError
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.http import JsonResponse
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
def Dashboard(request):
    user = request.user
    if user.groups.filter(name='Kasir').exists():
        return redirect('dashboard')
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
