import _thread
import time
def fun1(tread_name,delay):
    print('开始运行fun1,线程的名字：',tread_name)
    time.sleep(delay)
    print('fun1结束运行')
def fun2(tread_name,delay):
    print('开始运行fun2,线程的名字：',tread_name)
    time.sleep(delay)
    print('fun2结束运行')
if __name__=='__main__':
    print('开始运行')
    _thread.start_new_thread(fun1,('thread-1',2))
    _thread.start_new_thread(fun2, ('thread-2', 3))