from multiprocessing import Process,Queue
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
    q=Queue()
    wr=Process(target=write,args=(q,))
    rd=Process(target=read,args=(q,))
    wr.start()
    wr.join()
    rd.start()
    rd.join()
