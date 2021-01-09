from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.start,name='start'),
    path('submitform',views.submit,name='start'),
    path('search',views.search,name='start'),
    path('checkbox',views.searchbox,name='start'),
    #path('student/<int:rollnumber>',views.search,name='rollnumber'),
]