#使用工厂产品类
class Person(object):
    def __init__(self,name):
        self.name=name
    def work(self,axe_type):
        print('开始工作')
        #根据需要的斧头类型通过工厂模式获取斧头
        axe=Factory.create_axe(axe_type)
        axe.cut_tree()

class Axe(object):
    def __init__(self,name):
        self.name=name
        print(name)
    def cut_tree(self):
        print('%s砍树',self.name)
#工厂具体产品1
class StoneAxe(Axe):
    def cut_tree(self):
        print('石斧砍树')
#工厂具体产品2
class SteelAxe(Axe):
    def __init__(self,name):
        # super().__init__(name)
        self.name=name
    def cut_tree(self):
        print('铁斧砍树')
#工厂模式类，根据不同情况，提供不同解决方法
class Factory(object):
    #根据用户指定类型来生产
    @staticmethod
    def create_axe(type):
        if type=='stone':
            return StoneAxe('石头')
        elif type=='steel':
            return SteelAxe('铁')
p=Person('ll')
p.work('steel')