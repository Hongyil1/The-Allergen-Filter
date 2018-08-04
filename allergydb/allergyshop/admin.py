from django.contrib import admin
from .models import Ingredient, Allergen, Store, Category, Product

class CategoryAdmin(admin.ModelAdmin):
   list_display = ['name']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['allergens', 'stores', 'category']
admin.site.register(Product, ProductAdmin)

class AllergenAdmin(admin.ModelAdmin):
   list_display = ['name']
admin.site.register(Allergen, AllergenAdmin)

class StoreAdmin(admin.ModelAdmin):
   list_display = ['name']
admin.site.register(Store, StoreAdmin)

class IngredientAdmin(admin.ModelAdmin):
   list_display = ['name']
admin.site.register(Ingredient, IngredientAdmin)


# Register your models here.
