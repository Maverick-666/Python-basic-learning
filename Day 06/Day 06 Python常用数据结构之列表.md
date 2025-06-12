## 核心概念 

- **列表 (List)**: Python中一种重要的数据结构，是由一系列元素按特定顺序构成的**可变**数据序列。它可以存储多个数据项，并且这些数据项可以是不同类型的（但不推荐混用）。
    
- **容器型数据类型**: 列表可以容纳其他数据，因此称为容器。
    

## 一、创建列表 

### 1. 字面量语法 []

使用方括号 [] 定义列表，元素间用逗号 , 分隔。

```
numbers = [10, 20, 5, 30, 10]    # 整数列表，可有重复元素
names = ['Alice', 'Bob', 'Charlie'] # 字符串列表
mixed_list = [1, 'Hello', True, 3.14] # 混合类型 (不推荐)
empty_list = []                   # 空列表
print(type(numbers)) # <class 'list'>
```


### 2. list() 构造器

可以将其他可迭代对象（如 range 对象、字符串、元组等）转换为列表。

```
range_to_list = list(range(5))  # [0, 1, 2, 3, 4]
string_to_list = list('Python') # ['P', 'y', 't', 'h', 'o', 'n']
```



## 二、列表的运算 

### 1. 拼接 + 和 +=

连接两个列表，生成一个新列表。+= 就地修改原列表。

```
list1 = [1, 2]
list2 = [3, 4]
result = list1 + list2  # result is [1, 2, 3, 4]
list1 += list2          # list1 becomes [1, 2, 3, 4]
```


### 2. 重复 * 和 *=

将列表元素重复指定次数，生成一个新列表。*= 就地修改。

```
short_list = ['a', 'b']
repeated = short_list * 3 # repeated is ['a', 'b', 'a', 'b', 'a', 'b']
```


### 3. 成员运算 in 和 not in

判断元素是否存在于列表中，返回布尔值。```python  
my_list = [10, 20, 30]  
print(20 in my_list) # True  
print(40 not in my_list) # True

````
### 4. 索引运算 `[]`
访问或修改列表中特定位置的元素。
*   **正向索引**: 从 `0` (第一个元素) 到 `N-1` (最后一个元素)。
*   **反向索引**: 从 `-1` (最后一个元素) 到 `-N` (第一个元素)。
```python
fruits = ['apple', 'banana', 'cherry']
print(fruits[0])    # 'apple'
print(fruits[-1])   # 'cherry'
fruits[1] = 'blueberry' # 修改元素: ['apple', 'blueberry', 'cherry']
# print(fruits[3])  # IndexError: list index out of range
````


### 5. 切片运算 [start:end:step]

获取列表的一个子序列 (浅拷贝)。

- start: 起始索引 (包含)，默认为 0。
    
- end: 结束索引 (不包含)，默认为列表长度。
    
- step: 步长 (默认为 1)。
    

```
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters[1:4])     # ['b', 'c', 'd']
print(letters[:3])      # ['a', 'b', 'c']
print(letters[3:])      # ['d', 'e', 'f']
print(letters[::2])     # ['a', 'c', 'e'] (隔一个取一个)
print(letters[::-1])    # ['f', 'e', 'd', 'c', 'b', 'a'] (反转)
letters[1:3] = ['X', 'Y'] # 切片赋值: ['a', 'X', 'Y', 'd', 'e', 'f']
```


### 6. 关系运算 == , !=, <, <=, >, >=

比较两个列表。== 比较内容是否相同。大小比较按字典序逐个元素比较。

```
print([1, 2, 3] == [1, 2, 3]) # True
print([1, 2, 3] < [1, 2, 4])  # True
```

## 三、元素的遍历 (Day 08)

### 1. 通过索引遍历

```
items = ['one', 'two', 'three']
for i in range(len(items)):
    print(f"Index {i}: {items[i]}")
```



### 2. 直接遍历元素 (推荐)

```
items = ['one', 'two', 'three']
for item in items:
    print(item)
```


### 应用：重构掷色子统计 

使用列表可以更优雅地解决之前用多个变量统计点数的问题。

```
import random
counters = [0] * 6 # [0, 0, 0, 0, 0, 0]
for _ in range(6000):
    face = random.randrange(1, 7) # 1 to 6
    counters[face - 1] += 1 # 点数1对应索引0,以此类推
for i in range(6):
    print(f'{i+1}点出现了{counters[i]}次')
```



---

## 四、列表的方法 

列表对象有很多内置方法用于操作列表。语法：list_variable.method_name()

### 1. 添加和删除元素

