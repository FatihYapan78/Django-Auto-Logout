from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url="login/")
def index(request):
    idle_time = settings.AUTO_LOGOUT["IDLE_TIME"]
    return render(request, "index.html",{"idle_time":idle_time})

def login(request):

    return render(request, "login.html")