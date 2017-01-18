from django.shortcuts import render_to_response,render
from django.template import Context,loader
from django.http.response import HttpResponse
import urllib2
from EMANPrimeOptical.UserProvReporter.models import USER_TABLE
import logging
import re
from nested_dict import nested_dict
from rest_framework import generics,permissions
from EMANPrimeOptical.UserProvReporter.serializers import userSerializer

logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    return render_to_response('homepage.html')

class UserList(generics.ListCreateAPIView):
    queryset = USER_TABLE.objects.all().filter(subtypeofuser=1).order_by('userid')
    paginate_by = None
    paginate_by_param = None
    serializer_class = userSerializer
    
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

class UserTypeDetails(generics.ListAPIView):
    #queryset = USER_TABLE.objects.all().filter(subtypeofuser=1).order_by('userid')
    serializer_class = userSerializer
    
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        usertype = self.kwargs['username']
        return USER_TABLE.objects.filter(subtypeofuser=4)
    

class UserDeatils(generics.RetrieveUpdateDestroyAPIView):
    queryset = USER_TABLE.objects.all()
    serializer_class = userSerializer
    
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

def onramp_user_list(request,lifecycle,usertype):
    
    tmpl=loader.get_template("cpo_onramp_userlist.html")
        
    (user_subtype,cpo_user_role,role_description) = get_user_subtype(usertype)
        
    if user_subtype == None:
        error_msg = 'user not found'
        cont = Context({'error_msg':error_msg,'usr_type':usertype})
        return HttpResponse(tmpl.render(cont))
    else:
        get_cpo_usrlist_frm_onramp = USER_TABLE.objects.using('eon_rtp3_1_l').filter(subtypeofuser= user_subtype ).order_by('username')
        cpo_onramp_users=[]
        for user in get_cpo_usrlist_frm_onramp:
            cpo_onramp_users.append(user.username)
            
        cont = Context({'onramp_usr_list':cpo_onramp_users})
        return HttpResponse(tmpl.render(cont))
         
    
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

            if lifecycle == "all":
                
                user_status = nested_dict()
                
                get_usrlist_frm_cpo_dev1 = USER_TABLE.objects.using('eon_rtp3_1_l').filter(username=userid).order_by('userid')
                
                for user in get_usrlist_frm_cpo_dev1:
                    user_status['eon-rtp3-1-l']= user.subtypeofuser
                    user_status['eon-rch1-1-l']= user.subtypeofuser
                
                get_usrlist_frm_cpo_dev2 = USER_TABLE.objects.using('eon_rtp3_2_l').filter(username=userid).order_by('userid')
                for user in get_usrlist_frm_cpo_dev2:
                    user_status['eon-rtp3-2-l']= user.subtypeofuser
                    user_status['eon-rtp5-1-l']= user.subtypeofuser
                    
                
                cpo_dev_onramp_resource = {1:'cpo-dev-superuser',2:'cpo-dev-sysadmin',3:'cpo-dev-networkadmin',4:'cpo-dev-operator',5:'cpo-dev-provisioner',}
                                
                for subtypeoduser,onramp_resource in cpo_dev_onramp_resource.iteritems():
                    #onramp_provisioned_users = get_cpo_provisioned_userlist(onramp_resource)
                    onramp_provisioned_users = get_local_cpo_provisioned_userlist(request,userrole)
                    
                    logger.info("All user found under onramp resource : ")
                    logger.debug(onramp_provisioned_users)
                    
                    #onramp_approved_usrlist=[]
                    if onramp_provisioned_users != None:
                        if userid in onramp_provisioned_users:
                            logger.info("user found")
                            user_status['onramp_dev']=subtypeoduser


                cpo_prod_onramp_resource = {1:'cpo-prod-superuser',2:'cpo-prod-sysadmin',3:'cpo-prod-networkadmin',4:'cpo-prod-operator',5:'cpo-prod-provisioner',}
                
                for subtypeoduser,onramp_resource in cpo_prod_onramp_resource.iteritems():
                    #onramp_provisioned_users = get_cpo_provisioned_userlist(onramp_resource)
                    onramp_provisioned_users = get_local_cpo_provisioned_userlist(request,userrole)
                    
                    logger.info("All user found under onramp PROD resource : ")
                    logger.debug(onramp_provisioned_users)
                    
                    #onramp_approved_usrlist=[]
                    if onramp_provisioned_users != None:
                        if userid in onramp_provisioned_users:
                            user_status['onramp_prod']=subtypeoduser


                #Due to django template bug , defaultdict or nesteddict must be converted to python dict before passing to view
                user_status = dict(user_status)
                   
                
                return render_to_response('search_result.html', {'userid':userid, 'userrole':userrole, 'lifecycle':lifecycle,
                                                                 'user_status': sorted(user_status.items())},)
                #return render_to_response('search_result.html', {'userid':userid, 'userrole':userrole, 'lifecycle':lifecycle,
                #                                                 'user_status': user_status},)
            elif lifecycle == 'dev':
                
                #--------------------------------------------------------------------------------------------------------
                cpo_dev_onramp_resource = {'cpo-dev-superuser':1,'cpo-dev-sysadmin':2,'cpo-dev-networkadmin':3,'cpo-dev-operator':4,'cpo-dev-provisioner':5,}
                user_status = {}
                
                subtype_of_user= cpo_dev_onramp_resource[userrole]
                
                #get_usrlist_frm_cpo_dev1 = USER_TABLE.objects.using('eon_rtp3_1_l').filter(username=userid).filter(subtypeofuser=1).order_by('userid')
                get_usrlist_frm_cpo_dev1 = USER_TABLE.objects.using('eon_rtp3_1_l').filter(username=userid,subtypeofuser=subtype_of_user).order_by('userid')
                
                logger.info("**********Fetched data from dev1")
                logger.debug(get_usrlist_frm_cpo_dev1)
                
                for user in get_usrlist_frm_cpo_dev1:
                    user_status['eon-rtp3-1-l']= user.subtypeofuser
                
                #get_usrlist_frm_cpo_dev2 = USER_TABLE.objects.using('eon_rtp3_2_l').filter(username=userid).filter(subtypeofuser=1).order_by('userid')
                get_usrlist_frm_cpo_dev2 = USER_TABLE.objects.using('eon_rtp3_2_l').filter(username=userid,subtypeofuser=subtype_of_user).order_by('userid')
                
                for user in get_usrlist_frm_cpo_dev2:
                    user_status['eon-rtp3-2-l']= user.subtypeofuser
                    
                
                #cpo_dev_onramp_resource = {1:'cpo-dev-superuser',2:'cpo-dev-sysadmin',3:'cpo-dev-netwrokadmin',4:'cpo-dev-operator',5:'cpo-dev-provisioner',}
                #onramp_provisioned_users = get_cpo_provisioned_userlist(userrole)
                onramp_provisioned_users = get_local_cpo_provisioned_userlist(request,userrole)
                    
                logger.info("All user found under onramp resource : ")
                logger.debug(onramp_provisioned_users)
                    
                if onramp_provisioned_users != None:
                    if userid in onramp_provisioned_users:
                        logger.info("user found")
                        user_status['onramp_dev']=subtype_of_user


                #Due to django template bug , defaultdict or nesteddict must be converted to python dict before passing to view
                #user_status = dict(user_status)
                #--------------------------------------------------------------------------------------------------------
                return render_to_response('search_result.html',{'userid':userid, 'userrole':userrole,'lifecycle':lifecycle,'user_status':sorted(user_status.items())})
            
            elif lifecycle == 'prod':
                #--------------------------------------------------------------------------------------------------------
                cpo_prod_onramp_resource = {'cpo-prod-superuser':1,'cpo-prod-sysadmin':2,'cpo-prod-networkadmin':3,'cpo-prod-operator':4,'cpo-prod-provisioner':5,}
                user_status = {}
                
                subtype_of_user= cpo_prod_onramp_resource[userrole]
                
                #get_usrlist_frm_cpo_dev1 = USER_TABLE.objects.using('eon_rtp3_1_l').filter(username=userid).filter(subtypeofuser=1).order_by('userid')
                get_usrlist_frm_cpo_prod1 = USER_TABLE.objects.using('eon_rtp3_1_l').filter(username=userid,subtypeofuser=subtype_of_user).order_by('userid')
                
                logger.info("**********Fetched data from dev1")
                logger.debug(get_usrlist_frm_cpo_prod1)
                
                for user in get_usrlist_frm_cpo_prod1:
                    user_status['eon-rch1-1-l']= user.subtypeofuser
                
                get_usrlist_frm_cpo_prod2 = USER_TABLE.objects.using('eon_rtp3_2_l').filter(username=userid,subtypeofuser=subtype_of_user).order_by('userid')
                
                for user in get_usrlist_frm_cpo_prod2:
                    user_status['eon-rtp5-1-l']= user.subtypeofuser
                    
                
                #cpo_dev_onramp_resource = {1:'cpo-dev-superuser',2:'cpo-dev-sysadmin',3:'cpo-dev-netwrokadmin',4:'cpo-dev-operator',5:'cpo-dev-provisioner',}
                #onramp_provisioned_users = get_cpo_provisioned_userlist(userrole)
                onramp_provisioned_users = get_local_cpo_provisioned_userlist(request,userrole)    
                logger.info("All user found under onramp resource : ")
                logger.debug(onramp_provisioned_users)
                    
                if onramp_provisioned_users != None:
                    if userid in onramp_provisioned_users:
                        logger.info("user found")
                        user_status['onramp_prod']=subtype_of_user


                #Due to django template bug , defaultdict or nesteddict must be converted to python dict before passing to view
                #user_status = dict(user_status)
                #--------------------------------------------------------------------------------------------------------
                return render_to_response('search_result.html',{'userid':userid, 'userrole':userrole,'lifecycle':lifecycle,'user_status':sorted(user_status.items())})
            else:
                return render_to_response('search_result.html',{'userid':userid, 'userrole':userrole,'lifecycle':lifecycle,'user_status':'Hello'})
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
            #get_usrlist_frm_cpo_prod1 = USER_TABLE.objects.using('eon_rtp3_1_l').filter(subtypeofuser= user_subtype ).order_by('userid')
            cpo_prod1_users=[]
            for user in get_usrlist_frm_cpo_prod1:
                cpo_prod1_users.append(user.username)
                
            get_usrlist_frm_cpo_prod2 = USER_TABLE.objects.using('eon_rtp5_1_l').filter(subtypeofuser= user_subtype ).order_by('userid')
            #get_usrlist_frm_cpo_prod2 = USER_TABLE.objects.using('eon_rtp3_2_l').filter(subtypeofuser= user_subtype ).order_by('userid')
            cpo_prod2_users=[]
            for user in get_usrlist_frm_cpo_prod2:
                cpo_prod2_users.append(user.username)
                
            #onramp_provisioned_users = get_cpo_provisioned_userlist(cpo_user_role)
            onramp_provisioned_users = get_local_cpo_provisioned_userlist(request,cpo_user_role)
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
                
            #onramp_provisioned_users = get_cpo_provisioned_userlist(cpo_user_role)
            onramp_provisioned_users = get_local_cpo_provisioned_userlist(request,cpo_user_role)
            
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

def get_local_cpo_provisioned_userlist(request,usertype):
    cpo_onramp_resource = usertype
    local_host = request.get_host()
    print "LOCALHOST::",local_host
    url = "http://" + local_host + "/prime/optical/onramp/api/usertype/%s"%(cpo_onramp_resource)
    
    cpo_onramp_provisioned_users = urllib2.urlopen(url)
    cpo_provisioned_userlist = cpo_onramp_provisioned_users.read()
    provisioned_userlist = cpo_provisioned_userlist.split('\n')
    
    search_pattern= re.compile('not found')
    matchObj = search_pattern.search(cpo_provisioned_userlist)
    
    if matchObj:
        return None
    else: 
        user_list = []
        for user in provisioned_userlist:
            user = re.sub('\t|<br/>','', user.strip())
            user_list.append(user)
        
        #this will escape any empty(None) line(element) in the list 
        user_list = filter(None,user_list) #to remove any empty list item    
        return user_list

        

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
       