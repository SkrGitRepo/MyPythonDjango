import unittest
def fun(x):
    return x+1
def add(a,b):
    return a+b


class A:
    def __init__(self,age):
        self.a=45
    def display(self):
        return self.a


class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3),4)
    def testAdd(self):
        self.assertEqual(add(3,4),5) #this will fail
    def testB(self):
        self.assertEqual(A(45).display(),45)

unittest.main()

#to run use command prompt
#python TestCase1.py -v
'''
OUTPUT:
======================
c:\Python_Training\Day3>python Testcase1.py -v
test (__main__.MyTest) ... ok
testAdd (__main__.MyTest) ... FAIL
testB (__main__.MyTest) ... ok

======================================================================
FAIL: testAdd (__main__.MyTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "Testcase1.py", line 19, in testAdd
    self.assertEqual(add(3,4),5)
AssertionError: 7 != 5

----------------------------------------------------------------------
Ran 3 tests in 0.002s

FAILED (failures=1)
=================================================================
'''
