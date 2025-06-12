# day_13_dictionaries.py

# -----------------------------------------------------------------------------
# 核心概念：字典 (Dictionary)
# - 容器型数据类型，以键值对 (key-value pair) 的形式组织数据。
# - 通过键 (key) 来访问对应的值 (value)。
# - 键必须是不可变 (hashable) 类型 (如 int, float, str, tuple)。
# - 值可以是任意类型。
# - 字典中的键是唯一的。
# - 在Python 3.7+ 版本中，字典是有序的 (保持插入顺序)。在之前版本中是无序的。
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 一、创建和使用字典
# -----------------------------------------------------------------------------
print("--- 1. 创建和使用字典 ---")

# 1.1 使用 {} 字面量语法创建字典
xinhua_d13 = {
    '麓': '山脚下',
    '路': '道，往来通行的地方；方面，地区：南～货，外～货；种类：他俩是一～人',
    '蕗': '甘草的别名',
    '潞': '潞水，水名，即今山西省的浊漳河；潞江，水名，即云南省的怒江'
}
print(f"Xinhua dictionary sample: {xinhua_d13['路']}")

person_info_d13 = {
    'name': '王大锤',
    'age': 55,
    'height': 168,
    'weight': 60,
    'addr': '成都市武侯区科华北路62号1栋101',
    'tel': '13122334455',
    'emergence contact': '13800998877' # 键可以是包含空格的字符串
}
print(f"Person info: {person_info_d13}")

# 1.2 使用 dict() 构造器创建字典
# 方式一: 关键字参数 (键必须是合法的变量名)
person_dict_func_d13 = dict(name='王大锤', age=55, height=168, weight=60)
print(f"Using dict() with kwargs: {person_dict_func_d13}")

# 方式二: 从包含键值对的序列创建 (如元组列表)
person_from_tuples_d13 = dict([('name', '李小龙'), ('age', 32)])
print(f"Using dict() with list of tuples: {person_from_tuples_d13}")

# 方式三: 使用 zip 函数压缩两个序列
items1_zip_d13 = dict(zip('ABCDE', '12345')) # Keys 'A'-'E', Values '1'-'5' (as strings)
print(f"Using dict(zip()): {items1_zip_d13}")
items2_zip_d13 = dict(zip('ABCDE', range(1, 10))) # Values 1-5 (range is longer, extra ignored)
print(f"Using dict(zip()) with range: {items2_zip_d13}")

# 1.3 使用字典生成式 (Dictionary Comprehension)
items3_comp_d13 = {x: x ** 3 for x in range(1, 6)} # {1:1, 2:8, ..., 5:125}
print(f"Using dictionary comprehension: {items3_comp_d13}")

# 1.4 获取字典大小 (len()) 和遍历键
person_len_iter_d13 = {
    'name': '王大锤', 'age': 55, 'height': 168, 'weight': 60
}
print(f"Length of person_len_iter_d13: {len(person_len_iter_d13)}") # 4
print("Iterating through keys of person_len_iter_d13:")
for key_d13 in person_len_iter_d13: # 默认遍历键
    print(key_d13, end=" ") # name age height weight (顺序在3.7+保持插入顺序)
print("\n")

# 1.5 字典的值可以是复杂类型 (列表、其他字典等)
complex_person_d13 = {
    'name': '王大锤', 'age': 55,
    'addr': ['成都市武侯区科华北路62号1栋101', '北京市西城区百万庄大街1号'],
    'car': {
        'brand': 'BMW X7', 'maxSpeed': 250, 'displacement': 3.0
    }
}
print(f"Complex person data: {complex_person_d13}")
print(f"Car brand: {complex_person_d13['car']['brand']}") # BMW X7
print("\n")

# -----------------------------------------------------------------------------
# 二、字典的运算
# -----------------------------------------------------------------------------
print("--- 2. 字典的运算 ---")
person_ops_d13 = {'name': '王大锤', 'age': 55, 'height': 168}

# 2.1 成员运算 (in, not in) - 检查键是否存在
print(f"'name' in person_ops_d13: {'name' in person_ops_d13}") # True
print(f"'tel' in person_ops_d13: {'tel' in person_ops_d13}")   # False

# 2.2 索引运算 ([key]) - 获取值或设置/添加键值对
print(f"Name: {person_ops_d13['name']}") # 王大锤
person_ops_d13['age'] = 25 # 修改现有键的值
person_ops_d13['tel'] = '13122334455' # 添加新的键值对
print(f"Updated person_ops_d13: {person_ops_d13}")
# print(person_ops_d13['non_existent_key']) # KeyError if key doesn't exist

# 2.3 遍历键并获取值
print("\nIterating through keys and accessing values:")
for key_ops_d13 in person_ops_d13:
    print(f'{key_ops_d13}:\t{person_ops_d13[key_ops_d13]}')
print("\n")

# -----------------------------------------------------------------------------
# 三、字典的方法
# -----------------------------------------------------------------------------
print("--- 3. 字典的方法 ---")
person_methods_d13 = {'name': '王大锤', 'age': 25, 'height': 178}

# 3.1 get(key[, default]) - 安全获取值
print(f"person_methods_d13.get('name'): {person_methods_d13.get('name')}") # 王大锤
print(f"person_methods_d13.get('sex'): {person_methods_d13.get('sex')}")       # None (key 'sex' doesn't exist)
print(f"person_methods_d13.get('sex', 'Unknown'): {person_methods_d13.get('sex', 'Unknown')}") # Unknown (default value)

