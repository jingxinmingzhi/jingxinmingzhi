# -*- coding: utf-8 -*-
"""
    @Author  : LiuZhian
    @Time    : 2019/4/24 0024 上午 9:19
    @Comment :
"""
from xml.dom.minidom import parse
def readXML():
    domTree = parse("./customer.xml")
    # 文档根元素
    rootNode = domTree.documentElement
    print(rootNode.nodeName)

    # 所有顾客
    customers = rootNode.getElementsByTagName("customer")
    print("****所有顾客信息****")
    for customer in customers:
        if customer.hasAttribute("ID"):
            print("ID:", customer.getAttribute("ID"))
            # name 元素
            name = customer.getElementsByTagName("name")[0]
            print(name.nodeName, ":", name.childNodes[0].data)
            # phone 元素
            phone = customer.getElementsByTagName("phone")[0]
            print(phone.nodeName, ":", phone.childNodes[0].data)
            # comments 元素
            comments = customer.getElementsByTagName("comments")[0]
            print(comments.nodeName, ":", comments.childNodes[0].data)

if __name__ == '__main__':
    readXML()
