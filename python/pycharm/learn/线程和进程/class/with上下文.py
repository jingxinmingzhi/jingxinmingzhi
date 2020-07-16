with open(r'd.txt','a+') as f:
    b='efwwegeh3h'
    a=list(b)
    f.writelines(a)
    f.close()
with open(r'd.txt','r',encoding='utf-8') as f:
    for i in f:
        print(i,end="")