# 3.2 keys(), values(), items() - 获取视图对象
print(f"person_methods_d13.keys(): {person_methods_d13.keys()}")     # dict_keys(['name', 'age', 'height'])
print(f"person_methods_d13.values(): {person_methods_d13.values()}")   # dict_values(['王大锤', 25, 178])
print(f"person_methods_d13.items(): {person_methods_d13.items()}")    # dict_items([('name', '王大锤'), ('age', 25), ('height', 178)])

print("\nIterating using items():")
for key_item_d13, value_item_d13 in person_methods_d13.items(): # 解包键值对元组
    print(f'{key_item_d13}:\t{value_item_d13}')

# 3.3 update(other_dict or iterable_of_pairs) - 合并字典
print("\n--- 3.3 update() ---")
dict1_update_d13 = {'name': '王大锤', 'age': 55, 'height': 178}
dict2_update_d13 = {'age': 25, 'addr': '成都', 'tel': '123'}
print(f"Original dict1_update_d13: {dict1_update_d13}")
dict1_update_d13.update(dict2_update_d13) # dict2_update_d13 的内容合并到 dict1_update_d13
# 'age'会被更新，'addr'和'tel'会被添加
print(f"dict1_update_d13 after update: {dict1_update_d13}")

# Python 3.9+ 可以使用 | (合并) 和 |= (就地合并) 运算符
# dict1_merge_d13 = {'a': 1, 'b': 2}
# dict2_merge_d13 = {'b': 3, 'c': 4}
# merged_dict = dict1_merge_d13 | dict2_merge_d13 # {'a': 1, 'b': 3, 'c': 4} (Python 3.9+)
# print(f"Merged with | (Python 3.9+): {merged_dict}")
# dict1_merge_d13 |= dict2_merge_d13 # dict1_merge_d13 becomes {'a': 1, 'b': 3, 'c': 4}
# print(f"dict1_merge_d13 after |= (Python 3.9+): {dict1_merge_d13}")

# 3.4 pop(key[, default]) - 删除并返回值
print("\n--- 3.4 pop() and popitem() ---")
person_pop_d13 = {'name': '王大锤', 'age': 25, 'height': 178, 'addr': '成都'}
popped_age = person_pop_d13.pop('age') # 删除'age'键值对，并返回其值
print(f"Popped age: {popped_age}")       # 25
print(f"person_pop_d13 after pop('age'): {person_pop_d13}")
# popped_non_existent = person_pop_d13.pop('sex') # KeyError
popped_non_existent_default = person_pop_d13.pop('sex', 'N/A') # 提供默认值避免KeyError
print(f"Popped 'sex' with default: {popped_non_existent_default}") # N/A

# 3.5 popitem() - 删除并返回一个键值对 (LIFO顺序 in Python 3.7+)
# 在Python 3.6及更早版本中，popitem() 删除并返回一个随机的键值对。
if person_pop_d13: # 确保字典不为空
    key_val_pair_d13 = person_pop_d13.popitem() # (Python 3.7+ removes last inserted)
    print(f"Popped item: {key_val_pair_d13}")
    print(f"person_pop_d13 after popitem(): {person_pop_d13}")

# 3.6 clear() - 清空字典
person_pop_d13.clear()
print(f"person_pop_d13 after clear(): {person_pop_d13}") # {}

# 3.7 del dict[key] - 删除键值对
print("\n--- 3.7 del keyword ---")
person_del_d13 = {'name': '王大锤', 'age': 25, 'height': 178}
del person_del_d13['age'] # 删除 'age' 键值对
print(f"person_del_d13 after del ['age']: {person_del_d13}")
# del person_del_d13['sex'] # KeyError if key doesn't exist
print("\n")

# -----------------------------------------------------------------------------
# 四、字典的应用
# -----------------------------------------------------------------------------
print("--- 4. 字典的应用 ---")

# 4.1 例子1：统计英文字母出现次数
print("--- 4.1 统计字母出现次数 ---")
sentence_d13 = "Man is distinguished, not only by his reason, but by this singular passion from other animals" # 简化句子
counter_d13 = {}
for char_d13 in sentence_d13:
    if 'A' <= char_d13.upper() <= 'Z': # 统一转大写判断是否为字母
        char_lower_d13 = char_d13.lower() # 统计时用小写
        counter_d13[char_lower_d13] = counter_d13.get(char_lower_d13,0) + 1

# 按出现次数从高到低输出 (sorted的key参数使用lambda函数)
# sorted_keys_d13 = sorted(counter_d13, key=counter_d13.get, reverse=True)
# 或者使用 lambda:
sorted_keys_d13 = sorted(counter_d13, key=lambda k: counter_d13[k], reverse=True)
print("Letter counts (descending):")
for key_count_d13 in sorted_keys_d13:
    print(f'{key_count_d13} 出现了 {counter_d13[key_count_d13]} 次.')

# 4.2 例子2：筛选股价大于100的股票 (使用字典生成式)
print("\n--- 4.2 筛选高价股 ---")
stocks_d13 = {
    'AAPL': 191.88, 'GOOG': 1186.96, 'IBM': 149.24,
    'ORCL': 48.44, 'ACN': 166.89, 'FB': 208.09, 'SYMC': 21.29
}
high_value_stocks_d13 = {
    key_stock_d13: value_stock_d13
    for key_stock_d13, value_stock_d13 in stocks_d13.items()
    if value_stock_d13 > 100
}
print(f"High value stocks (>100): {high_value_stocks_d13}")
print("\n")

print("--- End of Day 13 Dictionaries Demo ---")