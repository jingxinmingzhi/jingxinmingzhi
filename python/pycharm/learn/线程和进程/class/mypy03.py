def RECUR():
    m=input('请输入recur函数的参数')
    n = int(m)
    def recur(n):
        if n==1:return 1/2
        else:
            return n/(n+1)+recur(n-1)
    print("recur({0})={1}".format(n,recur(n)))
RECUR()