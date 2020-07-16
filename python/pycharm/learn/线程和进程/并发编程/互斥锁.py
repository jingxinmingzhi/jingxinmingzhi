#同一个进程中的所有线程共享全局变量
import time
from threading import *
#定义全局变量
num=10
#创建一把互斥锁
mutex=Lock()
def test1():
    mutex.acquire()  # 上锁
    global num
    for i in range(100000):
        num += 1
    print('num的值为：',num)
    mutex.release()  # 释放锁

def test2():
    mutex.acquire()  # 上锁
    global num
    for i in range(100000):
        num += 1
    print('num的值为：',num)
    mutex.release()  # 释放锁

if __name__=='__main__':
    t1=Thread(target=test1)
    t2=Thread(target=test2)
    time1=time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print((time.time())-(time1))
