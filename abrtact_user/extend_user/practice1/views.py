from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
# Create your views here.

def home(request):
     return HttpResponse("Working")

@api_view(["POST"])
def all(request):
     return Response({"Succcess":"Welldone"},status=status.HTTP_202_ACCEPTED)