from django.shortcuts import render
from .food_api import get_recipes

def barcode_entry(request):
    return render(request, 'bclookup/entry.html')

def barcode_lookup(request):
    search = request.POST['search']
    allergies = request.POST['allergies']
    food_info = get_recipes(search, allergies)
    return render(request, 'bclookup/view.html', {'food_info': food_info})
