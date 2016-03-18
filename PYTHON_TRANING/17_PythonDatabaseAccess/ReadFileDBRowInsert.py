'''
Created on Mar 12, 2016

@author: sumkuma2
'''
from DBUtil import DbUtil
import MySQLdb
from datetime import datetime
from time import strftime,gmtime


#------------------------------------------------------------------------------------
def main():
    cfg = { 
           'db_user_table_records_file':'user_table_data.txt',
           'db_user_type_table_records_file':'user_type_table_data.txt',         
        }
    
    read_db_user_table_row_from_file(cfg)
    #read_db_user_type_table_row_from_file(cfg)

#------------------------------------------------------------------------------------
'''This will read each row(record) from file ,parse and map each data based on its correct mySQL datatype and
 insert into MySQL table:'pythondb.USER_TABLE' '''
def read_db_user_table_row_from_file(cfg):
    
    db_user_table_RowFile = cfg['db_user_table_records_file']
    count = 0    
    
    for dbrow in open(db_user_table_RowFile) :
        
        if count == 0:
            #print "First row is DB column header"
            dbTableHeader = dbrow.rstrip('\n')
            headerList = dbTableHeader.split(',')
            #print headerList
            
        elif count >= 1:
            dbTableRow = dbrow.rstrip('\n')
            rowData = dbTableRow.split(',')
            #print  rowData
            #parse_row_each_data(rowData)
            isExist = verify_row_exists_in_user_table(rowData[0])
            if (isExist == 0):
                insert_data_to_user_table(rowData)
                #print "Record will be inserted"
            else:
                print ("Record already exists with USERID: %s")%(rowData[0])
                pass
        else:
            pass
            
        count += 1

#------------------------------------------------------------------------------------
def verify_row_exists_in_user_table(userid):
        
    dbutil = DbUtil()
    con = dbutil.getMySQLConnection()
    cursor = con.cursor()

    try:
        sql = ("SELECT * FROM user_table where userid=%s")%(userid)
        cursor.execute(sql)
        
        '''Fetch one of the rows '''
        results = cursor.fetchone()
        if results > 0:
            found = 1
        else:
            found = 0
            
    except MySQLdb.Error, e:
        print "Error: unable to fetch data %s",e
        found =0
        
    finally:
        cursor.close()
        con.close()
    
    return found;

#------------------------------------------------------------------------------------
def insert_data_to_user_table(rowData):
    '''USERID=rowData[0]
    USERNAME=rowData[1]
    USERPASSWORD = rowData[2]
    TYPEOFUSER = rowData[3]
    SUBTYPEOFUSER = rowData[4]
    AREANAME = rowData[5]'''
    LASTLOGINTIME = convert_date_to_24hrdatetime(rowData[6])
    '''USERLOGINDISABLED = rowData[7]
    USERDESCRIPTION = rowData[8]
    CMSUSER = rowData[9]
    CMSPASSWORD = rowData[10]
    FAILEDATTEMPTS = rowData[11]
    STATUSOFUSER = rowData[12]'''
    PASSWORDSETTIME = convert_date_to_24hrdatetime(rowData[13])
    LASTLOGINFAILTIME = convert_date_to_24hrdatetime(rowData[14])
    '''LOCKEDSTATE = rowData[15]
    PROPAGATETONE = rowData[16]
    ENABLEPSWDCHANGE = rowData[17]
    FIRSTUSE = rowData[18]
    USEGLOBALLOCKOUT = rowData[19]
    LOCKOUTENABLED = rowData[20]
    LOCKOUTPERIOD = rowData[21]
    USEGLOBALLOGOUT = rowData[22]
    LOGOUTENABLED = rowData[23]
    LOGOUTPERIOD = rowData[24]
    ENABLEMULTIPLELOGIN = rowData[25]
    AUTODISABLEINTERVAL = rowData[26]'''
    
    insert_query = ("""insert into `javadb`.`user_table` values(%s,'%s','%s',%s,%s,
'%s','%s',%s,'%s','%s','%s',%s,%s,'%s','%s',%s,%s,%s,%s,%s,%s,'%s',%s,%s,'%s',%s,%s)""") %(rowData[0],rowData[1],rowData[2],rowData[3],rowData[4],
rowData[5],LASTLOGINTIME,rowData[7],rowData[8],rowData[9],rowData[10],rowData[11],rowData[12],PASSWORDSETTIME,LASTLOGINFAILTIME,rowData[15],rowData[16],rowData[17],rowData[18],
rowData[19],rowData[20],rowData[21],rowData[22],rowData[23],rowData[24],rowData[25],rowData[26])

    
    #print "SQL :",insert_query
    insert_row(insert_query,rowData[0])
    print "**** INSERTION TO USER_TABLE IS DONE *********"
    
    
