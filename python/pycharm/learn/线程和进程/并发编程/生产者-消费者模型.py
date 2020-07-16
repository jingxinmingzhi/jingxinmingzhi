import time
import threading
from queue import Queue

class Producer(threading.Thread):
    def run(self):
        global queue
        count=0
        while True:
            if queue.qsize()<1000:
                for i in range(101):
                    count+=1
                    msg='生成产品'+str(count)
                    queue.put(msg)
                    print(msg)
                time.sleep(1)
class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize()>100:
                for i in range(10):
                    msg=self.name+'消费了'+queue.get()[2:]
                    print(msg)
                #time.sleep(1)
if __name__=='__main__':
    queue = Queue()
    t1=Producer()
    t2=Consumer()
    t1.start()
    #time.sleep(1)
    t2.start()
    t1.join()
    t2.join()