from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
@api_view()
def hello():
    return Response({"message": "Hello for today! See you tomorrow!"})
