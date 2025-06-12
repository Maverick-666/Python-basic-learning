## 核心概念

- **字符串 (String)**: 由零个或多个字符组成的有限序列。例如：s = "hello"。
    
- **不可变性 (Immutable)**: 与元组类似，字符串一旦创建，其内容不能被修改。任何对字符串的操作（如拼接、替换）都会返回一个新的字符串对象，原字符串不变。
    
- **定义**: 可使用单引号 '...'，双引号 "..."，或三引号 '''...''' / """...""" (三引号允许字符串跨越多行，并保留其中的换行符)。
    

## 一、字符串的特殊表示

### 1. 转义字符 \

反斜杠 \ 用于表示特殊字符。

- \n: 换行符
    
- \t: 制表符
    
- \': 单引号
    
- \": 双引号
    
- \\: 反斜杠本身
    

```
print('Line 1\nLine 2')
print('He said, "Hi!"') # 或者 "He said, \"Hi!\""
```


### 2. 原始字符串 r'...' 或 R'...'

字符串中的所有字符都按其字面意义解释，没有转义。

```
print(r'C:\Users\name\new_folder') # \U 和 \n 不会被转义
```



### 3. 字符编码表示

- \ooo: 八进制表示字符 (如 \141 是 'a')。
    
- \xhh: 十六进制表示字符 (如 \x61 是 'a')。
    
- \uxxxx / \Uxxxxxxxx: Unicode编码表示字符 (如 \u4F60\u597D 是 "你好")。
    

## 二、字符串的运算 (与序列类型共性)

### 1. 拼接 + 和重复 *

```
greeting = "Hello" + " " + "World" # "Hello World"
separator = "-" * 10                # "----------"
```



### 2. 比较运算 ==, !=, <, >, <=, >=

按字典序（基于字符的Unicode编码值）比较。

```
print('apple' < 'banana') # True
print('Apple' < 'apple')  # True (大写字母编码 < 小写字母编码)
print(ord('A'), ord('a')) # 65, 97
```

### 3. 成员运算 in 和 not in

判断子字符串是否存在于主字符串中。

```
print('py' in 'python')    # True
print('java' not in 'python') # True
```



### 4. 长度 len()

返回字符串中字符的个数。

```
print(len("你好")) # 2 (中文字符算一个)
```



### 5. 索引 [] 和切片 [start:end:step]

与列表、元组用法类似，用于访问单个字符或子字符串。返回的是新字符串。

```
s = "Python"
print(s[0])    # 'P'
print(s[-1])   # 'n'
print(s[1:4])  # 'yth' (不包含索引4)
print(s[::-1]) # 'nohtyP' (反转)
# s[0] = 'J'   # TypeError: 'str' object does not support item assignment
```



## 三、字符的遍历

```
# 方法1: 通过索引 (不推荐，除非需要索引)
text = "abc"
for i in range(len(text)):
    print(text[i])

# 方法2: 直接遍历字符 (推荐)
for char in text:
    print(char)
```


## 四、字符串的常用方法

字符串方法不修改原字符串，而是返回一个新的字符串。

### 1. 大小写转换

- capitalize(): 返回首字母大写的字符串副本。
    
- title(): 返回每个单词首字母大写的字符串副本。
    
- upper(): 返回全部大写的字符串副本。
    
- lower(): 返回全部小写的字符串副本。
    

```
msg = "hello python"
print(msg.capitalize()) # "Hello python"
print(msg.title())      # "Hello Python"
print(msg.upper())      # "HELLO PYTHON"
```



### 2. 查找操作

- find(sub[, start[, end]]): 查找子串sub首次出现位置，返回索引。若未找到，返回 -1。
    
- index(sub[, start[, end]]): 同find，但若未找到，引发 ValueError。
    
- rfind(sub[, start[, end]]): 从右向左查找。
    
- rindex(sub[, start[, end]]): 从右向左查找，未找到引发 ValueError。
    

