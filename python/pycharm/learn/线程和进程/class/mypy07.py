class person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    def say_age(self):
        print(self.name,'年龄是：',self.__age)
        #print(self.name)
class student(person):
    def __init__(self,name,age,score):
        self.score=score
        person.__init__(self,name,age)
    def say_age(self):
        print('名字是',self.name,'年龄是', self._person__age)
        #print('名字是', self.name)
# s1=student('张三',17,80)
s1=student()
s1.say_age()
print(s1)
print(dir(s1))
print(student.mro())
print(student.__bases__)
#print(s1._person__age)
type(s1._person__age)
type(s1.name)




