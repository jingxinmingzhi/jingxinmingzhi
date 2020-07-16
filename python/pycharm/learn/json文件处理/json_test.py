import json

# test_dict = {"bigberg": [7600, {1: [['iPhone', 6300], ['Bike', 800], ['shirt', 300]]}]}
# print(type(test_dict["bigberg"][1][1][0][1]))
# print(test_dict)
# print(type(test_dict))
# #dumps 将数据转换成字符串
# json_str = json.dumps(test_dict)
# # print(type(json_str["bigberg"][1][1][0][1]))
# print((json_str[0]))
# print(json_str)
# print(type(json_str))


with open ("D:/untitled1/venv/json文件处理/sample.json",'r+',encoding = "utf-8") as j:
    # global a
    a = json.load(j)
    # print(type(a["items"][1]))
    for dict in a['items']:
        if dict != None:
            if 'name' in dict and dict["name"] == 'book':
                dict['amount'] = 200
                dict["owner"] = "alice"
                dict["update_at"] = '2019-04-13T14:23:53.193Z'
        else:
            a["items"].remove(dict)
    a['items'].append({"name": "pen", "price": 1.2})
    print(a)
    j.seek(0)
    b = json.dump(a,j,ensure_ascii=False,indent=4)





