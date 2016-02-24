import threading
import time
import logging

#setting the log of thread status
logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s](%(threadName)-10s) %(message)s',)


def consumer(cond):
    """wait for the condition and use the resource"""
    logging.debug('Starting consumer thread')
    with cond:
        cond.wait()
        logging.debug('Resource is being consumed by Consumer')

def producer(cond):
    """Set up the resource to be used by the consumer"""
    logging.debug('starting the producer thread')
    with cond:
        logging.debug('Making resource available')
        cond.notifyAll()

condition = threading.Condition()
c1=threading.Thread(name='c1',target=consumer,args=(condition,))
c2 = threading.Thread(name='c2',target=consumer,args=(condition,))
p =threading.Thread(name='p',target=producer,args=(condition,))
c1.start()
time.sleep(2)
c2.start()
time.sleep(2)
p.start()
