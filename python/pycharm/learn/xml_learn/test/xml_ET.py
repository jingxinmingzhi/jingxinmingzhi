import xml.etree.ElementTree as ET

import xmltodict

tree = ET.parse('D:/Study/PythonCharm/PycharmProjects/learn/xml_learn/test/sample.xml')
root = tree.getroot()


for node in root:                                             #items
    for child_node in node:                                   #item
        if child_node.text != None:                           #item不为空
            if child_node.find('name').text == 'book':
                child_node.find('owner').text = 'alice'
                child_node.find('amount').text = '200'
                child_node.find('update_at').text = '2019-04-13T14:23:53.193Z'

#构造xml节点
new_item = ET.SubElement(root.find('items'), "item")
name = ET.SubElement(new_item, "name")
name.text = "pen"

price = ET.SubElement(new_item, "price")
price.text = '1.2'


def pretty_xml(element, indent, newline, level=0):  # elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行
    if element:  # 判断element是否有子元素
        if (element.text is None) or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
            # else:  # 此处两行如果把注释去掉，Element的text也会另起一行
            # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    temp = list(element)  # 将element转成list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
            subelement.tail = newline + indent * level
        pretty_xml(subelement, indent, newline, level=level + 1)  # 对子元素进行递归操作


pretty_xml(root, '\t', '\n',level = 0)  # 执行美化方法
#element
print(len(root[1]))
print(dir(tree))

#显示到终端
# ET.dump(root)
#ElementTree似乎没有默认的prettyprinter
tree.write('D:/Study/PythonCharm/PycharmProjects/learn/xml_learn/test/sample.xml',encoding='utf-8',xml_declaration=True)
#
# with open ('D:/Study/PythonCharm/PycharmProjects/learn/xml_learn/test/sample.xml',encoding='utf-8') as xml:
#     xml_str = xmltodict.parse(xml.read())
#     print(xml_str)