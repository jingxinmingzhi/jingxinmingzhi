try:
    f=open('d:/a.txt','r')
    content=f.readline()
    print(content)
except:
    print('文件未找到')
finally:
    f.close()
