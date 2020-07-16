# _*_ coding:utf-8 _*_
__metaclass__=type
class A:
    def __init__(self):
        print(self)
        self.flag=1
    def write(self):
        if self.flag==1:
            self.flag=0
            print('Write file success')
        else:
            print('Write file fail')
class B(A):
    def __init__(self):
        print(self)
        A.__init__(self)
        self.s='Test case for class B'
    def output(self):
        print(self.s)

testB=B()