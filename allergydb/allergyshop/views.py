from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Category, Allergen, Store, Product
from django.shortcuts import render_to_response

from django.db.models import Q

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

    products = Product.objects.all()

    results = ""

    if 'barcode_search' in request.GET:
        search = request.GET.get('barcode_search')
        if search != "":
            results = Product.objects.filter(barcode__icontains=search)
        else:
            results = ""

    if 'item_search' in request.GET:  # If the form is submitted
        item_name = request.GET.get('item_search')
        item_category = request.GET.get('category')
        item_allergens = request.GET.get('allergens')
        print("name: ", item_name, " category: ", item_category, "allergens: ", item_allergens)
        allergen_list = item_allergens.split(",")

        products_not_allergen = Product.objects.all()
        for allergen in allergen_list:
            products_not_allergen = products_not_allergen.filter(~Q(allergens__icontains=allergen))
            # print("aaaa")
            # print(len(products_not_allergen))

        if item_category != "":
            if len(products_not_allergen) != 0:
                # print("ccc")
                results = products_not_allergen.filter(category__icontains=item_category)
                print("results: ", results)
                if len(results) != 0:
                    # print("ddd")
                    results = results.filter(name__icontains=item_name)

    return render_to_response('allergyshop/index.html', {'results': results, 'products': products})
