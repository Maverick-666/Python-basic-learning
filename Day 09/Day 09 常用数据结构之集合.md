## 核心概念

- **集合 (Set)**: Python中的一种容器型数据类型，用于存储多个不重复的、无序的元素。
    
- **数学集合特性**:
    
    - **无序性**: 元素没有特定的顺序，不支持索引访问。
        
    - **互异性**: 集合中不能有重复的元素。
        
    - **确定性**: 一个元素要么属于集合，要么不属于，通过成员运算 in / not in 判断。
        
- **性能**: 成员运算 (in) 通常比列表快，因为集合底层使用哈希存储。
    
- **元素类型**: 集合中的元素必须是 **hashable** 类型（通常是不可变类型，如数字、字符串、元组）。列表、字典、集合本身等可变类型不能作为集合的元素。
    

## 一、创建集合

### 1. 使用 {} 字面量 (推荐用于非空集合)

至少包含一个元素，因为 {} 表示空字典。重复元素会自动忽略。、】
``` python  
set1 = {1, 2, 3, 2, 1} # 结果是 {1, 2, 3} (顺序不定)  
fruits = {'apple', 'banana', 'apple'} # {'banana', 'apple'}

````
### 2. 使用 `set()` 构造器
*   创建空集合: `empty_set = set()`
*   将其他可迭代对象 (如列表、元组、字符串、range对象) 转换为集合:
    ```python
    list_to_set = set([1, 2, 2, 3]) # {1, 2, 3}
    string_to_set = set('hello')    # {'h', 'e', 'l', 'o'} (l只出现一次)
    ```

### 3. 使用集合生成式 `{expression for item in iterable if condition}`
类似于列表生成式，但创建的是集合。
```python
evens_set = {x for x in range(10) if x % 2 == 0} # {0, 2, 4, 6, 8}
````



## 二、元素的遍历

使用 for-in 循环遍历集合中的元素 (顺序不固定)。

```
my_set = {'a', 'b', 'c'}
for element in my_set:
    print(element) # 输出顺序不保证是 a, b, c
print(len(my_set)) # 3
```


## 三、集合的运算

### 1. 成员运算 in, not in

判断元素是否存在于集合中。

```
print('a' in my_set) # True
```



### 2. 二元运算 (返回新集合)

|   |   |   |   |
|---|---|---|---|
|运算|运算符|方法名|描述|
|交集|&|intersection()|两个集合共有的元素|
|并集|`|`|union()|
|差集|-|difference()|在第一个集合但不在第二个集合的元素|
|对称差|^|symmetric_difference()|只存在于其中一个集合的元素|

```
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 & s2)  # {3, 4} (交集)
print(s1 | s2)  # {1, 2, 3, 4, 5, 6} (并集)
print(s1 - s2)  # {1, 2} (s1中独有)
print(s1 ^ s2)  # {1, 2, 5, 6} (只在其中一个集合中)
```


### 3. 复合赋值运算 (就地修改原集合)

- |= (或 update()): 并集赋值。
    
- &= (或 intersection_update()): 交集赋值。
    
- -= (或 difference_update()): 差集赋值。
    
- ^= (或 symmetric_difference_update()): 对称差赋值。
    

```
s1 = {1, 2, 3}
s1 |= {3, 4, 5} # s1 变为 {1, 2, 3, 4, 5}
```


### 4. 比较运算 (返回布尔值)

- ==, !=: 判断集合是否相等 (元素完全相同，顺序无关)。
    
- <, <=: 判断是否为真子集/子集 (s1.issubset(s2))。
    
- >, >=: 判断是否为真超集/超集 (s1.issuperset(s2))。
    

```
s_sub = {1, 2}
s_super = {1, 2, 3}
print(s_sub < s_super)  # True (s_sub 是 s_super 的真子集)
print(s_sub.issubset(s_super)) # True
```


## 四、集合的常用方法 (修改集合)

- add(element): 向集合中添加一个元素。如果元素已存在，则不进行任何操作。
    
- remove(element): 从集合中移除指定元素。如果元素不存在，引发 KeyError。
    
- discard(element): 从集合中移除指定元素。如果元素不存在，不执行任何操作 (不报错)。
    
- pop(): **随机**移除并返回集合中的一个元素。如果集合为空，引发 KeyError。
    
- clear(): 移除集合中的所有元素。
    
- isdisjoint(other_set): 如果两个集合没有共同元素，返回 True，否则返回 False。
    

```
my_data = {10, 20}
my_data.add(30)      # {10, 20, 30}
my_data.remove(10)   # {20, 30}
my_data.discard(5)   # {20, 30} (5不存在，无事发生)
# item = my_data.pop() # item可能是20或30
```

## 五、不可变集合 frozenset

- frozenset 是集合的不可变版本。一旦创建，不能添加或删除元素。
    
- 由于不可变，frozenset 是 **hashable** 的，因此可以作为集合的元素或字典的键。
    
- 支持所有不修改集合的集合运算 (如交集、并集、成员运算、比较运算等)。
    
- 创建: fs = frozenset({1, 2, 3}) 或 fs = frozenset(iterable)。
    

```
fs1 = frozenset([1, 2])
fs2 = frozenset([2, 3])
print(fs1 & fs2) # frozenset({2})
# fs1.add(4)     # AttributeError

set_of_frozensets = {fs1, fs2, frozenset({1})}
print(set_of_frozensets)
```


## 总结

- 集合是处理不重复元素集合的强大工具，尤其在需要快速成员检查、去重以及执行数学集合运算时非常有用。
    
- 其无序性和元素互异性是核心特征。
    
- 元素必须是可哈希的。
    
- set 是可变的，frozenset 是不可变的。根据需求选择合适的类型。