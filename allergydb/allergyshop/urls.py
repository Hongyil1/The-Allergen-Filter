from django.conf.urls import url
from .import views

urlpatterns = [
        url(r'', views.listproducts, name='list_of_products'),
        url(r'^(?P<category_slug>[-\w]+)/$', views.listproducts
