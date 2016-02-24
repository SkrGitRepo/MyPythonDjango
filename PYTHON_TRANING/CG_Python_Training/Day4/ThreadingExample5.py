import threading
import random
import time
import logging

#setting the log of thread status
logging.basicConfig(level=logging.DEBUG,format='[%(levelname)s](%(threadName)-10s) %(message)s',)

def worker():
    """Thread worker function"""
    t= threading.currentThread()
    pause = random.randint(1,5)
    logging.debug('sleeping %s',pause)
    time.sleep(pause)
    logging.debug('ending')
    return
for i in range(3):
    t= threading.Thread(target=worker)
    t.setDaemon(True)
    t.start()
    main_thread = threading.currentThread()
for t in threading.enumerate(): #enumerate: to syschronize thread
    if t is main_thread:
        continue
    logging.debug('joninig %s',t.getName())
    t.join()
    



print help(threadin.enumerate())
