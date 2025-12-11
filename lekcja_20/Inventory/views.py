from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.http import HttpResponse

def info(request):
    return HttpResponse("Informacje o stronie")

def rules(request):
    return HttpResponse("Regulamin")

def user_profile(request, username):
    return HttpResponse(f"Witaj na profilu {username}")

def category_products(request, category_id):
    
    products = Product.objects.filter(category_id=category_id)
    
    return render(request, "category_products.html", {
        "category_id": category_id,
        "products": products
    })

