'''
Created on Feb 14, 2016

@author: sumkuma2
'''
import sys,getopt


def main(argv):
    
    inputfile=''
    outputfile=''

    try:
        (opts, args) = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'Usage :: test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)
    
    for opt,arg in opts:
        if (opt == '-h'):
            print 'HELP :: python Ex3.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif (opt in ("-i" ,"--ifile")):
            inputfile = arg
        elif (opt in ("-o","--ofile")):
            outputfile = arg
    
    print "\n Input file is :",inputfile
    print "\n Output file is :",outputfile
                
                
if __name__ == "__main__":
    main(sys.argv[1:])   
    
'''
EXECUTION:::::
 $ python Ex3.py -h
usage: Ex3.py -i <inputfile> -o <outputfile>
$ python Ex3.py -i BMP -o
usage: Ex3.py -i <inputfile> -o <outputfile>
$ python Ex3.py -i BMP
Input file is : BMP
$ python Ex3.py -i BMP -o JPG
 Input file is : BMP
 Output file is : JPG
$ python Ex3.py --ifile="BMP" --ofile="JPG"
 Input file is : BMP
 Output file is : JPG
'''      
    