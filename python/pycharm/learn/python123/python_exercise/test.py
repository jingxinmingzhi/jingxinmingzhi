import xmltodict

with open('sample.xml', 'r', encoding='utf-8') as fp:
    root = xmltodict.parse(fp.read(), dict_constructor=dict)

    sample = root['root']

    sample['items']['item'][0]['amount'] = 200
    if not sample['items']['item'][0]['owner']:
        sample['items']['item'][0]['owner'] = 'alice'

    sample['items']['item'][0]['update_at'] = '2019-04-13T14:23:53.193Z'

    sample['items']['item'] = list(filter(lambda x: x, sample['items']['item']))
    sample['items']['item'].append({"name": "pen", "price": 1.2})

print(xmltodict.unparse(root))