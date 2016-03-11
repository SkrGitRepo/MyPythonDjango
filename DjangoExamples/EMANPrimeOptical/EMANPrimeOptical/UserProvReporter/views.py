from django.shortcuts import render_to_response,render
from django.template import Context,loader
from django.http.response import HttpResponse
import urllib2
import cx_Oracle



from EMANPrimeOptical.UserProvReporter.models import USER_TABLE
from django.template.context_processors import request

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
            return render_to_response('search_result.html', {'userid':userid, 'userrole':userrole})
        else:
            error_message = 'Please provide valid userid'
            return render_to_response('search_result.html', {'error_msg':error_message})
    
        
    
def find_cpo_user(request,lifecycle,usr_subtype):

    #if lifecycle == "prod" and usr_subtype == '1':
    if lifecycle == "prod":
        #tmpl=loader.get_template("searchpage.html")
        
        get_usrlist_from_cpo_prd2 = USER_TABLE.objects.filter(subtypeofuser= usr_subtype ).order_by('userid')
        cpo_prod2_users=[]
        for user in get_usrlist_from_cpo_prd2:
            cpo_prod2_users.append(user.username)
    
        if usr_subtype == '1':
            onramp_provisioned_superusers = get_cpo_provisioned_userlist('cpo-prod-superuser')
            
            '''Passing CPO prod servername and cpo usersubtype (user role - SuperUser) '''
            cpo_prod1_users = get_cpo_db_connection('eon-rch1-1-l',1);
            
            merged_prod_superusers = merge_userlist(cpo_prod1_users,cpo_prod2_users,onramp_provisioned_superusers)
            
            cont = Context( {'cpo_prod2':cpo_prod2_users,'cpo_prod1_superusers':cpo_prod1_users,'cpo_prod2_superusers':cpo_prod2_users,
                     'cpo_onramp_prod_superusers':onramp_provisioned_superusers,'merged_prod1_pord2_userlist':merged_prod_superusers} )
            
            tmpl=loader.get_template("cpo_prod_superuser.html")
            
            return HttpResponse(tmpl.render(cont))
        else:
            error_msg ="Not a valid User Role of CPO"
            tmpl=loader.get_template("searchpage.html")
            cont = Context({'error_msg':error_msg})
             
            return HttpResponse(tmpl.render(cont))
        
        #cont = Context({'user_role':usr_subtype,'cpo_instance':lifecycle});
        #return HttpResponse(tmpl.render(cont))
        
        '''else:
            tmpl=loader.get_template("cpo_prod_superuser.html")
            return HttpResponse(tmpl.render(cont))
        '''
    else:
        error_msg ="Not a valid instace of CPO"
        tmpl=loader.get_template("searchpage.html")
        cont = Context({'error_msg':error_msg});
             
        return HttpResponse(tmpl.render(cont))
        
        
    
    
       

def cpo_prod_superuser(request):
    #cpo_user_list = USER_TABLE.objects.all()
    cpo_prod2_superuser_list = USER_TABLE.objects.filter(subtypeofuser= 1).order_by('userid')
    tmpl=loader.get_template("cpo_prod_superuser.html")
    
    
    cpo_prod2_superusers=[]
    
    for user in cpo_prod2_superuser_list:
        cpo_prod2_superusers.append(user.username)
    
    
    onramp_provisioned_superusers = get_cpo_provisioned_userlist('cpo-prod-superuser')
    
    cpo_prod1_superusers = get_cpo_db_connection('eon-rch1-1-l',1);
    
    merged_prod_superusers = merge_userlist(cpo_prod1_superusers,cpo_prod2_superusers,onramp_provisioned_superusers)
    
    cont = Context( {'cpo_prod2':cpo_prod2_superuser_list,'cpo_prod1_superusers':cpo_prod1_superusers,'cpo_prod2_superusers':cpo_prod2_superusers,
                     'cpo_onramp_prod_superusers':onramp_provisioned_superusers,'merged_prod1_pord2_userlist':merged_prod_superusers} )
    
    return HttpResponse(tmpl.render(cont))


def cpo_prod_sysadmin(request):
    
    cpo_prod2_sysadmin_list = USER_TABLE.objects.filter(subtypeofuser= 2).order_by('userid')
    tmpl=loader.get_template("cpo_prod_sysadmin.html")
    
    
    cpo_prod2_sysadmins=[]
    
    for user in cpo_prod2_sysadmin_list:
        cpo_prod2_sysadmins.append(user.username)
    
    
    onramp_provisioned_sysadmins = get_cpo_provisioned_userlist('cpo-prod-sysadmin')
    
    cpo_prod1_sysadmins = get_cpo_db_connection('eon-rch1-1-l',2);
    
    merged_prod_sysadmins = merge_userlist(cpo_prod1_sysadmins,cpo_prod2_sysadmins,onramp_provisioned_sysadmins)
    
    cont = Context( {'cpo_prod2':cpo_prod2_sysadmin_list,'cpo_prod1_sysadmins':cpo_prod1_sysadmins,'cpo_prod2_sysadmins':cpo_prod2_sysadmins,
                     'cpo_onramp_prod_sysadmins':onramp_provisioned_sysadmins,'merged_prod1_pord2_userlist':merged_prod_sysadmins} )
    
    return HttpResponse(tmpl.render(cont))


#---------------------------------------------------------------

