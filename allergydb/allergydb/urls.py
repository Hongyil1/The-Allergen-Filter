"""allergydb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
=======
from django.urls import include, path

urlpatterns = [
    path('recipe/', include('bclookup.urls')),
>>>>>>> e1ba368f6c233f804d7992584d0af78a613141a9
    path('admin/', admin.site.urls),
    path('allergyshop/', include('allergyshop.urls')),

]
