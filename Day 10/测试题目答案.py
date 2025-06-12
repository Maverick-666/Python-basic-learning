# 第1题
"""
key 必须满足的条件是可哈希类型，即不可变量
整数，元组（元组内元素也不可变）这两种可以
列表不可以
"""
# 第2题
dict1 = {'name': 'Bob', 'id': 101}
dict2 = dict(zip(['name','id'], ['Bob',101]))
dict3 = dict(name='Bob', id=101)
# 第3题
"""
会报错
会显示没找到，但不会报错
返回0
"""
# 第4题
config = {'host': 'localhost', 'port': 80}
config['port'] = 8080
# 第5题
user = {'name': 'Alice', 'age': 25}
for key in user.keys():
    print(key)
for value in user.values():
    print(value)
for key, value in user.items():
    print(key, value)
# 第6题
"""
dict1中没有的会添加，已有的会更新值
dict1 变为 {'x': 10, 'y': 30, 'z': 40}
"""
# 第7题
data = {'item1': 'A', 'item2': 'B', 'item3': 'C'}
print(data.pop('item2'))
print(data.popitem())
del data['item1']
# 第8题
"""
题目中没有展示出numbers的列表，在这里假设是
"""
numbers = [-1,0,1, 2, 3,4]
my_dict = {x:x**2 for x in numbers if x >2}
# 第9题
word_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# 改进方法1: 使用 get()
sum_dict_improved = {}
for word in word_list:
    sum_dict_improved[word] = sum_dict_improved.get(word, 0) + 1
print(sum_dict_improved)

# 改进方法2: 使用 collections.Counter (更Pythonic)
from collections import Counter
sum_dict_counter = Counter(word_list)
print(sum_dict_counter)
"""
LIFO顺序即后进先出顺序，之前的版本没有顺序，是随机的
"""
# 第11题
"""
value可以是任意类型，比如数字，字符串，bool，列表，没有限制
"""
# 第12题
"""
检查的是键是否存在
"""
# 第13题
my_dict.clear()
print(my_dict) #空字典
# 第14题
"""
因为列表中的元素可以用索引和直接访问来修改
"""
# 第15题
"""
都是键值对的形式，因为形式几乎相同，key和value能通过固定方式转换
"""