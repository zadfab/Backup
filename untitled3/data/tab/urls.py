from django.urls import path

from . import views

urlpatterns = [
    path('', views.default,name='blog home'),
    path('home', views.home,name='blog me'),
    path('next', views.next,name='blog ho'),
    path('login', views.login,name='blo'),
    path('logout', views.logout,name='blopop'),

]