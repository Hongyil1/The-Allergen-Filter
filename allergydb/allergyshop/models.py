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
    # allergens = models.ManyToManyField(Allergen)
    allergens = models.CharField(max_length=250, db_index=True, default=None)
    stores = models.CharField(max_length=250, db_index=True, default=None)
    barcode = models.CharField(max_length=250, db_index=True, default=None)
    picture = models.CharField(max_length=250, db_index=True, default=None)
    ingredients = models.TextField()

    def __str__(self):
        return self.name

    def get_stores(self):
        if self.stores:
            return self.stores.split(' ')
        return []

    def get_allergens(self):
        if self.allergens:
            return [f'image/{allergen}.jpg' for allergen in self.allergens.split(' ') if allergen != 'Nil'][:6:]
        return []

    class Meta:
        ordering = ('name',)

class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment_text = models.TextField()
    username = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.comment_text
       

    
        
