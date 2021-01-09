from django.urls import path

from . import views

urlpatterns = [
    path('', views.default,name='blog home'),
    path('home', views.home,name='blog home'),
    path('next', views.next,name='blog home'),

]