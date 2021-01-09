
from django.urls import path,include
from . import views


app_name='student'
urlpatterns = [

    path('',views.sos,name='studenturls'),
    path('submit',views.submit,name='studentsubmit'),
    path('info',views.info,name='studmit'),
    path('product/<int:id>/',views.product,name='studmit'),
    path('product/<int:id>/delete',views.product,name='studmit'),

]
