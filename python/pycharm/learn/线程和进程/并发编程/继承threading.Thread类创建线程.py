import threading
import time
def fun1(delay):
    print('线程{}开始运行'.format(threading.current_thread().getName()))
    time.sleep(delay)
    print('线程{}结束运行'.format(threading.current_thread().getName()))
def fun2(delay):
    print('线程{}开始运行'.format(threading.current_thread().getName()))
    time.sleep(delay)
    print('线程{}结束运行'.format(threading.current_thread().getName()))
class MyThread(threading.Thread):
    #重写父类的构造方法
    def __init__(self,func,name,args):
        super().__init__(target=func,name=name,args=args)
        #threading.Thread.__init__(self,target=func,name=name,args=args)
#    def run(self):
#      self._target(*self._args)     #*param(一个星号)将多个参数收集到一个“元组”对象中
if __name__=='__main__':
    print('正在运行')
    t1=MyThread(fun1,'thread-1',(2,))
    t2 = MyThread(fun1, 'thread-2', (3,))
    t1.start()
    t2.start()