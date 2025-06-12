## 核心概念

- **字典 (Dictionary)**: Python中的一种核心数据结构，用于存储**键值对 (key-value pairs)** 的集合。每个键唯一映射到一个值。
    
- **键 (Key)**:
    
    - 必须是**唯一的**。
        
    - 必须是**不可变 (hashable)** 类型，如数字、字符串、元组（元组内元素也必须不可变）。列表、集合、字典本身不能作为键。
        
- **值 (Value)**: 可以是任意Python对象，可重复。
    
- **顺序**: 从Python 3.7开始，字典会**保持插入顺序**。在之前的版本中，字典是无序的。
    
- **用途**: 非常适合表示真实世界对象的属性，或需要通过唯一标识符快速查找数据的场景。
    

## 一、创建字典

### 1. 使用 {} 字面量

键和值用冒号 : 分隔，键值对之间用逗号 , 分隔。

```
person = {
    'name': '张三',
    'age': 30,
    'city': '北京'
}
empty_dict = {} # 创建空字典
```


### 2. 使用 dict() 构造器

- **关键字参数 (键必须是合法标识符)**:
    
    ```
    config = dict(host='localhost', port=8080, debug=True)
    ```
    
    
    
- **可迭代的键值对序列 (如元组列表)**:
    
    ```
    pairs = [('a', 1), ('b', 2)]
    my_dict = dict(pairs) # {'a': 1, 'b': 2}
    ```
    

    
- **zip() 函数**:
    
    ```
    keys = ['one', 'two']
    values = [1, 2]
    zipped_dict = dict(zip(keys, values)) # {'one': 1, 'two': 2}
    ```

    

### 3. 字典生成式 {key_expr: value_expr for item in iterable if condition}

```
squares = {x: x**2 for x in range(5)} # {0:0, 1:1, 2:4, 3:9, 4:16}
```


## 二、字典的运算和基本操作

### 1. 获取字典大小 len()

返回字典中键值对的数量。

```
print(len(person)) # 3
```


### 2. 成员运算 in, not in

检查**键**是否存在于字典中。

```
print('age' in person)    # True
print('gender' not in person) # True
```


### 3. 索引运算 [] (访问和修改/添加)

通过键来访问、修改或添加键值对。

- **访问**: value = my_dict[key]
    
    - 如果键不存在，会引发 KeyError。
        
- **修改/添加**: my_dict[key] = new_value
    
    - 如果键已存在，则更新其对应的值。
        
    - 如果键不存在，则添加新的键值对。
        

```
print(person['name'])   # '张三'
person['age'] = 31      # 修改年龄
person['country'] = '中国' # 添加新条目
```



## 三、字典的常用方法

### 1. 安全获取值 get(key[, default])

通过键获取值。如果键不存在，返回 None (或指定的 default 值)，而不是引发 KeyError。

```
print(person.get('city'))      # '北京'
print(person.get('job'))       # None
print(person.get('job', '未知')) # '未知'
```



### 2. 获取键、值、键值对视图

这些方法返回的是“视图对象”，它们是动态的，会反映字典的后续更改。

- keys(): 返回一个包含所有键的视图。
    
- values(): 返回一个包含所有值的视图。
    
- items(): 返回一个包含所有 (键, 值) 元组对的视图。
    

```
print(list(person.keys()))   # ['name', 'age', 'city', 'country'] (顺序可能不同，3.7+保持插入顺序)
print(list(person.values())) # ['张三', 31, '北京', '中国']
print(list(person.items()))  # [('name', '张三'), ('age', 31), ...]

# 常用于遍历
for key, value in person.items():
    print(f"{key}: {value}")
```



### 3. 合并字典 update(other_dict_or_iterable)

将 other_dict_or_iterable 中的键值对合并到当前字典。如果键已存在，则其值会被更新。

```
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
dict1.update(dict2) # dict1 变为 {'a': 1, 'b': 3, 'c': 4}
```

- **Python 3.9+**: 可以使用 | (合并，返回新字典) 和 |= (就地合并) 运算符。
    
    ```
    # merged = dict1 | dict2
    # dict1 |= dict2
    ```
    


### 4. 删除键值对

- pop(key[, default]): 删除指定键的键值对，并返回其值。如果键不存在且未提供default，引发 KeyError。
    
- popitem(): (Python 3.7+) 删除并返回最后插入的 (键, 值) 对。在3.6及更早版本中，删除并返回一个随机对。如果字典为空，引发 KeyError。
    
- clear(): 清空字典中所有键值对。
    
- del my_dict[key]: del 关键字删除指定键的键值对。若键不存在，引发 KeyError。
    

```
age_val = person.pop('age') # age_val 为 31
# last_item = person.popitem()
# del person['name']
```


## 四、字典的应用实例

### 1. 统计字符出现次数

```
sentence = "hello world"
counter = {}
for char in sentence:
    counter[char] = counter.get(char, 0) + 1
# counter is {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
# 按次数排序输出
# sorted_items = sorted(counter.items(), key=lambda item: item[1], reverse=True)
```


### 2. 筛选字典 (字典生成式)

找出股价大于100的股票。

```
stocks = {'AAPL': 190, 'GOOG': 120, 'MSFT': 90}
high_value_stocks = {k: v for k, v in stocks.items() if v > 100}
# high_value_stocks is {'AAPL': 190, 'GOOG': 120}
```


## 总结

- 字典是Python中用于存储键值对数据的高效结构，非常适合通过键快速查找、添加和修改数据。
    
- 理解键的唯一性和不可变性是使用字典的关键。
    
- 字典的方法提供了丰富的操作，如安全获取、遍历、合并和删除。
    
- 字典生成式是创建字典的强大而简洁的方式。
    
- 从Python 3.7开始，字典保持插入顺序，这在某些应用中非常有用。