import xml.dom.minidom


def TestAddElement():
    doc = xml.dom.minidom.parse("book.xml")
    root = doc.documentElement
    item = doc.createElement("图书")
    item1 = doc.createElement("书名")
    text = doc.createTextNode("Python入门帮助")
    item1.appendChild(text)
    item2 = doc.createElement("作者")
    text = doc.createTextNode("陈锐")
    item2.appendChild(text)
    item3 = doc.createElement("价格")
    text = doc.createTextNode("42.5")
    item3.appendChild(text)
    text = doc.createTextNode("\n        ")
    item.appendChild(text)
    item.appendChild(item1)
    text = doc.createTextNode("\n        ")
    item.appendChild(text)
    item.appendChild(item2)
    text = doc.createTextNode("\n        ")
    item.appendChild(text)
    item.appendChild(item3)
    text = doc.createTextNode("\n    ")
    item.appendChild(text)

    text = doc.createTextNode("    ")
    root.appendChild(text)
    root.appendChild(item)
    text = doc.createTextNode("\n")
    root.appendChild(text)
    print(root.toxml())
    return doc


dom = TestAddElement()

try:
    with open('book.xml', 'w', encoding='UTF-8') as fh:
        # dom.writexml()第一个参数是目标文件对象，第二个参数是根节点的缩进格式，第三个参数是其他子节点的缩进格式，
        # 第四个参数制定了换行格式，第五个参数制定了xml内容的编码。
        dom.writexml(fh, indent='', addindent='', newl='', encoding='UTF-8')
        print('写入xml OK!')
except Exception as err:
    print('错误信息：{0}'.format(err))