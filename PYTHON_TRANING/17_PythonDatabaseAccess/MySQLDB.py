'''
Created on Feb 18, 2016

@author: sumkuma2
'''
import MySQLdb

class MySQLDB(object):
       
    '''
    This a MySQL DB connectivity class
    '''
    def __init__(self):
        '''
        Constructor
        '''
    
    
    def connect(self,dbuser,dbpwd,dbname,dbhost,port):
        try:
            self.db = MySQLdb.connect(dbhost,dbuser,dbpwd,dbname);
            
        except MySQLdb.Error as e:
            
            print "Error: unable to connect Python with MySQL DB %s",e
            error, = e.args
            if error.code == 1017:
                print('Please check your credentials.')
            else:
                print('Database connection error: %s'.format(e))
            # Very important part!
            raise
        
        # If the database connection succeeded create the cursor
        # we-re going to use.
        self.cursor = self.db.cursor()

    def disconnect(self):
        """
        Disconnect from the database. If this fails, for instance
        if the connection instance doesn't exist we don't really care.
        """
        try:
            self.cursor.close()
            self.db.close()
        except MySQLdb.Error as e:
            print "Error: Disconnecting MySQL DB",e
            pass
    
        
    def execute(self, sql, bindvars=None, commit=False):
        """
        Execute whatever SQL statements are passed to the method;
        commit if specified. Do not specify fetchall() in here as
        the SQL statement may not be a select.
        bindvars is a dictionary of variables you pass to execute.
        """

        try:
            self.cursor.execute(sql)
                       
            '''Fetch all the rows in a list of lists.'''
            resultset = self.cursor.fetchall()
            print "EMPID,FIRST_NAME,LAST_NAME,AGE,SEX,INCOME"
    
            for row in resultset:
                empid = row[0]
                fname = row[1]
                lname = row[2]
                age = row[3]
                sex = row[4]
                income = row[5]
                # Now print fetched result
                print empid,",",fname,",",lname,",",age,",",sex,",",income
                    
        except MySQLdb.Error as e:
            error, = e.args
            if error.code == 955:
                print('Table already exists')
            elif error.code == 1031:
                print("Insufficient privileges")
            print(error.code)
            print(error.message)
            print(error.context)

            # Raise the exception.
            raise

        # Only commit if it-s necessary.
        if commit:
            self.db.commit()



if __name__ == '__main__':
    try:        
        mysqldb = MySQLDB()
               
        con = mysqldb.connect(dbuser ='root', dbpwd = 'root', dbhost ='localhost', port = '1521', dbname = 'pythondb')
        
        sql = ('SELECT * FROM employee')
        #con.execute('DLL STATEMENT')
        #con.execute(sql)
        mysqldb.execute(sql)
    finally:
        mysqldb.disconnect()