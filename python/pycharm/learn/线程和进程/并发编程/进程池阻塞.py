#apply()单进程
import multiprocessing
import time
#定义进程执行函数
def func(msg):
    print('start',msg)
    time.sleep(2)
    print('end', msg)
if __name__=='__main__':
    #创建初始化进程池
    pool=multiprocessing.Pool(3)
    for i in range(1,6):
        msg='任务%d'%i
        pool.apply(func,(msg,))       #当进程1结束才会执行进程2
    #如果进程池不再接收新的请求
    pool.close()
    pool.join()

