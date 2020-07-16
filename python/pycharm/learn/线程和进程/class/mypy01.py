#打印九九乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        print('{0}*{1}={2}'.format(i,j,i*j),end='\t')
    print()
#使用列表和字典存储表格和数据

r1=dict(name='vgh',age=17,salary=30000,city='beijing')
r2=dict(name='ghj',age=17,salary=20000,city='beijing')
r3=dict(name='mnn',age=17,salary=15000,city='beijing')
r=[r1,r2,r3]
for i in r:
    if i.get('salary', 0)>18000:
        print(i)
'''
s='yftydtydtrxdgsdfsdgr'
a={a:s.count(a) for a in s }
print(a)
y=[x*2 for x in range(1,10) if x>2]
print(y)
y={x*2 for x in range(1,10) if x>2}
print(y)
y=(x*2 for x in range(1,10) if x>2)
print(y)
print(tuple(y))
print(tuple(y))