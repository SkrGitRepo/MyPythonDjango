from django.shortcuts import render_to_response


# Create your views here.
def home(request):
    return render_to_response('index.html')
def womenshop(request):
    return render_to_response('women.html')
def registration(request):
    return render_to_response('register.html')
def checkout(request):
    return render_to_response('checkout.html')
def prodetails(request):
    return render_to_response('details.html')
def contactdetails(request):
    return render_to_response('contact.html')