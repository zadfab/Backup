
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login,name='login'),
    path('home',views.gethome,name='home'),
    path('signup',views.signUp,name='mySignUp'),
    path('blog/',include('blog.tab.urls')),
    path('shop/',include('shop.shop.urls')),
    path('student/',include('student.urls')),






]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

