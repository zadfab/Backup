from django.urls import path
from . import views

urlpatterns = [


   path("",views.homepage, name ="homepage"),
   path("result",views.result, name ="result"),
   path("update",views.update, name ="update"),
   path("confirm",views.confirm, name ="confirm"),
   path("dashboard",views.dashboard, name ="confirm"),

]