# 第1题
"""
函数能省去重复的代码，节省开发时间，让代码更简洁，增加阅读性
"""
# 第2题
def function(num):
    """ 函数的文档: 返回传入的参数"""
    return num
# 第3题
"""
传入一个参数，然后对他进行递推调用求出他的阶乘
"""
# 第4题
import math
from math import sqrt
from math import *
from math import sqrt as sq
# 第5题
def describe_pet(animal_type, pet_name):
    return [animal_type, pet_name]
print(describe_pet("cat","Whiskers" ))
print(describe_pet(pet_name="Whiskers",animal_type="cat"))# 用键值对去调用就可以不看顺序

# 第6题
def greet_user(name, /, greeting="Hello"):
    return name
greet_user("Alice") # 合法
# greet_user(name="Bob") 不合法
greet_user("Carol", greeting="Hi") #合法
# 第7题
# *是关键字命名参数
def send_email(*, to_address, subject, body):
    return 0
send_email(to_address="test@example.com",subject="Meeting",body="See you at 3 PM.")
# 第8题
"""
默认值的参数在参数列表中必须放在不带默认值的参数后面
违反了会报错
"""
# 第9题
def print_all(*items):
    for item in items:
        print(item)
"""
收集多个位置参数，打包成一个元组
"""
# 第10题
def build_profile(**user_info):
    return user_info
"""
接收任意多个关键字参数，打包成一个字典 
"""
# 第11题
"""
from module_a.py import calculate as calc
"""
# 第12题
from math import factorial as fact
"""
这条语句从math库导入factorial函数，取别名叫fact
"""
print(fact(10))
# 第13题
"""
标准库有:math,time等
内置函数有get(),min(),max()等
"""
# 第14题
"""
None
"""
# 第15题
"""
一个车有四个轮子，发明一个轮子就能直接做出四个
不用再多发明
函数能省去重复的代码，把很多自己写的函数（模板）封装到一个文件中，需要使用的话直接调用那个文件的函数就行
免去了大量重新定义函数，以及不使用函数，用大量代码堆叠的工作
"""
