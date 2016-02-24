'''
Created on Feb 16, 2016

@author: sumkuma2
'''

# A sample code for user login Password attempt validation
login_attempt_count = 1
valid_pwd ='sumkuma2'
username = raw_input("Enter username :")

#Validating user password for max 3 valid login attempt
while (login_attempt_count <= 3):
        
    pwd = raw_input("Enter password :")
    
    if (pwd == valid_pwd):
        #print "Password %s is matched for USERNAME: %s"%(pwd,username)
        print "Login SUCCESSFUL for USERNAME: %s"%(username)
        break;
    
    else:
        attempt_left = (3 - login_attempt_count)
        
        if(attempt_left > 0):
            print "Invalid password, you have %d attempt left "%(attempt_left)
        #else:
            #print " '%s' Your account has been blocked..contact admin..!"%(username)
            
        login_attempt_count = login_attempt_count + 1
else:
    print " '%s' you have %d unsuccessful attempt of login "%(username,login_attempt_count-1)
    print " Your account has been blocked..contact admin..!"