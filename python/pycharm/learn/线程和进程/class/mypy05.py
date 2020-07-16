def transfer():
    t=input('请输入时间：')
    hour=lambda t:int(t)//(1000*3600)     #这里的t并不是上面的变量t
    minute=lambda t:(int(t)%(1000*3600))//(1000*60)
    second=eval('(int(t)%(1000*3600))%(1000*60)//(1000)')
#a=dict(hour=0,minute=0,second=0)
#print((a))
    print('hour:{0} minute:{1} second:{2}'.format(hour(t),minute(t),second))
transfer()