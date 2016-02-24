import fileinput
import re
import sys

#print dir(fileinput)

#pattern = re.compile(r'\b[\w.]+@\w+.\w{2,3}\b')
pattern = re.compile(sys.argv[1])
for line in fileinput.input(sys.argv[2:]):
    #textfilename = line.strip()
    #print textfilename
    m= pattern.search(line)
    if pattern.search(line):
        #print re.findall(r'\b[\w.]+@\w+.\w{2,3}\b',textfilename)
        fmt = '{filename:<20} : {lineno} : {line}'
        print fmt.format(filename=fileinput.filename(),
                         lineno=fileinput.filelineno(),
                         line=line.rstrip())
        print "Found email: ",m.group()
    
#print re.findall(r'\b[\w.]+@\w+.\w{2,3}\b',textfilename)





