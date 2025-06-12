## 核心概念

本单元主要探讨Python中函数的两种高级应用：**装饰器 (Decorators)** 和 **递归调用 (Recursion)**。

## 一、装饰器 (Decorators)

### 1. 定义与作用

- **定义**: 装饰器是一种特殊的函数 (高阶函数)，它接收一个函数作为参数，并返回一个新的函数。这个新函数通常会“装饰”或“包装”原始函数，为其添加额外的功能，而无需修改原始函数的代码。
    
- **核心目的**: 在不改变原函数定义（源代码）的前提下，动态地增强函数的功能。常用于日志记录、性能测试、事务处理、权限校验等场景。
    
- **语法糖**: Python提供了 @decorator_name 的语法糖，可以简洁地将装饰器应用于函数定义之上。
    

### 2. 装饰器的基本结构

```python
def my_decorator(func_to_decorate):
    # func_to_decorate 是被装饰的函数
    def wrapper(*args, **kwargs):
        # 1. 在调用原始函数之前执行的代码 (增强功能)
        print("Something is happening before the function is called.")

        # 2. 调用原始函数
        result = func_to_decorate(*args, **kwargs) # *args, **kwargs 保证能接受任意参数

        # 3. 在调用原始函数之后执行的代码 (增强功能)
        print("Something is happening after the function is called.")

        # 4. 返回原始函数的执行结果 (或者加工后的结果)
        return result
    return wrapper # 返回包装后的函数
```



### 3. 使用装饰器

- **方式一：直接调用装饰器函数**
    
    ```python
    def say_hello():
        print("Hello!")
    say_hello = my_decorator(say_hello) # 手动装饰
    say_hello()
    ```
    
    
- **方式二：使用 @ 语法糖 (推荐)**
    
    ```python
    @my_decorator
    def say_whee():
        print("Whee!")
    say_whee()
    ```
    
 
    上述 @my_decorator 等价于 say_whee = my_decorator(say_whee)。
    

### 4. 示例：记录函数执行时间

```python
import time
from functools import wraps # 用于保留原函数元信息

def record_time(func):
    @wraps(func) # 保留func的__name__, __doc__等属性
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} 执行时间: {end - start:.3f}秒')
        return result
    return wrapper

@record_time
def slow_function(delay):
    time.sleep(delay)
    print("Function finished.")

slow_function(0.5)
```


- **functools.wraps**: 一个装饰器，用于装饰 wrapper 函数。它可以将原始函数 func 的元信息 (如函数名、文档字符串等) 复制到 wrapper 函数上，这对于调试和内省非常有用。
    
- **调用被装饰前的原函数**: 如果使用了 @wraps(func)，可以通过 decorated_function.__wrapped__(...) 来调用未被装饰的原始函数。
    

### 5. 参数化的装饰器 (本单元未详述)

装饰器本身也可以接受参数，从而实现更灵活的装饰功能。这通常需要再嵌套一层函数。

## 二、递归调用 (Recursion)

### 1. 定义

函数在其定义中直接或间接调用自身的过程。

### 2. 递归的要素

- **基本情况 (Base Case / 收敛条件)**: 递归必须有一个或多个可以直接求解，不再进行递归调用的终止条件。否则会导致无限递归和栈溢出。
    
- **递归步骤 (Recursive Step / 递归公式)**: 将原问题分解为规模更小的、与原问题具有相同结构的子问题，并通过调用自身来解决这些子问题。
    

### 3. 示例：阶乘

```
N!=N×(N−1)!N!=N×(N−1)!
```

，其中 

```
0!=10!=1
```

，

```
1!=11!=1
```

 (基本情况)。

```python
def factorial(n):
    if n < 0: raise ValueError("阶乘只为非负整数定义")
    if n in (0, 1): # 基本情况
        return 1
    return n * factorial(n - 1) # 递归步骤

print(factorial(5)) # 120
```


### 4. 函数调用栈与栈溢出

- 每次函数调用都会在内存的“调用栈”上创建一个新的“栈帧 (stack frame)”来存储局部变量、返回地址等信息。
    
- 递归调用会不断向栈中压入新的栈帧。如果递归深度过大（基本情况未达到或收敛过慢），栈空间会被耗尽，导致**栈溢出 (Stack Overflow)**，在Python中通常表现为 RecursionError。
    
- Python默认的递归深度有限制 (通常1000左右)，可以通过 sys.getrecursionlimit() 查看和 sys.setrecursionlimit() 修改 (不推荐随意增大)。
    

### 5. 示例：斐波那契数列

```
Fn=Fn−1+Fn−2Fn​=Fn−1​+Fn−2​
```

，其中 

```
F1=1,F2=1F1​=1,F2​=1
```

 (或 

```
F0=0,F1=1F0​=0,F1​=1
```

)。

```python
# 未优化的递归斐波那契 (效率极低，大量重复计算)
def fib_recursive_naive(n):
    if n <= 0: raise ValueError("项数需为正整数")
    if n in (1, 2): return 1
    return fib_recursive_naive(n - 1) + fib_recursive_naive(n - 2)

# 使用循环递推 (效率高)
def fib_iterative(n):
    if n <= 0: raise ValueError("项数需为正整数")
    a, b = 1, 1 # F(1), F(2)
    for _ in range(n - 2): # 已有前两项
        a, b = b, a + b
    return b if n > 1 else a

# 使用 @lru_cache 优化递归 (缓存计算结果，避免重复计算)
from functools import lru_cache
@lru_cache(maxsize=None) # maxsize=None表示缓存无限制
def fib_recursive_cached(n):
    if n <= 0: raise ValueError("项数需为正整数")
    if n in (1, 2): return 1
    return fib_recursive_cached(n - 1) + fib_recursive_cached(n - 2)

# print(fib_recursive_cached(30)) # 可以快速计算较大项
```



- **functools.lru_cache**: 一个装饰器，用于实现“最近最少使用 (Least Recently Used)”缓存策略。它可以缓存函数的调用结果，当再次以相同参数调用该函数时，直接返回缓存的结果，极大提高重复计算场景下的性能。
    

## 总结

- **装饰器**提供了一种优雅的方式来扩展函数功能，遵循“开放封闭原则”（对扩展开放，对修改封闭）。
    
- **递归调用**是一种强大的编程范式，能够简洁地表达一些具有自相似结构的算法。但必须注意其收敛条件和潜在的栈溢出风险，并考虑性能优化（如缓存或转换为迭代）。
    
- 理解高阶函数、闭包 (装饰器的基础) 和函数调用机制有助于更好地掌握这些高级应用。