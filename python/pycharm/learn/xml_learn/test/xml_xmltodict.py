import xmltodict
from collections import OrderedDict

with open('sample.xml', 'r+', encoding='utf-8') as fp:
    #将xml文件转换成dict,默认是返回OrderedDict。其中，fp.read()返回的是str
    root = xmltodict.parse(fp.read(), dict_constructor=dict)
    print(root)
    sample = root['root']
    sample['items']['item'][0]['amount'] = 200
    if not sample['items']['item'][0]['owner']:
        sample['items']['item'][0]['owner'] = 'alice'
    sample['items']['item'][0]['update_at'] = '2019-04-13T14:23:53.193Z'
    sample['items']['item'] = list(filter(lambda x: x, sample['items']['item']))
    sample['items']['item'].append({"name": "pen", "price": 1.2})
#将改动写回到xml文件中
'''当打开文件后，首先用read（）对文件的内容读取，然后再用write（）写入，这时发现虽然是用“r+”模式打开，按道理是应该覆盖的，但是却出现了追加的情况。
这是因为在使用read后，文档的指针已经指向了文本最后，而write写入的时候是以指针为起始，因此就产生了追加的效果。
如果想要覆盖，需要先seek（0），然后使用truncate()清除后，即可实现重新覆盖写入'''
    # fp.seek(0)  # 指针定位到第0个字节前
    # fp.truncate()  # 从第0个字节以后的内容全部删除了
#     fp.write(xmltodict.unparse(root, pretty=True))


# with open('sample.xml', 'r+', encoding='utf-8') as fp:
#     #将xml文件转换成OrderedDict
#     root = xmltodict.parse(fp.read())
#     print(root)
#     sample = root['root']
#     sample['items']['item'][0]['amount'] = 200
#     if not sample['items']['item'][0]['owner']:
#         sample['items']['item'][0]['owner'] = 'alice'
#     sample['items']['item'][0]['update_at'] = '2019-04-13T14:23:53.193Z'
#     sample['items']['item'] = list(filter(lambda x: x, sample['items']['item']))
#     sample['items']['item'].append({"name": "pen", "price": 1.2})
#     # 将改动写回到xml文件中
#     '''当打开文件后，首先用read（）对文件的内容读取，然后再用write（）写入，这时发现虽然是用“r+”模式打开，按道理是应该覆盖的，但是却出现了追加的情况。
#     这是因为在使用read后，文档的指针已经指向了文本最后，而write写入的时候是以指针为起始，因此就产生了追加的效果。
#     如果想要覆盖，需要先seek（0），然后使用truncate()清除后，即可实现重新覆盖写入'''
#     fp.seek(0)      #指针定位到第0个字节前
#     fp.truncate()  # 从第0个字节以后的内容全部删除了
#     fp.write(xmltodict.unparse(root, pretty=True))





# #xmltodict包中使用#text来访问节点的text，使用 @属性名 访问节点属性，使用子节点名称（标签）访问子节点
# mydict = {
#     'text': {
#         '@color':'red',
#         '@stroke':'2',
#         '#text':'This is a test'
#         }
#     }
#pretty=True,加换行
# print(xmltodict.unparse(mydict, pretty=True))