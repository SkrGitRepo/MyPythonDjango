from django.shortcuts import render_to_response,render
from django.template import Context,loader
from django.http.response import HttpResponse
import urllib2
from EMANPrimeOptical.UserProvReporter.models import USER_TABLE
import logging
import re

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    return render_to_response('homepage.html')

def search_user(request):
    
    if request.method=='POST':
        userid = request.POST.get('userid');
        userrole = request.POST.get('userrole')
        #return render_to_response('search_result.html', {'userid':userid, 'userrole':userrole})
        return render(request,'search_result.html', {'userid':userid, 'userrole':userrole})
    
    elif request.method=='GET':
        if 'userid' in request.GET and request.GET['userid']:
            userid= request.GET['userid']
            userrole=request.GET['userrole']
            lifecycle_userrole = userrole.split('-')
            lifecycle = lifecycle_userrole[1]
            usertype = lifecycle_userrole[2] 
            #userrole = str(lifecycle_userrole[1]).title()
            
            if usertype == 'all':
                get_usrlist_from_cpo_prd2 = USER_TABLE.objects.filter(username= userid ).order_by('userid')
                cpo_prod2_users=[]
                for user in get_usrlist_from_cpo_prd2:
                    cpo_prod2_users.append(user.username)
                
                return render_to_response('search_result.html', {'userid':userid, 'userrole':userrole, 'lifecycle':lifecycle,'cpo_prod2':cpo_prod2_users})
            else:
                return render_to_response('search_result.html',{'userid':userid, 'userrole':userrole, 'lifecycle':lifecycle})
                
        else:
            error_message = 'Please provide valid userid'
            return render_to_response('search_result.html', {'error_msg':error_message})
    
        
def find_cpo_users(request,lifecycle,usertype):
    
    #logger.info("Lifecycle %s and usertype is : %s")%(lifecycle,usertype)
    if lifecycle == "prod":
        tmpl=loader.get_template("cpo_prod_users.html")
        
        (user_subtype,cpo_user_role,role_description) = get_user_subtype(usertype)
        
        if user_subtype == None:
            error_msg = 'Not a valid CPO usertype'
            cont = Context({'error_msg':error_msg,'usr_type':usertype})
            return HttpResponse(tmpl.render(cont))
        else:
            #usertype = usertype.title()
            get_usrlist_frm_cpo_prod1 = USER_TABLE.objects.using('eon_rch1_1_l').filter(subtypeofuser= user_subtype ).order_by('userid')
            cpo_prod1_users=[]
            for user in get_usrlist_frm_cpo_prod1:
                cpo_prod1_users.append(user.username)
                
            get_usrlist_frm_cpo_prod2 = USER_TABLE.objects.using('eon_rtp5_1_l').filter(subtypeofuser= user_subtype ).order_by('userid')
            cpo_prod2_users=[]
            for user in get_usrlist_frm_cpo_prod2:
                cpo_prod2_users.append(user.username)
                
            onramp_provisioned_users = get_cpo_provisioned_userlist(cpo_user_role)
            merged_prod_users = merge_userlist(cpo_prod1_users,cpo_prod2_users,onramp_provisioned_users)
            
            cont = Context( {'lifecycle':lifecycle,'usr_type':usertype,'role_description':role_description,'cpo_prod2':cpo_prod2_users,'cpo_prod1_users':cpo_prod1_users,'cpo_prod2_users':cpo_prod2_users,
                         'cpo_onramp_prod_users':onramp_provisioned_users,'merged_prod1_pord2_userlist':merged_prod_users} )
            
            return HttpResponse(tmpl.render(cont))
        
    elif lifecycle == 'dev':
        tmpl=loader.get_template("cpo_dev_users.html")
        
        (user_subtype,cpo_user_role,role_description) = get_user_subtype(usertype)
        
        if user_subtype == None:
            error_msg = 'Not a valid CPO usertype'
            cont = Context({'error_msg':error_msg,'usr_type':usertype})
        
            return HttpResponse(tmpl.render(cont))
        
        else: 
           
            get_usrlist_frm_cpo_dev1 = USER_TABLE.objects.using('eon_rtp3_1_l').filter(subtypeofuser= user_subtype ).order_by('userid')
            cpo_dev1_users=[]
            for user in get_usrlist_frm_cpo_dev1:
                cpo_dev1_users.append(user.username)
                
                
            get_usrlist_frm_cpo_dev2 = USER_TABLE.objects.using('eon_rtp3_2_l').filter(subtypeofuser= user_subtype ).order_by('userid')
            cpo_dev2_users=[]
            for user in get_usrlist_frm_cpo_dev2:
                cpo_dev2_users.append(user.username)
                
            onramp_provisioned_users = get_cpo_provisioned_userlist(cpo_user_role)
            
            merged_dev_users = merge_userlist(cpo_dev1_users,cpo_dev2_users,onramp_provisioned_users)
            
            cont = Context( {'lifecycle':lifecycle,'usr_type':usertype,'role_description':role_description,'cpo_dev2':cpo_dev2_users,'cpo_dev1_users':cpo_dev1_users,'cpo_dev2_users':cpo_dev2_users,
                         'cpo_onramp_dev_users':onramp_provisioned_users,'merged_dev1_dev2_userlist':merged_dev_users} )
            
            return HttpResponse(tmpl.render(cont))
                
    else:
        error_msg ="Not a valid instance of CPO"
        tmpl=loader.get_template("cpo_dev_users.html")
        cont = Context({'error_msg':error_msg});
             
        return HttpResponse(tmpl.render(cont))
        

