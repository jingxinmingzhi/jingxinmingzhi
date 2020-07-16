#析构方法
class person:
    def __del__(self):
        print('清除{0}'.format(self))
p1=person()
p2=person()
print('程序结束')