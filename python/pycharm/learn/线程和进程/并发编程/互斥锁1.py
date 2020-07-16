#同一个进程中的所有线程共享全局变量
import time
from threading import *
#定义全局变量
num=10
#创建一把互斥锁
mutex=Lock()
def test1():
    global  num
    for i in range(100000):
        mutex.acquire()  # 上锁
        num+=1
        mutex.release()  # 释放锁
    print('num的值为：',num)

def test2():
    global  num

    for i in range(100000):
        mutex.acquire()  # 上锁
        num+=1
        mutex.release()  # 释放锁
    print('num的值为：',num)

if __name__=='__main__':
    t1=Thread(target=test1)
    t2=Thread(target=test2)
    time1=time.time()      #返回当前时间时间戳，从1970开始计算浮点秒数
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print((time.time())-(time1))
