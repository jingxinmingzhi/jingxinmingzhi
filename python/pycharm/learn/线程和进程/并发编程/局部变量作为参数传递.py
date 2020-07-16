import threading
def process_student(name):
    student_name=name
    print('线程名：%s 学生名：%s '%(threading.current_thread().name,student_name))
def process_thread(name):
    process_student(name)
t1=threading.Thread(target=process_thread,args=('张三',),name='Thread-1')
t2=threading.Thread(target=process_thread,args=('李四',),name='Thread-2')
t1.start()
t2.start()
t1.join()
t2.join()