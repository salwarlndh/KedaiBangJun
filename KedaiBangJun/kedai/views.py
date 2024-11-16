from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage/index.html')

def about(request):
    return render(request, 'homepage/about.html')

<<<<<<< HEAD
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
=======
def product(request):
    return render(request, 'homepage/product.html')

def contact(request):
    return render(request, 'homepage/contact.html')
>>>>>>> 96dd5c79f8ecbdccb2c99f913cc1b33f07b1def3
