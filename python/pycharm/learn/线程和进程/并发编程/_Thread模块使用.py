import _thread
import time
def fun1():
    print('执行函数1')
    time.sleep(2)
    print('函数1结束运行')
def fun2():
    print('执行函数2')
    time.sleep(3)
    print('函数2结束运行')
if __name__=='__main__':
    print('开始运行')
    _thread.start_new_thread(fun1,())    #在线程1执行sleep函数时，释放CPU资源
    _thread.start_new_thread(fun2, ())
    time.sleep(8)
