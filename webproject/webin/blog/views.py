from django.shortcuts import render
from django.views.generic import (CreateView,ListView,FormView,DetailView,UpdateView,TemplateView)
from .models import blogdb
# Create your views here.
class blogclas(ListView):
    queryset = blogdb.objects.all();
    template_name = 'blog/blogdefault.html'
    def dove(self,request):
        cl={'qs':self.queryset}
        return (request,self.template_name,cl)
