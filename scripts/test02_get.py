# 1. 导包
import requests

# 2. 调用get方法  提示:调用get方法后返回的是响应对象
# 需求1
url1 = "http://www.baidu.com"

# 需求2
data1 = {"name": "李思思"}
# r 为响应对象
r = requests.get(url=url1, params=data1)
# 3.获取状态码
print("状态码为:", r.status_code)
# 4. 获取响应数据

# 5. 查看url
print(r.url)
# 6. 设置响应编码
print(r.encoding)
# 7. 设置编码
r.encoding = "utf-8"
print(r.text)

