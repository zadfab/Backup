from django.urls import path,include
from .views import blogclas



app_name='blog'
urlpatterns = [
    path('',blogclas.as_view(),name='blogdefault')
]