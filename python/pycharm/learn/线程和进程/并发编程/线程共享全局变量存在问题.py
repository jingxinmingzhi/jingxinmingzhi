#同一个进程中的所有线程共享全局变量
import time
from threading import *
#定义全局变量
num=10
def test1():
    global  num
    for i in range(100000):
        num+=1
    print('num的值为：',num)
def test2():
    global  num
    for i in range(100000):
        num+=1
    print('num的值为：',num)
if __name__=='__main__':
    t1=Thread(target=test1)              #两个线程同时修改变量num造成混乱
    t2=Thread(target=test2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
