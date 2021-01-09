import thread
import time

def show(name,delay):
    for i in range(5):

        print('this is ',name, 'thread')
        time.sleep(delay)
t1=thread.start_new_thread(show,("thread 1", 1))