#------------------------------------------------------------------------------------    
def insert_row(sql,uid):
    
    dbutil = DbUtil()
    con = dbutil.getMySQLConnection()
    cursor = con.cursor()
    
    try:
        cursor = con.cursor()
        # execute SQL query using execute() method.
        cursor.execute(sql)
        # Commit your changes in the database
        con.commit()
        print "One record inserted successfully with ID:",uid
        
    except MySQLdb.Error, e:
        # Rollback in case there is any error
        con.rollback()
        print "DB error while inserting record"
        print "Error: unable to insert row data %s",e
        
    finally:
        cursor.close()
        con.close()
    
#------------------------------------------------------------------------------------
'''
This will convert Date format from DD/MM/YYYY HH:MM:SS AM/PM to YYYY-MM-DD HH:MM:SS (24 Hrs) 
'''
def convert_date_to_24hrdatetime(date_time):

    parse_date_time=date_time.split(' ')
    
    # checking if datetime available or not
    if parse_date_time[0]:
        pdate = parse_date_time[0]
        #converting mm/dd/yyyy to yyyy-mm-dd
        new_date_yyyy_mm_dd = datetime.strptime(pdate, "%m/%d/%Y").strftime("%Y-%m-%d")
      
        ptime = parse_date_time[1]+ " " + parse_date_time[2]
        in_time = datetime.strptime(ptime, "%I:%M:%S %p")
        out_time = datetime.strftime(in_time, "%H:%M:%S")
        
        time_now = new_date_yyyy_mm_dd+" "+out_time
        
        return time_now
    
    else:
        '''Creating current time stamp if datetime not available'''
        time_now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        
        return time_now
   

def read_db_user_type_table_row_from_file(cfg):
    db_user_type_table_RowFile = cfg['db_user_type_table_records_file']
    count = 0    
    
    for dbrow in open(db_user_type_table_RowFile) :
        
        if count == 0:
            #print "First row is DB column header"
            dbTableHeader = dbrow.rstrip('\n')
            headerList = dbTableHeader.split(',')
            #print headerList
            
        elif count >= 1:
            dbTableRow = dbrow.rstrip('\n')
            rowData = dbTableRow.split(',')
            #print  rowData
            #parse_row_each_data(rowData)
            isExist = verify_row_exists_in_user_type_table(rowData[0])
            if (isExist == 0):
                insert_data_to_user_type_table(rowData)
                #print "Record will be inserted"
            else:
                print ("Record already exists with USERTYPEID: %s")%(rowData[0])
                pass
        else:
            pass
            
        count += 1


#------------------------------------------------------------------------------------
def verify_row_exists_in_user_type_table(usertypeid):
        
    dbutil = DbUtil()
    con = dbutil.getMySQLConnection()
    cursor = con.cursor()

    try:
        sql = ("SELECT * FROM user_type_table where usertypeid=%s")%(usertypeid)
        cursor.execute(sql)
        
        '''Fetch one of the rows '''
        results = cursor.fetchone()
        if results > 0:
            found = 1
        else:
            found = 0
            
    except MySQLdb.Error, e:
        print "Error: unable to fetch data %s",e
        found =0
        
    finally:
        cursor.close()
        con.close()
    
    return found;

#------------------------------------------------------------------------------------
def insert_data_to_user_type_table(rowData):
    ''''USERTYPEID   = rowData[0] 
    USERTYPENAME = rowData[1]
    PROPERTIES   = rowData[2]
    DESCRIPTION  = rowData[3]
    ISDEFAULT    = rowData[4]
    STATEENABLED = rowData[5]'''
    
    
    insert_query = ("""insert into `javadb`.`user_type_table` values(%s,'%s',%s,'%s',%s,
%s)""") %(rowData[0],rowData[1],rowData[2],rowData[3],rowData[4],rowData[5])

    
    insert_row(insert_query,rowData[0])
    print "**** INSERTION TO USER_TYPE_TABLE IS DONE *********"

    
#--------------------------------def main() call----------------------------------------------------        
'''From here Program execution starts'''    
if __name__ == "__main__":
    main()
