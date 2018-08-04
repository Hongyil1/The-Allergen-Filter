from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Category, Allergen, Store, Product 
from django.shortcuts import render_to_response
from django.utils import timezone


def listproducts(request, category_slug=None):
    category =  None
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category)
        products = Product.filter(category=category)
    return render(request, 'allergyshop/product/list.html', {'category': category, 'categories':categories, 'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'allergyshop/detail.html', {'product':product})

def product_comment(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product.comment_set.create(comment_text=request.POST['comment'], username=request.POST['username'], pub_date=timezone.now())
    return HttpResponseRedirect(reverse('product_detail', args=(product.id,)))

def index(request):
    context = {}
    products = Product.objects.all()
    return render_to_response('allergyshop/index.html', {'context': context, 'products': products})
