import threading
import logging
import time

#setting the log of thread status
logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s](%(threadName)-10s) %(message)s',)


def daemon():
    logging.debug('starting')
    time.sleep(2)
    logging.debug('Exiting')

d = threading.Thread(name='daemon',target=daemon)
#d.setDaemon(True)
d.setDaemon(False)

def non_daemon():
    #print (threading.currentThread().getName(),'Starting')
    logging.debug('starting')
    logging.debug('Exiting')

t=threading.Thread(name='non_daemon',target=non_daemon)


d.start()
t.start()
d.join(1) #1 seconds
print 'd.isAlive()',d.isAlive()
t.join()
print 'd.isAlive()',d.isAlive()

