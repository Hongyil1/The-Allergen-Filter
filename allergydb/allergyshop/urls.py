from django.conf.urls import url
from .import views
from django.urls import path

urlpatterns = [
        # url(r'', views.listproducts, name='list_of_products'),
        # url(r'^(?P<category_slug>[-\w]+)/$', views.listproducts,
        # http://localhost:8000/allergyshop/
        path('', views.index, name='index'),

]
