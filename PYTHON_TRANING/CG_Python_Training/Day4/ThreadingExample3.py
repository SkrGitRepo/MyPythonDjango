import threading
import logging
import time

#setting the log of thread status
logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s](%(threadName)-10s) %(message)s',)

def worker():
    logging.debug('starting')
    #print (threading.currentThread().getName(),'Starting')
    time.sleep(2)
    logging.debug('Exiting')
    #print (threading.currentThread().getName(),'Exiting')
    

def my_service():
    #print (threading.currentThread().getName(),'Starting')
    logging.debug('starting')
    time.sleep(3)
    logging.debug('Exiting')
    #print (threading.currentThread().getName(),'Exiting')


t=threading.Thread(name='my_service', target=my_service)
w=threading.Thread(name='worker', target=worker)
w2=threading.Thread(target=worker)


w.start()
w2.start()
t.start()
