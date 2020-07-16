from lxml import html
text='xxx'#测试的html文本
etree = html.etree
annotation = etree.Element("annotation")
etree.SubElement(annotation, "folder").text = "VOC2014_instance"
etree.SubElement(annotation, "filename").text = "test.jpg"
source = etree.SubElement(annotation, "source")
etree.SubElement(source, "database").text = "COCO"
etree.SubElement(source, "annotation").text = "COCO"
etree.SubElement(source, "image").text = "COCO"
etree.SubElement(source, "url").text = "http://test.jpg"
size = etree.SubElement(annotation, "size")
etree.SubElement(size, "width").text ='800'  # 必须用string
etree.SubElement(size, "height").text = '600'
etree.SubElement(size, "depth").text = '3'
etree.SubElement(annotation, "segmented").text = '0'
key_object = etree.SubElement(annotation, "object")
etree.SubElement(key_object, "name").text = 'person'
bndbox = etree.SubElement(key_object, "bndbox")
etree.SubElement(bndbox, "xmin").text = str(100)
etree.SubElement(bndbox, "ymin").text = str(200)
etree.SubElement(bndbox, "xmax").text = str(300)
etree.SubElement(bndbox, "ymax").text = str(400)
etree.SubElement(key_object, "difficult").text = '0'
doc = etree.ElementTree(annotation)
print(doc)

doc.write(open("test.xml", "w"), pretty_print=True)





