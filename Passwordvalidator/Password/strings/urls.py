from django.urls import path
from . import views


#app_name='strings'
urlpatterns = [

    path("",views.average,name="average"),
    path("avg",views.averagestring,name="averagestr"),
    path("scribble",views.scribble,name="avtr"),

    path("expressionextended",views.expressionextended,name="exnext"),
]