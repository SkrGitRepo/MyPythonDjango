'''
Created on Oct 20, 2015

@author: sumkuma2
'''
#import MySQLdb
from DBUtil import DbUtil


# Open database connection
#db = MySQLdb.connect("localhost","root","root","PYTHONDB" )
# prepare a cursor object using cursor() method
#cursor = db.cursor()

dbhost='localhost'
dbname='pythondb'
dbuser='root'
dbpwd='root'
# Prepare SQL query to INSERT a record into the database.
sql = """INSERT INTO EMPLOYEE(EMP_ID,FIRST_NAME,
LAST_NAME, AGE, SEX, INCOME)
VALUES (4,'Adam', 'Parore', 39, 'M', 200000)"""

'''sql = """INSERT INTO EMPLOYEE(EMP_ID,FIRST_NAME,
LAST_NAME, AGE, SEX, INCOME)
VALUES (1,'Sumit', 'Kumar', 29, 'M', 200000)"""'''
dbobj =  DbUtil(dbhost,dbuser,dbpwd,dbname)
dbh = dbobj.getMySQLDBH()

try:
    cursor = dbh.cursor()
    # execute SQL query using execute() method.
    cursor.execute(sql)
    # Commit your changes in the database
    dbh.commit()
    print "One record inserted successfully"
except:
    # Rollback in case there is any error
    dbh.rollback()
    
    print "DB error while inserting record"
finally:
    cursor.close()
    dbh.close()
    
# disconnect from server
