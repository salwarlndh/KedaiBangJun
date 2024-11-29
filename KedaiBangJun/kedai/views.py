from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Product, Order
from .cart import Cart
from .decorators import group_required
from django.http import HttpResponseForbidden, JsonResponse
from django.db.models import Q
from django.contrib.auth import logout
from rest_framework import viewsets
from .serializers import ProductSerializer

def homepage(request):
    product = Product.objects.all()
    return render(request, 'homepage/index.html', {'product': product})

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
        orders = Order.objects.all()
        for order in orders:
            order.total = order.quantity * order.price
        return render(request, 'dashboard/kasir.html', {'orders': orders})
    return HttpResponseForbidden("You do not have permission to access this page.")

def checkout(request):
    if request.method == 'POST':
        try:
            # Ambil data dari request
            data = json.loads(request.body)
            customer_name = data.get('customer_name')
            cart = data.get('cart')

            if not customer_name or not cart:
                return JsonResponse({'message': 'Nama pelanggan dan cart tidak boleh kosong.'}, status=400)

            # Debugging: Log data cart untuk memastikan semuanya sesuai
            print("Cart data received:", cart)

            # Proses setiap item dalam cart
            for item in cart:
                order = Order(
                    customer_name=customer_name,
                    product_id=item['product_id'],  # Pastikan product_id ada
                    product_name=item['product_name'],
                    quantity=item['quantity'],
                    price=item['price'],
                    total=item['total']  # Total dihitung di frontend
                )
                order.save()

            return JsonResponse({'message': 'Pemesanan berhasil!'}, status=200)

        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)

    return JsonResponse({'message': 'Invalid method'}, status=405)


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
    
@csrf_exempt  # Hanya untuk demo. Pastikan CSRF tetap diaktifkan untuk aplikasi yang sebenarnya.
def update_order(request, order_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            quantity = data.get('quantity')
            total = data.get('total')

            # Cari pesanan di database
            order = Order.objects.get(id=order_id)
            order.quantity = quantity
            order.total = total
            order.save()

            return JsonResponse({'message': 'Order updated successfully'})

        except Order.DoesNotExist:
            return JsonResponse({'message': 'Order not found'}, status=404)

        except Exception as e:
            return JsonResponse({'message': f'Error: {str(e)}'}, status=400)

    return JsonResponse({'message': 'Invalid request method'}, status=405)

def delete_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            customer_name = data.get('customer_name')

            # Cari order berdasarkan nama pelanggan
            order = Order.objects.filter(customer_name=customer_name)

            if order.exists():
                # Hapus order
                order.delete()
                return JsonResponse({'message': 'Pesanan berhasil dihapus!'}, status=200)
            else:
                return JsonResponse({'message': 'Pesanan tidak ditemukan!'}, status=404)
        except Exception as e:
            return JsonResponse({'message': f'Terjadi kesalahan: {str(e)}'}, status=500)
    return JsonResponse({'message': 'Metode tidak diizinkan'}, status=405)
