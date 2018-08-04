from django.shortcuts import render, get_object_or_404
from .models import Category, Allergen, Store, Product 
from django.shortcuts import render_to_response


def listproducts(request, category_slug=None):
    category =  None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category)
        products = Product.filter(category=category)
    return render(request, 'allergyshop/product/list.html', {'category': category, 'categories':categories, 'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'allergyshop/product/detail.html', {'product':product})
# Create your views here.

def index(request):
    context = {}
    products = Product.objects.all()
    return render_to_response('allergyshop/index.html', {'context': context, 'products': products})
