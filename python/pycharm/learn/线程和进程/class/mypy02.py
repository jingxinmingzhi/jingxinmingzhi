def jiecheng(n):
    if n==1:return 1
    else:
        return n*jiecheng(n-1)
for i in range(1,10):
    print(i,'!=',jiecheng(i))
