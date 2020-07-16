from multiprocessing import Process
import time
num=10
def work1():
    global num
    num+=5
    print('子进程1运行后，num加5，num值为%d'%num)
def work2():
    global num
    num+=10
    print('子进程2运行后，num加5，num值为%d'%num)
if __name__=='__main__':
    print('主进程开始运行')
    p1=Process(target=work1)
    p2 = Process(target=work2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
