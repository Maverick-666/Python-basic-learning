## 核心概念

- **表达式 (Expression)**: 由常量、变量、函数和运算符组合而成，可被计算以产生一个值。
    
- **运算符优先级**: 决定了表达式中多个运算符的执行顺序（见原文表格，**** > * / // % > + - > 比较运算符 > 逻辑运算符 > 赋值运算符）。不确定时，使用圆括号 () 明确顺序。
    

## 一、算术运算符

用于执行数学计算。

|   |   |   |   |
|---|---|---|---|
|运算符|描述|示例 (a=10, b=3)|结果|
|+|加法|a + b|13|
|-|减法|a - b|7|
|*|乘法|a * b|30|
|/|除法|a / b|3.333|
|//|整除|a // b|3|
|%|求模/取余|a % b|1|
|**|求幂|a ** b|1000|

```
print(2 + 3 * 5)      # 17 (乘法优先)
print((2 + 3) * 5)    # 25 (括号优先)
print(10 // 3)        # 3 (整除，取整数部分)
print(10 % 3)         # 1 (取余数)
```


## 二、赋值运算符

用于给变量分配值。

- **基本赋值**: =
    
    ```
    x = 100
    ```
    
    
- **复合赋值运算符**: 简化运算与赋值的组合。  
    | 运算符 | 等价于 | 示例 (a=10, b=3) | a 的结果 |  
    | :----- | :------------ | :----------------- | :--------- |  
    | += | a = a + b | a += b | 13 |  
    | -= | a = a - b | a -= b | 7 |  
    | *= | a = a * b | a *= b | 30 |  
    | /= | a = a / b | a /= b | 3.333 |  
    | //= | a = a // b | a //= b | 3 |  
    | %= | a = a % b | a %= b | 1 |  
    | **= | a = a ** b | a **= b | 1000 |
    
    ```
    a = 10
    a += 5  # a 现在是 15 (相当于 a = a + 5)
    print(a)
    ```

    
- **海象运算符 := (Python 3.8+)**: 在表达式内部赋值，并且表达式的值为赋给变量的值。
    
    ```
    # 传统方式
    # count = len(my_list)
    # if count > 10:
    #     print(f"List is too long: {count}")
    
    # 使用海象运算符
    my_list = list(range(15))
    if (count := len(my_list)) > 10:
        print(f"List is too long: {count}") # 输出: List is too long: 15
    ```
    
    - **讲解**: 赋值语句 a = 10 本身不返回值，不能直接用在 print() 等需要表达式的地方。海象运算符解决了这个问题。
        

## 三、比较运算符 (关系运算符)

用于比较两个值，返回布尔值 (True 或 False)。

|   |   |   |   |
|---|---|---|---|
|运算符|描述|示例 (x=5, y=10)|结果|
|==|等于|x == y|False|
|!=|不等于|x != y|True|
|>|大于|x > y|False|
|<|小于|x < y|True|
|>=|大于等于|x >= 5|True|
|<=|小于等于|y <= 10|True|

```
print(5 == 5.0)  # True (值相等)
print('apple' != 'orange') # True
```


## 四、逻辑运算符

用于组合或反转布尔表达式。

|   |   |   |   |
|---|---|---|---|
|运算符|描述|示例 (p=True, q=False)|结果|
|and|逻辑与|p and q|False|
|or|逻辑或|p or q|True|
|not|逻辑非|not p|False|

- **短路特性**:
    
    - expr1 and expr2: 若 expr1 为 False，则 expr2 不会被执行。
        
    - expr1 or expr2: 若 expr1 为 True，则 expr2 不会被执行。
        

```
age = 25
has_permission = False
print(age > 18 and has_permission)  # False
print(age > 18 or has_permission)   # True
print(not has_permission)           # True
```



## 五、其他重要运算符 (原文表格提及)

### 1. 身份运算符

比较两个变量是否引用内存中的**同一个对象**。

|   |   |
|---|---|
|运算符|描述|
|is|是同一个对象|
|is not|不是同一个对象|

```
a = [1, 2]
b = [1, 2]
c = a
print(a is b)    # False (内容相同，但内存地址不同)
print(a == b)    # True (内容相同)
print(a is c)    # True (c 是 a 的别名)
```

### 2. 成员运算符

判断一个元素是否存在于一个序列（如字符串、列表、元组）中。

|   |   |
|---|---|
|运算符|描述|
|in|成员存在|
|not in|成员不存在|

```
message = "hello"
print('e' in message)     # True
print('x' not in message) # True
```



### 3. 按位运算符

对整数的二进制表示进行操作（一般用于底层编程）。

|   |   |   |   |
|---|---|---|---|
|运算符|描述|示例 (x=5 (0101), y=3 (0011))|结果 (bin)|
|&|按位与|x & y|1 (0001)|
|`|`|按位或|`x|
|^|按位异或|x ^ y|6 (0110)|
|~|按位取反|~x|-6|
|<<|左移|x << 1|10 (1010)|
|>>|右移|x >> 1|2 (0010)|

## 六、运算符应用实例

### 1. 华氏转摄氏

C = (F - 32) / 1.8

```
f_temp = float(input('请输入华氏温度: '))
c_temp = (f_temp - 32) / 1.8
print(f'{f_temp:.1f}°F = {c_temp:.1f}°C')
```



- **讲解**: input() 获取用户输入 (字符串)，float() 转换为浮点数。f'' (f-string) 用于格式化输出，:.1f 保留一位小数。
    

### 2. 圆的周长和面积

周长 2πr, 面积 πr²

```
import math # 导入 math 模块以使用 math.pi

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f'周长: {perimeter:.2f}')
print(f'面积: {area:.2f}')
# Python 3.8+ f-string新特性:
# print(f'{perimeter=:.2f}') # 输出: perimeter=xx.xx
```



### 3. 判断闰年

公元年份 year (1582年后):

- 能被400整除是闰年。
    
- 或者，能被4整除但不能被100整除是闰年。
    

```
year = int(input('请输入年份: '))
is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
print(f'{year} 是闰年吗? {is_leap}')
```


## 总结

运算符是构建复杂逻辑和进行数据处理的基础。理解它们的种类、优先级和应用场景对编写高效、准确的Python代码至关重要。