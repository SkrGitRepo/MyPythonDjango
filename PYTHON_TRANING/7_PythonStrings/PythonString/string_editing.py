'''
Created on Feb 4, 2016

@author: sumkuma2
'''


class MyString():
    
    def reverse(self,some_seq):
        """
            Input:     Sequence
            output:    Sequence:
                         reversed version
        """
        return some_seq[::-1]
    
    def is_palindrom(self,some_seq):
        """
            @param some_seq: sequence of anything
            @return:         Boolean:
                        palindrome check of sequence passed 
        """
        return some_seq == self.reverse(some_seq)
        
        

#if __name__ == '__main__':
    
X = MyString()
string = "a barbie vanquished the knights of the round table by hitting them in the face"
print(X.reverse(string));

number='11011'

ispalindrom = X.is_palindrom(number);
if (ispalindrom == False):
    print "Not a Palindrom"
else:
    print "Palindrom"
    