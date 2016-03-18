import re
dir(re)
pattern =re.compile('aa?') #?matched 0 or 1 occurence of preceedding char
m=pattern.match('aa')
print  m.group()
print m.span()

pattern =re.compile('aa*') #*:Matches 0 or more occurrences of preceding expression
m=pattern.match('aaa')
print  m.group()
print m.span()


pattern =re.compile('aa+') #+:Matches 1 or more occurrence of preceding expression.
m=pattern.match('aaa')
print  m.group()
print m.span()



pattern =re.compile('aaa{3}') # re{n} : Matches exactly n number of occurrences of preceding expression
m=pattern.match('aaaaa')
print  m.group()
print m.span()


line = "Cats are smarter than dogs";
matchObj = re.match( r'dogs', line, re.M|re.I)
if matchObj:
    print "match --> matchObj.group() : ",matchObj.group()
else:
    print "No match!!"


line2 = "Mailer 'cpo-prod-networkadmin' not found"
matchObj = re.match( r'not found', line2, re.M|re.I)
if matchObj:
    print "****** match --> matchObj.group() : ",matchObj.group()
else:
    print "***** No match!!"

pattern =re.compile('not found') #+:Matches 1 or more occurrence of preceding expression.
m=pattern.search(line2)
if m:
    print m.group()
    print "result found"
    #print m.span()
else :
    "no search result"
    
print "------------------------------------------"




pattern =re.compile('\d{10}') #+:Matches 1 or more occurrence of preceding expression.
m=pattern.match('Mobile 9844816548 email sumit@gmail.com 8861733377 skr@gmail.com')
print m.group()
print m.span()

pattern =re.compile('\d{10}') #+:Matches 1 or more occurrence of preceding expression.
m=pattern.search('Mobile 9844816548 email sumit@gmail.com 8861733377 skr@gmail.com')
print m.group()
print m.span()


