from wsgiref import headers
from django.shortcuts import render, redirect
from django.http import HttpResponse
from api.models import User

# Create your views here.
def index(request):
    return HttpResponse("something")


def sign_up(request):
    # request get 'submission form'
    # request post 'submit form'
    return render(request, '../templates/registration/sign_up.html')

def logs(request):
    print(request.user)
    user = User.objects.filter(user_name=request.user)[0]
    logs = user.log_set.all()
    logs_html = "".join(["<li>"+log.description + "</li>" for log in logs])
    return HttpResponse(f"<div>{logs_html}<br /><a href='/'>back to home</a></div>") 