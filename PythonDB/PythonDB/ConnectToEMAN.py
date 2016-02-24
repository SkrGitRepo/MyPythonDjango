'''
Created on Feb 17, 2016

@author: sumkuma2
'''
import cx_Oracle

username ='eman_modify2'
password ='m5s51m5r5'

#username ='eman'
#password ='eman'

host = 'lnxdb-dev-vm-301.cisco.com'
port ='1522'
SID = 'EMANDEV'

con_identifier = 'EMANDEV'


con_uri = '{}/{}@{}'.format(username,password,con_identifier)


print (con_uri)

try:
    '''using connection str '''
    #con = cx_Oracle.connect(connStr) 
    ''' using make dsn '''
    #dsn_tns = cx_Oracle.makedsn('173.38.50.157', '1530','OPSDEV' )
    dsn_tns = cx_Oracle.makedsn(host,port,SID)
    
    con = cx_Oracle.connect(username, password,dsn_tns)
    print (con.version)
    
    #sql= "select *from employee where rownum<10";
    sql= "SELECT  employee_number,first_name,last_name,email_alias,job_title,hr_work_city,hr_work_country FROM employee WHERE email_alias='sumkuma2'"
    cur = con.cursor()
    #cur.execute("select *from employee where first_name='sumit'")
    cur.execute(sql)
    
    for row in cur:
        print (row)
    
    #data = cur.fetchone()
    #data = cur.fetchall()
    #print ("data: "),data
    
    cur.close()
    con.close()
    
    
except cx_Oracle.DatabaseError as e:
    print('Database connection error: %s'.format(e))
    raise



