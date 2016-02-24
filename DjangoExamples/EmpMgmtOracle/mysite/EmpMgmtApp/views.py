from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
#from mysite.EmpMgmtApp.models import Emp
#from django.contrib.auth import authenticate
#from django.template import RequestContext
#from django.core.context_processors import csrf


# Create your views here.

def home(request):
    return render_to_response('base.html')

def login(request):
    #c  ={}
    #c.update(csrf(request))
    
    #return render_to_response('login.html',c,context_instance=RequestContext(request))
    #'''
    return render(request,'login.html')
    #'''
    
def contactus(request):
    return render(request,'contactus.html')

def auth_view(request):
    username= request.POST.get('username','')
    password=request.POST.get('password','')
  
    user = auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request, user)
        #queryset=Emp.objects.all
        #return render_to_response('employee_list.html', {'full_name': request.user.username},queryset)
        return HttpResponseRedirect('/employees/')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('employee_list.html',{'full_name':request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/empmgmt')
    #return render_to_response('login.html')
    




