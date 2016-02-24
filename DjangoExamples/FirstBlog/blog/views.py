from django.shortcuts import render_to_response,render
from django.views.decorators.csrf import csrf_protect
from blog.models import posts
from django.http.response import HttpResponse
from django.template import RequestContext
from .forms import BlogPostForm
from .forms import userSignupForm
from django.db.transaction import commit
from datetime import datetime

def home(request):
    return render_to_response('base.html')
def contact(request):
    return render_to_response('Contact.html')
    
# Create your views here.

def viewblog(request):
    blog_posts = posts.objects.all()[:10] #this will fetch First 10 blog records from DB table 'posts'
    
    '''
    content = {
        'title':'My first post',
        'author':'Sumit',
        'date':'30th Oct,2015',
        'body':'The Internet is a beautiful thing. Everyone and anyone can have a slice of the pie, which means there are hundreds of thousands (if not millions!) of blogs cropping up every day.
         The number of fitness, health, and happiness blogs out there can be overwhelming.'
           
    }
    '''
    #return render_to_response('index.html',content)
    return render_to_response('ViewBlogs.html',{'posts':blog_posts})

def signup(request):
    return render(request,'Signup.html')
    

def submitBlog(request):
    form = BlogPostForm()
    #return render_to_response('AddBlog.html')
    return render_to_response('AddBlog.html',locals(),context_instance=RequestContext(request))
    

def saveBlog(request):
    '''
    if 'bauthor' in request.POST and request.POST['bauthor']:
        bauthor= request.GET['bauthor']
        btitle = request.GET['btitle']
        bcontents = request.GET['bcontent']
        btimestamp = request.GET['bdate']
        
        savepost = posts(author=bauthor,title=btitle,bodytext=bcontents,timestamp=btimestamp)
        savepost.save()
                
        return render_to_response('AddBlog.html',{'message':'Blog posted successfully.'},RequestContext(request))
    else :
        return HttpResponse('Please submit a search item.')
    '''
    '''
    if 'bauthor' in request.GET and request.GET['bauthor']:
        bauthor= request.GET['bauthor']
        btitle = request.GET['btitle']
        bcontents = request.GET['bcontent']
        btimestamp = request.GET['bdate']
        
        savepost = posts(author=bauthor,title=btitle,bodytext=bcontents,timestamp=btimestamp)
        savepost.save()
    '''
    form = BlogPostForm(request.POST or None)
    #current_date = datetime.today();
    #str(current_date);
    #timestamp = datetime.strptime(current_date, "%Y-%m-%d")
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        return render_to_response('AddBlog.html',{'message':'Blog posted successfully.'},
                                  context_instance=RequestContext(request))
    else :
        return HttpResponse('Please submit a search item.')


@csrf_protect
def saveUser(request):
    if request.method == 'POST':
        user_name = request.POST.get ('uname','')
        contact_no = request.POST.get('contactno','')
        password = request.POST.get('password','')
        email_id = request.POST.get('emailid','')
        address = request.POST.get('address','')
    
        signUp = userSignupForm(user_name=user_name,contact_no=contact_no,password=password,email_id=email_id,address=address)
        signUp.save();
    
        return render_to_response('Signup.html', {'SUCCESS' : 'User registered successfully'})
        
    