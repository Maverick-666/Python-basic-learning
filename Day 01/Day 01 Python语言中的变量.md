## 核心概念回顾

- **程序**：数据和指令的有序集合。
    
- **变量**：数据的载体，是内存中用于保存数据的一块空间。其值可以被读取和修改。
    

## 一、Python常用数据类型及其表示

Python 语言预设了多种数据类型，我们首先关注以下几种：

### 1. 整型 (int)

处理任意大小的整数。支持多种进制表示：

```
print(0b100)  # 二进制: 4
print(0o100)  # 八进制: 64
print(100)    # 十进制: 100
print(0x100)  # 十六进制: 256
```


- **讲解**：0b (二进制), 0o (八进制), 0x (十六进制) 是对应进制的前缀。
    

### 2. 浮点型 (float)

即小数。支持数学写法和科学计数法：

```
print(123.456)    # 数学写法
print(1.23456e2)  # 科学计数法: 1.23456 * 10^2
```


- **讲解**：e 或 E 用于表示科学计数法中的10的幂。
    

### 3. 字符串型 (str)

以单引号 ' ' 或双引号 " " 包裹的任意文本。

```
print('hello')
print("world")
```


- **讲解**：单双引号效果一致，常用于包含特殊字符（如字符串内有引号）的场景。
    

### 4. 布尔型 (bool)

只有 True (真) 和 False (假) 两种值。

```
is_active = True
has_error = False
print(is_active)
print(type(has_error)) # <class 'bool'>
```



- **讲解**：常用于逻辑判断和条件控制。
    

## 二、变量命名规范

良好的变量命名是代码可读性的关键。

- **规则**：
    
    1. 由**字母** (Unicode字符，建议用英文字母)、**数字**、**下划线 _** 构成。
        
    2. **数字不能开头**。
        
    3. **大小写敏感** (age 和 Age 是不同变量)。
        
    4. **严禁**与Python**关键字**重名 (如 if, else, True, False)。
        
    5. **避免**与Python**内置函数/模块名**重名 (如 int, print, str)。
        
- **惯例 (推荐)**：
    
    1. 使用**小写英文字母**，多个单词间用**下划线 _ 连接** (e.g., user_input, first_name)。
        
    2. 做到**见名知意**。
        

```
# 推荐命名
user_age = 25
error_message = "File not found"

# 不推荐或错误命名
# 2_users = []      # 数字开头
# max-value = 100   # 含非法字符 '-'
# class = "A"       # 关键字
```



## 三、变量的使用与类型检查

### 1. 赋值与运算

变量通过赋值操作 (=) 获得数据，并可参与运算。

```
a = 45
b = 12
print(a + b)  # 加: 57
print(a / b)  # 除: 3.75 (结果总是float)
```


### 2. type() 函数

用于检查变量存储的数据类型。

```
value_int = 10
value_str = "Python"
print(type(value_int))  # <class 'int'>
print(type(value_str))  # <class 'str'>
```


## 四、类型转换

Python提供了内置函数来显式转换数据类型。

### 1. int()

转换为整数。

```
print(int(123.78))       # float to int: 123 (直接截断小数)
print(int("456"))        # str to int: 456
print(int("1A", base=16)) # str (十六进制) to int: 26
print(int("101", base=2)) # str (二进制) to int: 5
```



- **讲解**：base 参数用于指定原字符串的进制。
    

### 2. float()

转换为浮点数。```python  
print(float(100)) # int to float: 100.0  
print(float("3.14")) # str to float: 3.14

````
### 3. `str()`
转换为字符串。
```python
print(str(789))        # int to str: '789'
print(str(True))       # bool to str: 'True'
````


### 4. bool()

转换为布尔型。

```
print(bool(0))         # int 0 to bool: False
print(bool(123))       # 非零 int to bool: True
print(bool(""))        # 空 str to bool: False
print(bool("text"))    # 非空 str to bool: True
print(bool(None))      # None to bool: False
```



- **讲解**：数值 0、0.0，空字符串 ''、""，以及 None 会转换为 False，其他多数情况为 True。
    

### 5. chr() 和 ord()

字符与对应的整数编码（如ASCII, Unicode）之间的转换。

```
print(chr(65))         # 整数编码 to 字符: 'A'
print(ord('A'))        # 字符 to 整数编码: 65
print(chr(9731))       # '☃' (雪人)
print(ord('中'))       # 20013
```

## 总结

本单元我们学习了Python中变量的基本概念、核心数据类型 (int, float, str, bool)、命名规范以及类型间的转换方法。理解并熟练运用这些基础是后续学习的关键。

---
