class MyClass:
    def method(self):
        print('method called id(self)', id(self))
        # return 'instance method called',self
    @classmethod
    def classmethod(cls):
        print('class method called id(cls)', id(cls))
        # return 'class method called',cls

    @staticmethod
    def staticmethod():
        print('static method called')
        # return 'static method called'

#实例化MyClass
print('id(MyClass):,MyClass是一个模具，它是固定不变的',id(MyClass))
print('id(MyClass()):',id(MyClass()))
print('id(MyClass()):',id(MyClass()))
obj=MyClass()    #带()调用初始化构造方法，不带()只是替换作用

obj.method()        #相当于MyClass() .method(),解释器翻译成     MyClass.method(obj)
obj.classmethod()
obj.staticmethod()

# MyClass.method()      method() missing 1 required positional argument: 'self',因为类MyClass没有实例化
MyClass.method(obj)     #obj就是self
MyClass.classmethod()
MyClass.staticmethod()
