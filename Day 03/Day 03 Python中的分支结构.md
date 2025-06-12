## 核心概念

- **顺序结构**: 代码从上到下依次执行。
    
- **分支结构 (选择结构)**: 根据特定条件，程序选择不同的执行路径。
    
- **关键字**: Python中用于构造分支结构的主要关键字是 if, elif, else。Python 3.10+ 引入了 match, case。
    
- **代码块与缩进**: Python使用**缩进**（通常是4个空格）来定义代码块。相同缩进级别的连续语句属于同一个代码块。**强烈建议使用4个空格进行缩进，避免使用Tab键或混用。**
    

## 一、if-elif-else 结构

### 1. 基本 if 结构

如果 if 后的条件表达式为 True，则执行其下的缩进代码块。

````
bmi = 22.0
if 18.5 <= bmi < 24:  # Python支持链式比较
    print('身材标准')
```*   **讲解**: `18.5 <= bmi < 24` 等价于 `bmi >= 18.5 and bmi < 24`。

### 2. `if-else` 结构
如果 `if` 条件为 `True`，执行 `if` 块；否则 (为 `False`)，执行 `else` 块。
```python
bmi = 25.0
if 18.5 <= bmi < 24:
    print('身材标准')
else:
    print('身材不够标准')
````


- **讲解**: if 块和 else 块中只有一个会被执行。
    

### 3. if-elif-else 结构 (多分支)

用于检查多个互斥条件。elif 是 "else if" 的缩写。

```
bmi = 28.0
if bmi < 18.5:
    print('体重过轻')
elif bmi < 24:  # 隐含 bmi >= 18.5
    print('身材标准')
elif bmi < 27:  # 隐含 bmi >= 24
    print('体重过重')
else:           # 隐含 bmi >= 27
    print('肥胖')
```



- **讲解**: Python会从上到下检查条件，一旦某个 if 或 elif 条件为 True，其对应的代码块被执行，其余的 elif 和 else 块将被跳过。else 块是可选的，用于处理所有其他情况。
    

## 二、match-case 结构 (Python 3.10+)

一种更结构化的多分支方式，常用于值匹配。

### 1. 基本用法

```` python
status_code = 404
match status_code:
    case 200: description = 'OK'
    case 400: description = 'Bad Request'
    case 404: description = 'Not Found'
    case _:   description = 'Unknown Code' # _ 是通配符，匹配任何其他值
print(f"Status: {status_code}, Description: {description}") # Not Found
```*   **讲解**: `match` 后的变量会与每个 `case` 后的模式进行匹配。`case _:` (下划线) 作为通配符，如果前面的 `case` 都没有匹配成功，则执行该分支。它必须放在最后。

### 2. 合并模式 (OR Pattern)
使用 `|` (或操作符) 允许一个 `case` 匹配多个值。

```python
status_code = 401
match status_code:
    case 200 | 201: description = 'Success'
    case 401 | 403 | 404: description = 'Client Error'
    case 500 | 503: description = 'Server Error'
    case _: description = 'Other'
print(f"Status: {status_code}, Category: {description}") # Client Error
````


## 三、分支结构的应用

### 1. 分段函数求值

根据自变量 x 的不同范围，计算 y 的值。

```
x = float(input('x = '))
if x > 1:
    y = 3 * x - 5
elif x >= -1: # 隐含 x <= 1
    y = x + 2
else:         # 隐含 x < -1
    y = 5 * x + 3
print(f'{y = }') # Python 3.8+ f-string
```

### 2. 嵌套分支

分支结构内部可以包含其他分支结构。

```
# 分段函数求值的嵌套写法 (通常不推荐，“扁平优于嵌套”)
x = 0
if x > 1:
    y = 3 * x - 5
else: # x <= 1
    if x >= -1: # -1 <= x <= 1
        y = x + 2
    else: # x < -1
        y = 5 * x + 3
print(f'{y = }')
```



- **Python之禅**: "Flat is better than nested." (扁平优于嵌套)。过多的嵌套会降低代码可读性。
    

### 3. 百分制成绩转等级

```
score = float(input('请输入成绩: '))
if score >= 90: grade = 'A'
elif score >= 80: grade = 'B'
elif score >= 70: grade = 'C'
elif score >= 60: grade = 'D'
else: grade = 'E'
print(f'{grade = }')
```



### 4. 计算三角形周长和面积

需要先判断三边是否能构成三角形（任意两边之和大于第三边）。

```
import math # 用于海伦公式中的开方，虽然**0.5也可以

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    s = perimeter / 2  # 半周长
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5 # 海伦公式
    print(f'周长: {perimeter:.2f}')
    print(f'面积: {area:.2f}')
else:
    print('不能构成三角形')
```



## 总结

分支结构是控制程序流程的关键工具，使得程序可以根据不同条件执行相应的操作。熟练掌握 if-elif-else 和 match-case (Python 3.10+) 的使用，以及理解缩进对于代码块的重要性，是编写复杂逻辑程序的基础。

---

这份精炼版的Markdown文件应该能帮助您更好地聚焦核心知识点。

接下来，我将针对这份精炼内容中的每个主要知识点为您出一道题。您准备好了吗？