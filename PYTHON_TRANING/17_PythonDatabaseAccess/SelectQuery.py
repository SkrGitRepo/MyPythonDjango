'''
Created on Feb 11, 2016

@author: sumkuma2
'''
import MySQLdb
from DBUtil import DbUtil


#dbhost='localhost'
#dbname='pythondb'
#dbuser='root'
#dbpwd='root'

#dbutil = DbUtil(dbhost,dbuser,dbpwd,dbname)
dbutil = DbUtil()
con = dbutil.getMySQLConnection()
cursor = con.cursor()

try:
    
    sql = "SELECT * FROM employee"
    cursor.execute(sql)
    
    '''Fetch all the rows in a list of lists.'''
    results = cursor.fetchall()
    print "empid,first_name,last_name,age,sex,income"
    
    for row in results:
        empid = row[0]
        fname = row[1]
        lname = row[2]
        age = row[3]
        sex = row[4]
        income = row[5]
        # Now print fetched result
        print empid,",",fname,",",lname,",",age,",",sex,",",income
        #print "empid=%d,fname=%s,lname=%s,age=%d,sex=%s,income=%d"%(empid,fname,lname,age,sex,income)
        
except MySQLdb.Error, e:
    print "Error: unable to fecth data %s",e
    
finally:
    cursor.close()
    con.close()
    



