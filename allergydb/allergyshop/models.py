from django.db import models

# Create your models here.

class Allergen(models.Model):
    name = models.CharField(max_length=1000, db_index=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Store(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
     
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
                
    def __str__(self):
        return self.name

class Barcode(models.Model):
    code = models.CharField(max_length=250, db_index=True)

    def __str__(self):
        return self.code

    class Meta:
        ordering = ('code',)

class Product(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    allergens = models.ManyToManyField(Allergen)
    stores = models.ManyToManyField(Store)
    barcode = models.CharField(max_length=250, db_index=True, default=None)
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
       

    
        
