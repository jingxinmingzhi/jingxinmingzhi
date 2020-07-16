class student:
    def __init__(a,name,age):
        a.name=name
        a.age=age
    def say_age(self):
       print(self.age)
s1=student('sdfg',18)
#s1.say_age()
#student.say_age(s1)
class math:
    pass
#print(dir(math))
#print(dir(student))
#print(dir(s1))
#print(s1.__dir__())
print(isinstance(s1,math))