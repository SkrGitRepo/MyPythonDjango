'''
Created on Feb 26, 2016

@author: sumkuma2
'''
def main(myfile):
    ''' This is a file reader'''
    fob=open(myfile,'r')
    print fob.read(3) #to read first 3 bytes
    fob.close()
    
    
    fob=open(myfile,'r')
    print fob.read() #if empty read() it read all content/lines of the file at once
    fob.close()
    
    

if __name__ == "__main__":
    filename ="readme.txt"
    main(filename)

    