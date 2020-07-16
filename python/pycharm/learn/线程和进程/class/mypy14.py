class student:
    company='saic'
    count=0
    def __init__(a,name,age):
        a.name=name
        a.age=age
        student.count +=1
    def say_age(self):
       print(self.age)
s1=student('sdfg',18)
student.say_age(s1)
print(student.count)