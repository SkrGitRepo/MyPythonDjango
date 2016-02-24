'''
Created on Oct 12, 2015

@author: sumkuma2
'''
from django.http.response import HttpResponse
def Hi(request):
    return HttpResponse('<center><h1>Welcome to <br/>Django Web Application</h1></center> ')

    
