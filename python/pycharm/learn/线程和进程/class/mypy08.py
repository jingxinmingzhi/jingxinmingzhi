class animal:
    def shout(self):
        print('动物叫了一声')

class dog:
    def shout(self):
        print('小狗，汪汪汪')


class cat:
    def shout(self):
        print('小猫，喵喵喵')
'''def animalshou(a):
    if isinstance(a,animal):
        a.shout()'''
def animalshou(a):
    a.shout()
animalshou(cat())

