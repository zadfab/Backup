from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.run1,name='start'),
    path('getstate',views.getstate,name='state'),
    #path('getcid',views.getcid,name='state'),
    #path('run2',views.run2,name='start'),

]