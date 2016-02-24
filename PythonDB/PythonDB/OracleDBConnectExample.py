'''
Created on Feb 18, 2016

@author: sumkuma2
'''
import cx_Oracle


class Oracle(object):

    def connect(self, username, password, hostname, port, servicename):
        """ Connect to the database. """
        
        try:
            #rcuser/D3v4CSPadmin@173.38.50.157:1530/OPSDEV.cisco.com
            #connString = '{}/{}@{}:{}/{}'.format(username,password,hostname,port,servicename)
            #print ("connString =") , connString , ("\n")
            SID=servicename
            dsn_tns = cx_Oracle.makedsn(hostname,port,SID)
            self.db = cx_Oracle.connect(username,password,dsn_tns)
            
        except cx_Oracle.DatabaseError as e:
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
        except cx_Oracle.DatabaseError:
            pass

    def execute(self, sql, bindvars=None, commit=False):
        """
        Execute whatever SQL statements are passed to the method;
        commit if specified. Do not specify fetchall() in here as
        the SQL statement may not be a select.
        bindvars is a dictionary of variables you pass to execute.
        """

        try:
            #resultset = self.cursor.execute(sql, bindvars)
            resultset = self.cursor.execute(sql)
            
            for result in resultset:
                print (result)
                
        except cx_Oracle.DatabaseError as e:
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
           


if __name__ == "__main__":
    
    try:        
        oracle = Oracle()
        #con = oracle.connect(username ='rcuser', password = 'D3v4CSPadmin', hostname ='173.38.50.157', port = '1530', servicename = 'OPSDEV.cisco.com')
        con = oracle.connect(username ='ctmreadonly', password = 'ctm123!', hostname ='173.38.48.103', port = '1521', servicename = 'OPTDB')
        
        sql = ('select *from user_table order by userid')
        #con.execute('DLL STATEMENT')
        #con.execute(sql)
        oracle.execute(sql)
    finally:
        oracle.disconnect()

