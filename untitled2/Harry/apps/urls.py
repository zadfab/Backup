from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name="nome"),
path('/item',views.item,name="nom"),
]