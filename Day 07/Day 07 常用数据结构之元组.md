## 核心概念

- **元组 (Tuple)**: Python中的一种有序序列，与列表类似，可以包含多个元素。
    
- **关键特性**: 元组是 **不可变类型 (immutable)**。一旦创建，其内容（元素本身或元素的顺序）不能被修改、添加或删除。
    
- **定义**: 通常使用圆括号 () 字面量语法，元素间用逗号 , 分隔。
    

## 一、元组的定义和运算

### 1. 定义元组

```
t1 = (10, 20, 30)             # 整数元组
t2 = ('apple', True, 3.14)    #混合类型元组
empty_tuple = ()              # 空元组
single_item_tuple = ('hello',) # 注意：单个元素的元组必须有尾随逗号!
# (100) 只是整数100，不是元组。(100,) 才是元组。
print(type(t1)) # <class 'tuple'>
```



### 2. 元组支持的运算 (与列表相似，但无修改操作)

- **长度**: len(my_tuple)
    
- **索引**: my_tuple[index] (正向/反向)
    
- **切片**: my_tuple[start:end:step] (返回新元组)
    
- **遍历**: for item in my_tuple:
    
- **成员运算**: element in my_tuple, element not in my_tuple
    
- **拼接**: tuple1 + tuple2 (返回新元组)
    
- **重复**: my_tuple * n (返回新元组)
    
- **比较运算**: ==, !=, <, <=, >, >= (按字典序比较)
    

```
point = (3, 4)
print(len(point))     # 2
print(point[0])       # 3
print(point[-1])      # 4
print(point + (5, 6)) # (3, 4, 5, 6)

# 尝试修改会引发 TypeError
# point[0] = 10 # TypeError: 'tuple' object does not support item assignment
```



## 二、打包 (Packing) 和解包 (Unpacking)

### 1. 打包

将多个用逗号分隔的值赋给一个变量时，这些值会自动“打包”成一个元组。

```
coordinates = 10, 20, 30 # 打包成元组 (10, 20, 30)
print(coordinates)       # (10, 20, 30)
print(type(coordinates)) # <class 'tuple'>
```

### 2. 解包

将一个序列（如元组、列表、字符串、range对象）赋值给对应数量的变量时，序列的元素会被“解包”并分别赋给这些变量。

```
data_tuple = ('Alice', 25, 'USA')
name, age, country = data_tuple # 解包
print(f"Name: {name}, Age: {age}, Country: {country}")

# 变量数量必须与序列元素数量匹配，否则引发 ValueError
# x, y = data_tuple # ValueError: too many values to unpack
```

### 3. 星号表达式 * 进行解包 (Extended Unpacking)

用于处理元素数量与变量数量不匹配的情况。带星号的变量会收集多余的元素，并形成一个**列表**。星号表达式在一次解包中只能使用一次。

```
numbers = (1, 2, 3, 4, 5)
first, second, *rest = numbers
# first is 1, second is 2, rest is [3, 4, 5]
print(f"{first=}, {second=}, {rest=}")

*initial, last = numbers
# initial is [1, 2, 3, 4], last is 5
print(f"{initial=}, {last=}")

first, *middle, last = numbers
# first is 1, middle is [2, 3, 4], last is 5
print(f"{first=}, {middle=}, {last=}")


## 三、交换变量的值

Python中交换变量值非常简洁，利用了类似元组赋值的机制（底层有字节码优化）。


a = 10
b = 20
a, b = b, a # a 变为 20, b 变为 10
print(f"{a=}, {b=}")

# 三变量轮换
x, y, z = 1, 2, 3
x, y, z = y, z, x # x=2, y=3, z=1
print(f"{x=}, {y=}, {z=}")
```



## 四、元组与列表的比较

### 为什么需要元组？

1. **不可变性 (Immutability)**:
    
    - **线程安全**: 在多线程环境中，不可变对象更安全，因为它们的状态不会被意外修改，减少了同步需求。
        
    - **可作为字典的键**: 只有不可变类型才能用作字典的键 (列表不行)。
        
    - **数据完整性**: 当你希望一组数据不被修改时，元组是更好的选择。
        
2. **性能**:
    
    - **创建时间**: 通常情况下，创建元组比创建包含相同元素的列表更快。
        
    - **存储空间**: 对于少量元素，元组可能占用略少的内存 (依赖具体实现和Python版本)。
        
    
    ```
    # import timeit
    # list_time = timeit.timeit('[1,2,3,4,5]', number=10000000) # 0.19s
    # tuple_time = timeit.timeit('(1,2,3,4,5)', number=10000000) # 0.02s
    # (实际时间因环境而异，但元组通常更快)
    ```
    

    

### 类型转换

可以使用 list() 和 tuple() 在列表和元组之间进行转换。

```
my_tuple = (1, 2, 3)
my_list = list(my_tuple)   # my_list is [1, 2, 3]

another_list = ['a', 'b']
another_tuple = tuple(another_list) # another_tuple is ('a', 'b')
```



## 总结

- 元组和列表都是有序的序列容器。
    
- **核心区别**: 列表是**可变**的，元组是**不可变**的。
    
- 由于不可变性，元组在某些场景下（如多线程、用作字典键、保护数据不被修改）更有优势，并且在创建时通常有性能优势。
    
- 打包和解包是元组（及其他序列）非常方便的特性，尤其星号表达式增强了其灵活性。
    
- 选择列表还是元组，取决于你是否需要修改数据以及对性能和数据完整性的具体要求。