from django.shortcuts import render
from .models import Product, Recommendation
from django.http import Http404
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,'index.html')

def product_list(request):
    products = Product.objects.all()
    return render(request,'product_list.html',{'all_products':products})

def product_details(request,id):
    global message
    try:
        product_details = Product.objects.get(pk=id)
        message = None
        if product_details is None:
            message = "Product Not Found"
    except Product.DoesNotExist:
        raise Http404("Product Doesnot Exists")
    return render(request,'product_details.html',{'product_details': product_details,'message': message})

def search_products(request):
    search_product = request.GET.get('q')
    if search_product:
        products = Product.objects.filter(id=search_product)
        product = products.first()
        if request.user.is_authenticated:
            user = request.user
            Recommendation.objects.create(user_id=user,product_id=product)
    else:
        products = Product.objects.none()
    return render(request,'product_list.html',{'all_products':products,'search_product':search_product})

