from django.urls import path

from . import views

app_name = 'bclookup'
urlpatterns = [
    path('enter/', views.barcode_entry, name='bcenter'),
    path('lookup/', views.barcode_lookup, name='bclookup'),
]
