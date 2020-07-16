#测试@property
class Person:
    __company='saic'

    def __init__(self,name,age):
        self.name=name
        self.__age=age  #私有属性
    @property
    def age(self):  
        print(self.__age)
    @age.setter
    def age(self,age):
        if 0<age<120:
            self.__age=age
        else:
            print('年龄输入范围在0-120之间')

p=Person('lhp',25)
#print(e.name)
#print(e._Employee__age)   #打印私有属性
#print(e._Employee__work())   #调用私有方法
print(p.age)      #测试@property,调用函数时不需要加后面的括号
p.age=10
print(p.age)
#print(e._Employee__company)
#print(dir(e))    #获取对象的所有属性、方法