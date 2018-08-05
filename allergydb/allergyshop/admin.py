from django.contrib import admin
from .models import Allergen, Store, Category, Product, Barcode, Comment

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

class BarcodeAdmin(admin.ModelAdmin):
    list_display = ['code']
admin.site.register(Barcode, BarcodeAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_text']
admin.site.register(Comment, CommentAdmin)
# Register your models here.
