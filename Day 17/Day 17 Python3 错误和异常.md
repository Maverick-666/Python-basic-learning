## 一、错误的类型

### 1. 语法错误 (Syntax Errors / Parsing Errors)

- 程序在开始运行**之前**，Python解释器在解析代码时发现不符合Python语法规则的错误。
    
- 解释器会指出错误发生的文件名和行号，并通常用一个小箭头指向检测到错误的第一个位置。
    
    ```
    # 示例 (会导致解析失败)
    # print "Hello"  # Python 3 中 print 是函数
    # if x > 0 y = 1 # 缺少冒号
    ```


### 2. 异常 (Exceptions)

- 程序语法正确，但在**运行期间**发生的错误。
    
- 当异常发生时，程序会创建一个异常对象。如果异常未被处理，程序将终止并打印一个“回溯 (Traceback)”信息，显示错误类型和发生位置。
    
- **常见内置异常**: NameError, TypeError, ValueError, IndexError, KeyError, FileNotFoundError, ZeroDivisionError, AttributeError, ImportError, OSError等。
    

## 二、异常处理 (Exception Handling)

### 1. try / except 语句

用于捕获和处理在 try 代码块中可能发生的异常。

```python
try:
    # 尝试执行的代码块
    x = int(input("请输入一个数字: "))
    result = 10 / x
    print(f"结果是: {result}")
except ValueError:
    print("输入无效，请输入一个整数！")
except ZeroDivisionError:
    print("错误：不能除以零！")
except Exception as e: # 捕获其他所有 Exception 类型的异常 (通常作为最后一个 except)
    print(f"发生了一个未预料的错误: {type(e).__name__} - {e}")
```


- **工作流程**:
    
    1. 执行 try 子句。
        
    2. 如果无异常，忽略所有 except 子句，try 语句执行完毕。
        
    3. 如果发生异常，try 子句剩余部分被忽略。Python查找匹配该异常类型的 except 子句。
        
    4. 如果找到匹配的 except 子句，则执行该子句，然后继续执行 try/except 语句之后的代码。
        
    5. 如果一个异常没有与任何 except 匹配，它会成为一个“未处理异常”，程序终止。
        
- 一个 try 语句可以有多个 except 子句来处理不同类型的特定异常。
    
- 一个 except 子句可以用元组同时处理多种异常：except (RuntimeError, TypeError):
    
- 最后一个 except 子句可以省略异常名称，作为通配符捕获所有未被前面处理的异常 (通常不推荐，除非明确知道如何处理或用于日志记录后重新抛出)。
    

### 2. try / except ... else 语句

else 子句是可选的，必须在所有 except 子句之后。

- **else 子句在 try 子句没有发生任何异常时执行。**
    
- 使用 else 可以让 try 块更专注于可能引发异常的代码，而将正常流程的代码放入 else。
    

```python
try:
    file = open("mydata.txt", "r")
except FileNotFoundError:
    print("文件未找到！")
else:
    # 只有当文件成功打开时才执行
    content = file.read()
    print("文件内容读取成功。")
    file.close()
```



### 3. try ... finally 语句

finally 子句定义了**无论是否发生异常都必须执行的清理行为**。

- 如果 try 子句中发生异常且未被 except 捕获，该异常会在 finally 子句执行完毕后被重新抛出。
    
- 如果 try 子句中的异常被 except 捕获，或 try 子句正常完成，finally 子句依然会执行。
    
- 常用于释放资源，如关闭文件、网络连接等。
    

```python
file = None # 在try外部初始化，确保finally中可访问
try:
    file = open("config.ini", "r")
    # ... 处理文件 ...
    # x = 1 / 0 # 模拟一个错误
except FileNotFoundError:
    print("配置文件未找到。")
finally:
    if file: # 确保文件对象已创建
        file.close()
        print("文件已关闭 (finally)。")
```



## 三、抛出异常 (raise)

使用 raise 语句手动引发一个指定的异常。  
**语法**: raise [ExceptionType([args])]

```python
def check_age(age):
    if age < 0:
        raise ValueError("年龄不能为负数。")
    elif age < 18:
        raise Exception("未成年人禁止访问。") # 可以抛出通用 Exception
    print("年龄有效。")

try:
    check_age(-5)
except ValueError as ve:
    print(f"捕获到值错误: {ve}")
except Exception as e: # 捕获上面未特定处理的 Exception
    print(f"捕获到其他错误: {e}")
```



- raise 不带参数时，会重新抛出当前作用域中最后被激活的异常 (通常在 except 块中使用)。
    

## 四、用户自定义异常

通过创建新的异常类（通常继承自 Exception 或其子类）来定义自己的异常类型。

- 有助于更精确地表达特定错误情况。
    
- 可以添加自定义属性和方法到异常类中。
    

```python 
class NetworkError(Exception):
    """网络相关的自定义错误基类"""
    pass

class ConnectionTimeoutError(NetworkError):
    """连接超时错误"""
    def __init__(self, host, port, timeout):
        message = f"连接到 {host}:{port} 超时 ({timeout}s)"
        super().__init__(message)
        self.host = host
        self.port = port
        self.timeout = timeout

try:
    # 模拟网络操作
    raise ConnectionTimeoutError("example.com", 80, 5)
except ConnectionTimeoutError as cte:
    print(f"网络错误: {cte} (Host: {cte.host})")
except NetworkError as ne: # 捕获基类
    print(f"一般网络错误: {ne}")
```


## 五、定义清理行为 (with 语句)

许多对象（如文件、锁、网络连接等）定义了标准的清理行为。with 语句（上下文管理器协议）提供了一种优雅的方式来确保这些对象的清理方法（通常是 __exit__()）无论如何都会被执行。

- **对于文件操作，with open(...) as f: 是首选方式**，它会自动处理文件的关闭。
    

```python
try:
    with open("important_data.txt", "r") as data_file:
        for line in data_file:
            print(line.strip())
        # 即使这里发生错误，文件也会被自动关闭
except FileNotFoundError:
    print("重要数据文件未找到。")
```

## 六、断言 (assert)

assert expression[, message]

- 用于在代码中插入调试性的检查。
    
- 如果 expression 为 False，则引发 AssertionError 异常，可选的 message 会作为错误信息。
    
- **主要用于开发和测试阶段**，检查不应发生的内部错误或不变量。
    
- 可以通过Python解释器的 -O (优化) 选项在运行时忽略所有 assert 语句。
    

```python
def set_discount(price, discount_rate):
    assert 0 <= discount_rate <= 1, "折扣率必须在0和1之间"
    return price * (1 - discount_rate)

try:
    final_price = set_discount(100, 1.2)
except AssertionError as ae:
    print(f"断言失败: {ae}")
```


## 总结

- 理解Python的错误和异常类型是编写健壮程序的基础。
    
- 使用 try-except-else-finally 结构可以优雅地处理运行时可能发生的各种错误情况。
    
- raise 语句允许程序主动抛出异常。
    
- 自定义异常可以使错误处理更具针对性。
    
- with 语句是管理需要清理的资源的最佳实践。
    
- assert 用于内部条件检查和调试。