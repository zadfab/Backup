
from django.urls import path
from . import  views

urlpatterns = [
    path('', views.std,name='students'),
    path('rollnumber',views.rn,name='rollnm'),
    path('std',views.student,name='std'),
    path('signup',views.signUp,name='signup'),
    path('home',views.gethome,name="home"),

    path('search',views.search,name="seacrh"),
    path('searchpage',views.searchpage,name='sp'),

]