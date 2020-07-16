#导入队列模块
from multiprocessing import Queue
#创建一个队列
q=Queue(3)  #可以指定队列的大小，如果不指定则默认队列是无限
#向队列中插入数据
q.put('消息1')
q.put('消息2')
q.put('消息3')
#put方法里面的可选参数
#q.put('消息4',block=True,timeout=1)
#判断队列是否已满
print('判断队列是否已满',q.full())
if not q.full():
    q.put('消息4', block=True, timeout=1)
print(q.get())
#print(q.get())
#print(q.get())
#if not q.empty():
#    print(q.get( block=True, timeout=1))

print('队列的大小',q.qsize())

