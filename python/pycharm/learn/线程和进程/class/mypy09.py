a,b=4,3
if True:
    print('{0}'.format(a or b))    # or中， 至少有一个非0时，返回第一个非0；C语言中，a,b只要有一个数大于0，a||b为1
    print('{0}'.format(a and b))   #and中含0，返回0； 均为非0时，返回后一个值；C语言中，a,b全大于0，a&&b为1
    print('{0}'.format(a | b))     #按位或；C语言中，a|b为7
    print('{0}'.format(a & b))     #按位与；C语言中，a&b为7
