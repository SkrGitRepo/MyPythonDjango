from django.shortcuts import render
from django.contrib.auth.decorators import login_required

#This login required decorator is to not allow any
# view without AUTHENTICATION

@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")