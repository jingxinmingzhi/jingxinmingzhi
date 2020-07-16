import threading
import time
def fun1(tread_name,delay):
    print('线程{0}开始运行'.format(tread_name))
    time.sleep(delay)
    print('线程{0}结束运行'.format(tread_name))

def fun2(tread_name, delay):
    print('线程{0}开始运行'.format(tread_name))
    time.sleep(delay)
    print('线程{0}结束运行'.format(tread_name))
if __name__=='__main__':
    t1=threading.Thread(target=fun1,args=('tread_1',3))
    t2 = threading.Thread(target=fun2, args=('tread_2', 4))
    t1.start()
    t2.start()
    t1.join()
    t2.join()