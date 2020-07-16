from multiprocessing import Process,Queue,Pool,Manager
import time
#定义进程执行函数
def write(q):
    a=['a','b','c','d']
    for i in a:
        print('开始写入的值:%s'%i)
        q.put(i)
def read(q):
   for i in range(q.qsize()):
       print('开始读入的值:%s'%(q.get()))
if __name__=='__main__':
    #创建初始化进程池
    pool=Pool(3)
    q = Manager().Queue()
    pool.apply(write,(q,))
    pool.apply(read, (q,))
    pool.close()
    pool.join()
