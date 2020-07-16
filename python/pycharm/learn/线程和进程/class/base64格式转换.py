import base64
url = 'cHM6'

str_url = base64.b64decode(url).decode("utf-8")
print((str_url))
print(type(str_url))
url = "https://www.jianshu.com/p/9b4ab709cffb"
bytes_url = url.encode("utf-8")
print(bytes_url)
str_url = base64.b64encode(bytes_url)  # 被编码的参数必须是二进制数据
print(str_url)

