#测试私有属性
class Employee:
    __company='saic'
    def __init__(self,name,age):
        self.name=name
        self.__age=age  #私有属性
    def __work(self):
        print('好好工作')
e=Employee('lhp',25)
print(e.name)
print(e._Employee__age)   #打印私有属性
print(e._Employee__work())   #调用私有方法
print(e._Employee__company)
print(dir(e))    #获取对象的所有属性、方法

