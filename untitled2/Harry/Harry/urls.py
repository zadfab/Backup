"""Harry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello',views.pop1,name='op'),
    path('',views.pun1,name="pun"),
    path('home',views.pun,name="pun1"),
    path('facebook',views.pop2,name='op'),
    path('twitter',views.pop3,name='op'),
    path('youtube',views.pop4,name='op'),
    path('app',include('apps.urls'),name='op'),

]
