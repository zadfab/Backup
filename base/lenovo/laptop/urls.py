from . import views
from django.urls import path
from . import views

urlpatterns=[

path('',views.home,name="my home"),
path('done',views.success,name="my home"),

]