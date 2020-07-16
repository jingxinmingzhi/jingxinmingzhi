# class A:
#     def m(self):
#         print('A')
#
#
# class B:
#     def m(self):
#         print('B')
#
#
# class C(A):
#     def m(self):
#         print('C')
#         super().m()       #找父类，MRO---Method Resolution Order
#
#
# C().m()

class Foo(object):
    def x(self):
        print('Foo',self)
        print ('Foo')

class Foo2(Foo):
    def x(self):
        print('Foo2')
        print('Foo2',self)
        # super(self.__class__, self).x() # wrong  #因为self为<__main__.Foo3 object at 0x000001BA8764FCC8>，所以一直重复在找Foo3的父类
        print('__class__',__class__)
        print('self.__class__',self.__class__)
        super(Foo2, self).x()

class Foo3(Foo2):
    def x(self):
        print ('Foo3')
        print('Foo3',self)
        super(Foo3, self).x()

f = Foo3()
f.x()
