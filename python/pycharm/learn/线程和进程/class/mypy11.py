try:
    a=3/0
except BaseException as e:
    print('除数不能是0')
    print(e)