```
s = "one two one two"
print(s.find("two"))    # 4
print(s.rfind("two"))   # 12
# print(s.index("three")) # ValueError
```



### 3. 性质判断 (返回布尔值)

- startswith(prefix[, start[, end]]): 是否以prefix开头。
    
- endswith(suffix[, start[, end]]): 是否以suffix结尾。
    
- isdigit(): 是否只包含数字字符。
    
- isalpha(): 是否只包含字母字符。
    
- isalnum(): 是否只包含字母和数字字符。
    
- isspace(): 是否只包含空白字符。
    
- islower(): 是否所有字母都小写。
    
- isupper(): 是否所有字母都大写。
    
- istitle(): 是否是标题化形式 (每个单词首字母大写)。
    

```
print("File.txt".endswith(".txt")) # True
print("12345".isdigit())         # True
print("HelloWorld".isalpha())    # True
```


### 4. 格式化与对齐

- center(width[, fillchar]): 返回指定宽度width居中，fillchar填充的字符串。
    
- ljust(width[, fillchar]): 左对齐。
    
- rjust(width[, fillchar]): 右对齐。
    
- zfill(width): 左侧补零至指定宽度。


```python
text = "OK"
print(text.center(10, '-')) # "----OK----"
print("42".zfill(5))        # "00042"
*   **字符串格式化方法**:
    *   **%-formatting (旧式)**: `'%s is %d' % (name, age)`
    *   **`str.format()` 方法**: `'{} is {}'.format(name, age)` 或 `'{n} is {a}'.format(n=name, a=age)`
    *   **f-strings (格式化字符串字面量, Python 3.6+, 推荐)**: `f'{name} is {age}'`
        *   f-strings 支持丰富的格式说明符，如精度、对齐、类型转换等：
            `f'{3.14159:.2f}'` -> `'3.14'`
            `f'{123:0>5d}'` -> `'00123'`
            `f'{0.25:.0%}'` -> `'25%'`

### 5. 修剪操作
*   `strip([chars])`: 返回移除字符串首尾指定字符（默认空格）后的副本。
*   `lstrip([chars])`: 移除左侧。
*   `rstrip([chars])`: 移除右侧。
python
s = "   hello   "
print(s.strip()) # "hello"
s2 = "---abc---"
print(s2.strip('-')) # "abc"
```


### 6. 替换操作

- replace(old, new[, count]): 返回将字符串中所有（或前count个）old子串替换为new后的副本。
    

```
s = "one two two three"
print(s.replace("two", "TWO"))      # "one TWO TWO three"
print(s.replace("two", "TWO", 1)) # "one TWO two three"
```


### 7. 拆分与合并

- split(sep=None, maxsplit=-1): 将字符串按sep分隔符拆分为子串列表。若sep未指定或为None，则以连续空白字符为分隔符。maxsplit指定最大拆分次数。
    
- separator_string.join(iterable): 将iterable（通常是字符串列表）中的所有元素用separator_string连接成一个新字符串。
    

```
csv_line = "apple,banana,cherry"
fruits = csv_line.split(',')  # ['apple', 'banana', 'cherry']
print("-".join(fruits))       # "apple-banana-cherry"
```

### 8. 编码与解码

- encode(encoding='utf-8', errors='strict'): 将字符串编码为字节串 (bytes)。
    
- bytes_object.decode(encoding='utf-8', errors='strict'): 将字节串解码为字符串。  
    编码和解码时使用的 encoding 必须一致，否则可能产生乱码或 UnicodeDecodeError。
    

```
text_cn = "你好"
bytes_utf8 = text_cn.encode('utf-8') # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(bytes_utf8.decode('utf-8'))    # "你好"
```


## 总结

字符串是Python中处理文本信息的基础。其不可变性保证了数据的一致性，但也意味着所有修改操作都会创建新对象。Python为字符串提供了极其丰富的内置方法和灵活的运算，熟练掌握它们对于文本处理、数据清洗、格式化输出等任务至关重要。