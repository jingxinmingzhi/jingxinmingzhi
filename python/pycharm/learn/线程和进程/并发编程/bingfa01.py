import multiprocessing
import time
def work(interval):
    for i in range(1,3):
        print('执行工作{}'.format(time.ctime()))
        time.sleep(interval)
        print('工作完成{}'.format(time.ctime()))
if __name__=='__main__':
    p=multiprocessing.Process(target=work,args=(4,))    #创建子进程
    p.start()
    p.join()
    print(p.pid)
    print(p.name)
    print(p.is_alive())