def get_cpo_provisioned_userlist(usertype):
    
    cpo_onramp_resource = usertype
    url = "http://mailer-api.cisco.com/itsm/mailer/rest/text/noauth/members/%s"%(cpo_onramp_resource)
    cpo_onramp_provisioned_users = urllib2.urlopen(url)
    cpo_provisioned_userlist = cpo_onramp_provisioned_users.read()
    provisioned_userlist = cpo_provisioned_userlist.split('\n')
    
    search_pattern= re.compile('not found')
    
    matchObj = search_pattern.search(cpo_provisioned_userlist)
    
    if matchObj:
        return None
   
    else: 
        #this will escape any empty(None) line(element) in the list 
        provisioned_userlist = filter(None,provisioned_userlist)
       
        return provisioned_userlist
        

def merge_userlist(userlist1,userlist2,userlist3):
    
    if userlist1 == None:
        merged_userlist = list( set(userlist1)|set(userlist3) )
        merged_userlist.sort()
    elif userlist2 == None:
        merged_userlist = list( set(userlist1)|set(userlist3) )
        merged_userlist.sort()
    elif userlist3 == None:
        merged_userlist = list( set(userlist1)|set(userlist2) )
        merged_userlist.sort()
    else:
        merged_userlist = list( set(userlist1)|set(userlist2)|set(userlist3) )
        merged_userlist.sort()
    
    return merged_userlist


def get_user_subtype(usertype):
    
    if usertype == 'superuser':
        user_subtype=1
        cpo_user_role='cpo-prod-superuser'
        role_description='Has all permissions'
        return (user_subtype,cpo_user_role,role_description)
    elif usertype == 'sysadmin':
        user_subtype=2
        cpo_user_role='cpo-prod-sysadmin'
        role_description='Has permissions for all EMS related operations'
        return (user_subtype,cpo_user_role,role_description)
    elif usertype == 'networkadmin':
        user_subtype=3
        cpo_user_role='cpo-prod-networkadmin'
        role_description='Has permissions for all NE related operations'
        return (user_subtype,cpo_user_role,role_description)
    elif usertype == 'operator':
        user_subtype=4
        cpo_user_role='cpo-prod-operator'
        role_description='User who performs network surveillance on allocated NEs'
        return (user_subtype,cpo_user_role,role_description)
    elif usertype == 'provisioner':
        user_subtype=5
        cpo_user_role='cpo-prod-provisioner'
        role_description='Has permissions to provision NEs'
        return (user_subtype,cpo_user_role,role_description)
    else:
        return (None,None,None)
       