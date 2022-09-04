from wsgiref import headers
from django.shortcuts import render, redirect
from django.http import HttpResponse
from api.models import User

# Create your views here.
def index(request):
    return HttpResponse("something")

def log(request):
    user = User.objects.filter()[0]
    return HttpResponse(str(user.__dict__),) 