def cpo_prod_networkadmin(request):
    
    cpo_prod2_networkadmin_list = USER_TABLE.objects.filter(subtypeofuser= 3).order_by('userid')
    tmpl=loader.get_template("cpo_prod_networkadmin.html")
    
    cpo_prod2_networkadmins=[]
    
    for user in cpo_prod2_networkadmin_list:
        cpo_prod2_networkadmins.append(user.username)
    
    onramp_provisioned_networkadmins = get_cpo_provisioned_userlist('cpo-prod-networkadmin')
    cpo_prod1_networkadmins = get_cpo_db_connection('eon-rch1-1-l',3);
    merged_prod_networkadmins = merge_userlist(cpo_prod1_networkadmins,cpo_prod2_networkadmins,onramp_provisioned_networkadmins)
    
    cont = Context( {'cpo_prod2':cpo_prod2_networkadmin_list,'cpo_prod1_networkadmins':cpo_prod1_networkadmins,'cpo_prod2_networkadmins':cpo_prod2_networkadmins,
                     'cpo_onramp_prod_networkadmins':onramp_provisioned_networkadmins,'merged_prod1_pord2_userlist':merged_prod_networkadmins} )
    
    return HttpResponse(tmpl.render(cont))


def cpo_prod_operator(request):
    
    cpo_prod2_operator_list = USER_TABLE.objects.filter(subtypeofuser= 4).order_by('userid')
    tmpl=loader.get_template("cpo_prod_operator.html")
    
    cpo_prod2_operators=[]
    
    for user in cpo_prod2_operator_list:
        cpo_prod2_operators.append(user.username)
    
    onramp_provisioned_operators = get_cpo_provisioned_userlist('cpo-prod-operator')
    
    cpo_prod1_operators = get_cpo_db_connection('eon-rch1-1-l',4);
    
    merged_prod_operators = merge_userlist(cpo_prod1_operators,cpo_prod2_operators,onramp_provisioned_operators)
    
    cont = Context( {'cpo_prod2':cpo_prod2_operator_list,'cpo_prod1_operators':cpo_prod1_operators,'cpo_prod2_operators':cpo_prod2_operators,
                     'cpo_onramp_prod_operators':onramp_provisioned_operators,'merged_prod1_pord2_userlist':merged_prod_operators} )
    
    return HttpResponse(tmpl.render(cont))


def cpo_prod_provisioner(request):
    
    cpo_prod2_provisioner_list = USER_TABLE.objects.filter(subtypeofuser= 5).order_by('userid')
    tmpl=loader.get_template("cpo_prod_provisioner.html")
    
    cpo_prod2_provisioners=[]
    
    for user in cpo_prod2_provisioner_list:
        cpo_prod2_provisioners.append(user.username)
    
    
    onramp_provisioned_provisioners = get_cpo_provisioned_userlist('cpo-prod-provisioner')
    
    cpo_prod1_provisioners = get_cpo_db_connection('eon-rch1-1-l',5);
    
    merged_prod_provisioners = merge_userlist(cpo_prod1_provisioners,cpo_prod2_provisioners,onramp_provisioned_provisioners)
    
    cont = Context( {'cpo_prod2':cpo_prod2_provisioner_list,'cpo_prod1_provisioners':cpo_prod1_provisioners,'cpo_prod2_provisioners':cpo_prod2_provisioners,
                     'cpo_onramp_prod_provisioners':onramp_provisioned_provisioners,'merged_prod1_pord2_userlist':merged_prod_provisioners} )
    
    return HttpResponse(tmpl.render(cont))


def get_cpo_provisioned_userlist(usertype):
    
    cpo_onramp_resource = usertype
    url = "http://mailer-api.cisco.com/itsm/mailer/rest/text/noauth/members/%s"%(cpo_onramp_resource)
    
    cpo_onramp_provisioned_users = urllib2.urlopen(url)
    cpo_provisioned_userlist = cpo_onramp_provisioned_users.read()
    
    provisioned_userlist = cpo_provisioned_userlist.split('\n')
    
    #this will escape any empty(None) line(element) in the list 
    provisioned_userlist = filter(None,provisioned_userlist)
   
    return provisioned_userlist
    
    
    
def merge_userlist(userlist1,userlist2,userlist3):
    
    merged_userlist = list( set(userlist1)|set(userlist2)|set(userlist3) )
    merged_userlist.sort()
    
    return merged_userlist
    
        
def get_cpo_db_connection(dbhost,subtypeofuser):
    
    dbhostname = dbhost
    SID ='OPTDB'
    dbusername = 'ctmreadonly'
    dbpassword = 'ctm123!'
    dbport='1521'
    myuserlist=[]
    error_message=''
    
    try:
         
        ''' using make dsn '''
        dsn_tns = cx_Oracle.makedsn(dbhostname,dbport,SID)
        con = cx_Oracle.connect(dbusername,dbpassword,dsn_tns)
        cur = con.cursor()
        
        sql =('''
            SELECT
                ut.username
            FROM
                user_table ut,user_type_table utt
            WHERE
                ut.subtypeofuser = utt.usertypeid and
                ut.subtypeofuser = %d
            ''') %(subtypeofuser)
        
        #execute sql query
        cur.execute(sql)
        rows = cur.fetchall()
        
        for row in rows:
            username = row[0]
            myuserlist.append(username)
        cur.close()
        con.close()
        
    except cx_Oracle.DatabaseError as e:
        error, = e.args
        
        if error.code == 1031:
            #error_message = ("Insufficient privileges")
            error_message.append("Insufficient privileges");
            
        error_message.ap = (error.message)
        raise

    return myuserlist