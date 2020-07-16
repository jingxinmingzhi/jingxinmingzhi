import copy
a=[10,20,[5,6]]
b=copy.copy(a)
b.append(30)
b[1]=10
print(b)
print(a)