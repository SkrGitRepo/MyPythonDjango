'''
Created on Feb 16, 2016

@author: sumkuma2
'''
count = 0
while (count < 9):
    print 'The count is:',count
    count = count+1


''' The else Statement Used with Loops 

Python supports to have an else statement associated with a loop statement.
-If the else statement is used with a for loop, the else statement is executed when the loop has exhausted
iterating the list.
-If the else statement is used with a while loop, the else statement is executed when the condition becomes
false.

'''
count = 0
while count < 5:
    print count, " is less than 5"
    count = count + 1
else:
    print count, " is not less than 5"
    
''' Single Statement Suites:
- Similar to the if statement syntax, if your while clause consists only of a single statement, it may be placed on the
same line as the while header. Here is the syntax and example of a one-line while clause:
'''
#This is an infinite loop example
#flag = 1 
#while (flag): print 'Given flag is really true!'
#print "Good bye!"
    