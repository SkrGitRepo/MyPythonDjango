'''
Created on Feb 11, 2016

@author: sumkuma2
'''
import MySQLdb

class DbUtil:
    '''
    This calss provide a DB connection handler for MySQLDB 
    '''
    
    
    def __init__(self):
        '''
        Constructor
        '''
    
        
        
    def getMySQLConnection(self):
        '''
            This method has been implemented to connect with MySQLDB and prepare a connection handler for DB operations.
            
        '''
        dbhost='localhost'
        dbname='javadb'
        dbuser='root'
        dbpwd='root'
        #dbhost = self.dbhost
        #dbname = self.dbname
        #dbuser = self.dbuser
        #dbpwd = self.dbpwd
        con = MySQLdb.connect(dbhost,dbuser,dbpwd,dbname);
        
        
        return con