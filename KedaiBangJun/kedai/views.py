from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

def product(request):
    return render(request, 'homepage/product.html')

def contact(request):
    return render(request, 'homepage/contact.html')
