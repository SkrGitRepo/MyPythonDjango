
try:
    x=int(input("Enter some data:"))
except ValueError as ve:
    print " ValueError Exception occured :",ve
except KeyBoardInterrupt:
    print " KeyBoardInterrupt Exception occured "
except Exception as e:
    print "Exception occured :",e
else:
    print "No exceptions",x
        


while True:
    try:
        x=int(input("Enter some data:"))
    except ValueError as ve:
        print " ValueError Exception occured :",ve
        break
    except KeyBoardInterrupt:
        print " KeyBoardInterrupt Exception occured "
    except Exception as e:
        print "Exception occured :",e
    else:
        print "No exceptions",x
        


