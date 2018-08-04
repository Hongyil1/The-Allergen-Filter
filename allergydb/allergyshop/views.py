from django.shortcuts import render, get_object_or_404
from .models import Category, Ingredient, Allergen, Store, Product 

def listproducts(request, category_slug=None):
    category =  None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category)
        products = products.filter(category=category)
    return render(request, 'allergyshop/product/list.html', {'category': category, 'categories':categories, 'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'allergyshop/product/detail.html', {'product':product})
# Create your views here.
