'''
Created on Nov 12, 2015

@author: sumkuma2
'''
import cx_Oracle

#For Oracle 11g-XE (Web Express Edition) default SID is 'XE' for ORACEL 11g edition SID will be 'ORCL'
con = cx_Oracle.connect('pythondb/sumkuma2@127.0.0.1/XE')
#print con.version
cur = con.cursor()
cur.execute('select *from demo_customers order by customer_id')

rows = cur.fetchone()

print rows
    
    
cur.close()
con.close()    