- append(element): 在列表末尾添加一个元素。
    
- insert(index, element): 在指定索引 index 处插入元素。
    
- remove(element): 删除列表中第一个出现的指定元素。若元素不存在，引发 ValueError。
    
- pop([index]): 删除并返回指定索引的元素。若无 index，删除并返回最后一个元素。若索引越界，引发 IndexError。
    
- clear(): 清空列表所有元素。
    
- del list_var[index] / del list_var[start:end]: del 关键字删除指定索引或切片的元素。
    

```
my_langs = ['C', 'Java']
my_langs.append('Python')    # ['C', 'Java', 'Python']
my_langs.insert(1, 'Go')     # ['C', 'Go', 'Java', 'Python']
my_langs.remove('Java')      # ['C', 'Go', 'Python']
popped_lang = my_langs.pop() # popped_lang is 'Python', my_langs is ['C', 'Go']
del my_langs[0]              # my_langs is ['Go']
```



### 2. 元素位置和频次

- index(element[, start[, end]]): 返回元素在列表中首次出现的索引。可指定查找范围。若元素不存在，引发 ValueError。
    
- count(element): 返回元素在列表中出现的次数。
    

```
data = [1, 2, 3, 2, 4, 2]
print(data.index(2))    # 1 (第一个2的索引)
print(data.index(2, 2)) # 3 (从索引2开始查找2)
print(data.count(2))    # 3
```



### 3. 元素排序和反转

- sort(key=None, reverse=False): **就地**对列表元素进行排序（不创建新列表）。reverse=True 实现降序。key 可指定一个函数用于排序比较。
    
- reverse(): **就地**反转列表中的元素顺序。
    

```
nums = [3, 1, 4, 1, 5, 9, 2]
nums.sort()          # nums is [1, 1, 2, 3, 4, 5, 9]
nums.sort(reverse=True) # nums is [9, 5, 4, 3, 2, 1, 1]
nums.reverse()       # nums is [1, 1, 2, 3, 4, 5, 9]
```



- **非就地排序**: 使用内置函数 sorted(iterable, key=None, reverse=False)，它返回一个新的已排序列表，原列表不变。
    
    ```
    original_nums = [3, 1, 2]
    new_sorted_nums = sorted(original_nums) # new_sorted_nums is [1, 2, 3]
    ```
    


## 五、列表生成式 (List Comprehensions) (Day 09)

一种简洁优雅地创建列表的语法，通常比传统的 for 循环加 append 更高效。  
**基本形式**: [expression for item in iterable if condition]

### 1. 示例

- **场景1**: 创建1-99中能被3或5整除的数的列表。
    
    ```
    items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
    ```
    
    
- **场景2**: 列表中元素的平方。
    
    ```
    nums1 = [2, 3, 4]
    squares = [num ** 2 for num in nums1] # [4, 9, 16]
    ```
    
 
    
- **场景3**: 筛选大于50的元素。
    
    ```
    data = [35, 60, 12, 97]
    filtered = [x for x in data if x > 50] # [60, 97]
    ```
    

    

## 六、嵌套列表 

列表的元素可以是另一个列表，形成嵌套结构，常用于表示表格、矩阵等。

```
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])    # [1, 2, 3] (第一行)
print(matrix[1][1]) # 5 (第二行第二列的元素)

# 使用列表生成式创建嵌套列表 (例如，3x3的零矩阵)
zero_matrix = [[0 for _ in range(3)] for _ in range(3)]
```



## 七、列表的应用：双色球随机选号 

**思路**:

1. 创建红球池 (1-33) 和蓝球池 (1-16)。
    
2. 从红球池中无放回地随机抽取6个球：
    
    - 方法1: 循环6次，每次 random.randrange() 生成索引，pop() 出元素并添加到选中列表。
        
    - 方法2 (推荐): random.sample(red_balls_pool, 6)。
        
3. 对选中的红球排序。
    
4. 从蓝球池中随机抽取1个球：random.choice(blue_balls_pool)。
    
5. 格式化输出。
    

```
import random
red_pool = list(range(1, 34))
blue_pool = list(range(1, 17))

selected_reds = sorted(random.sample(red_pool, 6))
selected_blue = random.choice(blue_pool)

# print(f"红球: {selected_reds}, 蓝球: [{selected_blue}]")
```


## 总结

列表是Python中功能强大且使用频繁的数据结构。掌握其创建、运算、遍历、常用方法以及列表生成式等，对于编写高效、简洁的Python代码至关重要。列表的动态性和可变性使其非常灵活，但也需注意操作时可能产生的副作用（如就地修改）。