from wsgiref import headers
from django.shortcuts import render, redirect
from django.http import HttpResponse
from api.models import User

# Create your views here.
def index(request):
    return HttpResponse("something")

def logs(request):
    user = User.objects.filter()[0]
    logs = user.log_set.all()
    print(logs[0].__dict__)
    return HttpResponse(str([log.description for log in logs])) 