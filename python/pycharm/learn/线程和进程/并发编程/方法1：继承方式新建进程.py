from multiprocessing import Process
import time
class ClockProcess(Process):
    #重写初始化方法
    def __init__(self,a):
        super().__init__(target=a)
        #Process.__init__(self)
        #self.interval=interval
    #重写run方法
def run(interval):
        print('子进程开始执行{}'.format(time.ctime()))
        time.sleep(interval)
        print('子进程结束执行{}'.format(time.ctime()))
if __name__=='__main__':
    p=ClockProcess(run(3))
    p.start()    #调用run方法
    p.join()
    print('主进程结束')


