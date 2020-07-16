import threading
#创建全局ThreadLocal对象
local=threading.local()
def process_student():
    #获取当前线程关联的name
    student_name=local.name
    print('线程名：%s 学生名：%s '%(threading.current_thread().name,student_name))
def process_thread(n):
    #绑定ThreadLocal的name：
    local.name=n
    process_student()
t1=threading.Thread(target=process_thread,args=('张三',),name='Thread-1')
t2=threading.Thread(target=process_thread,args=('李四',),name='Thread-2')
t1.start()
t2.start()
t1.join()
t2.join()
