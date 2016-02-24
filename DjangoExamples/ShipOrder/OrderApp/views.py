from django.shortcuts import render_to_response
from datetime import datetime
#from django.db.models.lookups import Hour
from OrderApp.models import Products
from django.http.response import HttpResponse
from OrderApp.from1 import ProductsForm



# Create your views here.
def home(self):
    
    message="Welcome to "
    username="Sumit"
    return render_to_response('Home.html',locals())

def currentdate(request):
    current_date=datetime.today()
    
    return render_to_response('current_datetime.html',locals())

def futuredate(request):
    #hours_offset=Hour
    #next_time=datetime.time()
    
    return render_to_response('Future_time.html',locals())


def order(request):
    
    person_name ='Sumit Kumar'
    company='Skr A2Z Shoppe Pvt. Ltd'
    item_list=['router','switch','laptop']
    ship_date=datetime.today()
    
    return render_to_response('OrderNotice.html',locals())


def search_form(request):
    return render_to_response('search.html')


def searchResult(request):
    if 'q' in request.GET and request.GET['q']:
        q= request.GET['q']
        fields = ProductsForm 
        
        products =  Products.objects.filter(productName__icontains=q)
        #products =  Products.objects.order_by('productName')
        return render_to_response('search_result.html',{'product':products,'query':q,'fields':fields})
        
    else:
        return HttpResponse('Please submit a search item.')
        