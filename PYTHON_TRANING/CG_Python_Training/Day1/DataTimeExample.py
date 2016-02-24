#Date and Time example
import time
print time.localtime()
(year,mon,day,hour,minute,sec,wd,yd,dst) = time.localtime()

print "Year is %d Month is %d Day is %d"%(year,mon,day)
print "Hour is %d Minute is %d Sec is %d"%(hour,minute,sec)
