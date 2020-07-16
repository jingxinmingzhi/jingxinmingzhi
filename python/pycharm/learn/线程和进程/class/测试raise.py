'''except BaseException as e:             #处理可能遗漏的异常
    print(e)
    print('An exception flew by!')
    #raise
try:
    raise NameError('HiThere')
except ValueError:
    print('值异常')
else:
    print('无异常')'''
import sys
print(sys.platform)
assert ('linux' in sys.platform)


