## 核心概念：函数 (Function)

- **目的**: 封装功能相对独立且可能被重复使用的代码块，以提高代码的复用性、可读性和可维护性。解决代码重复问题。
    
- **类比数学函数**: 如 
    
    ```
    y=f(x)y=f(x)
    ```
    
    ，f是函数名，x是自变量 (参数)，y是因变量 (返回值)。
    

## 一、定义函数 def

使用 def 关键字定义函数。

```python
def function_name(parameter1, parameter2, ...):
    """
    (可选) 文档字符串 (docstring): 描述函数功能、参数、返回值等。
    """
    # 函数体 (缩进的代码块)
    statement1
    statement2
    # ...
    return value # (可选) 返回值，若无return或return后无值，则返回 None
```


- **命名规则**: 与变量命名规则相同 (小写字母和下划线，见名知意)。
    
- **参数 (Parameters)**: 函数定义时声明的输入变量。
    
- **返回值 (Return Value)**: 函数执行后输出的结果。
    

**示例：阶乘函数**

```` python
def factorial(num):
    """计算非负整数num的阶乘。"""
    if num < 0:
        return "输入无效" # 或引发异常
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result
# 调用函数
print(factorial(5)) # 120
m, n = 7, 3
# C(m,n) = m! / (n! * (m-n)!)
combinations = factorial(m) // (factorial(n) * factorial(m - n))
print(f"C({m},{n}) = {combinations}") # 35
*   **重用**: 定义好的函数可以在多处调用。
*   **标准库**: Python的 `math` 模块提供了 `math.factorial()` 函数。应优先使用标准库或可靠的第三方库，避免“重复造轮子”。
````


## 二、函数的参数

### 1. 位置参数 (Positional Arguments)
调用时按顺序传递，数量必须匹配。
```python
def greet(name, message):
    print(f"{message}, {name}!")
greet("Alice", "Hello") # "Hello, Alice!"
````


### 2. 关键字参数 (Keyword Arguments)

调用时通过 参数名=值 的形式传递，顺序可以不一致。

```
greet(message="Good morning", name="Bob") # "Good morning, Bob!"
```



### 3. 强制位置参数 / (Python 3.8+)

在参数列表中，/ 左边的参数只能按位置传递。

```
def func_pos_only(a, b, /):
    print(a, b)
# func_pos_only(a=1, b=2) # TypeError
func_pos_only(1, 2)       # OK
```



### 4. 命名关键字参数 *

在参数列表中，单独的 * 或 *args 后面的参数必须以关键字形式传递。

```python
def func_kw_only(*, key1, key2): # key1, key2 必须用关键字传递
    print(key1, key2)
# func_kw_only(10, 20) # TypeError
func_kw_only(key1=10, key2=20) # OK

def func_mixed(pos_arg, *, kw_only_arg): # pos_arg可位置可关键字，kw_only_arg必须关键字
    print(pos_arg, kw_only_arg)
```



### 5. 参数默认值

定义函数时可以为参数指定默认值。带默认值的参数必须放在不带默认值的参数之后。

```python
def power(base, exponent=2): # exponent 默认值为 2
    return base ** exponent
print(power(3))    # 9 (3**2)
print(power(3, 3)) # 27 (3**3)
```


### 6. 可变参数

- ***args (任意多个位置参数)**: 将传入的多余位置参数打包成一个**元组 (tuple)**。
    
    ```python
    def sum_all(*numbers): # numbers 是一个元组
        total = 0
        for num in numbers:
            total += num
        return total
    print(sum_all(1, 2, 3, 4)) # 10
    ```
    
    
- ****kwargs (任意多个关键字参数)**: 将传入的多余关键字参数打包成一个**字典 (dict)**。
    
    ```python
    def print_info(**details): # details 是一个字典
        for key, value in details.items():
            print(f"{key}: {value}")
    print_info(name="Alice", age=30, city="New York")
    ```
    
    
    
- **参数顺序**: 位置参数, / , *args, 默认值参数, 命名关键字参数, **kwargs (大致顺序，具体组合需遵循规则)。
    

## 三、用模块 (Module) 管理函数

### 1. 什么是模块？

Python中，一个 .py 文件就是一个模块。模块可以包含函数、类、变量的定义。

### 2. 为什么使用模块？

- **代码组织**: 将相关的代码组织在不同的文件中，使项目结构更清晰。
    
- **命名空间**: 避免命名冲突。不同模块可以有同名函数/变量。
    
- **代码复用**: 模块可以被其他程序导入和使用。
    

### 3. 导入模块

- **import module_name**: 导入整个模块。使用时需通过 module_name.function_name 访问。
    
    ````python
    # main.py
    import my_math_module
    print(my_math_module.add(2, 3))
    ```*   **`import module_name as alias`**: 导入模块并给其指定别名。
    ```python
    import my_math_module as mm
    print(mm.add(2, 3))
    ````
  
    
- **from module_name import item1, item2**: 从模块中导入指定的函数、类或变量，可以直接使用其名称。
    
    ```python
    from my_math_module import add, subtract
    print(add(2, 3))
    ```
    

    
- **from module_name import item as alias**: 导入指定项并指定别名。
    
    ```python
    from my_math_module import add as plus
    print(plus(2, 3))
    ```
    
    
- **from module_name import ***: 导入模块中所有公共名称 (不推荐，易造成命名冲突和可读性下降)。
    

### 4. 命名冲突解决

如果从不同模块导入同名函数，后导入的会覆盖先导入的。使用模块名限定或别名可以解决。

```python
# test.py
# from module1 import foo # foo from module1
# from module2 import foo # foo is now from module2
# foo() # Calls foo from module2

from module1 import foo as foo_m1
from module2 import foo as foo_m2
foo_m1()
foo_m2()
```



## 四、标准库中的模块和函数

- **Python标准库 (Python Standard Library)**: Python自带的一组功能强大的模块，提供了广泛的功能，如数学运算 (math)、随机数生成 (random)、时间处理 (time, datetime)、文件系统操作 (os, shutil)、网络通信 (socket, http)、数据持久化 (pickle, json) 等。
    
- **内置函数 (Built-in Functions)**: 不需要 import 即可直接使用的函数。例如：print(), len(), type(), int(), str(), list(), dict(), set(), sum(), max(), min(), abs(), round(), range(), ord(), chr(), input() 等。
    

## 总结

- 函数是组织和复用代码的基本单元，通过参数接收输入，通过返回值提供输出。
    
- 理解不同类型的参数（位置、关键字、默认值、可变参数）及其使用规则非常重要。
    
- 模块是组织Python代码的方式，有助于管理大型项目和避免命名冲突。
    
- 熟练使用Python标准库和内置函数可以极大地提高开发效率。