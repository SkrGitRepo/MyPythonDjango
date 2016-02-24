'''
Created on Feb 17, 2016

@author: sumkuma2
'''
import cx_Oracle

username ='ctmreadonly'
password ='ctm123!'
host = 'eon-rtp5-1-l.cisco.com'
port ='1521'
SID = 'OPTDB'



#con_uri = '{}/{}@{}'.format(username,password,con_identifier)
#connStr='rcuser/D3v4CSPadmin@173.38.50.157:1530/OPSDEV.cisco.com'

#print (con_uri)
myuserlist=[]

try:
    '''using connection str '''
    #con = cx_Oracle.connect(connStr) 
    ''' using make dsn '''
    #dsn_tns = cx_Oracle.makedsn('173.38.50.157', '1530','OPSDEV' )
    dsn_tns = cx_Oracle.makedsn(host,port,SID)
    
    con = cx_Oracle.connect(username, password,dsn_tns)
    print ("Connection successful to :eon-rtp5-1-l : DB version: ",con.version)
    
    cur = con.cursor()
    sql =''' 
        SELECT
            ut.username
        FROM
            user_table ut,user_type_table utt
        WHERE
            ut.subtypeofuser = utt.usertypeid and
            ut.subtypeofuser = 1
        '''
    #execute sql query
    cur.execute(sql)
    
    #fetch one record
    #row = cur.fetchone()
    #print "(USERNAME,USERTYPE)"
    #print (row)
    
    '''for result in cur:
        print (result)
    else:
        print ("No result found")
    '''
    #data = cur.fetchone()
    rows = cur.fetchall()

    #print ("data: "),data
   
    for row in rows:
        username = row[0]
        myuserlist.append(username)
        
    
        
    cur.close()
    con.close()
    
    
    '''con = cx_Oracle.connect('ctmreadonly/ctm123!@173.38.48.103/OPTDB')
    cur = con.cursor()
    cur.execute('select * from user_table order by userid')
    for result in cur:
        print (result)
    cur.close()
    con.close()''' 
    
except cx_Oracle.DatabaseError as e:
    error, = e.args
    if error.code == 955:
        print('Table already exists')
    elif error.code == 1031:
        print("Insufficient privileges")
    print(error.code)
    print(error.message)
    print(error.context)
    
    #con.close()
    #print('Database connection error: %s'.format(e))
    print ('Database connection error: %s')%(e)
    raise


print myuserlist
